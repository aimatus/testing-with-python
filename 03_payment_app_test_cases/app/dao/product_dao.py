from app.model.product_model import Product

def get_product_by_id(id: int):
  product = Product()
  product.id = 1
  product.name = 'Nintendo Switch Oled'
  product.price = 50000
  