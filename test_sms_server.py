import unittest
from unittest.mock import patch, MagicMock
from sms_server import is_valid_phone_number, send_sms, twilio_client

class TestSMSServer(unittest.TestCase):
    def test_is_valid_phone_number(self):
        self.assertTrue(is_valid_phone_number('+1234567890'))
        self.assertFalse(is_valid_phone_number('1234567890'))
        self.assertFalse(is_valid_phone_number('123 456 7890'))

    @patch('sms_server.TWILIO_PHONE_NUMBER', 'test_twilio_number')
    @patch.object(twilio_client.messages, 'create')
    def test_send_sms(self, mock_create):
        mock_create.return_value = MagicMock()
        response = send_sms('+1234567890', 'test message')
        mock_create.assert_called_once_with(
            body='test message',
            from_='test_twilio_number',
            to='+1234567890'
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()