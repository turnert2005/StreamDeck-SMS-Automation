import unittest
from unittest.mock import patch
import config

class TestConfig(unittest.TestCase):
    @patch('os.getenv')
    def test_environment_variables(self, mock_getenv):
        mock_getenv.side_effect = ['test_account_sid', 'test_auth_token', 'test_phone_number', 'test_recipient_number', '127.0.0.1', 5000, 5]
        self.assertEqual(config.TWILIO_ACCOUNT_SID, 'test_account_sid')
        self.assertEqual(config.TWILIO_AUTH_TOKEN, 'test_auth_token')
        self.assertEqual(config.TWILIO_PHONE_NUMBER, 'test_phone_number')
        self.assertEqual(config.RECIPIENT_PHONE_NUMBER, 'test_recipient_number')
        self.assertEqual(config.FLASK_SERVER_HOST, '127.0.0.1')
        self.assertEqual(config.FLASK_SERVER_PORT, 5000)
        self.assertEqual(config.WAIT_FOR_SERVER_TO_START, 5)

if __name__ == '__main__':
    unittest.main()