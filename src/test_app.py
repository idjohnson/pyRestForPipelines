import unittest
from app import app

class FlaskApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_status_pending(self):
        response = self.app.get('/approved')
        self.assertEqual(response.data, b'{"status" : "pending"}')
        self.assertEqual(response.status_code, 200)

    def test_post_status_approved(self):
        self.app.post('/approved', json={"status": "approved"})
        response = self.app.get('/approved')
        self.assertEqual(response.data, b'{"status" : "approved"}')
        self.assertEqual(response.status_code, 200)

    def test_post_status_pending(self):
        self.app.post('/approved', json={"status": "pending"})
        response = self.app.get('/approved')
        self.assertEqual(response.data, b'{"status" : "pending"}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()