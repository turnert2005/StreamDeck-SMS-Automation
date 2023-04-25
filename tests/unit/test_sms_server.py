from unittest import TestCase
from unittest.mock import patch
import config
from main import send_sms

class TestSendSms(TestCase):
    @patch('config.TWILIO_PHONE_NUMBER', 'test_twilio_number')
    @patch('config.TWILIO_ACCOUNT_SID', 'test_twilio_account_sid')
    @patch('config.TWILIO_AUTH_TOKEN', 'test_twilio_auth_token')
    @patch('config.RECIPIENT_PHONE_NUMBER', 'test_recipient_phone_number')
    @patch('main.requests.post')
    def test_send_sms(self, mock_post):
        mock_post.return_value.status_code = 200
        response = send_sms()
        mock_post.assert_called_once_with(
            f'https://api.twilio.com/2010-04-01/Accounts/test_twilio_account_sid/Messages.json',
            auth=('test_twilio_account_sid', 'test_twilio_auth_token'),
            data={
                'From': 'test_twilio_number',
                'To': 'test_recipient_phone_number',
                'Body': 'I Love you Heather'
            }
        )
        self.assertEqual(response.status_code, 200)
