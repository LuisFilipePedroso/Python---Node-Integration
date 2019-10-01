from aiohttp import web
import socketio
import asyncio
import random

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

arr = {}

async def index(request):
    return web.json_response(arr)

@sio.on('message')
async def print_message(sid, message):
    await sio.emit('message', message)

@sio.event
async def connect(sid, environ):
    print('User has connected')

app.router.add_get('/', index)

async def emitMessage():
    while True:
        await sio.emit('message', 'Luis')
        number = random.randint(1, 500)
        key = 'N' + str(number)
        arr.update({key:number})
        await asyncio.sleep(5)

@sio.event
def emit(sid, environ):
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(emitMessage())
    loop.run_forever()

if __name__ == '__main__':
    web.run_app(app, port = 5000)
    

