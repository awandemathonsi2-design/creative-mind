import requests
import sys

#Checks that the command-line argument is a number and if so changes it to a float otherwise prints the appropriate response and exits
if len(sys.argv) == 2:
    try:
        num = float(sys.argv[1])
    except:
        print('Command-line argument is not a number')
        sys.exit(1)
else:
    print('Missing command-line argument')
    sys.exit(1)

#Gets the current Bitcoin price as a float
try:
    url = 'https://rest.coincap.io/v3/assets/bitcoin'
    headers = {'Authorization': 'Bearer c6389bccc4089a40a7ad38687cb928950b8665c5930e06bd849f75c015913c76'}
    response = requests.get(url, headers=headers)
    #Checks status code of the response object
    response.raise_for_status()
    bit_dict = response.json()
    bit_price = float(bit_dict["data"]["priceUsd"])
    print(f'${num*bit_price:,.4f}')

#If any error occured during the HTTP request using requests it will exit
except requests.RequestException:
    sys.exit(1)