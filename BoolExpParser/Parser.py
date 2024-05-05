from sympy.logic import simplify_logic
import time, os

def lexer(expression):
    tokens = []
    position = 0
    while position < len(expression):
        if expression[position] == " ":
            position += 1
    
        elif (expression[position].isalpha() or expression[position] == ")") and position < len(expression)-1  and (expression[position+1].isalnum() or expression[position+1] == "!" or expression[position+1] == "("):
            tokens.append(expression[position])
            tokens.append("&")
            position += 1

        elif expression[position].isalpha():
            tokens.append(expression[position])
            position += 1

        elif expression[position] in "!+*~|&()":
            tokens.append(expression[position])
            position += 1
            
    return tokens

def parser(tokens):
    exp_for_simp = []
    for token in tokens:
        if token.isalpha():
            exp_for_simp.append(token)

        elif token == "!":
            exp_for_simp.append("~")

        elif token == "+":
            exp_for_simp.append("|")

        elif token == "*":
            exp_for_simp.append("&")

        elif token in "~|&()":
            exp_for_simp.append(token)

    exp_for_simp = ''.join(exp_for_simp)
    return simplify_logic(exp_for_simp)

if __name__ == "__main__":
    while True:
        os.system('cls')
        print("Boolean Expression Parser\n")
        expression = input("Enter Boolean Expression (Leave blank to exit): ")
        if expression == "":
            print("Exiting...")
            time.sleep(1)
            break
        tokens = lexer(expression)
        simplified_exp = parser(tokens)
        print(f"Simplified Expression: {simplified_exp}\n")
        input("Press Enter to parse your next expression...")