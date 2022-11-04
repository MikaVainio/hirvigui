# AN EXAMPLE FILE FOR LEARNING TO USE VISUAL STUDIO CODE DEBUGGER


class BuggyPerson():
    def __init__(self, firstName, lastName, age):
        
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.ageGroup = ''
        
    def setAgeGroup(self):
            if self.age < 18:
                self.ageGroup = 'oppivelvollinen'

            else:
                self.ageGroup = 'Ei oppivelvollinen'

if __name__ == '__main__':
    person = BuggyPerson('Essi', 'Esimerkki', 100)
    person.setAgeGroup()
    print(person.ageGroup)
