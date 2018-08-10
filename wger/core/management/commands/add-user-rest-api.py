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


from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''
    Helper admin command to give a user permission to add users via REST API
    '''

    help = 'Allow a user to create users via REST API'

    def add_arguments(self, parser):
        """Receive positional argument (username)"""
        parser.add_argument('username', nargs='?', type=str)

    def handle(self, **options):
        """Change User Permission to True for accessing REST API(create users)"""
        username = options.get('username', None)
        try:
            user = User.objects.get(username=username)
            if user.userprofile.create_use_rest_api:
                print("{} is already allowed to access REST API to create users".format(username))
            else:
                user.userprofile.create_use_rest_api = True
                user.userprofile.save()
                print("{} is now able to access REST API to create users".format(username))
        except:
            print("User {} does not exist".format(username))
