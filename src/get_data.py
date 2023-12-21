"""Contains helper functions that retrieve corresponding data for pages."""

import json
from pathlib import Path

SRC = Path('./src')
DATA = Path(SRC / 'data')

PROJECTS = Path(DATA / 'projects.json')
EXPERIENCE = Path(DATA / 'experience.json')
COURSEWORK = Path(DATA / 'coursework.json')


def get_projects():
    """Returns personal projects data."""
    with open(PROJECTS, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_experience():
    """Returns experience data."""
    with open(EXPERIENCE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_coursework():
    """Returns coursework data."""
    with open(COURSEWORK, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_index():
    """Returns index data. Landing page content will be delivered here."""
    context = {
        "projects": get_projects(),
        "experience": get_experience(),
        "coursework": get_coursework()
    }
    # print(context)
    return context
