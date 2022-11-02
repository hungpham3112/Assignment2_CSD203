class Customer(object):
    def __init__(self, ccode: str, cus_name: str, phone: str):
        """

        :ccode: The code of the customer (this should be unique for the customer).
        :cus_name: The name of the customer.
        :phone: The phone number of the customer (must contain digits only).

        """
        self._ccode = ccode
        self._cus_name = cus_name
        self._phone = phone

    def __repr__(self):
        return f"""
Customer:
    - ccode: {self._ccode}
    - cus_name: {self._cus_name}
    - phone: {self._phone}
    """
