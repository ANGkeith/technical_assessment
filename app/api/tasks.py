from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from rest_framework.authtoken.models import Token
import os

@shared_task
def auto_increment_task():
    BASEURL = 'http://localhost:8000/'
    token = Token.objects.get(user=1).pk
    headers = {'Authorization': 'Token ' + token,'Content-type': 'application/json'}
    r = requests.get(url=BASEURL + 'api/doctype-datas/Email/', headers=headers)
    prev_value = r.json()['total_docs']
    data = '{ "name": "Email", "total_docs": ' + str(prev_value + 1) + '}'
    requests.put(url=BASEURL + 'api/doctype-datas/Email/', headers=headers, data=data)

@shared_task
def print_total_file():
    total_file = len([1 for x in list(os.scandir('/app/media/Files/')) if x.is_file()])
    # total_doc = 0
    # for lang_data in LanguageData.objects.all():
    #     total_doc = lang_data + total_doc
    # for doctype_data in LanguageData.objects.all():
    #     total_doc = doctype_data + total_doc
    # for confi_data in LanguageData.objects.all():
    #     total_doc = confi_data + total_doc
    print('There are ' + str(total_file) + ' files.')


