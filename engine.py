from product import Product
from customer import Customer
from ordering import Ordering
from binary_search_tree import ProductBSTree
from linkedlist import CustomerLinkedList, OrderingLinkedList
from node import Node
from utils import formatted_input
from contextlib import redirect_stdout

product_data, customer_data, ordering_data = ProductBSTree(), CustomerLinkedList(), OrderingLinkedList()


class ProductEngine:
    def __init__(self):
        self.bstree = product_data

    def save_object_list(self, file: str):
        if file == "":
            return True
        with open(file, "w") as f:
            with redirect_stdout(f):
                self.bstree.invisit()
            print("Save file successfully!!!")
        input("Press Enter to continue...")
        return True

    def search_by_object(self, code):
        node = self.bstree.findNode(code)
        if node:
            return node
        else:
            return "Not Found"

    def option1(self, linkedlist):
        try:
            file = input("Enter the file name: ").strip()
            if file == "":
                return True
            else:
                self.linkedlist = linkedlist
                self.load_data_from_file(file)
        except:
            print("File format is invalid")
        input("Press Enter to continue...")

    def option3(self):
        self.bstree.invisit()
        input("Press Enter to continue...")

    def option4(self):
        self.bstree.breadth_first()
        input("Press Enter to continue...")

    def option5(self):
        file = input("Enter file: ")
        self.save_object_list(file)

    def option6(self):
        pcode = formatted_input("Search pcode: ")
        print(self.bstree.findNode(pcode))
        input("Press Enter to continue...")

    def option7(self, code):
        try:
            if code == "":
                return True
            node = self.bstree.findNode(code)
            node = self.linkedlist.pop_code(code)
            assert node is not None
            if isinstance(node.data, Product):
                if not self.linkedlist.search(code):
                    print(f"Delete {node.data._pcode} successfully")
                else:
                    print(f"{code} does not exist!!!")

            if isinstance(node.data, Customer):
                if not self.linkedlist.search(code):
                    print(f"{code}")
                else:
                    print(f"Delete {node.data._ccode} successfully")
        except Exception:
            print(f"{code} is invalid input")
        input("Press Enter to continue...")
        

    def display_base_menu(self):
        return """
1.1.      Load data from file
1.2.      Input & insert data
1.3.      In-order traverse
1.4.      Breadth-first traverse
1.5.      In-order traverse to file
1.6.      Search by pcode
1.7.      Delete by pcode by copying
1.8.      Simply balancing
1.9.      Count number of products
"""

    def matching(self, stdin):
        match stdin:
            case "1":
                self.option1(ProductBSTree())
                return True
            case "2":
                while True:
                    try:
                        pcode = formatted_input("Enter pcode (blank to leave): ")
                        if pcode == "":
                            return True
                        elif (
                            pcode[0] != "P"
                            or (pcode[0] == "P" and not pcode[1:].isdigit())
                            or len(pcode) < 3
                        ):
                            print(
                                "Invalid product code. The format should be: P<number>. E.g: P02, P299..."
                            )
                            continue
                        elif self.search_by_object(pcode) != "Not Found":
                            print(f"The pcode: {pcode} already exist.")
                            continue
                        pro_name = formatted_input("Enter pro_name: ").capitalize()
                        if pro_name == "":
                            continue
                        quantity = int(formatted_input("Enter quantity: "))
                        saled = int(formatted_input("Enter saled (saled <= quantity): "))
                        if saled > quantity:
                            print("Invalid input!!!")
                            continue
                        price = float(formatted_input("Enter price: "))
                        product = Product(pcode, pro_name, quantity, saled, price)
                        self.bstree.insert(product)
                        input("Press Enter to continue...")
                        return True
                    except:
                        print("Invalid input!!!")
                        continue
            case "3":
                self.option3()
                return True
            case "4":
                self.option4()
                return True
            case "5":
                file = input("Enter the file name (blank to quit): ").strip()
                if file == "":
                    return True
                self.save_object_list(file)
                return True
            case "6":
                self.option6()
                return True
            case "7":
                while True:
                    try:
                        pcode = formatted_input("Enter pcode (blank to leave): ")
                        if pcode == "":
                            return True
                        elif (
                            pcode[0] != "P"
                            or (pcode[0] == "P" and not pcode[1:].isdigit())
                            or len(pcode) < 3
                        ):
                            print(
                                "Invalid product code. The format should be: P<number>. E.g: P02, P299..."
                            )
                            continue
                        self.deletebycopyleft(self.bstree.root, int(pcode[1:]))
                        print(f"Delete {pcode} successfully.")
                        input("Press Enter to continue...")
                        return True
                    except:
                        print("Invalid input!!!")
                        continue
            case "8":
                self.bstree.balanceTree()
                input("Press Enter to continue...")
                return True
            case "9":
                print(f"The number of product(s): {self.bstree.count_nodes(self.bstree.root)}")
                input("Press Enter to continue...")
                return True
            case "0":
                global product_data
                product_data = self.bstree
                return False
            case _:
                return True

    def deletebycopyleft(self, root, pcode):
        if not root: return None
        if int(root.data._pcode[1:]) == pcode:
            if not root.right and not root.left: return None
            if not root.right and root.left: return root.left
            if root.right and not root.left: return root.right
            else:
                temp = root.left
                while temp.right:
                    temp = temp.right
                root.data = temp.data
                temp.data = None
        elif int(root.data._pcode[1:]) > pcode:
            root.left = self.deletebycopyleft(root.left, pcode)
        else:
            root.right = self.deletebycopyleft(root.right, pcode)
        return root 

    def load_data_from_file(self, file: str, delimiter: str = "|"):
        try:
            with open(file, "r") as f:
                for i in map(
                    lambda lst: map(lambda char: char.strip(), lst),
                    map(
                        lambda line: line.split(delimiter),
                        filter(None, f.read().splitlines()),
                    ),
                ):
                    pcode, pro_name, quantity, saled, price = i
                    pcode, pro_name, quantity, saled, price = (
                        pcode,
                        pro_name,
                        int(quantity),
                        int(saled),
                        float(price),
                    )
                    node = Product(pcode, pro_name, quantity, saled, price)
                    self.bstree.insert(node)
            print("Loading file successfully!!!")
            return self.bstree

        except FileNotFoundError:
            print(f'File: "{file}" not found')

    def delete_after_pcode(self, pcode: str):
        if pcode == "":
            return True
        node = self.linkedlist.pop_after_code(pcode)

        if node:
            print(f"Delete after {node._pcode} successfully")
        elif not self.linkedlist.search(pcode):
            print(f"{pcode} does not exist!!!")
        else:
            print(f"No pcode after {pcode}")


