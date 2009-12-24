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
from zojax.catalog.utils import Indexable
from zc.catalog.catalogindex import ValueIndex

from interfaces import IContentFeaturedAware, IContentFeaturable


def isFeatured():
    return ValueIndex(
        'isFeatured',
        Indexable('zojax.content.featured.indexes.IsFeaturedChecker'))


class IsFeaturedChecker(object):
    """
    >>> from zojax.content.type.item import Item
    >>> from zope import interface
    >>> class Content(Item):
    ...     interface.implements(IContent)

    >>> content = Content()
    >>> IsFeaturedChecker(content).isFeatured
    False

    >>> from zojax.content.featured.interfaces import IContentFeaturedAware
    >>> interface.alsoProvides(content, IContentFeaturedAware)

    >>> IsDraftChecker(content).isFeatured
    True
    """

    def __init__(self, content, default=None):
        self.isFeatured = default
        if IContentFeaturable.providedBy(content):
            self.isFeatured = IContentFeaturedAware.providedBy(content)
