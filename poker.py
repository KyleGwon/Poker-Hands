import csv
def readwriteCSV(file, option, data=""):
	if option == "r":
		with open(file) as csv_file:
			lines = []
			read = csv.reader(csv_file, delimiter = ",")
			for line in read:
				lines.append(line)
		return lines
	elif option == "a":
		with open(file, "a") as csv_file:
			writer = csv.writer(csv_file, lineterminator="\n")
			writer.writerow(data)

def sorter(file):
	data = readwriteCSV(file, "r")
	returnData = []
	vectors = []
	for i in range(len(data)):
		line = data[i]
		if i != 0:
			features = line[:len(line)-1]
			resVector = line[len(line)-1]
			returnData.append(features)
			vectors.append(resVector)
	return returnData, vectors

def suit(data, vectors, option, index):
	h = []
	s = []
	d = []
	c = []
	for i in range(len(data)):
		card = data[i][index]
		vector = vectors[i]
		if card == "1":
			h.append(vector)
		elif card == "2":
			s.append(vector)
		elif card == "3":
			d.append(vector)
		elif card == "4":
			c.append(vector)
	return suitProb(option, [h, s, d, c])
def suitProb(op, suitData):
	hProb = suitData[0].count(op)/len(suitData[0])
	sProb = suitData[1].count(op)/len(suitData[1])
	dProb = suitData[2].count(op)/len(suitData[2])
	cProb = suitData[3].count(op)/len(suitData[3])
	return [hProb, sProb, dProb, cProb]

def rank(data, vectors, option, index):
	l1 = []
	l2 = []
	l3 = []
	l4 = []
	l5 = []
	l6 = []
	l7 = []
	l8 = []
	l9 = []
	l10 = []
	l11 = []
	l12 = []
	l13 = []
	for i in range(len(data)):
		card = data[i][index]
		vector = vectors[i]
		if card == "1":
			l1.append(vector)
		elif card == "2":
			l2.append(vector)
		elif card == "3":
			l3.append(vector)
		elif card == "4":
			l4.append(vector)
		elif card == "5":
			l5.append(vector)
		elif card == "6":
			l6.append(vector)
		elif card == "7":
			l7.append(vector)
		elif card == "8":
			l8.append(vector)
		elif card == "9":
			l9.append(vector)
		elif card == "10":
			l10.append(vector)
		elif card == "11":
			l11.append(vector)
		elif card == "12":
			l12.append(vector)
		elif card == "13":
			l13.append(vector)
	return rankProb(option, [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13], vectors)
def rankProb(op, rankData, vectors):
	total = vectors.count(op)
	prob1 = rankData[0].count(op)/len(rankData[0])
	prob2 = rankData[1].count(op)/len(rankData[1])
	prob3 = rankData[2].count(op)/len(rankData[2])
	prob4 = rankData[3].count(op)/len(rankData[3])
	prob5 = rankData[4].count(op)/len(rankData[4])
	prob6 = rankData[5].count(op)/len(rankData[5])
	prob7 = rankData[6].count(op)/len(rankData[6])
	prob8 = rankData[7].count(op)/len(rankData[7])
	prob9 = rankData[8].count(op)/len(rankData[8])
	prob10 = rankData[9].count(op)/len(rankData[9])
	prob11 = rankData[10].count(op)/len(rankData[10])
	prob12 = rankData[11].count(op)/len(rankData[11])
	prob13 = rankData[12].count(op)/len(rankData[12])
	return [prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10, prob11, prob12, prob13]

def vectorProbs(vectors):
	probs = []
	total = len(vectors)
	for i in range(10):
		prob = vectors.count(str(i))/total
		probs.append(prob)
	return probs

def prob(data, vectors, vectorProbs, relHand, op):
	probs = []
	for i in range(4):
		if i % 2 == 0:
			var = suit(data, vectors, op, i)
		else:
			var = rank(data, vectors, op, i)
		probs.append(var[relHand[i]-1])
	probability = probs[0]*probs[1]*probs[2]*probs[3]*vectorProbs[int(op)]
	return probability

def normalize(lst):
	newLst = []
	total = sum(lst)
	for i in range(len(lst)):
		item = lst[i]/total
		newLst.append(item)
	return newLst

def main():
	run = True
	data, vectors = sorter("pokerdata.csv")
	vecProbs = vectorProbs(vectors)
	probs = []
	"""
	for s1-s5, the zeroth item is hearts, first item spades, second item diamonds, third item clubs
	for c1-c5, it is just in numerical order: ace (considered 1), 2, 3,...10, jack (11), queen (12), king (13)
	"""
	card1 = input("Suit and rank of first card (1-4, 1-13): ").split(", ")
	card2 = input("Suit and rank of second card (1-4, 1-13): ").split(", ")
	if card1 == card2:
		run = False
	if run:
		s1, c1 = int(card1[0]), int(card1[1])
		s2, c2 = int(card2[0]), int(card2[1])
		lst = []
		newHand = [s1, c1, s2, c2]
		for i in range(10):
			var = prob(data, vectors, vecProbs, newHand, str(i))
			probs.append(var)
		newProbs = normalize(probs)
		for i in range(len(newProbs)):
			item = float("{:.4f}".format(float(str(newProbs[i]))))
			newItem = item*100
			lst.append(newItem)
		print(lst)
	else:
		print("Error: card is same")

main()