from api import app
import unittest, json

class FlaskTest(unittest.TestCase):
  # Check for response 404
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/')
    statuscode = response.status_code
    self.assertEquals(statuscode, 404)

  # Test Encrypt With GET Method
  def test_encrypt_with_get_method(self):
    tester = app.test_client(self)
    response =tester.get('/encrypt')
    statuscode = response.status_code
    self.assertEquals(statuscode, 405)

  # Test Encrypt
  def test_encrypt(self):
    tester = app.test_client(self)
    payload = {
      "data" : [
        {
            "text": "Message1"
        },
        {
            "text": "Message2"
        }
      ]
    }
    response = tester.post('/encrypt', data = json.dumps(dict(payload)), content_type='application/json')
    statuscode = response.status_code
    self.assertEquals(statuscode, 200)

  # Test Decrypt With GET Method
  def test_decrypt_with_get_method(self):
    tester = app.test_client(self)
    response =tester.get('/decrypt')
    statuscode = response.status_code
    self.assertEquals(statuscode, 405)

  # Test Decrypt 
  def test_decrypt(self):
    tester = app.test_client(self)
    payload = {
      "data" : [
        {
            "text": "Message1"
        },
        {
            "text": "Message2"
        }
      ]
    }
    encrypt_data = tester.post('/encrypt', data = json.dumps(dict(payload)), content_type='application/json')
    response = tester.post('/decrypt', data = json.dumps(dict(json.loads(encrypt_data.data))), content_type='application/json')
    statuscode = response.status_code
    self.assertEquals(statuscode, 200)

if __name__ == "__main__":
  unittest.main()