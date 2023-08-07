

from core.models import Court
from django.utils import timezone
from django.db import connection


def run():
    for i in range(0, 7):
        Court.objects.filter(id=i).delete()



