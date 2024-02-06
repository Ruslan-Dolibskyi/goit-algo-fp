class Node:
    """Клас, який представляє вузол в однозв'язному списку"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Клас для реалізації однозв'язного списку"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає новий вузол в кінець списку"""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        """Виводить вміст списку"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсує однозв'язний список"""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def sort(self):
        """Сортує однозв'язний список використовуючи сортування злиттям"""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Допоміжна функція для сортування злиттям"""
        if not head or not head.next:
            return head

        left_half, right_half = self._split_list(head)
        left = self._merge_sort(left_half)
        right = self._merge_sort(right_half)

        return self._merge(left, right)

    def _split_list(self, head):
        """Розділяє список на дві половини"""
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        return head, slow

    def _merge(self, left, right):
        """Об'єднує два відсортовані списки"""
        if not left:
            return right
        if not right:
            return left

        if left.data < right.data:
            left.next = self._merge(left.next, right)
            return left
        else:
            right.next = self._merge(left, right.next)
            return right

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об'єднує два відсортовані списки в один"""
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


# Тестування
# Створення двох списків
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

# Виведення вмісту списків
print("Перший список:")
list1.print_list()

print("Другий список:")
list2.print_list()

# Сортування списків
list1.sort()
list2.sort()

# Реверсування першого списку
list1.reverse()

# Виведення вмісту відсортованих та реверсованих списків
print("\nВідсортований та реверсований перший список:")
list1.print_list()

print("Відсортований другий список:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(list1.head, list2.head)

# Виведення вмісту об'єднаного списку
print("\nОб'єднаний відсортований список:")
current = merged_list
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")