import paho.mqtt.client as mqtt
import time

loop_num = 0

def onConnect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe('pknu63/rcv')

def onMessage(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = onConnect
mqttc.on_message = onMessage

mqttc.connect('192.168.5.2', 1883, 60)

mqttc.loop_start()

while True:    
    mqttc.publish('pknu63/data', loop_num)
    loop_num += 1
    time.sleep(1)

mqttc.loop_stop()