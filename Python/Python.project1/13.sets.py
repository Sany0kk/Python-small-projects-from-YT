# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon","knife"}
dishes = {"bowl","plate","cup","knife"}


#utensils.add("napkin")  # adds an element to set
#utensils.remove("fork") # removes an element from set
#utensils.clear()        # clears the set
#dishes.update(dishes)   # add all elements from another set to current

dinner_table = utensils.union(dishes) # combines sets

print(utensils.difference(dishes)) # shows the difference between sets

print(utensils.intersection(dishes)) # shows the elements that they have in common
#for x in dinner_table:
    #print(x)
