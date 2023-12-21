# MQTT Home Assistant Utils

A helper project designed to facilitate working with the MQTT integration in Home Assistant.

## Overview

This repository contains Python code for generating Home Assistant (HA) MQTT discovery payloads. These payloads are used to configure sensors and binary sensors in Home Assistant via MQTT.

## File Structure

- `mqtt_homeassistant_utils.py`: Python script containing the data classes and enums for generating HA MQTT discovery payloads.

## Usage

To use the provided code, you can create instances of the defined data classes, configure their properties, and publish the MQTT discovery messages. Here's a basic example:

```python
# Import necessary classes
from mqtt_homeassistant_utils import HASensor, HADeviceClassSensor
import paho.mqtt.client as mqtt

# Create a sensor instance
sensor = HASensor(
    component="sensor",
    node_id="node1",
    unique_id="temperature_sensor",
    name="Temperature Sensor",
    state_topic="sensor/temperature",
    device_class=HADeviceClassSensor.TEMPERATURE,
    unit_of_measurement="°C"
)

# Configure MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect("mqtt_broker_address", 1883)

# Publish the MQTT discovery payload
sensor.publish(mqtt_client, qos=1)
```

Make sure to customize the configurations according to your specific setup.

## Initial Development

This project was initially developed for personal use in my own Home Assistant projects. While it's tailored to my specific needs, I welcome feedback and contributions. If you have specific entries you'd like to see added, feel free to open a request!

## Enums

The code includes two enum classes:

* `HADeviceClassSensor`: Enum for sensor device classes.
* `HADeviceClassBinarySensor`: Enum for binary sensor device classes.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License.