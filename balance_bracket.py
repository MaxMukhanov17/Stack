from stack import Stack

def parChecker(sequence_bracket):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sequence_bracket):
        symbol = sequence_bracket[index]
        if symbol == "(" or symbol == '[' or symbol == '{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    
    if balanced and s.isEmpty():
        print('Сбалансировано')
    else:
        print('Несбалансировано')


if __name__ == '__main__':
    s = Stack()
    parChecker('(((([{}]))))')
    parChecker('[([])((([[[]]])))]{()}')
    parChecker('{{[()]}}')
    parChecker('}{}')
    parChecker('{{[(])]}}')
    parChecker('[[{())}]')