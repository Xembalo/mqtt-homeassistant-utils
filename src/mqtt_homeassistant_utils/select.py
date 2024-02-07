from dataclasses import dataclass
from typing import Optional, Tuple, List
from enum import Enum

from .base import __HAEntry, HAAvailability, HADevice
  
@dataclass(kw_only=True)
class HASelect(__HAEntry):
    command_topic: str
    options: List[str]
    
    command_template: Optional[str] = None
    optimistic: Optional[bool] = None
    retain: Optional[bool] = None
    state_topic: Optional[str] = None
    unique_id: Optional[str] = None
    
    def __post_init__(self):
        super().__post_init__()

        self.component = "select"

        if self.state_topic is None:
            self.state_topic = self.node_id + "/values"
    