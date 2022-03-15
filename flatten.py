def perfect_shuffle(deck):
    half = len(deck) // 2
    firsthalf = deck[:half]
    secondhalf = deck[half:]
    suffeled = []
    s = 0
    for x in range(1,len(deck),2):
        firsthalf.insert(x,secondhalf[s])
        s += 1


    print(firsthalf)
    print(secondhalf)

perfect_shuffle([1,2,3,4,5,6])