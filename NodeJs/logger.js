

const EventEmitter = require('events');
//const emitter = new EventEmitter();
var url = 'http://mylogger.io/log';

class Logger extends EventEmitter{
    log(message)
    {
        console.log(message);
    
        this.emit('MessageLogged', { id: 1, url: 'http://'});
    
    }
}


module.exports = Logger;
module.exports.endPoint = url;