#beer weight problem

w1=int(input("enter the weight of limak bear:"))
w2=int(input("enter the weight of bob bear:"))
year=0

while(w1<w2):
    w1*=3
    w2*=2
    year+=1

print(year)

