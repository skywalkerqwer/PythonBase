"""
    输入三角形高度和宽度用*打印出来
"""
"""
    *
    **
    ***
"""
delta = int(input("输入三角形宽度："))
wide = 1
while wide <= delta:
    print("*" * wide)
    wide += 1

"""
      *
     **
    ***
"""
delta = int(input("输入三角形宽度："))
wide = 1
while wide <= delta:
    print(" " * (delta - wide) + "*" * wide)
    wide += 1

"""
    ***
    **
    *
"""
delta = int(input("输入三角形宽度："))
wide = 0
while wide < delta:
    print("*" * (delta - wide) + " " * wide)
    wide += 1

"""
    ***
     **
      *
"""
delta = int(input("输入三角形宽度："))
wide = 0
while wide < delta:
    print(" " * wide + "*" * (delta-wide))
    wide += 1