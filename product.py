class Product(object):
    def __init__(
        self, pcode: str, pro_name: str, quantity: int, saled: int, price: float
    ):
        """

        :pcode: The code of the product (this should be unique for the product).
        :pro_name: The name of the product.
        :quantity: The number of  products with the same code in a shop at beginning of a day.
        :saled: The number of  products with the same code, which are saled in the day.
        :price: The price of the product.

        """
        self._pcode = pcode
        self._pro_name = pro_name
        self._quantity = quantity
        self._saled = saled
        self._price = price

    def __repr__(self):
        return f"""
Product:
    - pcode: {self._pcode}
    - pro_name: {self._pro_name}
    - quantity: {self._quantity}
    - saled: {self._saled}
    - price: {self._price}
"""


if __name__ == "__main__":
    product = Product("1", "1", 3, 3, 1.2)
    print(product)
