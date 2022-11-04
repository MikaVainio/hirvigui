# SOME TESTS FOR MODULE debug_example.py

# Import module to be tested
import debug_example

# Define a test
def test_personObject():

    # Create an objecto to make tests
    person1 = debug_example.BuggyPerson('Jakke', 'Jaynä', 33)
    person1.setAgeGroup() # Call the setAgeGroup method

    # Define what should be the correct value for ageGroup property in case of age over 18 years
    assert person1.ageGroup == 'Ei oppivelvollinen'

    person2 = debug_example.BuggyPerson('Jonne', 'Janttari', 16)
    person2.setAgeGroup()

    # Define what should be the correct value for ageGroup property in case of age less than 18 years
    assert person2.ageGroup == 'oppivelvollinen'
