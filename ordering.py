class Ordering(object):
    def __init__(self, pcode: str, ccode: str, quantity: int):
        """
        :pcode: The code of the product to be ordered.
        :ccode: The code of the customer.
        :quantity: The number of  ordered products.

        """
        self._pcode = pcode
        self._ccode = ccode
        self._quantity = quantity

    def __repr__(self):
        return f"""
Order:
    - pcode: {self._pcode}
    - ccode: {self._ccode}
    - quantity : {self._quantity}
    """
