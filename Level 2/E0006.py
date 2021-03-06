people = 5
capacity = 50

# CHALLENGE 1: Check if the number of people is lower than the capacity.
#              If it is, print "success"
#              If the number of people is higher than the capacity,
#              print "too full"
#              If the number of people is equal to the capacity,
#              print "maximum people"
if people < capacity:
    print("success")
elif people > capacity:
    print("too full")
else:
    # We can do an else here because all other possibilities are
    # accounted for in the other conditions.
    # If people is more than capacity is accounted for.
    # If people is less than capacity is accounted for.
    # So here else is only reached if people and capacity are equal.
    print("maximum people")

# CHALLENGE 2: Set the value of the people variable to 500.
#              Then run the same check from CHALLENGE 1 again.
people = 500
if people < capacity:
    print("success")
elif people > capacity:
    print("too full")
else:
    print("maximum people")

# CHALLENGE 3; Set the value of the people variable to 50.
#              Then run the same check from CHALLENGE 1 again.
people = 50
if people < capacity:
    print("success")
elif people > capacity:
    print("too full")
else:
    print("maximum people")