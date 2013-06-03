#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mihai Mocanu'
SITENAME = u'blog'
SITEURL = 'http://mvmocanu.github.io/blog.mvmocanu.com/'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'ro'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = "feeds/all.rss.xml"
TAG_FEED_RSS = "feeds/%s.rss.xml"

FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/%s.atom.xml"

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

MAIL_USERNAME = 'contact'
MAIL_HOST = 'mvmocanu.com'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PATH = 'content'
THEME = 'theme'

DISQUS_SITENAME = "bmvm"
#GOOGLE_ANALYTICS_ACCOUNT = "UA-822534-14"
#GOOGLE_ANALYTICS_DOMAIN = 'ionelmc.ro'

SECTIONS = [
    ('Blog', 'index.html'),
    ('Cu bicicleta', 'category/cu-bicicleta.html'),
    ('Arhivă', 'archives.html'),
    ('Tag-uri', 'tags.html'),
    #('Projects', 'projects.html'),
]
TAG_CLOUD_STEPS = 6
#~ TYPOGRIFY = True

PLUGINS = (
    #'sitemap',
)

#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.5,
#        'indexes': 0.5,
#        'pages': 0.5
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}

FILES_TO_COPY = [
    #('extra/robots.txt', 'robots.txt'),
    #('extra/CNAME', 'CNAME'),
    #('extra/favicon.ico', 'favicon.ico'),
]
STATIC_PATHS = ['images']

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'
