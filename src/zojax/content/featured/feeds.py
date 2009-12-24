##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
import time, rfc822
from zope import interface, component
from zope.component import getUtility
from zope.traversing.browser import absoluteURL
from zope.dublincore.interfaces import IDCTimes
from zope.app.component.interfaces import ISite

from zojax.catalog.interfaces import ICatalog
from zojax.content.feeds.rss2 import RSS2Feed

from interfaces import _, IFeaturedRSSFeed, IContentFeaturedConfiglet


class FeaturedRSSFeed(RSS2Feed):
    component.adapts(ISite)
    interface.implementsOnly(IFeaturedRSSFeed)

    name = u'featured'
    title = _(u'Featured')
    description = _(u'List of all available featured content.')

    def items(self):
        request = self.request
        configlet = getUtility(IContentFeaturedConfiglet)
        contents = configlet.getContentTypeFeatured()

        for content in contents[:15]:
            yield {
                'title': content.title,
                'description': content.description,
                'guid': '%s/'%absoluteURL(content, request),
                'isPermaLink': True,
                'pubDate': rfc822.formatdate(time.mktime(
                        IDCTimes(content).modified.timetuple())),}
