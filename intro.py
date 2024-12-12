# example of variable
# let name = variable; JS
name = "Jose" # string
age = 33 #integer
height = 1.83 #float
is_student = False #boolean
#using the f below adds concatonation to the string
print (f"Name: {name}, age: {age}, height: {height}")
#this is without concatonation
print ("Type of age: ", type(name))

#Example of an if statement
age = 42 #integer
if age <13:
    print ("Child")
elif age < 20:
    print ("Teenager")
else:
    print ("Adult")

# for loops
for i in range(5):
    if i == 3:
        continue
    print(i)
    # JS let range = 6
    # JS for(let i = 0; i < 5; i++)
    # {
    #     let temp = i dfljadlf
    # } its alot more info

    # List ---> array
    fruits = ["Apple", "Bannana", "Cherry"]
    print(fruits)
    fruits.append("Date")
    print(fruits)
    print(fruits[1:3])

    # dictionary
    student = {
        "name": "Jose",
        "age": 20,
        "courses": ["math","science"]
    }
    print(student["age"])
    student["grade"] = "A"
    student.update({"email":"jtorres@sd.com"})
    print(student)

    # functions
    def say_hello():
        print("Hello")
    def say_goodbye():
        print("Goodbye")

    #call the functions
    say_hello()
    say_goodbye()

    # concatenate
    print("Hello my name is " + name + " and I am " + str(age) + " years old")