class CustomerEngine(ProductEngine):
    def __init__(self):
        self.linkedlist = customer_data

    def load_data_from_file(self, file: str, delimiter: str = "|"):
        try:
            with open(file, "r") as f:
                for i in map(
                    lambda lst: map(lambda char: char.strip(), lst),
                    map(lambda line: line.split(delimiter), f.readlines()),
                ):
                    ccode, name, phone = i
                    node = Node(Customer(ccode, name, phone))
                    self.linkedlist.append(node)
            print("Loading file successfully!!!")
            return self.linkedlist

        except FileNotFoundError:
            print(f'File: "{file}" not found')

    def matching(self, stdin):
        match stdin:
            case "1":
                self.option1(CustomerLinkedList())
                return True
            case "2":
                while True:
                    try:
                        ccode = formatted_input("Enter ccode (blank to leave): ")
                        if ccode == "":
                            return self.linkedlist
                        elif (
                            ccode[0] != "C"
                            or (ccode[0] == "C" and not ccode[1:].isdigit())
                            or len(ccode) < 3
                        ):
                            print(
                                "Invalid product code. The format should be: C<number>. E.g: C02, C299..."
                            )
                            continue
                        name = formatted_input("Enter name: ").capitalize()
                        phone = int(formatted_input("Enter phone: "))
                        customer = Customer(ccode, name, str(phone))
                        self.linkedlist.append(Node(customer))
                        input("Press Enter to continue...")
                        return True
                    except:
                        print("Invalid input!!!")
                        continue
            case "3":
                print(self.display_data())
                input("Press Enter to continue...")
                return True
            case "4":
                file = input("Enter the file name (blank to quit): ").strip()
                if file == "":
                    return True
                with open(file, "w") as f:
                    f.write(self.display_data())
                    print("Save file successfully!!!")
                input("Press Enter to continue...")
            case "5":
                ccode = formatted_input("Enter ccode: ")
                node = self.linkedlist.search(ccode)
                if node:
                    print(node)
                else:
                    print("Not Found")
                input("Press Enter to continue...")
                return True
            case "6":
                code = formatted_input("Delete code: ")
                try:
                    if code == "":
                        return True
                    node = self.linkedlist.pop_code(code)
                    assert node is not None
                    if isinstance(node.data, Customer):
                        if not self.linkedlist.search(code):
                            print(f"Delete {node.data._ccode} successfully.")
                        else:
                            print(f"{code} does not exist!!!")
                except Exception:
                    print(f"{code} is invalid input")
                return True
            case "0":
                global customer_data
                customer_data = self.linkedlist
                return False
            case _:
                return True

    def display_base_menu(self):
        return """
2.1.      Load data from file
2.2.      Input & add to the end
2.3.      Display data
2.4.      Save customer list to file
2.5.      Search by ccode
2.6.      Delete by ccode
2.0.      Quit
"""

    def display_data(self):
        space = 15
        first_line = f"{'CustomerCode':<{space}}|{'Name':<{space}}|{'Phone':<{space}}"
        separate_line = "-" * space * 3
        detail = ""
        for node in self.linkedlist:
            data = node.data
            ccode = data._ccode
            name = data._cus_name
            phone = data._phone
            detail += f"{ccode:<{space}}|{name:<{space}}|{phone:<{space}}\n"
        table = f"{first_line}\n{separate_line}\n{detail}"
        global customer_table
        customer_table = table
        return table


