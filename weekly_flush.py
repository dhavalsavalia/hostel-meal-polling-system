import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polls.settings')
django.setup()
from django.contrib.auth.models import User
from mainapp.models import Profile

list_users = list(User.objects.order_by('-pk'))


def flush_all():
    for n_user in list_users:
        model_con = Profile.objects.get(user=n_user)
        model_con.has_voted = False
        model_con.save()

flush_all()
print('ALL RECORDS FLUSHED!!!')
