#range函式
#數列變數=range(整數值)
#起始值到終止值-1
list1=range(5)
print(list(list1))   #[0, 1, 2, 3, 4]

list2=range(3,8)
print(list(list2))   #[3, 4, 5, 6, 7]
#range函式的三個變數 數列變數=range(起始值,終止值,間隔值)
list3=range(3,8,2)
print(list(list3))   #[3, 5, 7]

list4=range(1,10,2)
print(list(list4))
list5=range(10,1,-2)
print(list(list5))

#for迴圈
#for 變數 in 數列:程式區塊
for n in range(3):
  print(n,end=",")
print()

#範例實作:計算正整數總和
num=int(input("請輸入正整數:"))
sum=0
for i in range(1,num+1):
    sum+=i
print("1到{}的整數合為{}".format(num,sum))

#延伸練習:奇數
n=int(input("請輸入正整數:"))
for i in range(1,n+1,2):
    print("%d "%i,end="")
print()

#範例實作:井字直角三角形
for i in range(1,6):
  print("外部第",i,"次迴圈,內部執行",i,"次迴圈",end="")
  for j in range(1,i+1):
    print("#",end="")
  print()  #換行   

#範例實作:九九乘法表
for i in range(1,10):
  for j in range(1,10):
    print("{}*{}={:2}  ".format(i,j,i*j),end="")
  print()