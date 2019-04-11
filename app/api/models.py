from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class LanguageLabel(models.Model):
    shortName           = models.CharField(primary_key=True, max_length=99)
    name                = models.CharField(max_length=99, null=False, blank=False)

    def __str__(self):
        return self.shortName

class LanguageData(models.Model):
    language_label      = models.OneToOneField(LanguageLabel, on_delete=models.CASCADE)
    total_docs          = models.IntegerField()

    def __str__(self):
        return self.language_label.name

class DoctypeLabel(models.Model):
    name                = models.CharField(max_length=99, null=False, blank=False)

    def __str__(self):
        return self.name

class DoctypeData(models.Model):
    name                = models.CharField(max_length=99, null=False, blank=False)
    total_docs          = models.IntegerField()

    def __str__(self):
        return self.name

class ConfidentialityLabel(models.Model):
    name                = models.CharField(max_length=99, null=False, blank=False)

    def __str__(self):
        return self.name

class ConfidentialityData(models.Model):
    name                = models.CharField(max_length=99, null=False, blank=False)
    total_docs          = models.IntegerField()

    def __str__(self):
        return self.name

class File(models.Model):
    doctype             = models.ForeignKey(DoctypeLabel, default=1, on_delete=models.CASCADE)
    confidentiality     = models.ForeignKey(ConfidentialityLabel, default=8, on_delete=models.CASCADE)

    date_stamp          = models.DateTimeField(auto_now_add=True)
    document_path       = models.FileField(upload_to='Files/')

