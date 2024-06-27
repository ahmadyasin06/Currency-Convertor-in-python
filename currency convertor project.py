def currency_convertor(my_amount, curr_currency, conv_currency):
    
    conversion_rates = {
    "PKR": {"CAD": 0.0048, "AUD": 0.0053, "USD": 0.0035},
    "USD": {"PKR": 283.94, "CAD": 1.36, "AUD": 1.52},
    "CAD": {"PKR": 209.20, "AUD": 1.12, "USD": 0.74},
    "AUD": {"PKR": 186.82, "CAD": 0.89, "USD": 0.66}
    }
    
    try:
        my_amount = float(my_amount)
        conv_amount = my_amount * conversion_rates[curr_currency] [conv_currency]
        return conv_amount
    except KeyError:
        print("Invaid Currency Code. Please use valid currency codes.")
    except ValueError:
        ("Invalid Amount. Please Enter a valid numeric amount")


def main():
    print("Welcome to the Currency Converter. \nHere, you can convert your amount between PKR, AUD, USD, and CAD.\n \tFormed by Ahmad Yasin\n")
    
    while True:
        my_amount = (input("Enter your amount for conversion: "))
        curr_currency = (input("Enter the Source Code of your currency (current code.) (e.g: PKR,USD): ")).upper()
        conv_currency = (input("Enter the Source Code of your currency (Code for conversion.) (e.g: USD,PKR): ")).upper()
        print("\n")
        result = currency_convertor(my_amount, curr_currency, conv_currency)
        
        if result is not None:
            print(f"{my_amount} {curr_currency} is equal to {result:.2f} {conv_currency}")
        
        another_conversion = input("Do you want another conversion (yes/no): ").lower()
        if another_conversion == "no":
                print("\n")
                print("Exiting the Currency Convertor. Goodbye!")
                break


if __name__ == "__main__":
    main()
    


