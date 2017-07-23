from sys import argv

script, file_name = argv
prompt = ">"

print(
f"""We are going to erase {file_name}.
If you don't want that, enter CTRL-C (^C).
If you do want that, enter RETURN.
"""
)

input(prompt)

print("Opening the file ... ")
txt = open(file_name, "w")

print("Erasing the file ... ")
txt.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("I'm going to write these to the file.")
txt.write(f"{line1}\n")
txt.write(f"{line2}\n")
txt.write(f"{line3}\n")

print("And finally, we close it.")
txt.close()
