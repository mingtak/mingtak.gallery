# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from mingtak.gallery.testing import MINGTAK_GALLERY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.gallery is properly installed."""

    layer = MINGTAK_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.gallery is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.gallery'))

    def test_browserlayer(self):
        """Test that IMingtakGalleryLayer is registered."""
        from mingtak.gallery.interfaces import (
            IMingtakGalleryLayer)
        from plone.browserlayer import utils
        self.assertIn(IMingtakGalleryLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['mingtak.gallery'])

    def test_product_uninstalled(self):
        """Test if mingtak.gallery is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.gallery'))

    def test_browserlayer_removed(self):
        """Test that IMingtakGalleryLayer is removed."""
        from mingtak.gallery.interfaces import IMingtakGalleryLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMingtakGalleryLayer, utils.registered_layers())
