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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory
from zojax.widget.checkbox.field import CheckboxList
from zojax.content.type.interfaces import IItem
from zojax.content.feeds.interfaces import IRSS2Feed

_ = MessageFactory('zojax.content.featured')


class IContentFeatured(interface.Interface):

    enabled = schema.Bool(
        title = _('Featured'),
        description = _('Featured content marker'),
        default=False)


class IContentFeaturable(interface.Interface):
    """Marker interface for featurable content."""


class IContentFeaturedAware(interface.Interface):
    """Content featured aware"""


class IContentFeaturedConfiglet(interface.Interface):
    """Content featured configlet """

    def getContentTypeFeatured(ct):
        """Return featured content for content type."""

    def listFeaturableContentTypes():
        """Return list of featurable content types."""


class IContentFeaturedPortlet(interface.Interface):
    """ Content featured portlet """

    label = schema.TextLine(
        title = _(u'Label'),
        required = False)

    count = schema.Int(
        title = _(u'Featured count'),
        description = _('Number of featured content items in portlet.'),
        default = 20,
        required = True)

    contentTypes = CheckboxList(
        title = _(u'Featured conten types'),
        description = _(u'Select featured types to use in this portlet.'),
        vocabulary = 'content.featured.types',
        default = [],
        required = False)


class IFeaturedRSSFeed(IRSS2Feed):
    """ featured rss feed """


class IFeaturedActivityRecord(interface.Interface):
    """ featured activity record """
