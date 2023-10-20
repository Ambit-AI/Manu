function hello(hello)
{
    console.log(hello);
}

hello("hello");

//console.log(window)

//global
// setTimeout()
// clearTimeout
// setInterval()
// clearInterval()

// window.console.log()

var message = "hi";

globalThis.console.log(message)

//console.log(module)

//const logger = require('./logger');
//console.log(logger)
//logger.log("message")

const os = require('os')

// var totalMem = os.totalmem();
// var freeMem = os.freemem();

//console.log('Total Memory: ' + totalMem);
// console.log(`Total Memory: ${totalMem}`);
// console.log(`Total Free Memory: ${freeMem}`);

// const EventEmitter = require('events');
// const emitter = new EventEmitter();





// const Logger = require('./logger');
// const logger = new Logger;


// logger.on('MessageLogged', (arg) => {
//     console.log('Listener called', arg)
// })

// logger.log('message');

const http = require('http');

const server = http.createServer((req, res) =>{
    if(req.url == '/')
    {
        res.write('Hello');
        res.end();
    }

    if(req.url === '/api/courses')
    {
        res.write(JSON.stringify([1,2,3]));
        res.end();
    }
});
// server.on('connection', (socket) => {
//     console.log('new connection');
// })
server.listen(3000);
console.log('Listening on port 3000...')