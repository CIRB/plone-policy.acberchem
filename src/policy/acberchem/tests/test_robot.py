from plone.testing import layered
import robotsuite
import unittest

from policy.acberchem import POLICY_ACBERCHEM_ROBOT_TESTING
import cirb.testplone

def test_suite():
    suite = unittest.TestSuite()
    robot_files = [
            'keywords.robot',
        ]

    for robot_file in robot_files:
        suite.addTests([
            layered(
                robotsuite.RobotTestSuite(robot_file, 
                                            package=cirb.testplone), 
                layer=POLICY_ACBERCHEM_ROBOT_TESTING)
        ])
    
    return suite
