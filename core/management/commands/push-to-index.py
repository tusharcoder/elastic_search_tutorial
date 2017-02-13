# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-13T22:20:09+05:30
# @Email:  tamyworld@gmail.com
# @Filename: dummy-data.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-14T00:33:52+05:30



from django.core.management.base import BaseCommand
from core.models import *
from model_mommy import mommy
import random
import names


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        # parser.add_argument('count', nargs=1,type=int)
        pass

    def handle(self, *args, **options):
        pass
