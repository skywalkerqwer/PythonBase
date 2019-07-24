high = int(input("输入高度："))
for i in range(1,high+1):
    print(" "*(high-i)+"*"*(2*i-1))
for j in range(high):
    print(" "*(high-1)+"*")