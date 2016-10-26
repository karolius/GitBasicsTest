from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    donation = models.CharField(max_length=8, blank=False, default="1$")
    doner_kebab = models.CharField(max_length=3, blank=False)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email