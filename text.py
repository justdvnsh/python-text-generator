import random

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
text = vowels + consonants 

user_input_one = input('What letter do you want ? Enter c for consonants, v for vowels and t for random text  ')


user_input_two = input('What letter do you want ? Enter c for consonants, v for vowels and t for random text  ')


user_input_three = input('What letter do you want ? Enter c for consonants, v for vowels and t for random text  ')


def text_gen():
	if user_input_one == 'c':
		text_gen_one = random.choice(consonants)
	elif user_input_one == 'v':
		text_gen_one = random.choice(vowels)
	elif user_input_one == 't':
		text_gen_one = random.choice(text)

	if user_input_two == 'c':
		text_gen_two = random.choice(consonants)
	elif user_input_two == 'v':
		text_gen_two = random.choice(vowels)
	elif user_input_two == 't':
		text_gen_two = random.choice(text)

	if user_input_three == 'c':
		text_gen_three = random.choice(consonants)
	elif user_input_three == 'v':
		text_gen_three = random.choice(vowels)
	elif user_input_three == 't':
		text_gen_three = random.choice(text)

	return text_gen_one + text_gen_two + text_gen_three

for i in range(20):
	print(text_gen())

