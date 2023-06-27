<template>
	<div class="body" :style="{width: `${squareSize}px`, height: `${squareSize}px`}">
		<ProgressCircle :square-size="squareSize" :percentage="percentage" />
		<img src="./assets/cxm-text.png" class="cxm-text" />
	</div>
</template>

<script>
import ProgressCircle from './progressCircle.vue';
export default {
	components: {ProgressCircle},
	data: () => ({
		squareSize: 355 + 55,
		percentage: 0,
	}),
};
</script>

<style scoped>
.body {
	margin: 0 auto;
	position: relative;
}

.cxm-text {
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}
</style>
