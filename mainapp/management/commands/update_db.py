from django.core.management.base import BaseCommand
from authapp.models import DealUser
from authapp.models import DealUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = DealUser.objects.all()
        for user in users:
            users_profile = DealUserProfile.objects.create(user=user)
            users_profile.save()
