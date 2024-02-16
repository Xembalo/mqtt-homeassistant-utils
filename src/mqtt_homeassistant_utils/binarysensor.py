from dataclasses import dataclass
from typing import Optional, ClassVar
from enum import Enum

from .base import __HAEntry

class HADeviceClassBinarySensor(Enum):
    NONE = None
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
  
@dataclass(kw_only=True)
class HABinarySensor(__HAEntry):
    component: ClassVar[str] = "binary_sensor"

    device_class: Optional[HADeviceClassBinarySensor] = HADeviceClassBinarySensor.NONE
    expire_after: Optional[int] = None
    force_update: Optional[bool] = None
    off_delay: Optional[int] = None
    payload_off: Optional[str] = None
    payload_on: Optional[str] = None
    state_topic: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()

        if self.state_topic is None:
            self.state_topic = self.node_id + "/values"

 
