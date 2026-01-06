from django.db import models
from companies.models import CompanyProfile

class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    min_cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    max_backlogs = models.IntegerField()
    branches_allowed = models.JSONField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
