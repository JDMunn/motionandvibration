from twilio.rest import Client


class Notifier(object):

    def __init__(self, client_number, recipient_numbers, account_sid, auth_token):
        self.client_number = client_number
        self.recipient_numbers = recipient_numbers.split(',')
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)

    def __notify__(self, message):
        for recipient_number in self.recipient_numbers:
            self.client.api.account.messages\
                .create(to=recipient_number,
                        from_=self.client_number,
                        body=message)
