graphicCardCount = int(input("Количество видеокарт: "))

graphicsCard = []
oldestCard = 0

for graphicCardNumber in range(1, graphicCardCount + 1):
    curGraphicCard = int(input(f"Видеокарта {graphicCardNumber}: "))
    graphicsCard.append(curGraphicCard)
    if curGraphicCard > oldestCard:
        oldestCard = curGraphicCard

for cardId in range(len(graphicsCard) - 1):
    if graphicsCard[cardId] == oldestCard:
        graphicsCard.remove(oldestCard)

print(f"Новый список видеокарт: {graphicsCard}")