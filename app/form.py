from dataclasses import field, fields
from socket import fromshare
from tkinter import Label
from django import froms
from app.models import *

class TopicForm(forms.modelForm):
    class meta:
        model=Topic
        fields='__all__'
        
class webpageForm(forms.modelForm):
    class meta:
        model=webpage
        fields='__alll__'
        #fields=['topic_name','name']
        #exclude=['topic_name','name']
        #widgets={'name':forms.passwordInput}
        Label={'name':g('changed'),'topic_name':g('again changed')}
        help_texts={'name':g('enter ur name')}



