# Problem 2: Countries and Capitals
# Create a function named list_countries() that returns the following list of countries: "India", "USA", "Germany", "Australia".

# Create a function named capital_of(country) which receives a string argument representing a country and returns the name of its capital. For example, "India" should return "New Delhi".

# Call list_countries() and use capital_of() to print statements about each country and its capital, like "The capital of India is New Delhi."

def list_countries():
    return ["India", "USA", "Germany", "Australia"]

def capital_of(coun,capi):
    return(f"capital of {coun} is : {capi}")

capital = ["delhi", "washington DC", "berlin", "Canberra"]
country = list_countries()

for coun, capi in zip(country,capital):
    print(capital_of(coun,capi))
