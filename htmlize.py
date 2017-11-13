import pystache

import json
import os

ROOT = os.path.dirname(os.path.realpath(__file__))
IN_DIR = os.path.join(ROOT, 'content')
PROJECTS_FILENAME = os.path.join(IN_DIR, 'projects.json')
OUT_DIR = os.path.join(ROOT, 'build')

RENDERER = pystache.Renderer(search_dirs=[IN_DIR])
TEMPLATE_CACHE = {}


def render(template_name, data):
    if template_name not in TEMPLATE_CACHE:
        template_path = os.path.join(IN_DIR, template_name + '.mustache')
        with open(template_path) as template_file:
            template_str = template_file.read()
            TEMPLATE_CACHE[template_name] = pystache.parse(template_str)
    return RENDERER.render(TEMPLATE_CACHE[template_name], data)


def make_page(filename, html):
    path = os.path.join(OUT_DIR, filename)
    print('Generating {0}...'.format(path))
    with open(path, 'w') as f:
        f.write(html)


def make_index_page(tags):
    html = render('index', {
        'pageTitle': 'Evan Savage',
        'tags': tags
    })
    make_page('index.html', html)


def load_json(name):
    fname = name
    if not fname.endswith('.json'):
        fname += '.json'
    fpath = os.path.join(IN_DIR, fname)
    with open(fpath) as jsonFile:
        return json.load(jsonFile)


def main():
    tags = load_json('tags')
    make_index_page(tags)


if __name__ == '__main__':
    main()
