from django.contrib import admin


from .models import LanguageData, LanguageLabel

admin.site.register(LanguageLabel)
admin.site.register(LanguageData)


