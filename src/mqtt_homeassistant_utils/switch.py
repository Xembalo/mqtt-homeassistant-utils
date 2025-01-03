from dataclasses import dataclass
from typing import Optional, ClassVar
from enum import Enum

from .base import __HAEntry

class HADeviceClassSwitch(Enum):
    NONE = None
    OUTLET = "outlet"
    SWITCH = "switch"

@dataclass(kw_only=True)
class HASwitch(__HAEntry):
    component: ClassVar[str] = "switch"

    device_class: Optional[HADeviceClassSwitch] = HADeviceClassSwitch.NONE

    command_template: Optional[str] = None
    command_topic: Optional[str] = None
    optimistic: Optional[bool] = None
    payload_off: Optional[str] = None
    payload_on: Optional[str] = None
    retain: Optional[bool] = None
    state_off: Optional[str] = None
    state_on: Optional[str] = None
    state_topic: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()


@dataclass(kw_only=True)
class HASwitchOutlet(HASwitch):
    device_class: HADeviceClassSwitch = HADeviceClassSwitch.OUTLET
    
    def __post_init__(self):
        super().__post_init__()

@dataclass(kw_only=True)
class HASwitchGeneric(HASwitch):
    device_class: HADeviceClassSwitch = HADeviceClassSwitch.SWITCH
    
    def __post_init__(self):
        super().__post_init__()