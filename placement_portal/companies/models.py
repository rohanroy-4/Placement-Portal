from django.db import models
from accounts.models import User

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    website = models.URLField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
