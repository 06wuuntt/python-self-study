def scope():
  var1=1
  print(var1,var2)

var1=10
var2=20
scope()
print(var1,var2)


#使用global宣告全域變數
def scope():
  global var1
  var1=1
  var2=2
  print(var1, var2)

scope()
var1=10
var2=20
print(var1,var2)

#pow函式
#pow(x,y,[z]):x的y次方除以z的餘數
n=pow(3,4)
print(n)   #81
n1=pow(3,4,7)
print(n1)  #4


#divmod函式
#divmod(x,y):x除以y的商數及餘數
ret=divmod(44,6)
print(ret[0],ret[1]) #ret[0]是商,ret[1]是餘數 #7 2


#round函式
#round(x[,y]):四捨六入取得x的近似值
n2=round(3.4)   #3
n3=round(3.6)   #4
n4=round(3.5)   #4,前一位是奇數,進位
n5=round(4.5)   #4,前一位是偶數,捨去
print(n2,n3,n4,n5)
#若y有參數,y為設定小數位數
n6=round(3.75,1)  #3.8
n7=round(3.65,1)  #3.6
print(n6,n7)