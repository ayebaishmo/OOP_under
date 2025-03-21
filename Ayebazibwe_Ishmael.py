"""1. Identify the OOP principles in that code."""
# 1.Abstraction, this shown when an object "drake = Dragon("Drake", 90, 60)" is created
# 2.Encapsulation, this shown on the instatiation of  "def __init__(self, name, species, power_level, speed, habitat, special_ability, weakness):"
# 3.Polymorphism, this is shown when a method is overided as seen drake.use_ability()
# 4.Inheritance, This is shown when class Creature is inherited in class Dragon "class Dragon(Creature):"

"""2. How many methods are in that script"""
# 8 Methods

"""3. How many properties are for the super class"""
# 7 properties

"""4. How many subclasses are in that script"""
# 4 subclasses 

"""5. Write relevant comment in the provided provisions"""
# Demostrated in the code below "Take a look at the code"


"""6. What will happen to subclasses when the class creature is deleted"""
# The subclasses will still exist and run however they will no t be able access the properties and methods of tha class creature


"""7. Does the script have errors, if yes what are the errors?"""
# Yes it does
# below are the errors 
# 1. In class Golem there is typo error the i was put after two "" instead of after """
    # class Golem(Mermaid):
    #     def __init__(self, name, power_level, speed):
    #         ""i" """
    #         super().__init__(name, "Golem", power_level, speed, "Forests", "Archery Mastery", "Dark Magic")
# 2. wrong number of arguments passed during the creation of drake legolas, ariel object. They are supposed to be 7 but only three were passed 
    # drake = Dragon("Drake", 90, 45)
    # legolas = Elf("Legolas", 80, 100)
    # ariel = Mermaid("Ariel", 70, 80)
    # HERE IS THE CORRECT WAY OF DOING IT 
    # drake = Dragon("Drake", 90, 45, "40km/hr", "forest", "sky diving", "prune")
    # legolas = Elf("Legolas", 80, 100, "60km/hr", "desert", "fast runner", "can't fly")
    # ariel = Mermaid("Ariel", 90, 45, "90km/hr", "water", "swimming", "net")

"""8. Which operators can you identify?"""
# 1. f string used to concatinent 
# 2. * multiplication in the describe method under the creature class print("-" * 30)
# 3. = assignment operater when assigning property names to prameters

"""9. How many constructors do you see on the script"""
# 2 constructors in the creature class and the Golem class "__init__"

"""10. How many behaviors are found in the script """
# 8 behaviors 

"""11. How many methods for the subclass Golem"""
# 2 methods

# Super Class "Creature" has been decalred
class Creature:
    """ Behaviors and Attributes initialiazed and assigned ."""
    def __init__(self, name, species, power_level, speed, habitat, special_ability, weakness):
        """Initializes an instatiation method 
        with its parameters."""
        self.name = name
        # Assigning Property self.name to Parameter name
        self.species = species
        # Assigning Property self.power_level to Parameter power_level
        self.power_level = power_level  
        # Assigning Property self.speed to Parameter speed
        self.speed = speed  
        # Assigning Property self.habitat to Parameter habitat
        self.habitat = habitat  
        # Assigning Property self.special_ability to Parameter special_ability
        self.special_ability = special_ability  
        # Assigning Property self.weakness to Parameter weakness
        self.weakness = weakness 

    def describe(self):
        """Prints the details of creature"""
        print(f"Creature: {self.name}")
        print(f"Species:{self.species}")
        print(f"Power Level:{self.power_level}")
        print(f"Speed:{self.speed}")
        print(f"Habitat:{self.habitat}")
        print(f"Special Ability:{self.special_ability}")
        print(f"Weakness:{self.weakness}")

    def use_ability(self):
        """A method use_ability is defined
        to print name and sepcial ability properties"""
        print(f"{self.name} uses {self.special_ability}!")

# Subclass Dragon inheriting feomm class Creature declared
class Dragon(Creature):
    def fly(self):
        """Defining a function/method fly and 
        commanding it to print, 
        with f string concatenation """
        """ """
        print(f"{self.name} spreads its wings and takes off into the sky")

# Subclass Elf inheriting feomm class Dragon declared
class Elf(Dragon):
    """Defining amethod stealth and 
    commanding it to print with f string 
    concatenation """
    def stealth(self):
        """ """
        print(f"{self.name} blends into the shadows, becoming nearly invisible")

# Subclass Mermaid inheriting feomm class Elf declared
class Mermaid(Elf):
    def swim(self):
        print(f"{self.name} glides effortlessly through the waves")

# Subclass Golem inheriting feomm class Mermaid declared
class Golem(Mermaid):
    def __init__(self, name, power_level, speed):
        ""i" """
        """The constructor uses the superclass (Mermaid) constructor to inherit 
        all necessary attributes while overriding some default values.
        """
        super().__init__(name, "Golem", power_level, speed, "Forests", "Archery Mastery", "Dark Magic")
    
    def smash(self):
        """A method smash is defines printing
        the property name with conact string"""
        print(f"{self.name} slams the ground, causing a small earthquake!")

# Creating objects with resepctive to the classes created and supplying the arguments with the values
drake = Dragon("Drake", 90, 45)
legolas = Elf("Legolas", 80, 100)
ariel = Mermaid("Ariel", 70, 80)
rocky = Golem("Rocky", 95, 30)

# Calling the methods for the object drake created 
drake.describe()
drake.use_ability()
drake.fly()

# Calling the methods for the object logolas created 
legolas.describe()
legolas.use_ability()
legolas.stealth()

# Calling the methods for the object ariel created 
ariel.describe()
ariel.use_ability()
ariel.swim()

# Calling the methods for the object rocky created 
rocky.describe()
rocky.use_ability()
rocky.smash()