# A container that contains multiple values in one variable is called list. 

numbers= [20,24,23]
print(numbers)

fruits = ["apple", "banana", "grapes"]
print(fruits[1])

fruits[1] = "orange" #change a particular value in the list
print(fruits)

fruits.append("mango") #add a new value at the end of the list
print(fruits)

fruits.remove("grapes") #remove a value from the list
print(fruits)

for item in fruits: #loop through the list
    print(item)

print(len(fruits)) #get the length of a list

#Important: List can contain different types of data. List starts with 0 index. List is mutable (can be changed). List can contain duplicate values. List can be nested (list inside list).

#practice : create a list of marks and print the average marks.
marks = []
total = 0

marks.append(int(input("Enter marks of subject 1: ")))
marks.append(int(input("Enter marks of subject 2: ")))
marks.append(int(input("Enter marks of subject 3: ")))

for mark in marks:
    total += mark

average = total / len(marks)

print("Makrs:", marks)
print("Average marks:", average)
print(f"Total marks: {total}")