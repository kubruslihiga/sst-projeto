# main/tasks.py
 
import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
 
 
def send_verification_email(user_id):
    logging.info('BLABLA')