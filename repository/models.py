from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Password(models.Model):
    title = models.CharField(max_length=255, verbose_name='موضوع')
    password = models.CharField(max_length=255, verbose_name='رمز')
    description = models.TextField(verbose_name='متن')
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE,
                             related_name='user_pass')
