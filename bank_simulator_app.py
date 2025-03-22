class Loan:
    def __init__(self,user_full_name,principal, interest_rate,term):
        self.user_full_name = user_full_name
        self.principal = float(principal)
        self.interest_rate  = float(interest_rate)
        self.term = int(term)
        self.monthly_rate = (interest_rate/1200)
        
    def monthly_payment(self):
        n = self.number_of_payments()
        monthly_due = (self.principal*self.monthly_rate*((1+self.monthly_rate)**n))/(((1+self.monthly_rate)**n)-1)
        return monthly_due
    def number_of_payments(self):
        return self.term * 12
    def total_interest():
        pass
    def check_50_percent():
        pass
    def adjust_loan_term():
        pass
    

loan1 = Loan("John Nti", 100000,5.2,20)
print(loan1.monthly_payment())