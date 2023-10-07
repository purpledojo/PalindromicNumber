num = input("Give num")
num_b = int(num)
rev = 0
if int(num) <= 0:
    print("error")
else:
     while int(num) > 0:
         ans = int(num) % 10
         rev = rev + (ans * pow(10,len(str(num))-1))
         num = int(num) // 10
if rev == num_b:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
