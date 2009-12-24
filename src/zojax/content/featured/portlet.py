##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
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
from zope import interface
from zope.component import getUtility
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zope.dublincore.interfaces import IDCTimes

from interfaces import IContentFeaturedPortlet, IContentFeaturedConfiglet


class ContentFeaturedPortlet(object):
    interface.implements(IContentFeaturedPortlet)

    items = []
    siteUrl = None

    def isAvailable(self):
        return bool(self.items)

    def update(self):
        configlet = getUtility(IContentFeaturedConfiglet)
        cnt = 0
        items = []
        for item in configlet.getContentTypeFeatured(self.contentTypes):
            items.append({'item': item,
                          'modified': IDCTimes(item).modified})
            cnt += 1
            if self.count is not None and self.count and self.count <= cnt:
                break
        self.items = items
        self.siteUrl = absoluteURL(getSite(), self.request)

        super(ContentFeaturedPortlet, self).update()
