from django.test import TestCase

from entities.models import Origin, Category, Entity, Hero, Villain

# test models
class OriginTestCase(TestCase):
    def setUp(self):
        self.origin_goku = Origin.objects.create(name='planeta sayayin',)
    
    def test_origin_creation(self):
        self.assertTrue(isinstance(self.origin_goku, Origin))

    def tearDown(self):
        del self.origin_goku

# test urls

# test views