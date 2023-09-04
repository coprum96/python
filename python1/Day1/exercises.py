# username = "John"

# print(username) # i receive the value from the variable
# print("username") # i will receive the value username

# ctrl+/
# shift + 3

my_age = 56
my_future_age = my_age + 123879
sentence = f"I will be {my_future_age} in 123879 years"
# print(sentence)

first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name # John Smith

# f is called string formatting
full_name_two = f"My fullname is {first_name} {last_name}"
# print(full_name_two)


info = f"My age next year is {34+1}"
# print(info)


user_miles = float(input("give me a number of miles"))
convert_to_km = user_miles * 1.60934
print(f"{user_miles} miles in km is {convert_to_km}")


name = 'John Doe'
if len(name) > 20:
    print(f"Name '{name}' is more than 20 chars long")
    length_description = 'long'
elif 20 >= len(name) > 15 :
    print(f"Name '{name}' is more than 15 chars long")
    length_description = 'semi long'
elif 15 >= len(name) > 10:
    print(f"Name '{name}' is more than 10 chars long")
    length_description = 'semi long'
elif 10 >= len(name) >= 8:
    print(f"Name '{name}' is 8, 9 or 10 chars long")
    length_description = 'semi short'
else:
    print(f"Name '{name}' is a short name")
    length_description = 'short'

