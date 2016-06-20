# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class Gallery(base.ViewletBase):
    """  """
    def portal(self):
        return api.portal.get()


class Carousel(base.ViewletBase):
    """  """
    def portal(self):
        return api.portal.get()

