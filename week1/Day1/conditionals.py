# if condition is true:
#     we do something
# else :
#     we do something else


# bank_amount = 10000
# computer_price = 2000

# if bank_amount >= computer_price :
#     print("I'm buying a computer")
#     # bank_amount = bank_amount - computer_price
#     # the same
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money")


# bank_amount = 1000
# computer_price = 2000

# if bank_amount >= computer_price :
#     print("I'm buying a computer")
#     # bank_amount = bank_amount - computer_price
#     # the same
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money") #here

# bank_amount = 10000
# computer_price = 2000
# current_computer_broken = True

# # both condition to be True
# if bank_amount >= computer_price and current_computer_broken == True:
#     print("I'm buying a computer") #here
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money") 

# bank_amount = 10000
# computer_price = 2000
# current_computer_broken = False

# # both condition to be True
# if bank_amount >= computer_price and current_computer_broken == True:
#     print("I'm buying a computer") 
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money")  #here

# bank_amount = 10000
# computer_price = 2000
# current_computer_broken = True

# # both condition to be True
# # no need for == True
# if bank_amount >= computer_price and current_computer_broken:
#     print("I'm buying a computer") #here
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money")  

# bank_amount = 10000
# computer_price = 2000
# current_computer_broken = False

# # at least one condition to be True
# if bank_amount >= computer_price or current_computer_broken:
#     print("I'm buying a computer") #here
#     bank_amount -= computer_price
#     print(f"I have {bank_amount} dollars left")
# else : 
#     print("I don't have enougn money") 

bank_amount = 10000
computer_price = 12000
phone_price = 13000
bottle_price = 10

# at least one condition to be True
if bank_amount >= computer_price:
    print("I'm buying a computer")
    bank_amount -= computer_price
    print(f"I have {bank_amount} dollars left")
elif bank_amount >= phone_price :
    print("I'm buying a phone") 
    bank_amount -= phone_price
    print(f"I have {bank_amount} dollars left")
elif bank_amount >= bottle_price :
    print("I'm buying a bottle") 
    bank_amount -= bottle_price
    print(f"I have {bank_amount} dollars left")
else : 
    print("I don't have enougn money") 

print("out")