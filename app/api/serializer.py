from rest_framework import serializers

from .models import LanguageData, LanguageLabel


class LanguageLabelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = LanguageLabel
        fields = (
            'shortName',
            'name'
        )
    def get_name(self, obj):
        return obj.get_name()

class LanguageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageData
        fields = (
            'name',
            'short_name',
            'total_docs',
        )


