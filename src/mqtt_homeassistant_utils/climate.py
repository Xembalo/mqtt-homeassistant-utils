from dataclasses import dataclass
from typing import Optional, List, ClassVar

from .base import __HAEntry

@dataclass(kw_only=True)
class HAClimate(__HAEntry):
    component: ClassVar[str] = "climate"

    action_template: Optional[str] = None
    action_topic: Optional[str] = None
    current_humidity_template: Optional[str] = None
    current_humidity_topic: Optional[str] = None
    current_temperature_template: Optional[str] = None
    current_temperature_topic: Optional[str] = None
    fan_mode_command_template: Optional[str] = None
    fan_mode_command_topic: Optional[str] = None
    fan_mode_state_template: Optional[str] = None
    fan_mode_state_topic: Optional[str] = None
    fan_modes: Optional[List[str]]
    initial: Optional[float] = None
    max_humidity: Optional[int] = None
    max_temp: Optional[float] = None
    min_humidity: Optional[int] = None
    min_temp: Optional[float] = None
    mode_command_template: Optional[str] = None
    mode_command_topic: Optional[str] = None
    mode_state_template: Optional[str] = None
    mode_state_topic: Optional[str] = None
    modes: Optional[List[str]]
    optimistic: Optional[bool] = None
    payload_off: Optional[str] = None
    payload_on: Optional[str] = None
    power_command_template: Optional[str] = None
    power_command_topic: Optional[str] = None
    precision: Optional[float] = None
    preset_mode_command_template: Optional[str] = None
    preset_mode_command_topic: Optional[str] = None
    preset_mode_state_topic: Optional[str] = None
    preset_mode_value_template: Optional[str] = None
    preset_modes: Optional[List[str]]
    retain: Optional[bool] = None
    swing_mode_command_template: Optional[str] = None
    swing_mode_command_topic: Optional[str] = None
    swing_mode_state_template: Optional[str] = None
    swing_mode_state_topic: Optional[str] = None
    swing_modes: Optional[List[str]]
    target_humidity_command_template: Optional[str] = None
    target_humidity_command_topic: Optional[str] = None
    target_humidity_state_template: Optional[str] = None
    target_humidity_state_topic: Optional[str] = None
    temp_step: Optional[float] = None
    temperature_command_template: Optional[str] = None
    temperature_command_topic: Optional[str] = None
    temperature_high_command_template: Optional[str] = None
    temperature_high_command_topic: Optional[str] = None
    temperature_high_state_template: Optional[str] = None
    temperature_high_state_topic: Optional[str] = None
    temperature_low_command_template: Optional[str] = None
    temperature_low_command_topic: Optional[str] = None
    temperature_low_state_template: Optional[str] = None
    temperature_low_state_topic: Optional[str] = None
    temperature_state_template: Optional[str] = None
    temperature_state_topic: Optional[str] = None
    temperature_unit: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()