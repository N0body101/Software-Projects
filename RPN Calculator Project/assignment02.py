"""
CS3B, stack implementation
Semmy Yoon
This is my second assignment. Thank you so much for the help that you gave after Wednesday class.
It was extremely helpful.
"""

import numpy as np

class MyStack:
    # Constants
    MAX_CAPACITY = 100000
    DEFAULT_CAPACITY = 10

    # Initializer method
    def __init__(self, default_item, capacity=DEFAULT_CAPACITY):
        # If the capacity is bad, fail right away
        if not self.validate_capacity(capacity):
            raise ValueError("Capacity " + str(capacity) + " is invalid")
        self.capacity = capacity
        self.default_item = default_item

        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def clear(self):
        # Allocate storage the storage and initialize top of stack
        self.stack = np.array([self.default_item for _ in range(self.capacity)])
        self.top_of_stack = 0

    @classmethod
    def validate_capacity(cls, capacity):
        return 0 <= capacity <= cls.MAX_CAPACITY



    def push(self, item_to_push):
        if self.is_full():
            raise OverflowError("Push failed - capacity reached")
        self.stack[self.top_of_stack] = item_to_push
        self.top_of_stack += 1


    def pop(self):
        if self.is_empty():
            raise IndexError("Pop failed - stack is empty")

        self.top_of_stack -= 1
        return self.stack[self.top_of_stack]

    def is_empty(self):
        return self.top_of_stack == 0

    def is_full(self):
        return self.top_of_stack == self.capacity

    def get_capacity(self):
        return self.capacity


def mystack_test():
    # Instantiate two empty stacks, one of 50 ints, another of 10 strings
    s1 = MyStack(-1, 50)
    s2 = MyStack("undefined")
    # and one more with bad argument
    try:
        s3 = MyStack(None, -100)
        print("Failed test: expected __init()__ to reject negative capcity but it didn't")
    except Exception as e:
        print("Successful test: handled negative capacity: " + str(e))

    # Confirm the stack capacities
    print("------ Stack Sizes -------\n  s1: {}   s2: {}\n".
          format(s1.get_capacity(), s2.get_capacity()))

    # Pop empty stack
    print("------ Test stack ------\n")
    try:
        s1.pop()
        print("Failed test: expected pop() to raise empty-stack exception but it didn't")
    except Exception as e:
        print("Successful test: handled popping empty s1: " + str(e))

    # Push some items
    s1.push(44)
    s1.push(123)
    s1.push(99)
    s1.push(10)
    s1.push(1000)
    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int stack")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s2.push(444)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s1.push(44.4)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    # Push to s2
    s2.push("bank")
    s2.push("-34")
    s2.push("should be okay")
    s2.push("a penny earned")
    s2.push("item #9277")
    s2.push("where am i?")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    try:
        s2.push("This is when stack is full")
        print("Failed test: expected push() to throw exception but it didn't")
    except Exception as e:
        print("Successful test: handled pushing when stack is full: " + str(e))
    print("\n--------- First Stack ---------\n")

    # Pop and inspect the items
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except Exception as e:
            print("Successful test: handled popping empty stack s1: " + str(e))
    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        print("[" + str(s2.pop()) + "]")

class RpnCalculator:
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "//"

    @staticmethod
    def eval(rpn_expression):
        my_parse = RpnCalculator.parse(rpn_expression)
        result = RpnCalculator.eval_tokens(my_parse)

        return result

    @staticmethod
    def parse(rpn_expression):
        return rpn_expression.split()

    @staticmethod
    def eval_tokens(tokens):
        if len(tokens) == 0:
            raise ValueError("Pop failed - stack is empty")
        count = 0
        x = MyStack(0, len(tokens))
        for token in tokens:
           try:
               x.push(int(token))
               count += 1
           except ValueError:
               if token == RpnCalculator.ADDITION:
                   a = x.pop()
                   b = x.pop()
                   x.push(b+a)
                   count -=1
               elif token == RpnCalculator.SUBTRACTION:
                   c = x.pop()
                   d = x.pop()
                   x.push(d-c)
                   count -= 1
               elif token == RpnCalculator.DIVISION:
                   e = x.pop()
                   f = x.pop()
                   x.push(f//e)
                   count -= 1
               elif token == RpnCalculator.MULTIPLICATION:
                   g = x.pop()
                   h = x.pop()
                   x.push(RpnCalculator.multiply(h, g))
                   count -= 1
               else:
                   raise ValueError("Not a number or a operator")

        if count == 1:
            return x.pop()
        else:
            raise ValueError("Not enough operator")


    @staticmethod
    def multiply(a, b):
        if a == 0 or b == 0:
            return 0
        elif b <0:
            return - a + RpnCalculator.multiply(a, b + 1)
        else:
            return a + RpnCalculator.multiply(a, b - 1)

def test_my_stack(default, capacity):
    try:
        s1 = MyStack(default, capacity)
        s1.push(2 ** 65)
    except OverflowError:
        print("There is an OverflowError. This code would work in list but"
              " not in numpy array. This is because numpy array have a fixed size. ")

def test_rpn():
    my_list = [" ", "1 1", "1 1 + +", "1 1 fly", "random junk",
               "3", "2 3 +", "2 3 -", "2 3 *", "2 3 4 + *", "2 3 + 5 -", "15 7 1 1 + - // 3 * 2 1 1 + + -"]
    for x in my_list:
        try:
            y = RpnCalculator.eval(x)
            print(f'({x}) = {y}')
            #print(f'\"{x}\" successfully to be evaluated: {y}')
        except Exception as e:
            print(f'\"{x}\" fails to evaluate: {e}')

    return ""


if __name__ == "__main__":
    test_my_stack(0, 4)
    print(test_rpn())
