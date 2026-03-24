from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.PositiveIntegerField()
    expired_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = random.randint(100000, 999999)
        if not self.expired_date:
            self.expired_date = timezone.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expired_date