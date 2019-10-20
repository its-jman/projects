import { ICanvas } from './main.js';

import { IAABB, IEntity } from './entities.js';

class CollisionManager {
    private readonly _rect: IAABB;
    private readonly _entities: IEntity[];

    constructor(rect: ICanvas, entities: IEntity[]) {
        this._rect = rect;
        this._entities = entities;
    }

    private static _broadMatches(e1: IEntity, e2: IEntity): boolean {
        return true;
    }

    private static _preciseMatches(e1: IEntity, e2: IEntity, doubleCheck: boolean = false): boolean {
        return true;
    }

    update(): void {
        const len = this._entities.length;

        for (let i = 0; i < len; i++) {
            const e1 = this._entities[i];
            for (let j = i + 1; j < len; j++) {
                const e2 = this._entities[j];

                if (CollisionManager._broadMatches(e1, e2)) {
                    if (CollisionManager._preciseMatches(e1, e2)) {
                        e1.collide(e2);
                        e2.collide(e1);
                    }
                }
            }
        }
    }
}
/*

Entity1
    startAABB
    endAABB
    velocity

*/
