from django.db import models



class LanguageLabel(models.Model):
    shortName            = models.CharField(primary_key=True, max_length=99, null=False, blank=False)

    def get_name(self):
        try:
            name = LanguageData.objects.get(short_name=self.shortName).name
        except LanguageData.DoesNotExist:
            name = None
        return name

    def __str__(self):
        return self.shortName

class LanguageData(models.Model):
    short_name = models.OneToOneField(LanguageLabel, on_delete=models.CASCADE)
    total_docs = models.IntegerField()
    name = models.CharField(max_length=99, null=False, blank=False)

    def __str__(self):
        return self.name


