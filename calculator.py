import tkinter as tk

# Fenêtre principale
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#45458B")
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
width = 250
height = 220
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
# Widget entrée libre
entree = tk.Entry(root, bg="#2F2F4F", fg="#F0F0F8")



# Fonctions
# Affichage valeur boutons
def callback_numerique(valeur):
    entree.insert(tk.END, valeur)

# Traitement du formulaire
def submit_form():
    numbers = []
    syntaxe = entree.get()
    numbers.append(syntaxe)
    clean_input()
    split_string(numbers)

# Add
def add(number) : 
    number1, number2 = number[0].split("+")
    result = float(number1) + float(number2)
    return result
# Substract
def substract(number) : 
    number1, number2 = number[0].split("-")
    result = float(number1) - float(number2)
    return result

# Multiply
def multiply(number) : 
    number1, number2 = number[0].split("X")
    result = float(number1) * float(number2)
    return result

# Divide
def divide(number) : 
    number1, number2 = number[0].split("/")
    result = float(number1) / float(number2)
    return result

# Découpage de la chaîne
def split_string(syntaxe):
    i = 0
    
    for i in syntaxe[i]:
        if i == "+":
            callback_numerique(add(syntaxe))
        if i == "-":
            callback_numerique(substract(syntaxe))
        if i == "X":
            callback_numerique(multiply(syntaxe))
        if i == "/":
            callback_numerique(divide(syntaxe))
        if i == ".":
            print("virgule")

            
def clean_input():
    entree.delete(0,"end")
    




# Creating bouttons
# Number buttons
button0 = tk.Button(root, text="0", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("0"))
button1 = tk.Button(root, text="1", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("1"))
button2 = tk.Button(root, text="2", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("2"))
button3 = tk.Button(root, text="3", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("3"))
button4 = tk.Button(root, text="4", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("4"))
button5 = tk.Button(root, text="5", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("5"))
button6 = tk.Button(root, text="6", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("6"))
button7 = tk.Button(root, text="7", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("7"))
button8 = tk.Button(root, text="8", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("8"))
button9 = tk.Button(root, text="9", fg='#F0F0F8', bg="#2F2F4F", command=lambda: callback_numerique("9"))

# Operator buttons
buttonAdd = tk.Button(root, text="+", fg='#F0F0F8', bg="#646495", command=lambda: callback_numerique("+"))
buttonSubstract = tk.Button(root, text="-", fg='#F0F0F8', bg="#646495", command=lambda: callback_numerique("-"))
buttonMultiply = tk.Button(root, text="X", fg='#F0F0F8', bg="#646495", command=lambda: callback_numerique("X"))
buttonDivide = tk.Button(root, text="/", fg='#F0F0F8', bg="#646495", command=lambda: callback_numerique("/"))

# Other buttons
buttonDot = tk.Button(root, text=".", fg='#F0F0F8',bg="#2F2F4F",command=lambda: callback_numerique("."))
buttonLParenthesis = tk.Button(root, text="(", fg='#F0F0F8',bg="#646495", command=lambda: callback_numerique("("))
buttonRParenthesis = tk.Button(root, text=")", fg='#F0F0F8',bg="#646495", command=lambda: callback_numerique(")"))
buttonModulo = tk.Button(root, text="%", fg='#F0F0F8',bg="#646495", command=lambda: callback_numerique("%"))
buttonAC = tk.Button(root, text="AC", fg='#F0F0F8',bg="#646495", command=lambda: clean_input())

# Created submit button
submit_button = tk.Button(root, text="=", font=('Helvetica',8, 'bold'), command=submit_form, bg="#7F7FFF")
submit_button.grid(row=6, column=2, sticky="ew", padx=5, pady=5)

# Positionings
button0.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
button1.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
button2.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
button3.grid(row=5, column=2, sticky="ew", padx=5, pady=5)
button4.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
button5.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
button6.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
button7.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
button8.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
button9.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

buttonAdd.grid(row=6, column=3, sticky="ew", padx=5, pady=5)
buttonSubstract.grid(row=5, column=3, sticky="ew", padx=5, pady=5)
buttonMultiply.grid(row=4, column=3, sticky="ew", padx=5, pady=5)
buttonDivide.grid(row=3, column=3, sticky="ew", padx=5, pady=5)
buttonDot.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
buttonLParenthesis.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
buttonRParenthesis.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
buttonModulo.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
buttonAC.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

entree.grid(row=0, column=0, padx=5, pady=5, sticky="we", columnspan=4)







# Faire en sorte que les boutons prennent l'espace complet de la ligne
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


# Démarrer la boucle principale
root.mainloop()
