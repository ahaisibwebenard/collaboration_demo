import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        root.resizable(False, False)

        self.expression = ""
        self.display = tk.Entry(
            root, font=("Arial", 24), justify="right", bd=8, state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="we")

        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, label in enumerate(row):
                tk.Button(
                    root,
                    text=label,
                    font=("Arial", 18),
                    width=4,
                    height=2,
                    command=lambda t=label: self.on_click(t),
                ).grid(row=r, column=c, padx=3, pady=3)

    def set_display(self, text):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, text)
        self.display.config(state="readonly")

    def on_click(self, label):
        if label == "C":
            self.expression = ""
        elif label == "⌫":
            self.expression = self.expression[:-1]
        elif label == "=":
            try:
                result = eval(self.expression, {"__builtins__": {}}, {})
                self.expression = str(result)
            except Exception:
                self.expression = ""
                self.set_display("Error")
                return
        else:
            self.expression += label
        self.set_display(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
