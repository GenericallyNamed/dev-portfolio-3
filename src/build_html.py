"""Builds HTML files from templates."""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from get_data import get_index

TEMPLATES = Path('./src/templates')
BUILD = Path('./build')


def render_template(template, output, **kwargs):
    """Renders a template file with the given arguments."""
    env = Environment(loader=FileSystemLoader(template))
    template = env.get_template(template)
    with open(output, 'w', encoding='utf-8') as f:
        f.write(template.render(**kwargs))


render_template(TEMPLATES / 'index.html', BUILD /
                'index.html', context=get_index())
