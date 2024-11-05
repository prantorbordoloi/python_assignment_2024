# Problem 3: Animal Sounds
# Create a function named list_animals() that returns the following list of animals: "Dog", "Cat", "Cow", "Lion".

# Create a function named animal_sound(animal) which receives a string argument representing an animal and returns the sound it makes. For example, "Dog" should return "barks".

# Call list_animals() and use animal_sound() to print statements about each animal and its sound, like "A Dog barks.


def list_animals():
    return ["Dog", "Cat", "Cow", "Lion"]
sound_of_animal = ["bark","mew","hamm","roar"]

def animal_sound(animal,sound):
    return (f"{animal} : {sound}")

animals = list_animals()

for ani,soun in zip(animals,sound_of_animal):
    print(animal_sound(ani,soun))