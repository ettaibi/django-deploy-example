import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from third_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry

        # Create the fake data fro that entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create the new webpage entry
        users = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print('populating complete')
