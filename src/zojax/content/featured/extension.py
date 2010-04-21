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
from rwproperty import getproperty, setproperty

from zope import interface
from zope.proxy import removeAllProxies

from interfaces import IContentFeatured, IContentFeaturedAware


class ContentFeaturedExtension(object):

    @getproperty
    def enabled(self):
        return self.data.get('enabled', IContentFeatured['enabled'].default)

    @setproperty
    def enabled(self, value):
        context = removeAllProxies(self.context)
        
        del self.data['enabled']

        if value is None or not value:
            if IContentFeaturedAware.providedBy(context):
                interface.noLongerProvides(context, IContentFeaturedAware)
            self.data['enabled'] = False
        else:
            if not IContentFeaturedAware.providedBy(context):
                interface.alsoProvides(context, IContentFeaturedAware)

            self.data['enabled'] = value
