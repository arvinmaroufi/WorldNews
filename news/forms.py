from django import forms
from .models import Message, Subscriber


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
