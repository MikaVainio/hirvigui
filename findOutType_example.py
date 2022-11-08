# EXAMPLE MODULE TO FIND DATATYPES OR CLASS MEMBERSHIPS

# Libraries and modules needed
import datetime
import pgModule

# Class definitions


class Jedi():
    """This is a superclass for Jedi subclases"""

    def __init__(self):
        super().__init__()

    def say(self):
        print("I am a jedi")


class EvilJedi(Jedi):
    """This is a subclass of the Jedi class"""

    def __init__(self):
        super().__init__()

    def proposal(self):
        print('Join the dark side!')


class Rebellian():
    """Class for Rebellians."""

    def __init__(self):
        super().__init__()

    def say(self):
        print('May the force be with you!')


# Examples of different simple datatypes, remember in python everything is an object
quote = 'Luke, I am your father'
print(quote, 'on tyyppiä', type(quote))
birthday = datetime.date(2000, 11, 7)
print(birthday, "on tyyppiä", type(birthday))

# Eamples of real objects and their properties
dbOperation = pgModule.DatabaseOperation()
print('dbOperation objektin tyyppi on', dbOperation, type(dbOperation))
print('Luokan virhekoodi on', dbOperation.errorCode, type(dbOperation.errorCode))
print('tulosjoukko on tyyppiä', type(dbOperation.resultset))

# Lets create some objects
darthVader = EvilJedi()
princessLeia = Rebellian()

# Lets chek who belongs to which class
print('Darth Vader on johdettu luokasta EvilJedi:',
      isinstance(darthVader, EvilJedi))
print('Hän on myös Jedi-luokan jäsen:',  isinstance(darthVader, Jedi))
print('Prinsessa Leia johdettu luokasta Jedi tai EvilJedi:',
      isinstance(princessLeia, (Jedi, EvilJedi)))
print('Hän kuuluukin Rebellian-luokkaan:', isinstance(princessLeia, Rebellian))

# Caution! if you ask for multiple classes it is OR not AND
print('Prinsessa kuuluu kapinallisiin TAI pahiksiin',
      isinstance(princessLeia, (Rebellian, EvilJedi)))

# This checks the AND case
print('Prinsessa kuuluu kapinallisiin JA pahiksiin', isinstance(
    princessLeia, Rebellian) and isinstance(princessLeia, EvilJedi))
