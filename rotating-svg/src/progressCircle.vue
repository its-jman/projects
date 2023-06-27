<template>
	<div>
		<svg
			class="progress-circle"
			xmlns="http://www.w3.org/2000/svg"
			:viewBox="`0 0 ${squareSize} ${squareSize}`"
		>
			<Arrow
				v-for="(arrow, i) in arrows"
				:i="i"
				:ci="currentRotationIndex"
				:circleDefs="circleDefs"
				:startAngle="degreesPer * i + 2.5"
				:endAngle="degreesPer * i + degreesPer - 2.5"
				:color="arrow.color"
				:text="arrow.text"
				:rotation="rotation + 90 - degreesPer / 2"
				@click.stop="rotateTo(i)"
			/>
			<path stroke="lightgrey" stroke-width="2" fill="none" :d="wrapPath" />
		</svg>
	</div>
</template>

<script>
import Arrow from './arrow.vue';
import {getArc as getArcBase, polarToCartesian} from './utils';

const TICK_DURATION = 13;
let lastTickTime = 0;
let accumulator = 0;

export default {
	name: 'progressCircle',
	components: {Arrow},
	props: ['squareSize', 'percentage'],
	data() {
		// prettier-ignore
		let arrows = [
      { color: "#21b5e2", text: "Communication" },
      { color: "#131c41", text: "Opportunities" },
      { color: "#28558d", text: "Service to Sales" },
      { color: "#2676be", text: "Campaigns" },
    ];

		let strokeWidth = 60;
		let outlineStrokeWidth = 5;
		let wrapPathWidth = 55 / 2;
		let outerRadius = this.squareSize / 2 - outlineStrokeWidth - wrapPathWidth;
		let centerRadius = outerRadius - strokeWidth / 2;
		let innerRadius = outerRadius - strokeWidth;
		let tipPercentage = 4;
		let degreesPer = 360 / arrows.length;

		return {
			arrows,
			strokeWidth,
			wrapPathWidth,
			outlineStrokeWidth,
			outerRadius,
			centerRadius,
			innerRadius,
			tipPercentage,
			degreesPer,
			animationDuration: 1250,
			animationTimer: -1,
			rotation: 0,
			raf: undefined,
		};
	},
	/*created() {
    this.raf = requestAnimationFrame(this.frameTick);
  },
  destroyed() {
    if (this.raf) cancelAnimationFrame(this.raf);
  },*/
	methods: {
		frameTick(ms) {
			const delta = (ms - (lastTickTime === 0 ? ms : lastTickTime)) / 1000;

			accumulator += delta;
			while (accumulator >= TICK_DURATION) {
				this.tickAnimation(TICK_DURATION);
				accumulator -= TICK_DURATION;
			}

			lastTickTime = ms;
			this.raf = requestAnimationFrame(this.frameTick);
		},
		tickAnimation(duration) {
			if (this.animationTimer >= 0) {
				this.animationTimer = Math.max(this.animationTimer - duration, -1);
			}
		},
		getPointOnCircle(radius, angleInDegrees) {
			return polarToCartesian(this.squareSize, radius, angleInDegrees);
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
		rotateTo(i) {
			if (this.currentRotationIndex !== i) {
				let diff = this.currentRotationIndex - i;
				if (diff < 0) {
					diff += this.arrows.length;
				}
				this.rotation += diff * this.degreesPer;
			}
		},
	},
	computed: {
		circleDefs() {
			return {
				squareSize: this.squareSize,
				strokeWidth: this.strokeWidth,
				outlineStrokeWidth: this.outlineStrokeWidth,
				tipPercentage: this.tipPercentage,
				innerRadius: this.innerRadius,
				centerRadius: this.centerRadius,
				outerRadius: this.outerRadius,
			};
		},
		currentRotationIndex() {
			let currentIndex = (this.rotation % 360) / this.degreesPer;
			return (this.arrows.length - currentIndex) % this.arrows.length;
		},
		drawnPercentage() {
			if (Number.isNaN(this.percentage)) {
				console.warn(`Progres Circle percentage NaN: ${this.percentage}`);
				return 0;
			}
			// Always draw a portion of the wheel, to give indication that something is there..?
			return Math.min(360, Math.max(0, this.percentage));
		},
		wrapPath() {
			let tipPercentage = 4;
			let start = this.getPointOnCircle(this.outerRadius + this.wrapPathWidth, 90);
			let p1 = this.getPointOnCircle(
				this.outerRadius + this.wrapPathWidth / 2,
				90 + tipPercentage
			);
			let arc = this.getArc(
				90 + tipPercentage,
				90 - tipPercentage,
				false,
				this.outerRadius + this.wrapPathWidth / 2
			);

			// prettier-ignore
			return [
        "M", start.x, start.y,
        "L", p1.x, p1.y,
        ...arc.arcDefs,
        "Z"
      ].join(" ");
		},
	},
};
</script>

<style scoped>
.progress-circle {
	display: block;
}
</style>
