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
from zope import interface
from zope.component import getUtility
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.schema.interfaces import IVocabulary, IVocabularyFactory

from interfaces import IContentFeaturedConfiglet


class Vocabulary(SimpleVocabulary):

    def getTerm(self, value):
        try:
            return self.by_value[value]
        except KeyError:
            return self.by_value[self.by_value.keys()[0]]


class FeaturedContentTypesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        configlet = getUtility(IContentFeaturedConfiglet)
        terms = []
        keys = []
        for name, ct in configlet.listFeaturableContentTypes():
            term = SimpleTerm(ct.name, ct.name, ct.title)
            term.description = ct.description
            if ct.name in keys:
                continue
            terms.append((ct.title, ct.name, term))
            keys.append(ct.name)
        terms.sort()
        return Vocabulary([term for t,n,term in terms])
