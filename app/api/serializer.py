from rest_framework import serializers

from .models import LanguageData, LanguageLabel, DoctypeData, DoctypeLabel, ConfidentialityLabel, ConfidentialityData


class LanguageLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageLabel
        fields = (
            'shortName',
            'name',
        )


class LanguageDataSerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(source='language_label.name', read_only=True)
    short_name = serializers.PrimaryKeyRelatedField(source='language_label', queryset=LanguageLabel.objects.all())


    class Meta:
        model = LanguageData
        fields = (
            'short_name',
            'total_docs',
            'name',
        )

class ConfidentialityLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialityLabel
        fields = '__all__'


class ConfidentialityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfidentialityData
        fields = '__all__'

class DoctypeLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctypeLabel
        fields = '__all__'


class DoctypeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctypeData
        fields = (
            'name',
            'total_docs',
        )

