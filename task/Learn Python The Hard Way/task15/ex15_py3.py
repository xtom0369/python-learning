from sys import argv

script, file_name = argv

txt = open(file_name)
prompt = ">"

print(f"Here is your file :\n\n{txt.read()}")
txt.close()

print("Type your filename again : ")
file_again = input(prompt)

txt_again = open(file_again)
print(f"Here is your file :\n\n{txt_again.read()}")
txt_again.close()
