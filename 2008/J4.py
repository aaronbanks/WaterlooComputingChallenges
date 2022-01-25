def main():

    while True:
        prefix_input = input()

        if prefix_input == '0':
            return False

        input_items = prefix_input.split()

        stack = []

        input_items.reverse()

        for symbol in input_items:
            if symbol != "-" and symbol != "+":
                stack.append(symbol)
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                working_string = operand_1 + " " + operand_2 + " " + symbol + " " 
                stack.append(working_string)

        postfix_output = " ".join(stack)
        print(postfix_output)

main()