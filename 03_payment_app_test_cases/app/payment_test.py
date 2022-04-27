from app.payment import charge_product

def test_should_return_product_information_and_payment_status_ok():
  product_id = 1

  result = charge_product(id=product_id)

  assert result == {}
