# generic


from rest_framework import generics, status
from rest_framework.response import Response
from .models import LanguageData, LanguageLabel
from .serializer import LanguageDataSerializer, LanguageLabelSerializer



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
    lookup_field = 'short_name'
    lookup_url_kwarg = 'label'


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
    lookup_url_kwarg = 'label'
