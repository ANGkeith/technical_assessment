# generic


from rest_framework import generics, status
from rest_framework.response import Response
from .models import LanguageData, LanguageLabel, ConfidentialityData, ConfidentialityLabel, DoctypeData, \
    DoctypeLabel, File
from .serializer import LanguageDataSerializer, LanguageLabelSerializer, ConfidentialityDataSerializer, \
    ConfidentialityLabelSerializer, DoctypeDataSerializer, DoctypeLabelSerializer, FileSerializer



# Language
class LanguageDataView(generics.ListCreateAPIView):
    queryset = LanguageData.objects.all()
    serializer_class = LanguageDataSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleLanguageDataRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LanguageData.objects.all()
    serializer_class = LanguageDataSerializer
    lookup_field = 'language_label'
    lookup_url_kwarg = 'short_name'

class LanguageLabelView(generics.ListCreateAPIView):
    queryset = LanguageLabel.objects.all()
    serializer_class = LanguageLabelSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleLanguageLabelRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LanguageLabel.objects.all()
    serializer_class = LanguageLabelSerializer
    lookup_field = 'shortName'
    lookup_url_kwarg = 'short_name'

# Confidentiality
class ConfidentialityDataView(generics.ListCreateAPIView):
    queryset = ConfidentialityData.objects.all()
    serializer_class = ConfidentialityDataSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleConfidentialityDataRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfidentialityData.objects.all()
    serializer_class = ConfidentialityDataSerializer
    lookup_field = 'name'

class ConfidentialityLabelView(generics.ListCreateAPIView):
    queryset = ConfidentialityLabel.objects.all()
    serializer_class = ConfidentialityLabelSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleConfidentialityLabelRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfidentialityLabel.objects.all()
    serializer_class = ConfidentialityLabelSerializer
    lookup_field = 'name'

# Doctype
class DoctypeDataView(generics.ListCreateAPIView):
    queryset = DoctypeData.objects.all()
    serializer_class = DoctypeDataSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleDoctypeDataRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctypeData.objects.all()
    serializer_class = DoctypeDataSerializer
    lookup_field = 'name'

class DoctypeLabelView(generics.ListCreateAPIView):
    queryset = DoctypeLabel.objects.all()
    serializer_class = DoctypeLabelSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SingleDoctypeLabelRudView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctypeLabel.objects.all()
    serializer_class = DoctypeLabelSerializer
    lookup_field = 'name'

class FileView(generics.ListCreateAPIView):
   queryset = File.objects.all()
   serializer_class = FileSerializer

class SingleFileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'pk'

