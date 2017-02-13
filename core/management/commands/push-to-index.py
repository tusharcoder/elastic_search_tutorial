# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-13T22:20:09+05:30
# @Email:  tamyworld@gmail.com
# @Filename: dummy-data.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-14T03:52:03+05:30


from elasticsearch.client import IndicesClient
from django.core.management.base import BaseCommand
from core.models import Student
from django.conf import settings
from elasticsearch.helpers import bulk


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.recreate_index()
        self.push_db_to_index()
    def push_db_to_index(self):
        data=[
        self.convert_for_bulk(s,'create') for s in Student.objects.all()
        ]
        bulk(client=settings.ES_CLIENT, actions=data,stats_only=True)
    def convert_for_bulk(self,django_object,action=None):
        data=django_object.es_repr()
        metadata={
        '_op_type':action,
        '_index':django_object._meta.es_index_name,
        '_type':django_object._meta.es_type_name,
        }
        data.update(**metadata)
        return data
    def recreate_index(self):
        indices_client=IndicesClient(client=settings.ES_CLIENT)
        index_name=Student._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Student._meta.es_type_name,
            body=Student._meta.es_mapping,
            index=index_name
        )
