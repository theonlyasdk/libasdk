/* The Logger class provides methods for logging messages with a specified prefix and additional features. */
class Logger {
    constructor(prefix, options = {}) {
        this.prefix = prefix;
        this.enabled = options.enabled ?? true;
        this.timeStamp = options.timeStamp ?? true;
        this.logLevel = options.logLevel ?? 'info';
        this.levels = {
            debug: 0,
            info: 1,
            warn: 2,
            error: 3
        };
    }

    buildString = (string) => {
        if (!this.enabled) return '';
        const time = this.timeStamp ? `[${new Date().toISOString()}] ` : '';
        return `${time}${this.prefix}: ${string}`;
    }

    error = (string) => {
        if (this.levels[this.logLevel] <= this.levels.error) {
            console.error(this.buildString(string));
        }
    }

    log = (string) => {
        if (this.levels[this.logLevel] <= this.levels.info) {
            console.log(this.buildString(string));
        }
    }

    warn = (string) => {
        if (this.levels[this.logLevel] <= this.levels.warn) {
            console.warn(this.buildString(string));
        }
    }

    debug = (string) => {
        if (this.levels[this.logLevel] <= this.levels.debug) {
            console.debug(this.buildString(string));
        }
    }

    setLogLevel = (level) => {
        if (this.levels.hasOwnProperty(level)) {
            this.logLevel = level;
        }
    }

    enable = () => this.enabled = true;
    disable = () => this.enabled = false;
}
