# dict = {
#     "name": "Vinay",
#     "Class": "TY b tech",
#     "Age": "21",
#     "CGPA": "7.62",
#     "Hobbies": ["Reading", "Cooking", "Gardening"],
#     "Address": "Gadhinglaj"
# }
# print(dict)

# set1 ={
#     1,2,3,4,5
# }

# set2={1,2,3}
# # print(set)
# # print(type(set))
# # print(len(set))
# print(set1.union(set2)


# for num in range(10) :
#     print(num) 

# n=int(input("Enter the number : "))
# # for num in range(1,11):
# #     print(num*n)
# fact =1
# for num in range(1,n+1):
#     fact*= num 

# print("The factorial of",n,"is",fact)




def factorial(n):
    fact = 1
    for num in range(1, n+1):
        fact *= num
    return fact

n = int(input("Enter the number : "))
print("The factorial of", n, "is", factorial(n))