print(10 / (10 % 6))
year = 2019
month = 10
day = 29

print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일")
print("오늘은 {}년 {}월 {}일".format(year, month, day))

print("저는 {}, {}, {}를 좋아합니다.".format("강아지","고양이","돼지"))
print("저는 {0}, {2}, {1}를 좋아합니다.".format("강아지","고양이","돼지"))
# 저는 강아지, 고양이, 돼지를 좋아합니다.
# 저는 강아지, 돼지, 고양이를 좋아합니다.
wage = 100
exchange_rate = 1200
print("{}시간에 {: .1f}{} 벌었습니다.".format(5, wage   * 5 *  exchange_rate, "원"))