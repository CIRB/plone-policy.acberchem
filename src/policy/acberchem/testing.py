from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import FunctionalTesting

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import policy.acberchem


POLICY_ACBERCHEM = PloneWithPackageLayer(
    zcml_package=policy.acberchem,
    zcml_filename='configure.zcml',
    gs_profile_id='policy.acberchem:default',
    name='POLICY_ACBERCHEM'
    )


POLICY_ACBERCHEM_ROBOT_TESTING = FunctionalTesting(
    bases=(POLICY_ACBERCHEM, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="POLICY_ACBERCHEM_ROBOT_TESTING")
