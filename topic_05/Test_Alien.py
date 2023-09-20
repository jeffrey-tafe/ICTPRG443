import unittest as ut
from Alien_Class import Alien


class AlienTestCase(ut.TestCase):
    def setUp(self):
        self.alien = Alien(8, 10, "Martian")
        print("Setup")

    def test_lives(self):
        lives = self.alien.get_lives()
        self.assertEqual(lives, 10)
        # self.assertTrue(lives == 10)

    def test_strength(self):
        strength = self.alien.get_strength()
        self.assertEqual(strength, 8)

    def test_alien_type(self):
        alien_type = self.alien.get_alien_type()
        self.assertIn(alien_type, "Martian")

    def test_alien_type_fail(self):
        alien_type = self.alien.get_alien_type()
        self.assertNotIn(alien_type, "martian")

    def tearDown(self):
        del self.alien
        print("Tear Down")


if __name__ == '__main__':
    ut.main()
