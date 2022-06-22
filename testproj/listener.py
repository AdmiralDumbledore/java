from collections import namedtuple
from kafka import KafkaConsumer
from json import loads
import requests
import jwt

consumer = KafkaConsumer(
    'messagepool',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    new_message = namedtuple("new_message", message.keys())(*message.values())
    success = ""

    if "АБРАКАДАБРА" in str(new_message.message_body).upper():
        success = "false"
    else:
        success = "true"

    requests.post('http://192.168.56.131:8000/api/v1/message_confirmation/', headers={'Authorization': 'Bearer token'}, json={
        "message_id": new_message.message_id,
        "success": success,
    })

    print(str(new_message.message_id) + " " + success)
