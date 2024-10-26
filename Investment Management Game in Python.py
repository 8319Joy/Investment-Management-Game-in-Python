#!/usr/bin/env python
# coding: utf-8
Creating a simplified investment management game in Python can illustrate the concepts of investing, portfolio management, and decision-making in financial contexts. Below is an example of a basic text-based investment game that allows players to invest in stocks, bonds, and real estate, all while managing a budget and attempting to grow their wealth over time.How to Play the Game
Initialization: At the start, you have $10,000 in cash and can choose to invest in Stocks, Bonds, and Real Estate.
Actions:
invest: You can invest a certain amount in any of the three investment types.
sell: You can sell your investments to convert them back to cash.
exit: End the game.
Value Change Simulation: Each time you make an action, the value of the investments is updated randomly to simulate market changes.
End Condition: The game continues until you choose to exit.
Notes
This is a simplified version and does not include complex logic like market trends, more nuanced investment strategies, or economic indicators. It's designed for demonstration purposes.
You can improve the complexity by adding features like historical data, real-time news impacts, or a more sophisticated investment strategy algorithm.
You can run this code in any Python environment. Make sure you have Python installed on your system, or you can use an online Python compiler.
# In[ ]:


import random

class Investment:
    def __init__(self, name, initial_value):
        self.name = name
        self.value = initial_value
        self.invested_amount = 0

    def get_value(self):
        # Simulate a change in value
        change_percentage = random.uniform(-0.1, 0.2)  # -10% to +20%
        self.value += self.value * change_percentage
        return self.value

    def invest(self, amount):
        if amount <= 0:
            print("Investment must be greater than zero.")
            return False
        if amount > self.value:
            print("Insufficient funds to invest that amount.")
            return False
        self.invested_amount += amount
        self.value -= amount
        return True

    def sell(self):
        sale_value = self.invested_amount * self.get_value() / self.value
        self.invested_amount = 0
        return sale_value


class Portfolio:
    def __init__(self):
        self.investments = []
        self.cash = 10000  # Initial cash available

    def add_investment(self, investment):
        self.investments.append(investment)

    def display_status(self):
        print("\nPortfolio Status:")
        print(f"Cash: ${self.cash:.2f}")
        for investment in self.investments:
            print(f"{investment.name}: Invested ${investment.invested_amount:.2f}, Current Value: ${investment.value:.2f}")

    def invest_in(self, investment_name, amount):
        for investment in self.investments:
            if investment.name == investment_name:
                if self.cash >= amount and investment.invest(amount):
                    self.cash -= amount
                    print(f"Invested ${amount:.2f} in {investment_name}.")
                else:
                    print("Investment failed.")
                return
        print(f"Investment {investment_name} not found.")

    def sell_investment(self, investment_name):
        for investment in self.investments:
            if investment.name == investment_name:
                if investment.invested_amount > 0:
                    sale_value = investment.sell()
                    self.cash += sale_value
                    print(f"Sold investment in {investment_name} for ${sale_value:.2f}.")
                else:
                    print(f"No investment made in {investment_name} to sell.")
                return
        print(f"Investment {investment_name} not found.")


def main():
    portfolio = Portfolio()
    stock = Investment("Stock", 1000)
    bond = Investment("Bond", 800)
    real_estate = Investment("Real Estate", 5000)

    portfolio.add_investment(stock)
    portfolio.add_investment(bond)
    portfolio.add_investment(real_estate)

    while True:
        portfolio.display_status()
        action = input("Choose an action: (invest/sell/exit) ").strip().lower()
        if action == "invest":
            investment_name = input("Enter investment name (Stock/Bond/Real Estate): ").strip()
            amount = float(input("Enter amount to invest: "))
            portfolio.invest_in(investment_name, amount)
        elif action == "sell":
            investment_name = input("Enter investment name to sell (Stock/Bond/Real Estate): ").strip()
            portfolio.sell_investment(investment_name)
        elif action == "exit":
            print("Exiting the game.")
            break
        else:
            print("Invalid action. Please choose again.")

        # Update investment values
        for investment in portfolio.investments:
            investment.get_value()

if __name__ == "__main__":
    main()


# Below is the modified version of the investment management game, which utilizes Indian Rupees (Rs) for display:

# In[ ]:


import random

class Investment:
    def __init__(self, name, initial_value):
        self.name = name
        self.value = initial_value
        self.invested_amount = 0

    def get_value(self):
        # Simulate a change in value
        change_percentage = random.uniform(-0.1, 0.2)  # -10% to +20%
        self.value += self.value * change_percentage
        return self.value

    def invest(self, amount):
        if amount <= 0:
            print("Investment must be greater than zero.")
            return False
        if amount > self.value:
            print("Insufficient funds to invest that amount.")
            return False
        self.invested_amount += amount
        self.value -= amount
        return True

    def sell(self):
        sale_value = self.invested_amount * self.get_value() / self.value
        self.invested_amount = 0
        return sale_value


