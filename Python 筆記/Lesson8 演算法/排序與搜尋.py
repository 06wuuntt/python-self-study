#範例實作:泡沫排序
def disp_data():
  for item in datas:
    print(item,end=" ")
  print()

datas=[3,5,1,2]
print("排序前:",end=" ")
disp_data()
n=len(datas)-1

for i in range(0,n):
  for j in range(0,n-i):
    if(datas[j]>datas[j+1]):
      datas[j],datas[j+1]=datas[j+1],datas[j]  #兩數交換

print("排序後:",end=" ")
disp_data()


#延伸練習:循序搜尋
num=[67,12,9,52,91,3]

while True:
  Isfound=False
  no=input("請輸入中獎者編號(Enter結束):")
  for i in range(len(num)):
    if(num[i]==int(no)):
      Isfound=True
      break
  if(Isfound==True):
    print("恭喜你，號碼%d中獎了!\n"%int(no))
  else:
    print("號碼%d未中獎!\n"%int(no))
  if(no=="\n"):
    break
    