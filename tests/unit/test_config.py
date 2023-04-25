import os
import unittest
from importlib import reload
import config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.original_env = os.environ.copy()
        os.environ.update({
            'TWILIO_ACCOUNT_SID': 'test_account_sid',
            'TWILIO_AUTH_TOKEN': 'test_auth_token',
            'TWILIO_PHONE_NUMBER': 'test_phone_number',
            'RECIPIENT_PHONE_NUMBER': 'test_recipient_number',
            'FLASK_SERVER_HOST': '127.0.0.1',
            'FLASK_SERVER_PORT': '5000',
            'WAIT_FOR_SERVER_TO_START': '5'
        })
        reload(config)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.original_env)
        reload(config)

    def test_environment_variables(self):
        self.assertEqual(config.TWILIO_ACCOUNT_SID, 'test_account_sid')
        self.assertEqual(config.TWILIO_AUTH_TOKEN, 'test_auth_token')
        self.assertEqual(config.TWILIO_PHONE_NUMBER, 'test_phone_number')
        self.assertEqual(config.RECIPIENT_PHONE_NUMBER, 'test_recipient_number')
        self.assertEqual(config.FLASK_SERVER_HOST, '127.0.0.1')
        self.assertEqual(config.FLASK_SERVER_PORT, 5000)
        self.assertEqual(config.WAIT_FOR_SERVER_TO_START, 5)

if __name__ == '__main__':
    unittest.main()
