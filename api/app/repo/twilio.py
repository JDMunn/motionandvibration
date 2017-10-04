from twilio.rest import Client


class Notifier(object):

    def __init__(self, client_number, recipient_number, account_sid, auth_token):
        self.client_number = client_number
        self.recipient_number = recipient_number
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)

    def __notify__(self, message):
        self.client.api.account.messages\
            .create(to=self.recipient_number,
                    from_=self.client_number,
                    body=message)
