# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingtak.gallery


class MingtakGalleryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=mingtak.gallery)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingtak.gallery:default')


MINGTAK_GALLERY_FIXTURE = MingtakGalleryLayer()


MINGTAK_GALLERY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGTAK_GALLERY_FIXTURE,),
    name='MingtakGalleryLayer:IntegrationTesting'
)


MINGTAK_GALLERY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGTAK_GALLERY_FIXTURE,),
    name='MingtakGalleryLayer:FunctionalTesting'
)


MINGTAK_GALLERY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGTAK_GALLERY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MingtakGalleryLayer:AcceptanceTesting'
)
