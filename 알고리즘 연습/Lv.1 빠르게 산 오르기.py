# 신입 사원 장그래는 마부장님을 따라 등산을 가게 되었습니다.
#
# 탈수를 방지하기 위해서 1km당 1L의 물을 반드시 마셔야 하는데요. 다행히 등산길 곳곳에는 물통을 채울 수 있는 약수터가 마련되어 있습니다. 다만 매번 줄서 기다려야 한다는 번거로움이 있기 때문에, 시간을 아끼기 위해서는 최대한 적은 약수터를 들르고 싶습니다.
#
# 함수 select_stops는 파라미터로 약수터 위치 리스트 water_stops와 물통 용량 capacity를 받고, 장그래가 들를 약수터 위치 리스트를 리턴합니다. 앞서 설명한 대로 약수터는 최대한 적게 들러야겠죠.
#
# 참고로 모든 위치는 km 단위이고 용량은 L 단위입니다. 그리고 등산하기 전에는 이미 물통이 가득 채워져 있으며, 약수터에 들르면 늘 물통을 가득 채운다고 가정합시다.
#
# 예시를 하나 볼게요.
#
# # 약수터 위치: [1km, 4km, 5km, 7km, 11km, 12km, 13km, 16km, 18km, 20km, 22km, 24km, 26km]
# # 물통 용량: 4L
# select_stops([1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26], 4)
# 처음에 4L의 물통이 채워져 있기 때문에, 장그래는 약수터에 들르지 않고 최대 4km 지점까지 올라갈 수 있습니다. 탈수 없이 계속 올라가기 위해서는 1km 지점이나 4km 지점에서 물통을 채워야겠죠?
#
# 최대한 적은 약수터를 들르면서 올라가야 하고, 마지막에 산 정상인 26km 지점의 약수터를 들르면 성공적인 등산입니다.
def select_stops(water_stops, capacity):

    # 약수터 리스트
    stop = []

    # 마지막 들른 약수터
    prev_stop = 0

    for i in range(len(water_stops)):
        if water_stops[i] - prev_stop > capacity:
            stop.append(water_stops[i-1])
            prev_stop = water_stops[i-1]

    stop.append(water_stops[-1])
    return stop

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))