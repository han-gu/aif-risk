import cPickle
import matplotlib.pyplot as plt


#ideally, pull date of each filing from 10-k and scrape from yahoo finance the prices
prices=[1.74,1.04,1.94,5.75,9.47,12.44,17.86,12.76,29.23,48.98,75.11,63.06,75.36,129.62,93.49]
priceChanges=[]

for x in range(0,len(prices)-1):
	priceChanges.append(prices[x+1]-prices[x])

numChanges = cPickle.load(open("numChangesList.p", "rb"))

print(len(priceChanges))
print(len(numChanges))

plt.plot(numChanges, priceChanges,'ro')
plt.show()