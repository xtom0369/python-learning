people_num = input("people's num : ")
car_num    = input("cat's num : ")
bus_num    = input("bus's num : ")

if car_num > people_num:
    print("We should take the cars.")
elif car_num < people_num:
    print("We should not take the cars.")
else:
    print("There is no difference.")

if bus_num > people_num:
    print("We should take the buses.")
elif bus_num < people_num:
    print("We should not take the buses.")
else:
    print("There is no difference.")


