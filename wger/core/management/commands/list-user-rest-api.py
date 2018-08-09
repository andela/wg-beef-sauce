# -*- coding: utf-8 *-*

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from wger.core.models import UserProfile
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """List users created via rest api"""

    help = 'List users created via rest API'

    def add_arguments(self, parser):
        """Receive positional argument (creator)"""
        parser.add_argument('creator', nargs='?', type=str)

    def handle(self, **options):
        """Process the options"""

        creator = options.get('creator', None)

        user = User.objects.all()
        if creator is not None and not User.objects.filter(username=creator):
            print(f"Creator {creator} does not exist")
        else:
            for u in user:
                if creator and u.userprofile.creator == creator:
                    print(u.username)
                elif u.userprofile.creator is not None:
                    print(f"{u.username} created by {u.userprofile.creator}")
