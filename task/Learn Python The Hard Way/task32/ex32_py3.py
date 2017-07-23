count_list  = [1, 2, 3, 4, 5]
fruits_list = ['apples', 'oranges', 'pears', 'apricots']
change_list = [1, 'pennies', 2, 'dimes', 3, 'quarters']  # Lua中的混合table效率会很低，不知道python是不是也会有一样的问题

# this first kind of for-loop goes through a list
for number in count_list:
    print(f"This is count {number}")

for fruit in fruits_list:
    print(f"A fruit of type : {fruit}")

# also we can go through mixed lists too
for i in change_list:
    print(f"I got {i}")

# We can also build lists, first start with an empty list.
elements = []

# then use the range dunction to do 0 to 5 counts
for i in range(0, 6):
    print(f"Add {i} to the list.")
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"element was : {i}")
