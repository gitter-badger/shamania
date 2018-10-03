from aiohttp import web

import .config
from .routes import setup_routes


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    web.run_app(app)
