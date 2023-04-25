import unittest
from unittest.mock import patch, MagicMock
import main

class TestSendSMSTrigger(unittest.TestCase):
    def test_is_server_running(self):
        main.server_started = False
        self.assertFalse(main.is_server_running())

    @patch('requests.post')
    def test_send_sms(self, mock_post):
        mock_post.return_value.status_code = 200
        response = main.send_sms()
        mock_post.assert_called_once_with(
            f"https://api.twilio.com/2010-04-01/Accounts/{main.config.TWILIO_ACCOUNT_SID}/Messages.json",
            auth=(main.config.TWILIO_ACCOUNT_SID, main.config.TWILIO_AUTH_TOKEN),
            data={
                'From': main.config.TWILIO_PHONE_NUMBER,
                'To': main.config.RECIPIENT_PHONE_NUMBER,
                'Body': 'I Love you Heather'
            }
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
