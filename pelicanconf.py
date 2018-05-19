#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '/Users/crinaldi/Blog/theme'

########################################
# Plugins and Extensions
########################################
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']

MD_EXTENSIONS = ['codehilite(css_class=highlight)']
PLUGINS = ['ipynb.markup']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

AUTHOR = u'Chris Rinaldi'
SITENAME = u'Chris Rinaldi'
SITEURL = ''
DISQUS_SITENAME = "chrisrinaldi"
MAILCHIMP_FORM_ACTION = "https://github.us9.list-manage.com/subscribe/post?u=081c3e9463b18e38690f5894f&id=389be875d6"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'
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

# Social
SOCIAL_PROFILE_LABEL = ' '
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/cgrinaldi/'),
          ('Github', 'http://github.com/cgrinaldi'),
          ('Twitter', 'http://twitter.com/cgrinaldi'),
          ('Email', 'mailto:cgrinaldi@gmail.com'))

DEFAULT_PAGINATION = 10

########################################
# About Me and Projects
########################################

# PROJECTS = [
#     {
#         'name': '',
#         'url': '',
#         'description': ''
#     }
# ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
