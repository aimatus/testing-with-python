def charge_payment(email: str, amount: int):
  print('Connecting to Paypal')
  print(f'Charging ${amount} to ${email}')
  raise Exception(f'PayPal Error! Could not charge amount to user ${email}. API key required')
