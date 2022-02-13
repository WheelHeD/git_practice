import requests

print("Welcome to Will's Weather Report Program! ")

# Request weather results by city.

def use_city():
    city = input("Please enter a city name: ")
    url = "https://api.openweathermap.org/data/2.5/weather?q={},us&appid=bed943d3ea06b663bb1b6efbc0b13cac&units=imperial".format(city)
    response = requests.get(url)
    data = response.json()
    display_data(data)


    search = input("Would you like to perform another search? Type Yes or No: ")
    if search == "Yes" or search == "yes" or search == "y":
        main()
    if search == "No" or search == "no" or search == "n":
        print("Thank you for using Will's Weather Program. Have a nice day!")
        exit()

# Request weather results by zip code.

def use_zip():
    zip_code = int(input("Please enter a zip code: "))
    url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=bed943d3ea06b663bb1b6efbc0b13cac".format(zip_code)
    response = requests.get(url)
    data = response.json()
    display_data(data)

    search = input("Would you like to perform another search? Type Yes or No: ")
    if search == "Yes" or search == "yes" or search == "y":
        main()
    if search == "No" or search == "no" or search == "n":
        print("Thank you for using Will's Weather Program. Have a nice day!")
        exit()

# This will pull the weather data to be used in the program.


def display_data(data):
    
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    description = data['weather'][0]['description']
   
    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Description : {}'.format(description))
    

# Define the main function using a while loop to run the program

def main():
    while True:
        question = input("Want to to check the weather? Please type zip to search by zip code, or city to search by city name: ")
        
        if question == 'city':
            try:
                use_city()
                
            except Exception:
                print("Sorry, That is not a valid city name. Try again")
                use_city()
            

        if question == 'zip':
            try:
                use_zip()
                
            except Exception:
                print("Sorry, That is not a valid zip code. Try again")
                use_zip()
            
        else:
            print("That is not a valid option. Try again.")

main()