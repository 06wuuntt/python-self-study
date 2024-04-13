# %字串格式化
#print(項目%(參數列))
name,score="林小明",80
print("%s的成績為%d"%(name,score))


#format字串格式化
#print(字串.format(參數列))
#字串中{}的位置表示參數位置
print("{}的成績為{}".format("林小明",score))
print("考{1:3}的人是{0:3}\n\n".format("林小明",score))


#範例實作:格式化列印成績單
print("姓名  座號  國文  數學  英文")
print("%3s%4d%6d%6d%6d"%("林大明",1,100,87,79))
print("%3s%4d%6d%6d%6d"%("陳阿中",2,74,88,100))
print("%3s%4d%6d%6d%6d\n\n"%("張小瑛",11,82,65,8))

#延伸練習
print("年度　所得稅　營業稅　證交稅")
print("%4d　%6.2f　%6.2f　%6.2f"%(2017,98.34,90.2,104.79))
print("%4d　%6.2f　%6.2f　%6.2f"%(2018,83,110.5,82.45))
print("%4d　%6.2f　%6.2f　%6.2f\n\n"%(2019,98,79.32,102))