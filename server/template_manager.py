from jinja2 import Environment, FileSystemLoader, select_autoescape

from . import config


class TemplateManager:

    env = Environment(
        loader=FileSystemLoader(config.TEMPLATES_PATH),
        enable_async=True,
    )

    @classmethod
    async def render_template(cls, template_name, data):
        template = cls.env.get_template(
            '{}{}'.format(template_name, config.TEMPLATE_EXTENSION)
        )
        return await template.render_async(**data)
