"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Allison Nguyen and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ann2464
UT EID 2:
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        Inserts the term into the current polynomial
        """
        my_node = Node(coeff,exp)

        if coeff == 0:
            return

        my_node = Node(coeff, exp)

        if self.head is None or self.head.exp < exp:
            my_node.next = self.head
            self.head = my_node
            return

        current = self.head
        previous = None

        while current is not None and current.exp > exp:
            previous = current
            current = current.next

        if current is not None and current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
            return

        my_node.next = current
        previous.next = my_node


    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        Adds another polynomial p to the current polynomial and returns a new linked list
        """
        result = LinkedList()
        current = self.head

        while current:
            result.insert_term(current.coeff, current.exp)
            current = current.next

        current = p.head

        while current:
            result.insert_term(current.coeff, current.exp)
            current = current.next

        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        Multiplies our current polynomial by another polynomial changing the coefficients and exponents, and returns a new linked list
        """
        result = LinkedList()

        current = self.head
        while current:
            temp = LinkedList()

            other = p.head
            while other:
                temp.insert_term(current.coeff*other.coeff, current.exp + other.exp)
                other = other.next

            result = result.add(temp)
            current = current.next
        return result

    # Return a string representation of the polynomial.
    def __str__(self): 
        """
        Outputs how we want our polynomial formatted once printed
        """
        if self.head is None:
            return ""
            
        poly = []
        current = self.head

        while current is not None:
            poly.append(f"({current.coeff}, {current.exp})")
            current = current.next

        return " + ".join(poly)


def main():
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product

    n = int(input().strip())
    p = LinkedList()

    for _ in range(n):
        p.insert_term(*map(int, input().split()))

    input()

    m = int(input().strip())
    q = LinkedList()

    for _ in range(m):
        q.insert_term(*map(int, input().split()))

    print(p.add(q))
    print(p.mult(q))

if __name__ == "__main__":
    main()
