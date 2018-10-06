from aiohttp import web

import config
from template_manager import TemplateManager
from logger_manager import LoggerManager


logger = LoggerManager.get_logger(__name__)

async def index(request):
    log_msg = '[handler - index] handling {} from {}'
    logger.info(log_msg.format(str(request), request.remote))

    data = {'app_name': config.APP_NAME}
    rendered_index = await TemplateManager.render_template('index', data=data)

    return web.Response(text=rendered_index)
