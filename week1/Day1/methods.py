# >>> "HELLO".lower()
# 'hello'
# >>> "I like javascript".replace("javascript", "python")
# 'I like python'

sentence = "I like javascript"

# ask the user, what language does he want to replace Javscript with
user_choice = input("what language to you want \n")

sentence = sentence.replace("javascript",user_choice)

print(sentence)

# >>> "hello"[0]
# 'h'
# >>> "hello"[4]
# 'o'


game = input("Give me a sentence \n")

# always show him the last letter of whatver word

# last_character = game[len(game)-1]
last_character = game[-1]

print(f"the last character of the word {game} is {last_character}")

# >>> age = int(input("what is your age"))
# what is your age
# 12
# >>> age
# 12