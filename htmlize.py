import pystache

import json
import os
import re

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


def get_project_filename(project):
    title = project.get('titleShort', project['title'])
    title = title.lower()
    title = re.sub('[!@#$\'\. ,:&]+', '-', title)
    title = title.strip('-')
    return title + '.html'


def years_human(project):
    year_from, year_to = project['years']
    if year_to is None:
        return '{0} - present'.format(year_from)
    if year_from == year_to:
        return '{0}'.format(year_from)
    return '{0} - {1}'.format(year_from, year_to)


def normalize_project(project):
    project['filename'] = get_project_filename(project)
    project['years'] = years_human(project)
    return project


def make_index_page(projects, tags):
    html = render('index', {
        'pageTitle': 'Evan Savage',
        'projects': projects,
        'tags': tags
    })
    make_page('index.html', html)


def make_project_pages(projects):
    for project in projects:
        html = render('projectPage', {
            'pageTitle': project['title'] + ' - Evan Savage',
            'project': project
        })
        make_page(project['filename'], html)


def load_json(name):
    fname = name
    if not fname.endswith('.json'):
        fname += '.json'
    fpath = os.path.join(IN_DIR, fname)
    with open(fpath) as jsonFile:
        return json.load(jsonFile)


def main():
    projects = load_json('projects')
    projects = list(map(normalize_project, projects))
    tags = load_json('tags')
    make_index_page(projects, tags)
    make_project_pages(projects)


if __name__ == '__main__':
    main()
