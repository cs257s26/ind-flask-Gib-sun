from app import app
import unittest
class TestSomething(unittest.TestCase):
    def setUp(self):
        # set up test app
        self.client = app.test_client()
        self.client.testing = True

    def test_creator_found(self): 

        response = self.client.get("/creator/Shoes")
        
        self.assertEqual(response.status_code, 200)
        

    def test_creator_not_found(self):
        response = self.client.get("/creator/ThisDoesNotExist")
        
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()