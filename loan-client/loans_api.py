import requests

class LoansClient:
    def __init__(self, base_url):
        self.url = base_url

    def set_url(self, url):
        self.url = url

    def get_loan(self, loan_id):
        get_url = self.url + '/get/'
        payload = { 'loanId': loan_id }
        r = requests.get(get_url, data=payload)
        return r.json()

    def create_loan(self, amount, interest, length, payment_amount):
        payload = {
            'amount': amount,
            'interest': interest,
            'length': length,
            'payment_amount': payment_amount
        }

        r = requests.post(self.url, payload)
        print(r.text)

    def update_loan(self, loanId, amount, interest, length, payment_amount):
        payload = {
            'amount': amount,
            'interest': interest,
            'length': length,
            'payment_amount': payment_amount
        }
        r = requests.put(self.url + '/' + str(loanId), payload)
        print(r.text)