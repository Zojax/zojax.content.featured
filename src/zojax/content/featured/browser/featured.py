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
from zope.component import getUtility, queryMultiAdapter
from zope.traversing.browser import absoluteURL
from zope.schema.interfaces import IVocabularyFactory

from zojax.content.featured.interfaces import \
    IContentFeaturedConfiglet, IContentFeatured


class FeaturedWorkspace(object):

    def update(self):
        if self.request._traversed_names[-1] != '':
            self.request._traversed_names.append('')

        self.voc = getUtility(
            IVocabularyFactory, 'content.featured.types')(self.context)

        super(FeaturedWorkspace, self).update()

    def publishTraverse(self, request, name):
        view = queryMultiAdapter((self, request), name=name)
        if view is not None:
            return view

        configlet = getUtility(IContentFeaturedConfiglet)

        self.itemslst = configlet.getContentTypeFeatured(name)
        return self
