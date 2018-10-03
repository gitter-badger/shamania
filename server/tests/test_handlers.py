from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web

from .. import handlers
from .. import config

class TestIndexHandler(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/', handlers.index)
        return app

    @unittest_run_loop
    async def test_content(self):
        resp = await self.client.request('GET', '/')
        assert resp.status == 200
        text = await resp.text()
        assert "Welcome on {}".format(config.APP_NAME) == text
