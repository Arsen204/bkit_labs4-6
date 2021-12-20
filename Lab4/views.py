from django.shortcuts import render
from rest_framework import viewsets
from Lab4.serializers import PersonSerializer, TechnologySerializer
from Lab4.models import Technology
from Lab4.models import Person


def get_langs(request):
    return render(request, 'langs.html', {
        'langs': Technology.objects.all(),
    })


def get_lang(request, lang_id):
    return render(request, 'lang.html', {
        'lang': Technology.objects.filter(id=lang_id)[0],
        'persons': Person.objects.all().filter(technology_id=lang_id)
    })


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
