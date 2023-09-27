import random
from validator import Validator


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"

        return result

    def insert_from_keyboard(self):
        number = input("Введіть кількість елементів\n")
        while not Validator.is_positive_integer(number):
            number = input("Введіть кількість елементів\n")
        number = int(number)

        for i in range(number):
            elem = input("Введіть елемент ")

            while not Validator.is_integer(elem):
                elem = input("Введіть число ")

            self.insert(int(elem))

    def insert_random(self, a, b, n):
        for _ in range(n):
            self.insert(random.randint(a, b + 1))

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_in_k(self, data, k):
        if k < 0:
            raise ValueError("Позиція має бути невід'ємним числом.")

        if not self.head:
            raise ValueError("Цей список порожній")

        new_node = Node(data)

        if k == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while count < k - 1 and current.next:
            current = current.next
            count += 1

        if not current.next and count < k - 1:
            raise IndexError("Позиція виходить за межі списку.")

        new_node.next = current.next
        current.next = new_node

    def delete_at(self, k):
        # Видалити елемент з k позиції
        if k < 0:
            raise ValueError("Позиція має бути невід'ємним числом.")

        if not self.head:
            raise ValueError("Цей список порожній")

        if k == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0
        while current and count < k:
            prev = current
            current = current.next
            count += 1
        if not current:
            raise IndexError("Позиція виходить за межі списку.")
        prev.next = current.next

    def is_sorted(self):
        if not self.head:
            raise ValueError("Цей список порожній")

        current = self.head
        while current.next:
            if current.next.data < current.data:
                return False
            current = current.next

        return True

    def calc_neighbor_differ_product(self):
        if not self.head:
            raise ValueError("Цей список порожній")

        if not self.head.next:
            raise ValueError("Недостатньо елементів для розрахунку")

        product = 1
        current = self.head
        while current.next:
            product *= current.next.data-current.data
            current = current.next

        return product

    def sum_of_positive(self):
        if not self.head:
            raise ValueError("Цей список порожній")

        sum = 0
        current = self.head
        while current:
            if current.data>0:
                sum += current.data
            current = current.next
        return sum
