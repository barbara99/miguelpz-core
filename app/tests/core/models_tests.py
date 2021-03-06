import os
import unittest
import tempfile
from app.core.models import User
from app.core.models import Session

class SessionTestCase(unittest.TestCase):
    
    def setUp(self):
        session = Session(session_id='test_id', data={'_flash':[['message', 'Invalid error']]})
        session.save()
        self.id = session.id
        self.session = Session

    def testSessionId(self):
        session = self.session.objects(id=self.id).first()
        self.assertEquals(session.session_id, 'test_id')

    def tearDown(self):
        Session.drop_collection()

class UserTestCase(unittest.TestCase):
    def setUp(self):
        user = User(
            username = 'Test username',
            email = 'Test email',
            job = 'Test Job',
            city = 'Test City',
            name = 'Test Name',
            github = 'Test github',
            twitter = 'Test twitter',
            linkedin = 'Test linkedin',
            facebook = 'Test facebook',
            github_id =  '12345',
            gravatar_id = 'test gravatar id',   
            googleplus = 'Test googleplus',
            foursquare = 'Test foursquare',
            personal_web =  'Test personal web',
            token_github = 'test github token'
            )
        user = user.save()
        self.id = user.id
        
    def tearDown(self):
        User.drop_collection()

    def testGithubToken(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.token_github,'test github token')

    def testGravatarID(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.gravatar_id, 'test gravatar id')

    def testGithubID(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.github_id, 12345)

    def testUsername(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.username, 'Test username')

    def testJob(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.job, 'Test Job')

    def testCity(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.city, 'Test City')

    def testName(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.name, 'Test Name')
    
    def testGithub(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.github, 'Test github')

    def testTwitter(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.twitter, 'Test twitter')

    def testLinkedin(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.linkedin, 'Test linkedin')

    def testLinkedin(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.linkedin, 'Test linkedin')

    def testFaceBook(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.facebook, 'Test facebook')

    def testGooglePlus(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.googleplus, 'Test googleplus')

    def testFoursquare(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.foursquare, 'Test foursquare')

    def testPersonalWeb(self):
        user = User.objects(id=self.id).first()
        self.assertEquals(user.personal_web, 'Test personal web')