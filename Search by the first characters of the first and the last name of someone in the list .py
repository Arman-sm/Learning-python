#Students' names
names = ['Arsalan Ghasemi', 'Ali Bahonar', 'Negin Soleimani', 'Farzaneh Talebi', 'Sina Ghahremani',
         'Saman Sorayaie', 'Abtin Tavanmand', 'Masoud Jahani', 'Roya Pendar', 'Zeynab Arabi',
         'Amirhossein Tajbakhsh', 'Aria Irani']
#Gathering the inputs (the first characters of the first and the last name)
userFirstChar = input("The first letter of his/her first name: ").lower()
userSecondChar = input("The first letter of his/her last name: ").lower()
#Organizing the names for the operation. The result looks like this ==> [[firstName, lastName], [firstName, lastName], etc.]
fixedNames = [[name.split(" ")[0][0].lower(), name.split(" ")[1][0].lower()] for name in names]
#Looking for a name with the specified requirements
for index, name in enumerate(fixedNames):
    if name[0] == userFirstChar and name[1] == userSecondChar:
       print(names[index])