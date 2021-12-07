# Task 1

lower = 50
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)



# Task 2

def show_student(name, GPA=0):
    print (name , GPA)

show_student("Reema" , 87)



# Task 3

my_dict = {'Physics': 90, 'Math': 100, 'history': 70}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum grade: ',my_dict[key_max])
print('Minimum grade: ',my_dict[key_min])
 