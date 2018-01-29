import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polls.settings')
django.setup()

from mainapp.models import Choice

all_choices = [
			'vada_paw', 'paw_bhaji', 'ghughra', 'pani_puri', 'dal_pakwan', 'fruit_salad',
			'sandwhich', 'bhajiya', 'punjabi', 'pizza', 'dabeli', 'manchurian',
]


def create_choice():
	for choice in all_choices:
		Choice.objects.get_or_create(choices=choice)


create_choice()
print("DATA HAS BEEN SUCCESSFULLY POPULATED!!!")
