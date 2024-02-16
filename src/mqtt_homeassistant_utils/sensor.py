from dataclasses import dataclass, field
from typing import Optional, ClassVar
from enum import Enum

from .base import __HAEntry

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

@dataclass(kw_only=True)
class HASensor(__HAEntry):
    component: ClassVar[str] = "sensor"

    device_class: Optional[HADeviceClassSensor] = HADeviceClassSensor.NONE
    expire_after: Optional[int] = None
    force_update: Optional[bool] = None
    last_reset_value_template: Optional[str] = None
    suggested_display_precision: Optional[int] = None
    state_class: Optional[str] = None
    state_topic: Optional[str] = None
    unit_of_measurement: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()        

        if self.state_topic is None:
            self.state_topic = self.node_id + "/values"

@dataclass(kw_only=True)
class HASensorEnergy(HASensor):
    device_class: HADeviceClassSensor = HADeviceClassSensor.ENERGY
    state_class: str = "measurement"
    unit_of_measurement: str = "kWh"
    
    def __post_init__(self):
        super().__post_init__()

@dataclass(kw_only=True)
class HASensorTemperature(HASensor):
    device_class: HADeviceClassSensor = HADeviceClassSensor.TEMPERATURE
    state_class: str = "measurement"
    unit_of_measurement: str = "°C"

    def __post_init__(self):
        super().__post_init__()

@dataclass(kw_only=True)
class HASensorBattery(HASensor):
    device_class: HADeviceClassSensor = HADeviceClassSensor.BATTERY
    unit_of_measurement: str = "%"

    def __post_init__(self):
        super().__post_init__()