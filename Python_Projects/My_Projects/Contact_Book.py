contact = {}

finish = "\nPlease enter a contact"
finish += "\nType 'quit' to Finish"

while finish != 'quit':
    name = input("Please enter a name: ")
    address = input("Please enter an address: ")
    postcode = input("Please enter a postcode: ")
    number = input("Please enter a number: ")

    contact[name] = {name, address, postcode, number}
    
    finish = input("Would you like to add another? Type quit to finish")


print(contact)
