from dataclasses import dataclass
from typing import Optional, ClassVar
from enum import Enum

from .base import __HAEntry

class HADeviceClassCover(Enum):
    NONE = None
    AWNING = "awning"
    BLIND = "blind"
    CURTAIN = "curtain"
    DAMPER = "damper"
    DOOR = "door"
    GARAGE = "garage"
    GATE = "gate"
    SHADE = "shade"
    SHUTTER = "shutter"
    WINDOW = "window"

@dataclass(kw_only=True)
class HACover(__HAEntry):
    component: ClassVar[str] = "cover"

    device_class: Optional[HADeviceClassCover] = HADeviceClassCover.NONE

    command_topic: Optional[str] = None
    optimistic: Optional[bool] = None
    payload_close: Optional[str] = None
    payload_open: Optional[str] = None
    payload_stop: Optional[str] = None
    position_closed: Optional[int] = None
    position_open: Optional[int] = None
    position_template: Optional[str] = None
    position_topic: Optional[str] = None
    retain: Optional[bool] = None
    set_position_template: Optional[str] = None
    set_position_topic: Optional[str] = None
    state_closed: Optional[str] = None
    state_closing: Optional[str] = None
    state_open: Optional[str] = None
    state_opening: Optional[str] = None
    state_stopped: Optional[str] = None
    state_topic: Optional[str] = None
    tilt_closed_value: Optional[int] = None
    tilt_command_template: Optional[str] = None
    tilt_command_topic: Optional[str] = None
    tilt_max: Optional[int] = None
    tilt_min: Optional[int] = None
    tilt_opened_value: Optional[int] = None
    tilt_optimistic: Optional[bool] = None
    tilt_status_template: Optional[str] = None
    tilt_status_topic: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()