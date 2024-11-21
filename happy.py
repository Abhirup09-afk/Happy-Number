#program to find a happy number
#Defination: A number which eventually reaches 1 when replaced by the sum 
# of the square of each digit. For example, 19 is a happy number because 
# 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1.


num = int(input("Enter a number: ")) 

x = num 
a = set() 

while num != 1 and num not in a: 

    a.add(num) 
    num = sum(int(b)**2 for b in str(num)) 

if num == 1: 
    print(f"{x} is a Happy Number.") 
else: 
    print(f"{x} is a not Happy Number.")