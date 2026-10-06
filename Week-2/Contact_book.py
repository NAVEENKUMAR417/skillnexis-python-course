Contact={}
def create():
    person=input("Enter your name: ")
    mobile=input("Enter your mobile: ")

    Contact[person]=mobile

def search(person):
    if person in Contact:
        print("yes! mobile no:",Contact[person])
    else:
        print("the contact doesn't exist")

def update(person,new_mobile):
    if person in Contact:
        Contact[person]=new_mobile
    else:
        print("the contact doesn't exist")


def delete(person):
    if person in Contact:
        del Contact[person]
    else:
        print("the contact doesn't exist")

while (True):
    print("###LETS START THE OPERATION###")
    print("1. create new contact")
    print("2. search contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. to stop")

    option = int(input("Enter your option: "))
    if option == 1:
        create()
    elif option == 2:
        search(input("Enter name of person: "))

    elif option == 3:
        new_mobile = input("Enter new mobile: ")
        update(input("Enter name of person: "), new_mobile)

    elif option == 4:
        delete(input("Enter name of person: "))
    elif option == 5:
        print("Contact is closed")
        break
    else:
        break