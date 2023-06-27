// Reference: http://jsbin.com/quhujowota
export function polarToCartesian(size, radius, angleInDegrees) {
  const angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;

  return {
    x: size / 2 + radius * Math.cos(angleInRadians),
    y: size / 2 + radius * Math.sin(angleInRadians),
  };
}

export function getArc(
  squareSize,
  startDegrees,
  endDegrees,
  counterClockwise,
  radius,
  name
) {
  let start = polarToCartesian(squareSize, radius, startDegrees);
  let end = polarToCartesian(squareSize, radius, endDegrees);

  let angle = counterClockwise
    ? startDegrees > endDegrees
      ? startDegrees - endDegrees
      : startDegrees + (360 - endDegrees)
    : startDegrees > endDegrees
    ? 360 - startDegrees + endDegrees
    : endDegrees - startDegrees;

  let arcFlag = angle <= 180 ? 0 : 1;
  let sweepFlag = counterClockwise ? 0 : 1;

  let arcDefs = ["A", radius, radius, 0, arcFlag, sweepFlag, end.x, end.y];

  if (false && name) {
    console.log(name);
    console.log(counterClockwise);
    console.log(startDegrees);
    console.log(endDegrees);
    console.log(angle);
    console.log(start);
    console.log(end);
    console.log(startDegrees > endDegrees);
    console.log(arcFlag);
    console.log(sweepFlag);
    console.log("");
    console.log("");
  }

  return {
    start,
    end,
    arcFlag,
    sweepFlag,
    arcDefs,
  };
}

export function capDegrees(angle) {
  // Angles can NOT meet at 0 and 360.
  return Math.min(359.9999, Math.max(0.0001, angle));
}

// https://gist.github.com/gre/1650294
export const EasingFunctions = {
  // no easing, no acceleration
  linear: (t) => t,
  // accelerating from zero velocity
  easeInQuad: (t) => t * t,
  // decelerating to zero velocity
  easeOutQuad: (t) => t * (2 - t),
  // acceleration until halfway, then deceleration
  easeInOutQuad: (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t),
  // accelerating from zero velocity
  easeInCubic: (t) => t * t * t,
  // decelerating to zero velocity
  easeOutCubic: (t) => --t * t * t + 1,
  // acceleration until halfway, then deceleration
  easeInOutCubic: (t) =>
    t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1,
  // accelerating from zero velocity
  easeInQuart: (t) => t * t * t * t,
  // decelerating to zero velocity
  easeOutQuart: (t) => 1 - --t * t * t * t,
  // acceleration until halfway, then deceleration
  easeInOutQuart: (t) =>
    t < 0.5 ? 8 * t * t * t * t : 1 - 8 * --t * t * t * t,
  // accelerating from zero velocity
  easeInQuint: (t) => t * t * t * t * t,
  // decelerating to zero velocity
  easeOutQuint: (t) => 1 + --t * t * t * t * t,
  // acceleration until halfway, then deceleration
  easeInOutQuint: (t) =>
    t < 0.5 ? 16 * t * t * t * t * t : 1 + 16 * --t * t * t * t * t,
};
