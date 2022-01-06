from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name="contact_name")
    subject = models.CharField(max_length=50, verbose_name="contact_subject")
    email = models.EmailField(verbose_name='contact_email')
    message = models.TextField(verbose_name="contact_message")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'