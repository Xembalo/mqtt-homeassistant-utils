from dataclasses import dataclass, asdict, field
from typing import Optional, Union, Any, Dict, Tuple
from enum import Enum

import json
import paho.mqtt.client as mqtt


class HADeviceClassSensor(Enum):
    NONE = None
    APPARENT_POWER = "apparent_power"
    AQI = "aqi"
    ATMOSPHERIC_PRESSURE = "atmospheric_pressure"
    BATTERY = "battery"
    CARBON_DIOXIDE = "carbon_dioxide"
    CARBON_MONOXIDE = "carbon_monoxide"
    CURRENT = "current"
    DATA_RATE = "data_rate"
    DATA_SIZE = "data_size"
    DATE = "date"
    DISTANCE = "distance"
    DURATION = "duration"
    ENERGY = "energy"
    ENERGY_STORAGE = "energy_storage"
    ENUM = "enum"
    FREQUENCY = "frequency"
    GAS = "gas"
    HUMIDITY = "humidity"
    ILLUMINANCE = "illuminance"
    IRRADIANCE = "irradiance"
    MOISTURE = "moisture"
    MONETARY = "monetary"
    NITROGEN_DIOXIDE = "nitrogen_dioxide"
    NITROGEN_MONOXIDE = "nitrogen_monoxide"
    NITROUS_OXIDE = "nitrous_oxide"
    OZONE = "ozone"
    PH = "ph"
    PM1 = "pm1"
    PM25 = "pm25"
    PM10 = "pm10"
    POWER_FACTOR = "power_factor"
    POWER = "power"
    PRECIPITATION = "precipitation"
    PRECIPITATION_INTENSITY = "precipitation_intensity"
    PRESSURE = "pressure"
    REACTIVE_POWER = "reactive_power"
    SIGNAL_STRENGTH = "signal_strength"
    SOUND_PRESSURE = "sound_pressure"
    SPEED = "speed"
    SULPHUR_DIOXIDE = "sulphur_dioxide"
    TEMPERATURE = "temperature"
    TIMESTAMP = "timestamp"
    VOLATILE_ORGANIC_COMPOUNDS = "volatile_organic_compounds"
    VOLATILE_ORGANIC_COMPOUNDS_PARTS = "volatile_organic_compounds_parts"
    VOLTAGE = "voltage"
    VOLUME = "volume"
    VOLUME_STORAGE = "volume_storage"
    WATER = "water"
    WEIGHT = "weight"
    WIND_SPEED = "wind_speed"

class HADeviceClassBinarySensor(Enum):
    NONE = "None"
    BATTERY = "battery"
    BATTERY_CHARGING = "battery_charging"
    CARBON_MONOXIDE = "carbon_monoxide"
    COLD = "cold"
    CONNECTIVITY = "connectivity"
    DOOR = "door"
    GARAGE_DOOR = "garage_door"
    GAS = "gas"
    HEAT = "heat"
    LIGHT = "light"
    LOCK = "lock"
    MOISTURE = "moisture"
    MOTION = "motion"
    MOVING = "moving"
    OCCUPANCY = "occupancy"
    OPENING = "opening"
    PLUG = "plug"
    POWER = "power"
    PRESENCE = "presence"
    PROBLEM = "problem"
    RUNNING = "running"
    SAFETY = "safety"
    SMOKE = "smoke"
    SOUND = "sound"
    TAMPER = "tamper"
    UPDATE = "update"
    VIBRATION = "vibration"
    WINDOW = "window"
  


