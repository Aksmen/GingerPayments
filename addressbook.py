class Person(object):
    def __init__(self, first, last, streets, mails, groups):
        self.first = first
        self.last = last
        self.streets = streets
        self.mails = mails
        self.groups = groups
        
    def printPerson(self):
        print("Name: "+self.first + " " +self.last)
        for String in self.streets:
            print("Street(s): "+String + "; ")
        for String in self.mails:
            print("Mail(s): "+String + "; ") 
        for String in self.groups:
            print("Group(s): "+String + "; ")         
        print("")
        
class Group(object):
    def __init__(self, name):
        self.name = name
        self.persons = []

class Book(object):
    def __init__(self):
        self.persons = []
        self.groups = []
        
def addPerson(person, book):
    book.persons.append(person)    
    for persongroupname in person.groups:
        if not book.groups:
            addGroup(persongroupname, book)                                   
        for bookgroup in book.groups:
            if bookgroup.name == persongroupname:
                bookgroup.persons.append(person)                                   
                break
        else:
            addGroup(persongroupname, book)
            i = len(book.groups)-1
            book.groups[i].persons.append(person)            

def addGroup(groupname, book):
    for group in book.groups:
        if group.name == groupname:
            print("Group '%s' is alreaddy in given address book." % groupname)
            return
    book.groups.append(Group(groupname))
    
def findGroupMembers(group, book):
    for Group in book.groups:
        if Group.name == group.name:
            members = Group.persons
            print("The following members are in group '%s':" % Group.name)
            for Person in members:
                print(Person.first + " " + Person.last)                            
            return
    print("Group '%s' is not found in given address book." % group.name)
    
def findPersonGroups(person, book):
    for Person in book.persons:
        if Person == person:
            for String in Person.groups:
                print(Person.first + " " + Person.last+" is part of the following group(s): "+ String + "; ")
                return
    print("Person with name '%s %s' is not found in given address book." % (person.first,person.last))

def findPersonByName(name, book):
    for Person in book.persons:
        if Person.first == name or Person.last == name or Person.first+" "+Person.last == name:
            Person.printPerson()
            return
    print("Person with name '%s' is not found in given address book." % name)
            
def findPersonByMail(mail, book):    
    for Person in book.persons:        
        for String in Person.mails:
            if String.startswith(mail):
                Person.printPerson()
                return
    print("Email address starting with '%s' is not found in given address book." % mail)
                
                
#Some testing code            
p = Person('Menno' , 'Selman', ['Rode Klaver 91'], ['menno.selman@planet.nl'], ['gingers'])
q = Person('Pietje' , 'Puk', ['Legmeerplein 22'], ['pietjepuk@hotmail.com'], ['gingers'])
z = Person('Klaas' , 'Schuurman', ['Leidsestraat 8'], ['klaasschuurman@live.com'], ['boosters'])
b = Book()
addPerson(p,b)
addPerson(q,b)
addPerson(z,b)
findGroupMembers(Group('gingers'), b)
findPersonGroups(p,b)
findPersonByName('Menno Selman', b)
findPersonByMail('men',b)


            