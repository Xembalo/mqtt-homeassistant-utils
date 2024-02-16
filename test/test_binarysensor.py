import unittest

from mqtt_homeassistant_utils import HABinarySensor

class TestHABinarySensor(unittest.TestCase):
    def test_mandatory_attributes(self):
        testDict = HABinarySensor(name="MyTestSensor", node_id="justATest").to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestSensor")

        self.assertIn("component", testDict)
        self.assertEqual(testDict["component"], "binary_sensor")
        
        self.assertIn("discovery_prefix", testDict)
        self.assertEqual(testDict["discovery_prefix"], "homeassistant")

        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestsensor")

        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "justATest/values")

        self.assertIn("node_id", testDict)
        self.assertEqual(testDict["node_id"], "justATest")

    def test_mandatory_missing(self):
        
        with self.assertRaises(TypeError):
            myBinarySensor = HABinarySensor(node_id="justATest")

    def test_own_uniqueid(self):
        testDict = HABinarySensor(name="MyTestSensor", node_id="justATest", unique_id="uid").to_dict()
        
        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "uid")

    def test_own_statetopic(self):
        testDict = HABinarySensor(name="MyTestSensor", node_id="justATest", state_topic="state/topic").to_dict()
        
        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "state/topic")
        
if __name__ == '__main__':
    unittest.main()    