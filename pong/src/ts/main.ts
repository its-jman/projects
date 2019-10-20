import { Ball, IEntity, Paddle, IAABB } from './entities.js';

export interface ICanvas extends IAABB {
    scale: number;
}

class Pong {
    private readonly _canvasID: string;
    private _rect: ICanvas;

    public canvas: HTMLCanvasElement;
    public context: CanvasRenderingContext2D;

    private _frameCallback: (millis: number) => void;
    private _rafID: number;

    /**
     * _frozen  : Indicates the status of game animation. RAF active, or frozen. 
     * _paused  : The pause menu should show, the  
     * _started : If the level has been started, velocity of balls has been set. 
     */
    private _frozen: boolean;
    private _paused: boolean;
    private _started: boolean;

    private _tickDuration: number;
    private _accumulator: number;
    private _lastTickTime: number;
    // private _accumulator: number;
    // private _frameCallback: (millis: number) => void;
    // public started: boolean;
    // public tickDuration: number;
    // public lastTickTime: number;

    private _entities: IEntity[];
    private _balls: Ball[];
    private _playerPaddle: Paddle;
    private _computerPaddle: Paddle;

    /**
     * Base constructor of game.
     * @param canvasID ID of the element in DOM to select
     * @param tps game ticks per second
     */
    constructor(canvasID: string, tps: number) {
        this._canvasID = canvasID;
        this._tickDuration = 1 / tps;

        this._setupCanvas();
        this._setupTimer();
        this._setupEntities();
        this._setupEventListeners();

        // Ensure game is animating. 
        this.unfreeze();
    }

    private _setupCanvas(): void {
        this.canvas = document.getElementById('pongCanvas') as HTMLCanvasElement;
        this.context = this.canvas.getContext('2d');

        // https://stackoverflow.com/questions/17130395/real-mouse-position-in-canvas
        const rect = this.canvas.getBoundingClientRect();
        const scale = this.canvas.height / rect.height;

        this._rect = {
            'left': 0,
            'right': this.canvas.width,
            'top': 0,
            'bottom': this.canvas.height,
            'width': this.canvas.width,
            'height': this.canvas.height,
            'scale': scale
        };
    }

    private _setupTimer(): void {
        this._accumulator = 0;
        this._lastTickTime = 0;
        this._paused = false;
        this._frozen = true;

        this._frameCallback = (millis: number): void => {
            const delta = (millis - this._lastTickTime) / 1000;

            if (!this._paused) {
                this.update(delta);
            }

            this._lastTickTime = millis;
            requestAnimationFrame(this._frameCallback);
        };
    }

    private _setupEntities(): void {
        this._entities = [];

        this._balls = new Array(10).fill(undefined).map(() => {
            const ball = new Ball(this._rect);
            this._entities.push(ball);

            return ball;
        });

        this._playerPaddle = new Paddle(this._rect, 30, () => this._balls[0].pos.y);
        this._entities.push(this._playerPaddle);

        this._computerPaddle = new Paddle(this._rect, -30, () => {
            let closeX = this._balls[0];

            this._balls.forEach((entity) => {
                if (entity.vel.x > 0) {
                    if (entity.right > closeX.right && entity.right <= this._computerPaddle.right) {
                        closeX = entity;
                    }
                }
            });

            return closeX.pos.y;
        });
        this._entities.push(this._computerPaddle);
    }

    private _setupEventListeners(): void {
        this.canvas.addEventListener('click', (e) => {
            this.startGame();
            this.unpause();
        });

        /*
        on blur/focus will always fire when clicking away from window. They also SOMETIMES fire when changing tabs within the same window (not 100%)

        vis change fires only when changing tabs, and it occurs after the blur event if the blur event fires.
        */
        // Tab change (fires once when changing to other tab, and once when changing to this tab)
        window.addEventListener('visibilitychange', (e) => {
            if (document.visibilityState === 'hidden') { game.freeze(); }

            else if (document.visibilityState === 'visible') { game.unfreeze(); }
            
            else { console.log('Unknown event type in visibilitychange'); }
        });

        // Fires when changing focused window -> fires before vis change
        window.onblur = (e) => {
            game.freeze();
        };

        // Fires when the game is the focused window.
        window.onfocus = (e) => {
            game.unfreeze();
        };

    }

    pause(): void {
        this._paused = true;
    }

    unpause(): void {
        this._paused = false;
    }

    /**
     * Freeze the game and animation when the game should no longer be rendered. 
     */
    freeze(): void {
        if (!this._frozen) {
            this._frozen = true;
            
            this.pause();

            if (this._rafID) {
                window.cancelAnimationFrame(this._rafID);
            }
        }
    }

    unfreeze(): void {
        if (this._frozen) {
            this._frozen = false;

            this._rafID = requestAnimationFrame((millis) => {
                this._lastTickTime = millis - this._tickDuration;

                // Extraneous call to ensure the first frame is drawn (esp. when debugging)
                this.draw();

                this._rafID = requestAnimationFrame(this._frameCallback);
            });
        }
    }

    startGame(): void {
        if (!this._started) {
            this._balls.forEach((elem) => {
                elem.vel.x = Math.random() * 150 - 75;
                elem.vel.y = Math.random() * 150 - 75;
            });

            this._started = true;
        }
    }

    update(deltaTime: number): void {
        this._accumulator += deltaTime;
        while (this._accumulator >= this._tickDuration) {
            this.tickGame(this._tickDuration);
            this.draw();

            this._accumulator -= this._tickDuration;
        }
    }

    tickGame(deltaTime: number): void {
        this._entities.forEach((entity) => {
            entity.getDeltaPos(deltaTime);
        });

        this._entities.forEach((entity) => {
            entity.react(this._entities);
        });
    }

    draw(): void {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.context.fillStyle = '#000';
        this.context.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this._entities.forEach((entity) => {
            entity.draw(this.context);
        });
    }
}

const game = new Pong('pongCanvas', 240);

// game.startAnimation();
//
// window.addEventListener('visibilitychange', (e) => {
//     console.log('vis', e);
// });
//
// window.onblur = (e) => {
//     console.log('blur', e);
// };
//
// window.onfocus = (e) => {
//     console.log('foc', e);
// };
