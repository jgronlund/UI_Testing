import unittest
from app import app

class WebAppTestCases(unittest.TestCase):

    def setup(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_loginpage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        response = self.app.post('/login', data=dict(
            username='admin',
            password='1234'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_login_fail(self):
        response = self.app.post('/login', data=dict(
            username='wrong',
            password='wrong'
        ))
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()