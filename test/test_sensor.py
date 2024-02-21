import unittest

from mqtt_homeassistant_utils import HASensor, HASensorEnergy, HASensorTemperature, HASensorBattery

class TestHASensor(unittest.TestCase):
    def test_mandatory_attributes(self):
        testDict = HASensor(name="MyTestSensor", node_id="justATest").to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestSensor")

        self.assertNotIn("component", testDict)
        self.assertNotIn("node_id", testDict)
        self.assertNotIn("discovery_prefix", testDict)


        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestsensor")

        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "justATest/values")


    def test_mandatory_missing(self):
        with self.assertRaises(TypeError):
            mySensor = HASensor(node_id="justATest")

    def test_own_uniqueid(self):
        testDict = HASensor(name="MyTestSensor", node_id="justATest", unique_id="uid").to_dict()
        
        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "uid")

    def test_own_statetopic(self):
        testDict = HASensor(name="MyTestSensor", node_id="justATest", state_topic="state/topic").to_dict()
        
        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "state/topic")

class TestHASensorEnergy(unittest.TestCase):
    def test_default_paramters(self):
        testDict = HASensorEnergy(name="MyTestSensor", node_id="justATest").to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestSensor")

        self.assertNotIn("component", testDict)
        self.assertNotIn("node_id", testDict)
        self.assertNotIn("discovery_prefix", testDict)

        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestsensor")

        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "justATest/values")

        self.assertIn("device_class", testDict)
        self.assertEqual(testDict["device_class"], "energy")

        self.assertIn("state_class", testDict)
        self.assertEqual(testDict["state_class"], "measurement")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "kWh")

    def test_override_paramters(self):
        testDict = HASensorEnergy(name="MyTestSensor", node_id="justATest", state_class="increasing", unit_of_measurement="mWh").to_dict()

        #check for attributes
        self.assertIn("state_class", testDict)
        self.assertEqual(testDict["state_class"], "increasing")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "mWh")

class TestHASensorTemperature(unittest.TestCase):
    def test_default_paramters(self):
        testDict = HASensorTemperature(name="MyTestSensor", node_id="justATest").to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestSensor")

        self.assertNotIn("component", testDict)
        self.assertNotIn("node_id", testDict)
        self.assertNotIn("discovery_prefix", testDict)

        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestsensor")

        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "justATest/values")

        self.assertIn("device_class", testDict)
        self.assertEqual(testDict["device_class"], "temperature")

        self.assertIn("state_class", testDict)
        self.assertEqual(testDict["state_class"], "measurement")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "°C")

    def test_override_paramters(self):
        testDict = HASensorTemperature(name="MyTestSensor", node_id="justATest", state_class="increasing", unit_of_measurement="°F").to_dict()

        #check for attributes
        self.assertIn("state_class", testDict)
        self.assertEqual(testDict["state_class"], "increasing")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "°F")

class TestHASensorEnergy(unittest.TestCase):
    def test_default_paramters(self):
        testDict = HASensorBattery(name="MyTestSensor", node_id="justATest").to_dict()

        #check for attributes
        self.assertIn("name", testDict)
        self.assertEqual(testDict["name"], "MyTestSensor")

        self.assertNotIn("component", testDict)
        self.assertNotIn("node_id", testDict)
        self.assertNotIn("discovery_prefix", testDict)


        self.assertIn("unique_id", testDict)
        self.assertEqual(testDict["unique_id"], "justATest_mytestsensor")

        self.assertIn("state_topic", testDict)
        self.assertEqual(testDict["state_topic"], "justATest/values")

        self.assertIn("device_class", testDict)
        self.assertEqual(testDict["device_class"], "battery")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "%")

    def test_override_paramters(self):
        testDict = HASensorBattery(name="MyTestSensor", node_id="justATest", state_class="increasing", unit_of_measurement="mAh").to_dict()

        #check for attributes
        self.assertIn("state_class", testDict)
        self.assertEqual(testDict["state_class"], "increasing")

        self.assertIn("unit_of_measurement", testDict)
        self.assertEqual(testDict["unit_of_measurement"], "mAh")        

if __name__ == '__main__':
    unittest.main()    