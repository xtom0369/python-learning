from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi, {user_name}, I'm the {script} script!")
print("I'd like ask you a few questions.")

print(f"Do you like me, {user_name} ?")
like = input(prompt)

print(f"Where do you live now, {user_name} ?")
pos = input(prompt)

print("What kind of computer do you have ? ")
computer = input(prompt)

print(
f"""
Alright, so you said {like} about liking me.
You live in {pos}. Not sure where that is.
And you have a {computer} computer. Nice
""")
