from django.db import models

class User(models.Model):
    UID = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    nickname = models.CharField(max_length=128)
    school = models.CharField(max_length=128)

    def __str__(self):
        return self.nickname
    