import external_libraries.paypal as paypal
import app.dao.product_dao as dao

def charge_product(id: int, email: str):
  product = dao.get_product_by_id(id)

  paypal.charge_payment(email, product.price)

  return {
    'product': product.__dict__,
    'payment_status': 'ok'
  }
