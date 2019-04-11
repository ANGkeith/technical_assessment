from django.contrib import admin


from .models import LanguageData, LanguageLabel, DoctypeLabel, DoctypeData, ConfidentialityData,\
    ConfidentialityLabel, File

admin.site.register(LanguageLabel)
admin.site.register(LanguageData)
admin.site.register(DoctypeLabel)
admin.site.register(DoctypeData)
admin.site.register(ConfidentialityData)
admin.site.register(ConfidentialityLabel)
admin.site.register(File)


