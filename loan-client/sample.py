import loans_api

l = loans_api.LoansClient('http://localhost:3000/loans')

loan = l.get_loan(13)
print(loan)

l.create_loan(57050, 0.87, 36, 3075)

l.update_loan(10, 750523, .9, 24, 1250.75)