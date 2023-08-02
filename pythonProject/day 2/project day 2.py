A = input("What was the total Bill? $")
B = input("What percentage of tip would you like to give? 10, 12 or 15 ?")
C = input("How many people to split? ")
a = float(A)
b = float(B)
c = float(C)
D = (a + (a*b/100)) / c
d = round(D, 2)
print(f"Each Person should pay : ${d}")


