#elephant distance problem

n=int(input("enter the distance of friends house:"))
if(n<=5):
    print(1,"steps")
elif(n%5==0):
    print(n/5,"steps")
else:
    print(n//5+1,"steps")
