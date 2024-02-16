from dataclasses import dataclass, asdict, field
from typing import Optional, Union, Any, Dict, Tuple, ClassVar, Type
from enum import Enum

import json
import paho.mqtt.client as mqtt
import re

def find_class_var(klass: Type, var_name: str) -> str:
    """Recursively search for a class variable in the given class and its parent classes."""
    if hasattr(klass, var_name):
        return getattr(klass, var_name)
    else:
        for base_class in klass.__bases__:
            result = find_class_var(base_class, var_name)
            if result is not None:
                return result
    return None


@dataclass
class __BaseDataClass():
     """ Base function for all Entries, like to_json """
    def to_json(self) -> json:
        data_dict = self.to_dict()
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
        
    def to_dict(self) -> dict:
        data_dict = asdict(self)
        
        component = find_class_var(self.__class__, "component")
        if component is not None:
            data_dict["component"] = component

        data_dict = self.remove_null_values(data_dict)

        return data_dict
        
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
    node_id: str

    component: ClassVar[str] = ""
    discovery_prefix: str = "homeassistant"
    
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
    unique_id: Optional[str] = None
    value_template: Optional[str] = None

    def publish(self, mqttClient: mqtt.Client):
        topic = (self.discovery_prefix + "/" + 
                 self.component + "/" + 
                 self.node_id + "/" + 
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
            self.value_template = "{{ value_json." + self.cleanName() + " }}"
                
