# Use proper naming conventions for a class name
class MortgageCalculator(FinancialCalculator):
  def __init__(self, loan_amount, annual_interest_rate, years):
    super().__init__()
    self.loan_amount = loan_amount
    self.monthly_interest_rate = self.monthly_interest(annual_interest_rate)
    self.months = self.multiply(years, 12)
  
  # Use proper naming conventions for a function name
  def calculate_monthly_payment(self):
    numerator = self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.months
    denominator = (1 + self.monthly_interest_rate) ** self.months - 1
    multiplier = self.divide(numerator, denominator)
    monthly_payment = round(self.multiply(self.loan_amount, multiplier), 2)
    return monthly_payment
