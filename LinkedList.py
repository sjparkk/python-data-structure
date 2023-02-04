class LinkedList(object):
    def __init__(self):
        self.head = None
        """
        O(1) version -> tail version
        self.tail = None
        """

    def append(self, value):
        new_node = Node(value)
        #head는 무조건 첫번째를 가리켜야 하기 때문에 head가 값이 없을 때만 설정
        if self.head is None:
            self.head = new_node
            """
            O(1) version -> tail version
            self.tail = new_node
            """
        # O(n) - 이후로는 head로 접근하여 다음 노드를 찾는다. 그리고 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        """
        O(1) version -> tail version
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        """


class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next