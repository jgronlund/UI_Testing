import unittest

from unittest import mock
from apis.user_service import UserService, BillingService

def get_auth(username):
    user_app = UserService()
    if user_app.external_auth_check(username):
        return True
    else:
        raise ValueError("Username not registered")


class All_Tests(unittest.TestCase):
    
    def setUp(self):
        self.userservice = UserService()
        self.billingservice = BillingService()
        self.my_mock = mock.Mock()

    def test_get_users(self):
        self.assertDictEqual(self.userservice.get_user("alice"), {"email": "alice@example.com", "role": "admin"})
        self.assertDictEqual(self.userservice.get_user("bob"), {"email": "bob@example.com", "role": "user"})

        
    def test_get_user_fails(self):
        with self.assertRaises(ValueError) as context:
            self.userservice.get_user("nonuser")
        self.assertEqual(str(context.exception), "User not found")

    @mock.patch('apis.user_service.UserService.external_auth_check')
    def test_get_auth(self, mock_auth):
        mock_auth.return_value = True
        result = get_auth("bob")
        self.assertTrue(result)
        mock_auth.assert_called_once_with("bob")

    @mock.patch('apis.user_service.UserService.external_auth_check')
    def test_get_auth_fail(self, mock_auth):
        mock_auth.return_value = False
        with self.assertRaises(ValueError) as context:
            get_auth("non_user")
        self.assertEqual(str(context.exception), "Username not registered")

    @mock.patch('apis.user_service.UserService.create_user')
    def test_billing_charge(self, mock_createuser):
        mock_createuser.return_value = {"email": "bob@example.com", "role": "user"}
        self.assertTrue(self.billingservice.charge("bob", "bob@example.com"))
        mock_createuser.assert_called_once_with("bob", "bob@example.com")

    def test_deleting_user(self):
        result = self.userservice.delete_user("bob")
        self.assertTrue(result)

        with self.assertRaises(ValueError) as context:
            self.userservice.get_user("bob")
        self.assertEqual(str(context.exception), "User not found")


if __name__ == "__main__":
    unittest.main()
    


