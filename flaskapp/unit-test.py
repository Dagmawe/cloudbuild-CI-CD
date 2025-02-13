import unittest
import app 

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        result = self.app.get('/')
        self.assertEqual(result.data.decode('utf-8'), "Hello, World! This is a simple Flask application.")

    def test_about_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_about_data(self):
        result = self.app.get('/about')
        self.assertEqual(result.data.decode('utf-8'), "This is the about page.")

    def test_greet_status_code(self):
        result = self.app.get('/greet/Dagmawi')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()