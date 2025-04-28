class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def add_product_to_list(product: Product):
        if product in product:
            #print("Please check products")
            raise ValueError(f"Please check products")