#延伸練習:倒印姓名
names=["林小虎","王中森","張大明"]
for s in range(2,-1,-1):
  print("%s"%names[s])


#串列搜尋與計次
#index()搜尋:搜尋指定串列元素索引值
#索引值=串列名稱.index(串列元素)
list1=["香蕉","蘋果","橘子"]
n=list1.index("蘋果")
print(n)


#count()計算次數:計算指定串列元素出現的次數
m=list1.count("橘子")
print(m)


#增加串列元素
#(1)append()方法:將元素加在串列最後面
list2=[1,2,3,4,5,6]
list2.append("哈囉")
print(list2[6])
print(len(list2))

#(2)insert()方法:將元素插入在串列中指定的索引位置
list2.insert(3,"四")
print(list2[3])
print(len(list2))


#範例實作:以串列計算班級成績
scores=[]
total=inscore=0
while(inscore!=-1):
  inscore=int(input("請輸入學生成績:"))
  if(inscore!=-1):
    scores.append(inscore)
print("共有%d位學生"%(len(scores)))
for score in scores:
  total+=score
average=total/(len(scores))
print("本班總成績:%d分，平均成績:%5.2f"%(total,average))


#延伸練習:存款累加
saves=[]
save=total=0
for i in range(1,8):
  save=int(input("請輸入第%d天的存款:"%(i)))
  saves.append(save)
for item in saves:
  total+=item
print("存款總額:{}元".format(total))

#刪除串列元素
#(1)remove():刪除串列中指定的元素
list1=["春天","夏天","秋天","冬天"]
list1.remove("夏天")
print(list1)

#(2)pop():從串列中取出元素，同時將該元素從串列中移除
list2=[1,2,3,4,5,6]
n=list2.pop()         #會取出最後一個元素
print(n,list2)
m=list2.pop(2)
print(m,list2)

#(3)del:可以刪除變數、串列，也可以刪除串列元素
list3=[1,2,3,4,5,6,7]
del list3[-1]
print(list3)
list4=[1,2,3,4,5,6,7]
del list4[1:5:2]            #刪除索引1,3的元素
print(list4)


#範例實作:刪除指定串列元素
fruits=["香蕉","蘋果","橘子","鳳梨","西瓜"]
while(True):
  print("串列元素有:",fruits)
  fruit=input("請輸入要刪除的水果(Enter結束):")
  if (fruit==""):
    break
  n=fruits.count(fruit)
  if(n>0):
    fruits.remove(fruit)
  else:
    print(fruit,"不再串列中!")


#串列排序
#(1)sort():由小到大排序
list5=[3,2,1,5]
list5.sort()
print(list5)

#(2)reverse():反轉串列順序
list6=[3,2,1,5]
list6.reverse()
print(list6)

#sorted()
list7=[3,2,1,5]
list8=sorted(list7,reverse=True)    #由大到小
list9=sorted(list7,reverse=False)   #由小到大
print(list8,list9)


#延伸練習:成績
scores=[]
while(True):
  inscore=(input("請輸入學生成績:"))
  if(inscore==""):
    break
  scores.append(int(inscore))
scores.sort()
print(scores)


#綜合演練:找最高分
names=[]
scores=[]
for i in range(1,4):
  name=input("請輸入第%d同學的姓名:"%(i))
  score=input("請輸入第%d同學的成績:"%(i))
  names.append(name)
  scores.append(int(score))
n=scores.index(max(scores))
print("姓名: {}   成績: {}".format(names[n],max(scores)))  