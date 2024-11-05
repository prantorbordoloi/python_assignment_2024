# Problem 4: Planets and Distances
# Create a function named list_planets() that returns the following list of planets: "Mercury", "Venus", "Earth", "Mars".

# Create a function named distance_from_sun(planet) which receives a string argument representing a planet and returns its average distance from the Sun in millions of kilometers. For example, "Earth" should return "149.6 million km."

# Call list_planets() and use distance_from_sun() to print statements about each planet’s distance from the Sun, like "Earth is 149.6 million km away from the Sun."

def list_planets():
    return ["Mercury", "Venus", "Earth", "Mars"]

def distance_from_sun(planet,dist):
    return(f"{planet} is {dist}km away from the sun ...")

dist = ["66.3 million" , "108.93 million" , "148.3 million", "142 million"]
planet = list_planets()
for planet, distance in zip(planet,dist):
    print(distance_from_sun(planet,distance))