import pytest

from app.payment import charge_product

# Add description to logic
def test_should_return_product_information_and_payment_status_ok(mocker):
  # Arrange
  mocker.patch('external_libraries.paypal.charge_payment')
  product_id = 1
  email_dummy = 'mytestemail@test.com'
  expected_result = {
    'product': {
      'id': 1,
      'name': 'Nintendo Switch Oled',
      'price': 50000
    },
    'payment_status': 'ok'
  }

  # Act
  result = charge_product(id=product_id, email=email_dummy)

  # Assert
  assert result == expected_result


def test_should_charge_paypal_for_product_price(mocker):
  # Arrange
  charge_payment_spy = mocker.patch('external_libraries.paypal.charge_payment')
  product_id = 1
  email_dummy = 'mytestemail@test.com'

  # Act
  result = charge_product(id=product_id, email=email_dummy)

  # Assert
  charge_payment_spy.assert_called()


def test_should_email_user_with_product_details():
  pass


def test_should_use_proper_item_from_database():
  product_id = 89156
