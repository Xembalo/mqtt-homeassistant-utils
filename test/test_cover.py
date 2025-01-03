import unittest

from mqtt_homeassistant_utils import HACover, HADeviceClassCover

class TestHACover(unittest.TestCase):
    def test_mandatory_attributes(self):
        testDict = HACover(name="MyTestCover", node_id="justATest", device_class=HADeviceClassCover.SHUTTER).to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestCover")

        self.assertNotIn("component", testDict)
        self.assertNotIn("node_id", testDict)
        self.assertNotIn("discovery_prefix", testDict)


        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestcover")

        self.assertIn("mode_state_topic", testDict)
        self.assertEqual(testDict["mode_state_topic"], "justATest/values")


    def test_mandatory_missing(self):
        with self.assertRaises(TypeError):
            myCover = HACover(node_id="justATest")

    def test_own_uniqueid(self):
        testDict = HACover(name="MyTestCover", node_id="justATest", unique_id="uid").to_dict()
        
        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "uid")

    def test_own_statetopic(self):
        testDict = HACover(name="MyTestCover", node_id="justATest", mode_state_topic="state/topic").to_dict()
        
        self.assertIn("mode_state_topic", testDict)
        self.assertEqual(testDict["mode_state_topic"], "state/topic")

if __name__ == '__main__':
    unittest.main()    