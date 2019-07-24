"""
    在控制台中录入学生成绩
	  先输入：学生总数
      再依次录入成绩。
	  计算总分
"""
list_score=[]
count = int(input("输入学生总数"))
for i in range(count):
    score = int(input("输入第%d个学的的成绩"%(i+1)))
    list_score.append(score)
sum_score = sum(list_score)
print("%d位学生的总成绩为%d"%(count,sum_score))
