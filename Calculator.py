import math

print("This is Soumik's Calculator")
print("Which operation of the following do you want to do:")
print("[1]Addition, [2]Subtraction, [3]Multiplication, [4]Division, [5]Sqauring, [6]Square Rooting: ")
user_ans = int(input("Enter the no. beside the operation you want to do: "))

if user_ans == 1:
       add_1 = int(input("Enter the 1st no. to be added: "))
       add_2 = int(input("Enter the 2nd no. to be added: "))
       sum_0 = add_1 + add_2
       print("The sum is: ")
       print(sum_0)
       
elif user_ans == 2:
       sub_1 = int(input("Enter the no. to be subtracted from: "))
       sub_2 = int(input("Enter the no. to be subtracted: "))
       dif_0 = sub_1 - sub_2
       print("The difference is: ")
       print(dif_0)
       
elif user_ans == 3:
       fac_1 = int(input("Enter the 1st factor: "))
       fac_2 = int(input("Enter the 2nd factor: "))
       pro_0 = fac_1 * fac_2
       print("The product is: ")
       print(pro_0)

elif user_ans == 4:
       div_1 = int(input("Enter the dividend: "))
       div_2 = int(input("Enter the divisor: "))
       quo_0 = div_1 / div_2
       print("The quotient is: ")
       print(quo_0)

elif user_ans == 5:
       squ_1 = int(input("Enter the no. to be squared: "))
       squ_0 = squ_1 * squ_1
       print("The square is: ")
       print(squ_0)

elif user_ans == 6:
       sqr_1 = int(input("Enter the no. to be square rooted: "))
       sqr_0 = math.sqrt(sqr_1)
       print("The square root is:")
       print(sqr_0)

else:
    print("Invalid Entry!!")
    
