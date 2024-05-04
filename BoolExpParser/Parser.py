from sympy.logic import simplify_logic

def lexer(expression):
    tokens = []
    position = 0
    while position < len(expression):
        if expression[position] == " ":
            position += 1

        elif expression[position] == "(":
            tokens.append(expression[position])
            position += 1

        elif expression[position] == ")":
            tokens.append(expression[position])
            position += 1

        elif expression[position] == "+" or expression[position] == "|":
            tokens.append(expression[position])
            position += 1

        elif expression[position] == "*" or expression[position] == "&":
            tokens.append(expression[position])
            position += 1

        elif expression[position] == "!" or expression[position] == "~":
            tokens.append(expression[position])
            position += 1

        elif expression[position].isalnum():
            tokens.append(expression[position])
            position += 1
   
    return tokens

def parser(tokens):
    exp_for_simp = []
    for token in tokens:
        if token.isalnum():
            exp_for_simp.append(token)

        elif token == "!":
            exp_for_simp.append("~")

        elif token == "+":
            exp_for_simp.append("|")

        elif token == "*":
            exp_for_simp.append("&")

        elif token == "~":
            exp_for_simp.append(token)

        elif token == "|":
            exp_for_simp.append(token)

        elif token == "&":
            exp_for_simp.append(token)

        elif token == "(":
            exp_for_simp.append(token)

        elif token == ")":
            exp_for_simp.append(token)

    exp_for_simp = ''.join(exp_for_simp)
    return simplify_logic(exp_for_simp)


if __name__ == "__main__":
    while True:
        expression = input("Enter Boolean Expression: ")
        if expression == "":
            break
        tokens = lexer(expression)
        print(f"Simplified Expression: {parser(tokens)}\n")