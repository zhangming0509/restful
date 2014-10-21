from rest_framework import serializers
from rest.models import RequestInfo

from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from datetime import datetime


class HyperRequestInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestInfo
        fields = ('url', 'email', 'first_name', 'last_name',
                  'contact_number', 'title', 'content', 'link')

        
class RequestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInfo
        fields = ('id', 'email', 'first_name', 'last_name',
                  'contact_number', 'title', 'content', 'link')

    def send_to_requester(self):
        subject = 'Thanks for your application'
        template = get_template('requester_email.txt')
        context = Context({
            'last_name': self.data['last_name']
        })
        message = template.render(context)
        send_mail(
            subject, message,
        settings.DEFAULT_FROM_EMAIL, [self.data['email']]
        )

    def send_to_dedicated(self):
        date_time = datetime.now()
        subject = 'Application Received from %s' % self.data['email']
        template = get_template('dedicated_email.txt')
        context = Context({
            'last_name': self.data['last_name'],
            'first_name': self.data['first_name'],
            'datetime': str(date_time)[:-7]
        })
        message = template.render(context)
        send_mail(
            subject, message,
        settings.DEFAULT_FROM_EMAIL, [settings.DEDICATED_EMAIL]
        )






