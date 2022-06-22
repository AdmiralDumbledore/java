from email import message
import json
from django.shortcuts import render
from kafka import KafkaProducer
from kafka.errors import KafkaError
from messenger.models import *
from user.models import *
import jwt
from utils.authentication import TokenAuthentication

from django.core import serializers


from rest_framework.views import APIView
from rest_framework.response import Response
from json import dumps


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

class SendMessage(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        message = request.data.get('message')

        try:
            User.objects.get(pk = user_id)
        except:
            return Response(status=204, data={"message": "No user with this id"})

        new_message = Message.objects.create(user_id = user_id, message_body = message, status = 'review')
        data = {"message_id": new_message.pk, "message_body": message}
        producer.send('messagepool', value=data)
        

        return Response(status=200, data = "saved")

class SetStatus(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        message_id = request.data.get('message_id')
        success = request.data.get('success')
        try:
            message = Message.objects.get(pk = message_id)
        except:
            return Response(status=204, data={"message": "No messages with this id"})
        if success == 'true':
            message.status = 'correct'
        elif success == 'false':
            message.status = 'blocked'
        message.save()
        return Response(status=204, data={"message": success})







# Create your views here.
