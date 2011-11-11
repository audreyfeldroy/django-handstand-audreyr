from django.contrib.auth.models import User
from django.test import TestCase

        
class login(object):
    def __init__(self, testcase, user, password):
        self.testcase = testcase
        success = testcase.client.login(username=user, password=password)
        self.testcase.assertTrue(
             success,
             "login with username=%r, password=%r failed" % (user, password)
        )

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.testcase.client.logout()        

class BaseTestCase(TestCase):
    
    urls = 'handstand.urls'    
    
    def setUp(self):
        """
usage::

    from core.tests_utils import BaseTestCase
    class MyTest(BaseTestCase):

        def setUp(self):
            super(MyTest,self).setUp()                
            # stick in custom setUp bits here
            # stick in custom setUp bits here
            # stick in custom setUp bits here                                
        """

        self.user_pw = 'test'        
        self.user = User.objects.create_user('aroy','aroy@test.com',self.user_pw,)
        self.user.first_name = "Audrey"
        self.user.last_name = "Roy"
        self.user.save()
        
        self.user2 = User.objects.create_user('pydanny','pydanny@test.com',self.user_pw,)
        self.user2.first_name = "Danny"
        self.user2.last_name = "Greenfeld"
        self.user.save()
        
        
    def tearDown(self):
        self.client.logout()
        
    def login(self, user, password):
        return login(self, user, password)