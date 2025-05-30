import time
import random

class UserService:
    def __init__(self):
        # Simulated user "database"
        self.users = {
            "alice": {"email": "alice@example.com", "role": "admin"},
            "bob": {"email": "bob@example.com", "role": "user"}
        }

    def get_user(self, username):
        """Simulates fetching user data from a database or API."""
        time.sleep(0.5)  # simulate latency
        if username in self.users:
            return self.users[username]
        else:
            raise ValueError("User not found")

    def create_user(self, username, email, role="user"):
        """Creates a new user"""
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = {"email": email, "role": role}
        return self.users[username]

    def delete_user(self, username):
        """Deletes a user"""
        if username not in self.users:
            raise ValueError("User does not exist")
        del self.users[username]
        return True

    def external_auth_check(self, username):
        """Simulates an external API call (to mock)"""
        # Pretend this is a call to an external authentication service
        time.sleep(0.2)
        return random.choice([True, False])