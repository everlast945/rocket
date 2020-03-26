from django.core.management import BaseCommand

from regions.models import Region, Town
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.exists():
            test_user = User(username='test', email='test@yandex.ru')
            test_user.set_password('test')
            test_user.save()

        if not Region.objects.exists():
            region_1 = Region.objects.create(name='Регион 001')
            region_2 = Region.objects.create(name='Регион 002', parent=region_1)
            region_3 = Region.objects.create(name='Регион 003', parent=region_2)
            region_4 = Region.objects.create(name='Регион 004', parent=region_3)
            region_5 = Region.objects.create(name='Регион 005')
            region_6 = Region.objects.create(name='Регион 006', parent=region_5)
            region_7 = Region.objects.create(name='Регион 007', parent=region_6)
            region_8 = Region.objects.create(name='Регион 008')

            Town.objects.create(name='Город 001', region=region_1)
            Town.objects.create(name='Город 002', region=region_2)
            Town.objects.create(name='Город 003', region=region_3)
            Town.objects.create(name='Город 004', region=region_4)
            Town.objects.create(name='Город 005', region=region_5)
            Town.objects.create(name='Город 006', region=region_6)
            Town.objects.create(name='Город 007', region=region_7)
            Town.objects.create(name='Город 008', region=region_8)
            Town.objects.create(name='Город 009', region=region_1)
            Town.objects.create(name='Город 010', region=region_1)
            Town.objects.create(name='Город 011', region=region_1)
            Town.objects.create(name='Город 012', region=region_2)
            Town.objects.create(name='Город 013', region=region_2)
