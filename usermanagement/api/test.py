import requests
import unittest

class TestUserCreation(unittest.TestCase):
    def setUp(self):
        # Set up the base URL of your Django application
        self.base_url = 'http://localhost:8000/api/users/'

    def test_create_user(self):
        # Define the payload for the POST request
        payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'company_name': 'Test Company',
            'age': 30,
            'city': 'New York',
            'state': 'NY',
            'zip': 12345,
            'email': 'joh@example.com',
            'web': 'http://www.example.com'
        }

        # Send a POST request to create a new user
        response = requests.post(self.base_url, json=payload)

        # Assert that the status code is 201 Created
        self.assertEqual(response.status_code, 201)

        user_data = response.json()
        self.assertEqual(user_data['first_name'], 'John')

    def test_get_users(self):
        # Send a GET request to retrieve the list of users
        response = requests.get(self.base_url)

        self.assertEqual(response.status_code, 200)

        users = response.json()['results']
        self.assertGreaterEqual(len(users), 0)


if __name__ == '__main__':
    unittest.main()
