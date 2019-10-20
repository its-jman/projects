import { Vec, clamp, intersect, getRandomColor, startsWithin } from './math.js';
import { ICanvas } from './main.js';

export interface IAABB {
    left: number;
    right: number;
    top: number;
    bottom: number;

    width: number;
    height: number;
}

export interface IEntity extends IAABB {
    pos: Vec;
    size: Vec;

    deltaPos: Vec;

    getDeltaPos(deltaTime: number): void;
    react(entities: IEntity[]): void;
    finalize(): void;
    collide(e: IEntity): void;

    draw(context: CanvasRenderingContext2D): void;
}

class Rect implements IAABB {
    public pos: Vec;
    public size: Vec;
    public color: string;

    constructor(pos: Vec, size: Vec, color: string) {
        this.pos = pos;
        this.size = size;
        this.color = color;
    }

    get left(): number {
        return this.pos.x - (this.size.x / 2);
    }
    set left(val: number) {
        this.pos.x = val + (this.size.x / 2);
    }

    get right(): number {
        return this.pos.x + (this.size.x / 2);
    }
    set right(val: number) {
        this.pos.x = val - (this.size.x / 2);
    }

    get top(): number {
        return this.pos.y - (this.size.y / 2);
    }
    set top(val: number) {
        this.pos.y = val + (this.size.y / 2);
    }

    get bottom(): number {
        return this.pos.y + (this.size.y / 2);
    }
    set bottom(val: number) {
        this.pos.y = val - (this.size.y / 2);
    }

    get width(): number {
        return this.size.x;
    }
    set width(val: number) {
        this.size.x = val;
    }

    get height(): number {
        return this.size.y;
    }
    set height(val: number) {
        this.size.y = val;
    }

    draw(context: CanvasRenderingContext2D): void {
        context.fillStyle = this.color;
        context.fillRect(Math.round(this.left), Math.round(this.top), Math.round(this.width), Math.round(this.height));
    }
}

export class Ball extends Rect implements IEntity {
    private readonly _rect: ICanvas;
    public vel: Vec;
    public deltaPos: Vec;

    constructor(rect: ICanvas) {
        const pos = new Vec(rect.width / 2, rect.height / 2);
        const size = new Vec(10, 10);

        super(pos, size, getRandomColor());

        this._rect = rect;

        this.vel = new Vec(0, 0);
        this.deltaPos = new Vec(0, 0);
    }

    private _bounceWalls(): void {
        if (this.left < 0) {
            // this.vel.x = 0;
            // this.vel.y = 0;
            this.vel.x = -this.vel.x;
            this.left = 0;
        }
        else if (this.right > this._rect.width) {
            // this.vel.x = 0;
            // this.vel.y = 0;
            this.vel.x = -this.vel.x;
            this.right = this._rect.width;
        }

        if (this.top < 0) {
            this.vel.y = -this.vel.y;
            this.top = 0;
        }
        else if (this.bottom > this._rect.height) {
            this.vel.y = -this.vel.y;
            this.bottom = this._rect.height;
        }
    }

    collide(e: IEntity): void {
        return;
    }

    getDeltaPos(deltaTime: number): void {
        this.deltaPos.x = this.vel.x * deltaTime;
        this.deltaPos.y = this.vel.y * deltaTime;
    }

    react(entities: IEntity[]): void {
        this.pos.x += this.deltaPos.x;
        this.pos.y += this.deltaPos.y;

        this._bounceWalls();
    }

    finalize(): void {
        this.pos.x = this.pos.x;
    }
}

export class Paddle extends Rect implements IEntity {
    private readonly _rect: ICanvas;
    private readonly _getYPos: () => number;

    private readonly _maxDelta: Vec;
    public deltaPos: Vec;

    constructor(rect: ICanvas, xPos: number, getYPos: () => number) {
        if (xPos < 0) {
            xPos += rect.width;
        }

        const pos = new Vec(xPos, rect.height / 2);
        const size = new Vec(15, 100);

        super(pos, size, '#fff');

        this._rect = rect;
        this._getYPos = getYPos;

        this._maxDelta = new Vec(0, 5);
        this.deltaPos = new Vec(0, 0);
    }

    collide(e: IEntity): void {
        return;
    }

    getDeltaPos(deltaTime: number): void {
        let newY = clamp(
            this._getYPos(),
            this.pos.y - this._maxDelta.y,
            this.pos.y + this._maxDelta.y
        );

        newY = clamp(
            newY,
            0,
            this._rect.height
        );

        this.deltaPos.y = newY - this.pos.y;
    }

    react(): void {
        this.pos.y += this.deltaPos.y;
    }

    finalize(): void {
        this.pos.x = this.pos.x;
    }
}
