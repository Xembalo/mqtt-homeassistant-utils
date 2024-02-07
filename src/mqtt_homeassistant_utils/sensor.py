from dataclasses import dataclass, field
from typing import Optional, Tuple
from enum import Enum

from .base import __HAEntry, HAAvailability, HADevice

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
    state_topic: str = field(init=False, default=None)

    device_class: Optional[HADeviceClassSensor] = HADeviceClassSensor.NONE
    expire_after: Optional[int] = None
    force_update: Optional[bool] = None
    last_reset_value_template: Optional[str] = None
    suggested_display_precision: Optional[int] = None
    state_class: Optional[int] = None
    unit_of_measurement: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()        
        
        self.component = "sensor"

        if self.state_topic is None:
            self.state_topic = self.node_id + "/values"

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