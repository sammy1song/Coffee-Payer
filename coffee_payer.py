import json
import tkinter as tk
from tkinter import simpledialog, messagebox

class UpdateCoffeePricesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Update Coffee Prices")
        self.geometry("300x400")
        self.parent = parent

        self.lbl_info = tk.Label(self, text="Update Coffee Prices:")
        self.lbl_info.pack(pady=10)

        self.entries = {}
        for name, price in parent.coffee_prices.items():
            frame = tk.Frame(self)
            frame.pack(pady=5, fill=tk.X, padx=10)
            lbl_name = tk.Label(frame, text=f"{name}: ", anchor="w")
            lbl_name.pack(side=tk.LEFT)
            entry_price = tk.Entry(frame)
            entry_price.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            entry_price.insert(0, str(price))
            self.entries[name] = entry_price

        self.btn_save = tk.Button(self, text="Save Changes", command=self.save_changes)
        self.btn_save.pack(pady=20)

    def save_changes(self):
        for name, entry in self.entries.items():
            try:
                new_price = float(entry.get())
                self.parent.coffee_prices[name] = new_price
            except ValueError:
                messagebox.showerror("Error", f"Invalid price for {name}. Please enter a valid number.")
                return
        self.parent.save_coffee_prices()
        self.destroy()

class CoffeePayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Payer Selector")
        self.geometry("400x300")
        
        self.state = load_state()
        self.coffee_prices = coffee_prices  

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=20)
        
        self.lbl_next_payer = tk.Label(self.main_frame, text="Click 'Decide' to see who pays next!", font=('Arial', 12))
        self.lbl_next_payer.pack(pady=10)

        self.lbl_total_price = tk.Label(self.main_frame, text="Total Price: $0.00", font=('Arial', 12))
        self.lbl_total_price.pack(pady=10)
        
        self.btn_decide = tk.Button(self.main_frame, text="Decide Who Pays", command=self.decide_next_payer)
        self.btn_decide.pack(pady=10)
        
        self.btn_update_coffee = tk.Button(self.main_frame, text="Update Coffee Prices", command=self.update_coffee_prices)
        self.btn_update_coffee.pack(pady=10)

        self.btn_reset = tk.Button(self.main_frame, text="Reset State", command=self.reset_state)
        self.btn_reset.pack(pady=10)

    def reset_state(self):
        # Resets the state to the initial values
        initial_state = {name: {'total': 0, 'count': 0} for name in self.coffee_prices}
        save_state(initial_state)
        self.state = initial_state
        self.lbl_next_payer.config(text="Click 'Decide' to see who pays next!")
        self.lbl_total_price.config(text="Total Price: $0.00")
        messagebox.showinfo("Reset", "The state has been reset.")

    def decide_next_payer(self):
        payer, total_cost = decide_who_pays(self.state)
        self.lbl_next_payer.config(text=f"{payer} should pay next!")
        self.lbl_total_price.config(text=f"Total Price: ${total_cost:.2f}")
        save_state(self.state)

    def update_coffee_prices(self):
        UpdateCoffeePricesWindow(self)

    def save_coffee_prices(self):
        # Implement saving the updated coffee prices to the file or wherever it's stored
        global coffee_prices
        coffee_prices = self.coffee_prices
        save_state(self.state)  # Assuming modify save_state to also save coffee_prices


# File to store the total paid amounts and counts
state_file = 'total_paid.json'

# Prices for each coworker's preferred coffee
coffee_prices = {
    'Bob': 6.50,  # cappuccino
    'Jeremy': 2.00,  # black coffee
    'Alice': 2.50,  # latte
    'Carol': 5.00,  # espresso
    'Dave': 7.75,  # flat white
    'Eve': 3.25,  # mocha
    'Frank': 1.75  # americano
}

# Load or initialize the total paid amounts and payment counts from file
def load_state():
    try:
        with open(state_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Initialize not just totals but also a count of payments for fairness adjustments
        return {name: {'total': 0, 'count': 0} for name in coffee_prices}

# Save the total paid amounts and counts to file
def save_state(state):
    with open(state_file, 'w') as f:
        json.dump(state, f)

# Decide who pays next, considering both the amount paid and how often they've paid
def decide_who_pays(state):
    # Calculate fairness by considering both total paid and count of payments
    # The least amount paid per count of payments is considered fairer
    payer = min(state, key=lambda x: (state[x]['total'] / (state[x]['count'] if state[x]['count'] > 0 else 1)))
    
    # Calculate today's total cost
    total_cost = sum(coffee_prices.values())
    
    # Update the chosen payer's total and count
    state[payer]['total'] += total_cost
    state[payer]['count'] += 1
    
    # Save the updated state
    save_state(state)
    
    return payer, total_cost


def main():
    app = CoffeePayerApp()
    app.mainloop()

if __name__ == "__main__":
    main()