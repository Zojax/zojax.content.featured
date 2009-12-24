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
from zope.component import getUtility, getUtilitiesFor
from zojax.catalog.interfaces import ICatalog
from zojax.content.type.interfaces import IContentType

from interfaces import _
from interfaces import \
    IContentFeatured, IContentFeaturable, IContentFeaturedConfiglet


class ContentFeaturedConfiglet(object):
    interface.implements(IContentFeaturedConfiglet)

    title = _('Content featured')

    def listFeaturableContentTypes(self):
        return [(name, ct) for name, ct
                in getUtilitiesFor(IContentType)
                if IContentFeaturable.implementedBy(ct.klass)]

    def getContentTypeFeatured(self, cts=()):
        query = dict(sort_on = 'modified',
                     isFeatured={'any_of': (True,)},
                     sort_order='reverse')
        if cts:
            query['type'] = {'any_of': cts,}

        return getUtility(ICatalog).searchResults(**query)

    def isAvailable(self):
        return False
