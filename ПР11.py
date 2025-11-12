import tkinter as tk
from tkinter import ttk, messagebox, filedialog

root = tk.Tk()
root.title("Стоянцев Никита Алексеевич")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

calc_tab = ttk.Frame(notebook)
notebook.add(calc_tab, text="Калькулятор")

tk.Label(calc_tab, text="Первое число:").pack(pady=5)
num1_entry = tk.Entry(calc_tab)
num1_entry.pack(pady=5)

tk.Label(calc_tab, text="Второе число:").pack(pady=5)
num2_entry = tk.Entry(calc_tab)
num2_entry.pack(pady=5)

operation = tk.StringVar(value="+")
operations = ttk.Combobox(calc_tab, textvariable=operation, values=['+', '-', '*', '/'])
operations.pack(pady=10)

def calculate():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        op = operation.get()
        
        if op == '+': result = a + b
        elif op == '-': result = a - b
        elif op == '*': result = a * b
        elif op == '/': result = a / b
        
        messagebox.showinfo("Результат", f"Ответ: {result}")
    except:
        messagebox.showerror("Ошибка", "Проверьте введенные числа")

tk.Button(calc_tab, text="Вычислить", command=calculate).pack(pady=10)

check_tab = ttk.Frame(notebook)
notebook.add(check_tab, text="Чекбоксы")

check1 = tk.BooleanVar()
check2 = tk.BooleanVar()
check3 = tk.BooleanVar()

tk.Checkbutton(check_tab, text="Первый", variable=check1).pack(pady=10)
tk.Checkbutton(check_tab, text="Второй", variable=check2).pack(pady=10)
tk.Checkbutton(check_tab, text="Третий", variable=check3).pack(pady=10)

def show_choice():
    choices = []
    if check1.get(): choices.append("первый")
    if check2.get(): choices.append("второй") 
    if check3.get(): choices.append("третий")
    
    if choices:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

tk.Button(check_tab, text="Показать выбор", command=show_choice).pack(pady=20)

text_tab = ttk.Frame(notebook)
notebook.add(text_tab, text="Текст")

text_area = tk.Text(text_tab, height=10)
text_area.pack(fill='both', expand=True, padx=10, pady=10)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

file_menu.add_command(label="Загрузить из файла", command=load_file)

root.mainloop()