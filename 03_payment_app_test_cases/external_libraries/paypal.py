def charge_payment(email: str, price: int):
  print('Connecting to Paypal')
  print(f'Charging ${price} to ${email}')
  raise Exception(f'PayPal Error! Could not charge amount to user ${email}. API key required')
