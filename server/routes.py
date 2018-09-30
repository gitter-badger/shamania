from aiohttp import web

import handlers


routes = [
    web.get('/', handlers.index),
]

def setup_routes(app):
    app.router.add_routes(routes)
