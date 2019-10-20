import { IAABB, IEntity } from './entities.js';

export class Vec {
    private __x: number;
    private __y: number;

    constructor(x: number, y: number) {
        this.__x = x;
        this.__y = y;
    }

    get x(): number {
        return this.__x;
    }
    set x(val: number) {
        this.__x = val;
    }

    get y(): number {
        return this.__y;
    }
    set y(val: number) {
        this.__y = val;
    }
}

/**
 * Restricts input value to a given range (inclusive)
 * @param val Value to check
 * @param min lowest value to clamp within (inclusive)
 * @param max highest value to clamp within (inclusive)
 */
export function clamp(val: number, min: number, max: number): number {
    if (min > max) {
        [min, max] = [max, min];
    }

    if (val < min) {
        return min;
    }
    else if (val > max) {
        return max;
    }
    else {
        return val;
    }
}

export function startsWithin(e1: IEntity, e2: IEntity): boolean {
    return e1.left < e2.right &&
        e1.right > e2.left &&
        e1.top < e2.bottom &&
        e1.bottom > e2.top;
}

export function intersect(e1: IEntity, e2: IEntity): boolean {
    return e1.left + e1.deltaPos.x < e2.right + e2.deltaPos.x &&
        e1.right + e1.deltaPos.x > e2.left + e2.deltaPos.x &&
        e1.top + e1.deltaPos.y < e2.bottom + e2.deltaPos.y &&
        e1.bottom + e1.deltaPos.y > e2.top + e2.deltaPos.y;
}

/**
 * Generates random rgb color
 */
export function getRandomColor(): string {
    return `rgb(
        ${ (Math.floor(Math.random() * 256)) },
        ${ (Math.floor(Math.random() * 256)) },
        ${ (Math.floor(Math.random() * 256)) }
    )`;
}
