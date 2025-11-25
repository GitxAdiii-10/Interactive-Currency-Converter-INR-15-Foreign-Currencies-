 **README.md** 



# Currency Converter (INR 15 Foreign Currencies)

An interactive Python-based **currency converter** that allows users to convert between **Indian Rupees (INR)** and **15 major foreign currencies**.
Uses only **built-in Python** and **NumPy**.



##  Supported Currencies

* **USD** – US Dollar
* **EUR** – Euro
* **GBP** – British Pound
* **JPY** – Japanese Yen
* **AUD** – Australian Dollar
* **CAD** – Canadian Dollar
* **CHF** – Swiss Franc
* **CNY** – Chinese Yuan
* **NZD** – New Zealand Dollar
* **SGD** – Singapore Dollar
* **HKD** – Hong Kong Dollar
* **KRW** – South Korean Won
* **THB** – Thai Baht
* **MYR** – Malaysian Ringgit
* **RUB** – Russian Ruble



##  Features

✔ Convert **INR → Foreign Currency**
✔ Convert **Foreign Currency → INR**
✔ Handles invalid inputs
✔ Built with simple and clean logic
✔ Interactive menu-driven interface
✔ Easily updatable exchange rate dictionary
✔ Uses **NumPy** for efficient calculations

---

## How It Works

The program uses a predefined dictionary:


exchange_rates = {
    "USD": 83.20,
    "EUR": 90.50,
    ...
}


Where each value represents:

> **1 unit of foreign currency = X INR**

### Conversion formulas:

* **INR → Foreign:**
  `foreign_amount = INR_amount / rate`

* **Foreign → INR:**
  `INR_amount = foreign_amount * rate`

NumPy is used for simple but efficient arithmetic operations.


##  Running the Program

### **Step 1 — Install NumPy**


pip install numpy
### **Step 2 — Run the script**


python currency_converter.py
```


##  Code Overview

### **Main Functions**

```python
def inr_to_foreign(amount_inr, currency):
    return amount_inr / exchange_rates[currency]

def foreign_to_inr(amount_foreign, currency):
    return amount_foreign * exchange_rates[currency]
```

### **Interactive Menu**

* Choose conversion direction
* Enter required values
* View results instantly


## Sample Output

```
------------- Currency Converter (INR  Foreign) -------------
Available currencies:
USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, NZD, SGD, HKD, KRW, THB, MYR, RUB

Choose an option:
1. Convert INR → Foreign Currency
2. Convert Foreign Currency → INR
3. Exit
Enter choice (1/2/3): 1

Enter amount in INR: 5000
Convert to (e.g., USD, EUR, GBP): USD

✔ ₹5000 INR = 60.096 USD
```

---

## Future Enhancements

* Live exchange rate API integration
* GUI version using Tkinter or PyQt
* Add more currencies
* Add conversion history tracking
* Export results to PDF or Excel


## Educational Value

This program is useful for:

* Python beginners
* Students learning functions and NumPy
* Understanding currency conversion logic
* Mini projects and practical assignments
