# Define a basic class for a human, class names start with a capital letter this is a parent class

class Human:

    # A Function to create an object of this class -> constructor (method) __init__
    def __init__(self, firstName, lastName, employer):
        self.firstName = firstName
        self.lastName = lastName
        self.employer = employer

    # A function to print introduction to a console -> introduction method
    def introduction(self):
        print("My name is", self.firstName, self.lastName)

    def myEmployer(self):
        print("I am working in", self.employer)

# Lets create a human object of the Human class, object names start with a small letter
human = Human('Jakke', 'Jäynä', 'Raseko')

# Lets use the introduction method
human.introduction()
human.myEmployer()

# Class for creating secret agent who inherit properties and methods from Human class.
# This is referred as a child class or a sub class
class SecretAgent(Human):
    
    # Constructor method includes all necessary Human and agent properties also called as fields
    def __init__(self, firstName, lastName, employer, number, licenseToKill):
        
        # Define which arguments have been defined in the parent class (super class) ie Human class
        super().__init__(firstName, lastName, employer)
        self.number = number
        self.licenseToKill = licenseToKill
        
    # An agent has different way of introducing him (or her) self -> method over riding
    def introduction(self):
        print("My name is", self.lastName, ",", self.firstName, self.lastName)
        
# Lets create a secretAgent object of SecretAgent class
secretAgent = SecretAgent('James', 'Bond', 'Universal Exports', '007',True)

# Lets use introduction method which is over rided in the child class
secretAgent.introduction()

# Lets use myEmployer method inherited from parent class Human
secretAgent.myEmployer()


        