import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.categories = set()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label_category = tk.Label(self.frame, text="Category:")
        self.label_category.grid(row=0, column=0, padx=10)
        self.entry_category = tk.Entry(self.frame)
        self.entry_category.grid(row=0, column=1)

        self.label_amount = tk.Label(self.frame, text="Amount ($):")
        self.label_amount.grid(row=1, column=0, padx=10)
        self.entry_amount = tk.Entry(self.frame)
        self.entry_amount.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        self.label_total = tk.Label(root, text="Total Expenses: $0.00")
        self.label_total.pack()

        self.alert_threshold_label = tk.Label(root, text="Set Alert Threshold ($):")
        self.alert_threshold_label.pack()
        self.alert_threshold_entry = tk.Entry(root)
        self.alert_threshold_entry.pack()
        self.alert_button = tk.Button(root, text="Check Spending Alert", command=self.check_spending_alert)
        self.alert_button.pack()
        self.alert_message = tk.Label(root, text="")
        self.alert_message.pack()

    def add_expense(self):
        category = self.entry_category.get()
        amount = self.entry_amount.get()
        
        if not category or not amount:
            messagebox.showerror("Error", "Please enter both category and amount.")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a valid number.")
            return

        self.expenses.append({"category": category, "amount": amount})
        self.categories.add(category)
        self.entry_category.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.update_total()

    def update_total(self):
        total = sum(item["amount"] for item in self.expenses)
        self.label_total.config(text=f"Total Expenses: ${total:.2f}")

    def check_spending_alert(self):
        threshold = self.alert_threshold_entry.get()
        
        if not threshold:
            messagebox.showerror("Error", "Please enter a threshold amount.")
            return
        
        try:
            threshold = float(threshold)
        except ValueError:
            messagebox.showerror("Error", "Threshold must be a valid number.")
            return
        
        total = sum(item["amount"] for item in self.expenses)
        
        if total > threshold:
            alert_message = f"Warning: You've spent ${total:.2f}, exceeding the threshold of ${threshold:.2f}!"
        else:
            alert_message = f"Total spending is within the budget."

        self.alert_message.config(text=alert_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()
