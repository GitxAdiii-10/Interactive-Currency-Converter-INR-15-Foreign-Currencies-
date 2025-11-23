"""
Interactive Currency Converter: INR ↔ Foreign Currencies
Uses only built-in Python + NumPy.
Supports 15 currencies:
USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, NZD, SGD,
HKD, KRW, THB, MYR, RUB
"""
import numpy as np
# Exchange Rates (1 unit of foreign currency = X INR)
# Update these rates whenever needed
exchange_rates = {
    "USD": 83.20,
    "EUR": 90.50,
    "GBP": 104.30,
    "JPY": 0.55,
    "AUD": 54.60,
    "CAD": 61.30,
    "CHF": 92.80,
    "CNY": 11.50,
    "NZD": 49.70,
    "SGD": 62.00,
    "HKD": 10.65,
    "KRW": 0.063,
    "THB": 2.30,
    "MYR": 17.70,
    "RUB": 0.90
}
def inr_to_foreign(amount_inr, currency):
    """Convert INR to foreign currency."""
    rate = exchange_rates[currency]
    return np.divide(amount_inr, rate)
def foreign_to_inr(amount_foreign, currency):
    """Convert foreign currency to INR."""
    rate = exchange_rates[currency]
    return np.multiply(amount_foreign, rate)
# Interactive Program
def main():
    print("------------- Currency Converter (INR ↔ Foreign) -------------")
    print("Available currencies:")
    print(", ".join(exchange_rates.keys()))
    while True:
        print("\nChoose an option:")
        print("1. Convert INR → Foreign Currency")
        print("2. Convert Foreign Currency → INR")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")
        # Convert INR to foreign currency
        if choice == "1":
            try:
                amount_inr = float(input("Enter amount in INR: "))
                currency = input("Convert to (e.g., USD, EUR, GBP): ").upper()
                if currency not in exchange_rates:
                    print("❌ Invalid currency! Try again.")
                    continue
                result = inr_to_foreign(amount_inr, currency)
                print(f"✔ ₹{amount_inr} INR = {result:.3f} {currency}")
            except ValueError:
                print("❌ Please enter a valid number.")
        # Convert foreign currency to INR
        elif choice == "2":
            try:
                currency = input("Enter currency (e.g., USD, EUR, GBP): ").upper()
                if currency not in exchange_rates:
                    print("❌ Invalid currency! Try again.")
                    continue
                amount_foreign = float(input(f"Enter amount in {currency}: "))
                result = foreign_to_inr(amount_foreign, currency)
                print(f"✔ {amount_foreign} {currency} = ₹{result:.2f} INR")
            except ValueError:
                print("❌ Please enter a valid number.")
        # Exit
        elif choice == "3":
            print("✔ Exiting converter. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
# Run program
main()
