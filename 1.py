import random
countCoin=int(input("Введите количество монет: "))
countGrid,countEdge=0,0
for i in range(countCoin):
    side=random.randint(0,1)
    if side==0:countEdge+=1
    else:countGrid+=1
print(f"Количество монеток лежащих решеткой = {countGrid}, гребром = {countEdge}")
print("Минимальное количество монет, которые нужно перевернутьчтобы все монетки были повернуты вверх одной и той же стороной =")
if(countGrid>countEdge):print(countEdge)
else:print(countGrid)