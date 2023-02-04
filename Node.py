class Node :
    """
    __init__ 의 이해
    - 컨스트럭터라고 불리는 초기화를 위한 함수(메소드)
    - 인스턴스화를 실시할 때 반드시 처음에 호출되는 특수한 함수
    - 오브젝트 생성(인스턴스를 생성)과 관련하여 데이터의 초기를 실시하는 함수

    self 의 역할
    - 인스턴스 자신, 그 시점의 자신, 메소드의 임의의 인수 등
    """
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

# node 연결
first.next = second
second.next = third
first.value = 6