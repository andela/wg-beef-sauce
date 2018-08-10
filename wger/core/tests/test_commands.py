from io import StringIO
from django.core.management import call_command
from wger.core.tests.base_testcase import WorkoutManagerTestCase


class ApiCommandsTest(WorkoutManagerTestCase):
    """Tests the commands running for the api"""

    def test_authorize_use_rest_api(self):
        """Test to authorize a user to access the create users rest API"""
        # test if you can authorize user once
        out = StringIO()
        call_command('add-user-rest-api', 'admin', stdout=out)
        self.assertIn('', out.getvalue())

        # test if user can be authorized twice
        call_command('add-user-rest-api', 'admin', stdout=out)
        self.assertIn('', out.getvalue())

        # test with no user
        call_command('add-user-rest-api', '', stdout=out)
        self.assertIn('', out.getvalue())

        # test with non-existent user
        call_command('add-user-rest-api', 'fakeuser', stdout=out)
        self.assertIn('', out.getvalue())

    def test_list_users_created(self):
        """Test if list command will show"""
        # test with a user
        out = StringIO()
        call_command('list-user-rest-api', 'admin', stdout=out)
        self.assertIn('', out.getvalue())

        # test with no user
        call_command('list-user-rest-api', stdout=out)
        self.assertIn('', out.getvalue())

        # test with non-existent user
        call_command('list-user-rest-api', 'fake', stdout=out)
        self.assertIn('', out.getvalue())
