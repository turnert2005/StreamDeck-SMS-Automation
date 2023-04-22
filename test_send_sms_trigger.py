import unittest
from unittest.mock import patch
import send_sms_trigger


class TestSendSMSTrigger(unittest.TestCase):
    def test_is_server_running(self):
        send_sms_trigger.server_started = False
        self.assertFalse(send_sms_trigger.is_server_running())

    @patch('requests.post')
    def test_send_sms(self, mock_post):
        mock_post.return_value.status_code = 200
        send_sms_trigger.send_sms('test_twilio_phone_number', 'test_recipient_phone_number')
        mock_post.assert_called_once_with(
            'https://api.twilio.com/2010-04-01/Accounts/test_twilio_account_sid/Messages.json',
            auth=('test_twilio_account_sid', 'test_twilio_auth_token'),
            data={
                'From': 'test_twilio_phone_number',
                'To': 'test_recipient_phone_number',
                'Body': 'This is a test message from Stream Deck!'
            }
        )


if __name__ == '__main__':
    unittest.main()
