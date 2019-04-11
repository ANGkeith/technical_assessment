from django.db import models



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

