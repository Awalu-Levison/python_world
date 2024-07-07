#!/usr/bin/python3
stack = []

# append() function
stack.append('A')
stack.append('W')
stack.append('A')
stack.append('L')
stack.append('U')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\n=========Elements popped from the stack in LIFO order=======')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements popped:')
print(stack)
