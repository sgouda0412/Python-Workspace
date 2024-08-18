currency = {'Pound': 1, 'Euro': 1.10, 'USD': 1.30, 'Canada': 1.71, 'Brazil': 7.33, 'Norway' : 12.05,
            'Qatar' : 2.54, 'Swiss' : 1.18, 'India' : 96.23, 'Bitcoin' : 0.0001}

location = input("Please choose a currency: ")
amount = int(input("Please choose how much you would like to change in GBP: "))

for item, value in currency.items():
    if location == item:
        print(f"You have a rate of {value} to 1 GBP")
        new_amount = (currency['Pound'] * amount) * value
        print(f"With the current exchange rate, you will have {new_amount} from £{amount}")

