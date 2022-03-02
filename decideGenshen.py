import random
import os
num = 3
mission = ""
Todo = ["圣遗物本", "水晶矿", "捡圣遗物", "世界boss", "刷怪", "天赋、武器本"]
res = round(random.random()*(len(Todo))-0.5)
for i in range(num):
    res = round(random.random()*(len(Todo))-0.5)
    mission += Todo[res]+" "
print(mission)
os.system("pause")
