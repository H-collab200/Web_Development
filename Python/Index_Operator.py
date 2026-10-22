#Use of Index Operator []

#Index Operator = Enables to access a sequence's (list, tuple, string) element

#Accessing an element from a list through index operator

Languages=["English", "French", "Arabic", "Urdu", "Russian", "Japanese"]

print(Languages[-1])    


#Accessing an element from a tuple through index operator

Color=("Blue", "Green", "Yellow", "Pink", "White")

print(Color[2])

#Accessing an element from a string through index operator

Name="ABC XYZ"

print(Name[-3])

#if (Name[0].isupper()):
#    Name=Name[0].lower()
#print(Name)

first_name=Name[:3].lower()
last_name=Name[5:].lower()

print(first_name)
print(last_name)
