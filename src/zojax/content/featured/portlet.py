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
from zojax.catalog.interfaces import ICatalog
from zope.app.intid.interfaces import IIntIds
from zope.traversing.api import getRoot
"""

$Id$
"""
from zope import interface
from zope.component import getUtility, queryUtility
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zope.dublincore.interfaces import IDCTimes

from interfaces import IContentFeaturedPortlet, IContentFeaturedConfiglet


class ContentFeaturedPortlet(object):
    interface.implements(IContentFeaturedPortlet)

    items = []
    siteUrl = None
    index = 'modified'

    def isAvailable(self):
        return bool(self.items)

    def update(self):
        self.site = getSite()
        self.siteUrl = absoluteURL(self.site, self.request)
        catalog = queryUtility(ICatalog)
        if catalog is not None:
            ids = queryUtility(IIntIds)
            query = dict(isDraft={'any_of': (False,)},
                         #searchContext=getRoot(self.site),
                         isFeatured={'any_of': (True,)},
                         sort_order='reverse', sort_on=self.index)

            if self.contentTypes:
                query['type'] = {'any_of': self.contentTypes,}

            if '__all__' not in self.spaces:
                query['contentSpaces']= {'any_of': self.spaces}

            results = []
            for item in catalog.searchResults(**query)[:self.count]:
                results.append({'item': item,
                                'modified': IDCTimes(item).modified})
            self.items = results
