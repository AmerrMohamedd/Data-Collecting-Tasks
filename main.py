# Use this web service
# https://api.frankfurter.app/latest?amount=1&from=USD&to=EUR
# and then use it to make a software that takes amount of USD Dollars from the user and calculate how much will it cost in EUR.
# hint : take a look on the url of the service can you guess how I can modify it to calculate the 10$ for EUR for example ?!

import requests
import csv
import pandas as pd


def convert_usd_to_eur(amount):
    api_url = "https://api.frankfurter.app/latest"
    params = {
        "amount": amount,
        "from": "USD",
        "to": "EUR"
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        converted_amount = data['rates']['EUR'] * amount
        return converted_amount
    else:
        return None


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USD Amount', 'EUR Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(data)


def main():
    try:
        usd_amount = float(input("Enter the amount in USD: $"))
        converted_amount = convert_usd_to_eur(usd_amount)

        if converted_amount is not None:
            print(f"${usd_amount} USD is approximately {converted_amount:.2f} EUR.")

            data = {'USD Amount': usd_amount, 'EUR Amount': converted_amount}
            save_to_csv(data, 'conversion_data.csv')

            df = pd.read_csv('conversion_data.csv')
            print("\nConversion Data:")
            print(df)
        else:
            print("Error in fetching conversion data.")
    except ValueError:
        print("Please enter a valid numerical amount.")


if __name__ == "__main__":
    main()
