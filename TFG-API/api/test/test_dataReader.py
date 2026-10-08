import os
import pytest
import psycopg2
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfgApi.settings')
app = get_wsgi_application()

from api.dataReader import Reader
from api.models import Weather


@pytest.mark.django_db
def test_read_csv():
    reader = Reader(r'C:\Users\Yusepp\Desktop\datasets')
    reader.read_all()
    data = Weather.objects.all().count()
    assert data > 0

@pytest.mark.django_db
def test_read_all():
    reader = Reader(r'C:\Users\Yusepp\Desktop\datasets')
    reader.read_csv(reader.files[0])
    data = Weather.objects.all().count()
    assert data > 0
