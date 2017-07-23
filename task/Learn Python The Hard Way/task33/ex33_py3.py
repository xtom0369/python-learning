space_number = int(input("Input a space number : "))
max_number   = int(input("Input a max number : "))

i = 0
numbers = []

while i < max_number:
    
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + space_number
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
