from aiohttp import web
from .routes import index

app = web.Application()

app.router.add_get('/', index)

web.run_app(app, host='127.0.0.1', port=8080)