class OrderingEngine():
    matching_list, value_list = [], []
    def __init__(self):
        super().__init__()
        self.linkedlist = ordering_data

    def matching(self, stdin):
        match stdin:
            case "1":
                while True:
                    try:
                        pcode = formatted_input("Enter pcode (blank to leave): ")
                        product_search = product_data.findNode(pcode)
                        if pcode == "":
                            return True
                        elif (
                            pcode[0] != "P"
                            or (pcode[0] == "P" and not pcode[1:].isdigit())
                            or len(pcode) < 3
                        ):
                            print(
                                "Invalid product code. The format should be: P<number>. E.g: P02, P299..."
                            )
                            continue
                        elif product_search in (False, None):
                            print(f"{pcode} is not in database")
                            continue
                        ccode = formatted_input("Enter ccode: ")
                        global customer_data
                        customer_search = customer_data.search(ccode)
                        if (
                            ccode[0] != "C"
                            or (ccode[0] == "C" and not ccode[1:].isdigit())
                            or len(ccode) < 3
                        ):
                            print(
                                "Invalid product code. The format should be: C<number>. E.g: C02, C299..."
                            )
                            continue
                        elif customer_search == False:
                            print(f"{ccode} is not in database")
                            continue
                        global ordering_data
                        if (pcode, ccode) in self.matching_list:
                            print(f"{pcode} and {ccode} already in order list!!!")
                            continue

                        if product_search and customer_search:
                            assert isinstance(product_search, Product)
                            if product_search._saled == product_search._quantity:
                                print("The product is exhauted")
                                continue
                            else:
                                print(f"{pcode} has {product_search._quantity - product_search._saled} remainders")

                        quantity = int(input(("Enter quantity: ")))
                        assert isinstance(product_search, Product)
                        if quantity <= (product_search._quantity - product_search._saled):
                            self.linkedlist.append(Node(Ordering(pcode, ccode, quantity)))
                            product_search._saled += quantity
                            print("Order successfully!!!")
                            self.matching_list.append((pcode, ccode))
                            self.value_list.append(f"{product_data.findNode(pcode)._price * quantity:.1f}")
                        else:
                            print("Not enough item to order!!!")
                            continue
                        input("Press Enter to continue...")
                        return True
                    except:
                        print("Invalid input!!!")
                        continue
            case "2":
                print(self.display_data())
                input("Press Enter to continue...")
                return True
            case "3":
                print(self.display_sorted_data())
                input("Press Enter to continue...")
                return True
            case "0":
                ordering_data = self.linkedlist
                return False
            case _:
                return True

    def display_base_menu(self):
        return """
3.1.      Input data
3.2.      Display data with total value
3.3.      Sort by pcode + ccode
3.0.      Quit
"""
    def display_data(self):
        space = 15
        first_line = f"{'Pcode':<{space}}|{'Ccode':<{space}}|{'Value':<{space}}"
        separate_line = "-" * space * 3
        detail = ""
        global value_list
        for (pcode, ccode), value in zip(self.matching_list, self.value_list):
            detail += f"{pcode:<{space}}|{ccode:<{space}}|{value:<{space}}\n"
        table = f"{first_line}\n{separate_line}\n{detail}"
        return table

    def display_sorted_data(self):
        space = 15
        first_line = f"{'Pcode':<{space}}|{'Ccode':<{space}}|{'Value':<{space}}"
        separate_line = "-" * space * 3
        detail = ""
        global value_list
        for (pcode, ccode), value in sorted(zip(self.matching_list, self.value_list)):
            detail += f"{pcode:<{space}}|{ccode:<{space}}|{value:<{space}}\n"
        table = f"{first_line}\n{separate_line}\n{detail}"
        return table


if __name__ == "__main__":
    product_engine = ProductEngine()
    product_engine.load_data_from_file("product.txt")
    product_engine.option3()
    customer_engine = CustomerEngine()
    customer_engine.load_data_from_file("customer.txt")
    print(customer_engine.display_data())
    ordering = OrderingEngine()
    ordering.matching("1")
    ordering.matching("2")
    ordering.matching("1")
    ordering.matching("2")
    ordering.matching("1")
    ordering.matching("2")
    ordering.matching("3")
    print(sorted(zip(ordering.matching_list, ordering.value_list)))
