import unittest

from mqtt_homeassistant_utils import HADevice, HAAvailability

class TestHADevice(unittest.TestCase):
    def test_hadevice(self):
        modelstring = "aNiceModel"
        testDict = HADevice(model=modelstring).to_dict()

        #check for attributes
        self.assertIn("model", testDict)
        self.assertEqual(testDict["model"], modelstring)

        self.assertNotIn("sw_version", testDict)

class TestHAAvailability(unittest.TestCase):
    def test_haavailability_mandatory(self):
        path_string = "path/to/topic"

        testDict = HAAvailability(topic=path_string).to_dict()

        #check for attributes
        self.assertIn("topic", testDict)
        self.assertEqual(testDict["topic"], path_string)

        self.assertNotIn("payload_available", testDict)

    def test_haavailability_mandatory_missing(self):
        
        with self.assertRaises(TypeError):
            myAv = HAAvailability(payload_available="off")

if __name__ == '__main__':
    unittest.main()    