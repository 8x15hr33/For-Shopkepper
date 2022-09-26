



print("ENTER CUSTOMERS PRODUCT PRICE BELOW ")
sum = 0
while True:
    user = input(" ENTER YOUR PRICE OR PRESS Q TO QUIT : \n")

    if (user!='q'):
        sum = sum + int(user)
        print(f" Your Initial Prise Is {sum} Wait For Your Discount")

    else:
      total = (sum*15)/100
      all = sum - total
      print(f"your total amount is {sum}")
      print(f"your discount amount is {total}")
      print(f"Your Payble Amount Is {all} After The Discount Rate Of 15% Off Also Thanks For Shopping With Us")
      break









































































































