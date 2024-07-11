from sympy.logic import simplify_logic
import tkinter as tk

def lexer(expression):
    tokens = []
    position = 0
    while position < len(expression):
        if expression[position] == " ":
            position += 1
    
        elif (expression[position].isalpha() or expression[position] == ")") and position < len(expression)-1  and (expression[position+1].isalpha() or expression[position+1] == "!" or expression[position+1] == "("):
            tokens.append(expression[position])
            tokens.append("&")
            position += 1

        elif expression[position].isalpha():
            tokens.append(expression[position])
            position += 1

        elif expression[position] in "01!+*~|&()":
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

        elif token == "0":
            exp_for_simp.append("False")

        elif token == "1":
            exp_for_simp.append("True")

        elif token in "~|&()":
            exp_for_simp.append(token)

    exp_for_simp = ''.join(exp_for_simp)
    return simplify_logic(exp_for_simp)

def parse_expression():
    expression = entry.get()
    result.config(state='normal')
    result.delete(1.0, tk.END)

    if expression:
        tokens = lexer(expression)
        parsed_expression = parser(tokens)
        if parsed_expression == True:
            result.insert(tk.END, f'1')
        elif parsed_expression == False:
            result.insert(tk.END, f'0')
        else:
            result.insert(tk.END, f'{parsed_expression}')

    else:
        result.insert(tk.END, f'Invalid Expression!')

    result.config(state='disabled')

if __name__ == "__main__":
    main = tk.Tk()
    main.title("Boolean Expression Parser")
    main.resizable(False, False)

    entry_label = tk.Label(main, text="Expression: ")
    entry_label.grid(column=0, row=0, padx=10, pady=10)

    entry = tk.Entry(main, width=27)
    entry.grid(column=1, row=0)

    parse_button = tk.Button(main, text="Parse", command=parse_expression)
    parse_button.grid(column=2, row=0, padx=10, pady=10)

    result_label = tk.Label(main, text="Result: ")
    result_label.grid(column=0, row=2, columnspan=3, padx=10)

    result = tk.Text(main, width=42, height=1, state='disabled', font=('Arial', 10))
    result.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

    main.mainloop()