class Portfolio:
    def __init__(self):
        self.investments = []
        self.cash = 10000 * 75  # Initial cash available in INR (Assuming 1 USD = 75 INR)

    def add_investment(self, investment):
        self.investments.append(investment)

    def display_status(self):
        print("\nPortfolio Status:")
        print(f"Cash: ₹{self.cash:.2f}")
        for investment in self.investments:
            print(f"{investment.name}: Invested ₹{investment.invested_amount:.2f}, Current Value: ₹{investment.value:.2f}")

    def invest_in(self, investment_name, amount):
        for investment in self.investments:
            if investment.name == investment_name:
                if self.cash >= amount and investment.invest(amount):
                    self.cash -= amount
                    print(f"Invested ₹{amount:.2f} in {investment_name}.")
                else:
                    print("Investment failed.")
                return
        print(f"Investment {investment_name} not found.")

    def sell_investment(self, investment_name):
        for investment in self.investments:
            if investment.name == investment_name:
                if investment.invested_amount > 0:
                    sale_value = investment.sell()
                    self.cash += sale_value
                    print(f"Sold investment in {investment_name} for ₹{sale_value:.2f}.")
                else:
                    print(f"No investment made in {investment_name} to sell.")
                return
        print(f"Investment {investment_name} not found.")


def main():
    portfolio = Portfolio()
    stock = Investment("Stock", 1000 * 75)           # Converting initial value to INR
    bond = Investment("Bond", 800 * 75)               # Converting initial value to INR
    real_estate = Investment("Real Estate", 5000 * 75)  # Converting initial value to INR

    portfolio.add_investment(stock)
    portfolio.add_investment(bond)
    portfolio.add_investment(real_estate)

    while True:
        portfolio.display_status()
        action = input("Choose an action: (invest/sell/exit) ").strip().lower()
        if action == "invest":
            investment_name = input("Enter investment name (Stock/Bond/Real Estate): ").strip()
            amount = float(input("Enter amount to invest: "))
            portfolio.invest_in(investment_name, amount)
        elif action == "sell":
            investment_name = input("Enter investment name to sell (Stock/Bond/Real Estate): ").strip()
            portfolio.sell_investment(investment_name)
        elif action == "exit":
            print("Exiting the game.")
            break
        else:
            print("Invalid action. Please choose again.")

        # Update investment values
        for investment in portfolio.investments:
            investment.get_value()

if __name__ == "__main__":
    main()


# In[ ]:


Portfolio Status:
Cash: ₹750000.00
Stock: Invested ₹0.00, Current Value: ₹812.43
Bond: Invested ₹0.00, Current Value: ₹600.56
Real Estate: Invested ₹0.00, Current Value: ₹37500.34
Choose an action: (invest/sell/exit) invest
Enter investment name (Stock/Bond/Real Estate): Stock
Enter amount to invest: 5000
Invested ₹5000.00 in Stock.
Portfolio Status:
Cash: ₹745000.00
Stock: Invested ₹5000.00, Current Value: ₹812.43
Bond: Invested ₹0.00, Current Value: ₹600.56
Real Estate: Invested ₹0.00, Current Value: ₹37500.34
Choose an action: (invest/sell/exit) invest
Enter investment name (Stock/Bond/Real Estate): Bond
Enter amount to invest: 2000
Invested ₹2000.00 in Bond.
Portfolio Status:
Cash: ₹743000.00
Stock: Invested ₹5000.00, Current Value: ₹812.43
Bond: Invested ₹2000.00, Current Value: ₹600.56
Real Estate: Invested ₹0.00, Current Value: ₹37500.34
Choose an action: (invest/sell/exit) sell
Enter investment name to sell (Stock/Bond/Real Estate): Stock
Sold investment in Stock for ₹4420.52.
Portfolio Status:
Cash: ₹747420.52
Stock: Invested ₹0.00, Current Value: ₹812.43
Bond: Invested ₹2000.00, Current Value: ₹600.56
Real Estate: Invested ₹0.00, Current Value: ₹37500.34
Choose an action: (invest/sell/exit) invest
Enter investment name (Stock/Bond/Real Estate): Real Estate
Enter amount to invest: 15000
Invested ₹15000.00 in Real Estate.
Portfolio Status:
Cash: ₹732420.52
Stock: Invested ₹0.00, Current Value: ₹812.43
Bond: Invested ₹2000.00, Current Value: ₹600.56
Real Estate: Invested ₹15000.00, Current Value: ₹37500.34
Choose an action: (invest/sell/exit) exit
Exiting the game.


# In[ ]:




