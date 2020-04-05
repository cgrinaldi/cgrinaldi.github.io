#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Rinaldi'
SITENAME = 'Chris Rinaldi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = '/Users/chrisrinaldi/Repositories/blog/theme'


PLUGIN_PATHS = ['/Users/chrisrinaldi/Repositories/pelican-plugins']
PLUGINS = ['sitemap', 'pelican-ipynb.markup']

MARKUP = ('md', 'ipynb')
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_USE_METACELL = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_PROFILE_LABEL = ' '
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/cgrinaldi/'),
          ('Github', 'http://github.com/cgrinaldi'),
          ('Twitter', 'http://twitter.com/cgrinaldi'),
          ('Email', 'mailto:cgrinaldi@gmail.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
