# Tuesday program. 
# Eoin Lees


import datetime

today = datetime.datetime.today()
print(today)
dayofweek = today.weekday()

print("Let's check if it's Tuesday.")

if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("It will be Tuesday tomorrow luckily.")

else:
    print("Unfortunately it's not Tuesday.")
    print("Today is ", dayofweek)

print("Thanks for checking if it's Tuesday")