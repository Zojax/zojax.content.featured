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
from zope import interface, component
from zope.component import getUtility

from zojax.activity.record import ActivityRecord
from zojax.activity.interfaces import IActivity, IActivityRecordDescription
from zojax.content.activity.interfaces import IContentActivityRecord
from zojax.content.activity.record import ContentActivityRecord

from interfaces import _, IFeaturedActivityRecord, IContentFeaturable


class FeaturedActivityRecord(ContentActivityRecord):
    interface.implements(IFeaturedActivityRecord, IContentActivityRecord)

    type = u'featured'
    verb = _('made featured')


class FeaturedActivityRecordDescription(object):
    interface.implements(IActivityRecordDescription)

    title = _(u'Featured')
    description = _(u'Content object was made featured.')


def featuredAddedHandler(content):
    getUtility(IActivity).add(content, FeaturedActivityRecord())
