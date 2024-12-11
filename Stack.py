def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''
    for char in expression:
        if char.isdigit():  # Check if character is a digit
            postfix += char
        if char == '(':
            stack.append(char)
        if char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Pop the '('
        else:  # Operator
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():  # Check if character is a digit
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)
    return stack.pop()

def main():
    infix_expression = input("Enter the infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Postfix expression:", postfix_expression)
    result = evaluate_postfix(postfix_expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
