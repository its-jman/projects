<template>
	<svg :class="[ci === i && 'active']">
		<path
			class="arrow"
			:fill="color"
			stroke="none"
			:stroke-width="circleDefs.outlineStrokeWidth"
			:d="arrowPath"
			:style="{
				transform: `rotate(${rotation || 0}deg)`,
			}"
			@click="$emit('click', $event)"
		/>
		<path stroke="none" stroke-width="1" fill="none" :id="uid" :d="fullCenterPath" />
		<text
			v-if="text"
			class="arrowText"
			:style="{
				transform: `rotate(${rotation || 0}deg)`,
			}"
		>
			<textPath
				:href="`#${uid}`"
				text-anchor="middle"
				startOffset="50%"
				alignment-baseline="middle"
				dominant-baseline="middle"
				pointer-events="none"
			>
				{{ text }}
			</textPath>
		</text>
	</svg>
</template>

<script lang="js">
import {polarToCartesian, getArc as getArcBase} from './utils';

export default {
	props: [
		'circleDefs',
		'startAngle',
		'endAngle',
		'color',
		'text',
		'rotation',
		'i',
		'ci',
		'log',
	],
  beforeCreate() {
    this.uuid = crypto.randomUUID()
  },
	methods: {
		getPointOnCircle(radius, angleInDegrees) {
			return polarToCartesian(this.circleDefs.squareSize, radius, angleInDegrees);
		},
		getArc(startDegrees, endDegrees, counterClockwise, radius, name) {
			return getArcBase(
				this.circleDefs.squareSize,
				startDegrees,
				endDegrees,
				counterClockwise,
				radius,
				name
			);
		},
	},
	computed: {
		uid() {
			return this.uuid;
		},
		arrowPath() {
			let innerArc = this.getArc(
				this.startAngle,
				this.endAngle,
				false,
				this.circleDefs.innerRadius
			);
			let tip = this.getPointOnCircle(
				this.circleDefs.centerRadius,
				this.endAngle + this.circleDefs.tipPercentage
			);
			let outerArc = this.getArc(
				this.endAngle,
				this.startAngle,
				true,
				this.circleDefs.outerRadius
			);
			let concaveTip = this.getPointOnCircle(
				this.circleDefs.centerRadius,
				this.startAngle + this.circleDefs.tipPercentage
			);

			// prettier-ignore
			return [
        "M", innerArc.start.x, innerArc.start.y,
        ...innerArc.arcDefs,
        "L", tip.x, tip.y,
        "L", outerArc.start.x, outerArc.start.y,
        ...outerArc.arcDefs,
        "L", concaveTip.x, concaveTip.y,
        "Z"
      ].join(' ');
		},
		fullCenterPath() {
			let arc = this.getArc(
				this.startAngle + this.circleDefs.tipPercentage,
				this.endAngle,
				false,
				this.circleDefs.centerRadius
			);

			// prettier-ignore
			return [
        "M", arc.start.x, arc.start.y,
        ...arc.arcDefs
      ].join(" ");
		},
	},
};
</script>

<style scoped>
:root {
	--transition-duration: 0.5s;
}
svg.active .arrow {
	stroke: #2c3e50;
}

.textAlignPath {
	transform-origin: center;
	transition: all 0.5s ease-in-out;
}

.arrow {
	transition: all 0.5s ease-in-out, stroke 0.3s ease-in-out;
	transform-origin: center;
	stroke: transparent;
	&:hover {
		/*transform: scale(1.1) translate(-3%, 3%);*/
		stroke: #2c3e50;
	}
}

.arrowText {
	transition: all 0.5s ease-in-out;
	fill: white;
	font-weight: 500;
	font-size: 15px;
	transform-origin: center;
	text-transform: uppercase;
}
</style>
