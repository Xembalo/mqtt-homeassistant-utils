from dataclasses import dataclass
from typing import Optional, List, ClassVar

from .base import __HAEntry

@dataclass(kw_only=True)
class HAWaterHeater(__HAEntry):
    component: ClassVar[str] = "water_heater"

    current_temperature_template: Optional[str] = None
    current_temperature_topic: Optional[str] = None
    initial: Optional[int] = None
    max_temp: Optional[float] = None
    min_temp: Optional[float] = None
    mode_command_template: Optional[str] = None
    mode_command_topic: Optional[str] = None
    mode_state_template: Optional[str] = None
    mode_state_topic: Optional[str] = None
    modes: Optional[List[str]]
    optimistic: Optional[bool] = None
    payload_available: Optional[str] = None
    payload_not_available: Optional[str] = None
    payload_off: Optional[str] = None
    payload_on: Optional[str] = None
    power_command_template: Optional[str] = None
    power_command_topic: Optional[str] = None
    precision: Optional[float] = None
    retain: Optional[bool] = None
    temperature_command_template: Optional[str] = None
    temperature_command_topic: Optional[str] = None
    temperature_state_template: Optional[str] = None
    temperature_state_topic: Optional[str] = None
    temperature_unit: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
