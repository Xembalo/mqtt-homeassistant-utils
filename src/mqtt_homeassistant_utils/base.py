from dataclasses import dataclass, asdict, field
from typing import Optional, Union, Any, Dict, Tuple
from enum import Enum

import json
import paho.mqtt.client as mqtt
import re


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
class __HAEntry(__BaseDataClass):
    name: str
    
    discovery_prefix: str = "homeassistant"
    component: str = None
    node_id: str = None
    unique_id: str = field(init=False, default=None)
    
    availability: Optional[Tuple[HAAvailability]] = None
    availability_mode: Optional[str] = None
    device: Optional[HADevice] = None
    enabled_by_default: Optional[bool] = None
    encoding: Optional[str] = None
    entity_category: Optional[str] = None
    icon: Optional[str] = None
    json_attributes_template: Optional[str] = None
    json_attributes_topic: Optional[str] = None
    object_id: Optional[str] = None
    qos: Optional[int] = None
    value_template: Optional[str] = field(init=False, default=None)

    def publish(self, mqttClient: mqtt.Client):
        topic = (self.discovery_prefix + "/" + 
                 self.component + "/" + 
                 (self.node_id + "/" if self.node_id else "" ) + 
                 self.unique_id + "/config"
                )
        qos = (self.qos if self.qos else 0)
        
        mqttClient.publish(topic, self.to_json(), qos=qos, retain=True)

    def cleanName(self):
        return re.sub(r'[^A-Za-z]', '', self.name).lower()
        
    def __post_init__(self):
        if self.unique_id is None:
            self.unique_id = self.node_id + "_" + self.cleanName()
        if self.value_template is None:
            self.unique_id = "{{ value_json." + self.cleanName() + " }}"
                
