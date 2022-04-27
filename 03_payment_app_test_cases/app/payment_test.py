from app.payment import charge_product

# Add description to logic
def test_should_return_product_information_and_payment_status_ok():
  # Arrange
  product_id = 1
  expected_result = {
    'product': {
      'id': 1,
      'name': 'Nintendo Switch Oled',
      'price': 50000
    },
    'payment_status': 'ok'
  }

  # Act
  result = charge_product(id=product_id)

  # Assert
  assert result == expected_result
