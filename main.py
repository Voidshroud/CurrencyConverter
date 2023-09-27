import json

import requests as requests

currencies = {
    1: "EUR",
    2: "USD",
    3: "GBP",
    4: "CAD",
    5: "AUD",
}
flag = True

print("Welcome to currency converter.")
while flag:

    while True:

        print("Convert FROM: (Enter numerical code)")
        print("1: EUR \t 2: USD \t 3: GBP \t 4: CAD \t 5: AUD")

        try:
            convertFromCode = int(input())

            if int(convertFromCode) in currencies:
                convertFrom = currencies.get(convertFromCode)
                break
            else:
                print("Invalid code, try again.")

        except ValueError:
            print("Invalid entry. Please enter numerical code!")

    while True:

        print("Convert TO: (Enter numerical code)")
        print("1: EUR \t 2: USD \t 3: GBP \t 4: CAD \t 5: AUD")

        try:
            convertToCode = int(input())

            if int(convertToCode) in currencies:
                convertTo = currencies.get(convertToCode)
                break
            else:
                print("Invalid code, try again.")

        except ValueError:
            print("Invalid entry. Please enter numerical code!")

    while True:

        print("Amount to be converted:")

        try:
            amount = int(input())
            break
        except ValueError:
            print("Invalid entry. Please enter numerical value!")

    api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want=' + convertTo + '&have=' + convertFrom + '&amount=' + str(amount)

    print("Converting " + str(amount) + " " + convertFrom + " to " + convertTo + "." + " Please wait...")

    try:
        response = requests.get(api_url)

        if response.status_code == requests.codes.ok:
            responseDictionary = json.loads(response.text)
            print(str(amount) + " " + convertFrom + " = " + str(responseDictionary.get("new_amount")) + " " + convertTo)

            while True:
                print("Do you want to make another conversion? (Y/N)")
                repeat = input().upper()
                if repeat == "Y":
                    break
                elif repeat == "N":
                    flag = False
                    break
                else:
                    print("Invalid input.")

        else:
            print("Error: ", response.status_code, response.text)
            flag = False
    except:
        print("Unable to establish connection to the server. Please check your internet connection or try again later.")
        while True:
            print("Do you want to try again? (Y/N)")
            repeat = input().upper()
            if repeat == "Y":
                break
            elif repeat == "N":
                flag = False
                break
            else:
                print("Invalid input.")
