#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Michael C. Hughes'
SITENAME = u'Michael C. Hughes'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
SOCIAL = None

# Theme is pelican-bootstrap3
THEME = 'theme'
BOOTSTRAP_THEME = 'simplex'

SITELOGO = 'images/logo.jpg'
SITELOGO_SIZE = 40
FAVICON = 'images/favicon.ico'

CUSTOM_CSS = 'custom.css'
STATIC_PATHS = ['images', 'talks', 'papers', 'customstyles']
EXTRA_PATH_METADATA = {
    'customstyles/custom.css': {'path':'custom.css'},
    }


AVATAR = '/images/Mike_Headshot_201805.jpg'
ABOUT_ME = '''<strong>Mike Hughes</strong>
	<br />mike@michaelchughes.com
    <br />Twitter: <a href="https://www.twitter.com/mike_c_hughes">@mike_c_hughes</a>
	<br />
	<br />Assistant Professor 
    <br /><a href="https://www.cs.tufts.edu/">Dept. of Computer Science</a>
    <br /><a href="https://www.tufts.edu/">Tufts University</a>
    <br />
    <br />Office: Halligan 210
	'''

HIDE_SIDEBAR = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
	('Papers', '/papers.html'),
	('CV', '/cv.html'),
	('Bio', '/bio.html'),
    ('Research', '/research.html'),
	]

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False


# Sitemap pluging

PLUGIN_PATHS = [os.path.expandvars("$HOME/git/pelican-plugins/")]

PLUGINS=['sitemap']

SITEMAP = {
    'exclude': [
    	'archives.html',
    	'categories.html',
    	'tags.html',
    	'tag/', 'category/', 'feeds/'],
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'pages': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly',
    }
}
