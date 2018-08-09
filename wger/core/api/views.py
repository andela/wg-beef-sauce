# -*- coding: utf-8 -*-

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
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.parsers import JSONParser
from rest_framework import status

from wger.config.models import GymConfig
from rest_framework.authtoken.models import Token

from wger.core.models import (
    UserProfile,
    Language,
    DaysOfWeek,
    License,
    RepetitionUnit,
    WeightUnit)
from wger.core.api.serializers import (
    UsernameSerializer,
    LanguageSerializer,
    DaysOfWeekSerializer,
    LicenseSerializer,
    RepetitionUnitSerializer,
    WeightUnitSerializer,
    UserSerializer
)

from wger.gym.models import GymUserConfig

from wger.core.api.serializers import UserprofileSerializer
from wger.utils.permissions import UpdateOnlyPermission, WgerPermission


class UserProfileViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for workout objects
    '''
    is_private = True
    serializer_class = UserprofileSerializer
    permission_classes = (WgerPermission, UpdateOnlyPermission)
    ordering_fields = '__all__'

    def get_queryset(self):
        '''
        Only allow access to appropriate objects
        '''
        return UserProfile.objects.filter(user=self.request.user)

    def get_owner_objects(self):
        '''
        Return objects to check for ownership permission
        '''
        return [(User, 'user')]

    @detail_route()
    def username(self, request, pk):
        '''
        Return the username
        '''

        user = self.get_object().user
        return Response(UsernameSerializer(user).data)


class UserCreateViewSet(viewsets.ViewSet):
    """API endpoint for creating a new user"""

    # Protect endpoint from unauthorised access.
    is_private = True

    def create(self, request):
        """
        Crete new user instance.

        :param request: request object
        :return:Response object
        """

        if len(UserProfile.objects.filter(token=request.auth)) >= 3:
            msg = "Token has reached user create limit, generate a new token"
            return Response({"msg": msg}, status=status.HTTP_403_FORBIDDEN)

        data = JSONParser().parse(request)

        # Check if user is allowed to access REST API
        check_access = UserProfile.objects.get(user=self.request.user)
        if check_access.create_use_rest_api:
            # Check if password equal to confirm_password.
            if data["password"] and data["confirm_password"] and \
                    data["password"] != data["confirm_password"]:
                return Response({"msg": "password mismatch"}, status=status.HTTP_400_BAD_REQUEST)

            user_serializer = UserSerializer(data=data)
            if user_serializer.is_valid():
                creator = User.objects.get(pk=Token.objects.get(key=request.auth).user_id)
                u = user_serializer.data
                email = u.get("email") or ""
                user = User.objects.create_user(u["username"], email, u["password"])
                user.save()
                user.userprofile.creator = creator.username
                user.userprofile.token = request.auth.key
                user.save()

                gym_config = GymConfig.objects.get(pk=1)
                if gym_config.default_gym:
                    user.userprofile.gym = gym_config.default_gym

                    # Create gym user configuration object
                    config = GymUserConfig()
                    config.gym = gym_config.default_gym
                    config.user = user
                    config.save()

                user.userprofile.save()

                msg = f'Successfully created user: {u["username"]}'

                return Response({"msg": msg}, status=status.HTTP_201_CREATED)

            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        msg = "You're NOT authorised to create a user via rest api"
        return Response({"msg": msg}, status=status.HTTP_403_FORBIDDEN)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    ordering_fields = '__all__'
    filter_fields = ('full_name',
                     'short_name')


class DaysOfWeekViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
    ordering_fields = '__all__'
    filter_fields = ('day_of_week', )


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for workout objects
    '''
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    ordering_fields = '__all__'
    filter_fields = ('full_name',
                     'short_name',
                     'url')


class RepetitionUnitViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for repetition units objects
    '''
    queryset = RepetitionUnit.objects.all()
    serializer_class = RepetitionUnitSerializer
    ordering_fields = '__all__'
    filter_fields = ('name', )


class WeightUnitViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint for weight units objects
    '''
    queryset = WeightUnit.objects.all()
    serializer_class = WeightUnitSerializer
    ordering_fields = '__all__'
    filter_fields = ('name', )
