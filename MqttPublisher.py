#!/usr/bin/python
import paho.mqtt.client as paho
import time
import datetime
from urllib.parse import urlparse

# Mqtt client definitio
mqttc = paho.Client()
counter = 0
#We are not using the authentication, so no username and password
#mqttc.username_pw_set("", "")

def sendmqtt(mess):
    try:
        #Connection to the Broker runing in the same raspberry. Instead the
        #"localhost" you can define the IP address of the device where the Broker
        #is running
        mqttc.connect("localhost", 1883)
        #We are going to publish the message in the topic /sensors/temperature
        mqttc.publish("/sensors/temperature", mess)
    except:
        pass

#We will publish the temperature or a generic number every second in an infinite loop
while True:
    try:
        #Increase the counter, here you can use something else for example
        #a temeprature coming from a real sensor connected to the raspberry
        counter = counter+1
        #Here we publish the message
        sendmqtt(str(counter))
        #We wait 1 second before send the next message
        time.sleep(1)
    except KeyboardInterrupt:
            # quit
            sys.exit()