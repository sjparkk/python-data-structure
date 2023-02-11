"""
괄호 유효성 문제

‘() {} []’ 를 포함하고 있는 문자열 s 주어졋을 때, 괄호가 유효한지 아닌지 판별

제약 조건
1. 1 <= s.length <= 10의 4승
    -> n의2승 으로 문제를 풀게 되면 10의 8승이 되므로 제약조건에 문제가 발생할 수 있다 -> 그러니 nlogn 이하 (nlogn -> n -> logn)로 문제를 해결해야됨
2. 문자열 s는 ‘()[]{}’의 괄호 들로만 구성되어 있다
    -> 이것은 다른 예외 케이스가 없으니 신경 쓸 필요가 없다는 도움을 준 것.
"""
"""
스택의 LIFO 특성으로 문제를 해결
리스트의 append와 pop을 통해 구현 가능.
"""
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack


s = ["{", "(", "(", "[", "]", ")", ")", "[", "]", "}"]

print(isValid(s))