@dataclass
class __BaseDataClass():

    """ Base function for all Entries, like to_json """
    def to_json(self) -> str:
        data_dict = asdict(self)
        data_dict = self.remove_null_values(data_dict)
        json_data = json.dumps(data_dict, indent=2)
        return json_data

    def remove_null_values(self, obj: Union[Dict[str, Any], Any]) -> Union[Dict[str, Any], Any]:
        if isinstance(obj, list):
            return [self.remove_null_values(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.remove_null_values(value) for key, value in obj.items() if value is not None}
        elif isinstance(obj, Enum): 
            return obj.value if obj.value is not None else None
        elif hasattr(obj, '__dict__'):
            # Dataclass oder Objekt mit __dict__ (z.B. NamedTuple)
            return self.remove_null_values(asdict(obj))
        else:
            return obj
        

@dataclass(kw_only=True)
class __HAEntry(__BaseDataClass):
    discovery_prefix: str = "homeassistant"
    component: str = None
    node_id: str = None
    unique_id: str = None

    def publish(self, mqttClient: mqtt.Client, qos: int):
        mqttClient.publish(self.discovery_prefix + "/" + self.component + "/" + self.node_id + "/" + self.unique_id + "/config", self.to_json(), qos=qos, retain=True)
   

@dataclass(kw_only=True)
class HADevice(__BaseDataClass):
    """ Device Subentry for all integrations """
    configuration_url: Optional[str] = None
    connections: Optional[Tuple[Tuple[str, str]]] = None
    hw_version: Optional[str] = None
    identifiers: Union[str, Tuple[str], None] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    name: Optional[str] = None
    suggested_area: Optional[str] = None
    sw_version: Optional[str] = None
    via_device: Optional[str] = None

@dataclass(kw_only=True)
class HAAvailability(__BaseDataClass):
    topic: str

    payload_available: Optional[str] = None
    payload_not_available: Optional[str] = None
    value_template: Optional[str] = None

@dataclass(kw_only=True)
class HASensor(__HAEntry):
    name: str
    state_topic: str

    availability: Optional[Tuple[HAAvailability]] = None
    availability_mode: Optional[str] = None
    availability_template: Optional[str] = None
    availability_topic: Optional[str] = None
    device: Optional[HADevice] = None
    device_class: Optional[HADeviceClassSensor] = HADeviceClassSensor.NONE
    enabled_by_default: Optional[bool] = None
    encoding: Optional[str] = None
    entity_category: Optional[str] = None
    expire_after: Optional[int] = None
    force_update: Optional[bool] = None
    icon: Optional[str] = None
    json_attributes_template: Optional[str] = None
    json_attributes_topic: Optional[str] = None
    last_reset_value_template: Optional[str] = None
    object_id: Optional[str] = None
    payload_available: Optional[str] = None
    payload_not_available: Optional[str] = None
    suggested_display_precision: Optional[int] = None
    qos: Optional[int] = None
    state_class: Optional[int] = None
    unit_of_measurement: Optional[str] = None
    value_template: Optional[str] = None

    def __post_init__(self):
        self.component = "sensor"

@dataclass(kw_only=True)
class HASensorEnergy(HASensor):
    def __post_init__(self):
        super().__post_init__()
        self.device_class = HADeviceClassSensor.ENERGY
        self.state_class = "measurement"
        self.unit_of_measurement = "kWh"

@dataclass(kw_only=True)
class HASensorTemperature(HASensor):
    def __post_init__(self):
        super().__post_init__()
        self.device_class = HADeviceClassSensor.TEMPERATURE
        self.state_class = "measurement"
        self.unit_of_measurement = "°C"

@dataclass(kw_only=True)
class HASensorBattery(HASensor):
    def __post_init__(self):
        super().__post_init__()
        self.device_class = HADeviceClassSensor.BATTERY
        self.unit_of_measurement = "%"    

@dataclass(kw_only=True)
class HABinarySensor(__HAEntry):
    name: str
    state_topic: str
    availability: Optional[Tuple[HAAvailability]] = None
    availability_mode: Optional[str] = None
    availability_template: Optional[str] = None
    availability_topic: Optional[str] = None
    device: Optional[HADevice] = None
    device_class: Optional[HADeviceClassBinarySensor] = HADeviceClassBinarySensor.NONE
    enabled_by_default: Optional[bool] = None
    encoding: Optional[str] = None
    entity_category: Optional[str] = None
    expire_after: Optional[int] = None
    force_update: Optional[bool] = None
    icon: Optional[str] = None
    json_attributes_template: Optional[str] = None
    json_attributes_topic: Optional[str] = None
    object_id: Optional[str] = None
    off_delay: Optional[int] = None
    payload_off: Optional[str] = None
    payload_on: Optional[str] = None
    payload_available: Optional[str] = None
    payload_not_available: Optional[str] = None
    qos: Optional[int] = None
    value_template: Optional[str] = None

    
    def __post_init__(self):
        self.component = "binary_sensor"
 
