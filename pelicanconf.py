#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
STATIC_PATHS = ['images', 'papers', 'customstyles']
EXTRA_PATH_METADATA = {
    'customstyles/custom.css': {'path':'custom.css'},
    }


AVATAR = '/images/Mike_IceCreamSocialHeadshot.jpg'
ABOUT_ME = '''<strong>Mike Hughes</strong>
	<br />mike@michaelchughes.com
	<br />
	<br />Postdoctoral fellow
	<br /><a href="http://www.seas.harvard.edu/">SEAS Computer Science</a>
	<br />Harvard University
	'''

HIDE_SIDEBAR = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
	('Papers', '/papers.html'),
	('CV', '/cv.html'),
	('Bio', '/bio.html'),
	]

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False

