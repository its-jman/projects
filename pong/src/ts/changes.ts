import { Vec } from './math.js';

class Changes {
    private _pos: Vec;
    private _vel: Vec;

    constructor() {
        this._pos = new Vec(0, 0);
        this._vel = new Vec(0, 0);
    }
}
