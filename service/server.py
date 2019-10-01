from aiohttp import web
import socketio
import asyncio

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def index(request):
    return web.Response(text="Hello World", content_type='text/html')

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
        await asyncio.sleep(5)

@sio.event
def emit(sid, environ):
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(emitMessage())
    loop.run_forever()

if __name__ == '__main__':
    web.run_app(app, port = 5000)
    

