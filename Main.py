class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here
    


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
     self.top = -1
    self.size_of_stack = size
    self.stack = []



  def isEmpty(self):
    
      # Write your code here
      return self.top == -1



  def pop(self):
   
    # Write your code here
    if not self.isEmpty():
        x = self.stack.pop()
        self.top = self.top - 1
        return x


  def push(self, operand):
    
    # Write your code here
  
        self.top += 1
        self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    
    # Write your code here
     counter_digit = counter_operand = 0
    for token in expression:
        if token.isdigit():
            counter_digit += 1
        else:
            counter_operand += 1
    return counter_digit == counter_operand + 1



  def evaluate_postfix_expression(self, expression):
    
    
    # Write your code here
     ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    }
    for token in expression:
        if token.isdigit():
            self.push(int(token))
        else:
            operand2 = self.mypop()
            operand1 = self.mypop()
            result = ops[token](operand1, operand2)
            self.push(int(result))
    return self.stack[0]


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
