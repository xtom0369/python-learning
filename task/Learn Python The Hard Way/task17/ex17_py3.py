from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file)
indata = input.read()

print(
f"""The input file is {len(indata)} bytes long
Does the output file exist? {exists(to_file)}        
""")

output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")

input.close()
output.close()

