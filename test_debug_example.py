# SOME TESTS FOR MODULE debug_example.py

# Import module to be tested
import debug_example

# Define a test for an adult student
def test_personObject_ei_oppivelvollinen():

    # Create an objecto to make tests
    person = debug_example.BuggyPerson('Jakke', 'Jaynä', 33)
    person.setAgeGroup() # Call the setAgeGroup method

    # Define what should be the correct value for ageGroup property 
    assert person.ageGroup == 'Ei oppivelvollinen'

# Define a test for a student under 18 years of age
def test_personObject_oppivelvollinen():
    person = debug_example.BuggyPerson('Jonne', 'Janttari', 16)
    person.setAgeGroup()

    # Define what should be the correct value for ageGroup property 
    assert person.ageGroup == 'Oppivelvollinen'

