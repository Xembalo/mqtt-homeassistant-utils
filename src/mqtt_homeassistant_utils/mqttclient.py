import paho.mqtt.client as mqtt

#from .base import HAAvailability


class HAMqttClient:
    def __init__(self, identifier: str, root_topic: str, broker_address: str, broker_port: int = 1883, username: str = None, password: str = None, qos: int = 0) -> None:
        self.__root_topic = root_topic
        self.__qos = qos
        self.is_connected: bool = False
        self.sent_autodiscovery: bool = False

        availtopic = self.__root_topic + "/state"
        #todo: sensors im in_connect senden
        self.client = mqtt.Client(identifier)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        if username is not None and password is not None:
            self.client.username_pw_set(username, password)
        
        #register last will
        self.client.will_set(availtopic,"offline",qos,retain=True)

        try:
            self.client.connect(broker_address, broker_port)
        except:
            self.is_connected = False

    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            self.is_connected = True
        else:
            self.is_connected = False
        
    def on_disconnect(self, client, userdata, rc):
        self.is_connected = False
        self.sent_autodiscovery = False

    def publish(self, sub_topic: str, payload: str, retain: bool = False) -> None:
        self.client.publish(self.__root_topic + "/" + sub_topic.lstrip('/'), payload, qos=self.__qos, retain=retain)
    
    def loop(self) -> None:
        self.client.loop()
    
    def loop_forever(self) -> None:
        self.client.loop_forever()

    def loop_start(self) -> None:
        self.client.loop_start()

    def loop_stop(self) -> None:
        self.client.loop_stop()
