import tkinter as tk

# ---------- DECORATOR ----------
def my_decorator(func):
    def wrapper():
        return "Decorated → " + func()
    return wrapper

@my_decorator
def decorator_example():
    return "Hello"

# ---------- CLOSURE ----------
def closure_example(x):
    def inner(y):
        return x + y
    return inner

# ---------- GENERATOR ----------
def generator_example():
    for i in range(1, 4):
        yield i

# ---------- ITERATOR ----------
nums = [10, 20, 30]
iterator_example = iter(nums)

# ---------- GUI ----------
def show_decorator():
    result.set(decorator_example())

def show_closure():
    f = closure_example(10)
    result.set(f(5))

def show_generator():
    gen = generator_example()
    result.set(list(gen))

def show_iterator():
    try:
        result.set(next(iterator_example))
    except StopIteration:
        result.set("Iterator finished")

root = tk.Tk()
root.title("Python Concepts GUI")

result = tk.StringVar()

tk.Button(root, text="Decorator", command=show_decorator).pack(pady=5)
tk.Button(root, text="Closure", command=show_closure).pack(pady=5)
tk.Button(root, text="Generator", command=show_generator).pack(pady=5)
tk.Button(root, text="Iterator", command=show_iterator).pack(pady=5)

tk.Label(root, textvariable=result, font=("Arial", 12)).pack(pady=10)

root.mainloop()
