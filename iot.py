
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


# Install below packages
'''
sudo pip3 install azure-iot-device
sudo pip3 install azure-iot-hub
sudo pip3 install azure-iothub-service-client
sudo pip3 install azure-iothub-device-client
'''

# Run below on Azure CLI
'''
#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

'''

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=Shamyukths-iot.azure-devices.net;DeviceId=mydevice;SharedAccessKey=PXEhlPRrgHdqaaAGx71I1U59To902VJmkHQeSMDw/+w="

# Define the JSON message to send to IoT Hub.
CO = 5.0
TEMPERATURE = 20
NO2 = 100
NH3 = 15
MSG_TXT = '{{"co": {co},"temperature": {temperature},"no2":{no2},"nh3": {nh3}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with simulated telemetry values.
            temperature = TEMPERATURE + (random.random() * 15)
            co = CO + (random.random() * 15)
            no2 = NO2 + (random.random() * 15)
            nh3=NH3 + (random.random() * 15)
            #NO2=random. randint(0,50)
            #NH3=random. randint(0,40)
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, co=co, no2=no2, nh3=nh3)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if temperature > 30:
              #message.custom_properties["temperatureAlert"] = "true"
            #else:
              #message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()

