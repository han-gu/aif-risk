#Sentence Matching
#Jeevan Karamsetty & Han Gu 
#AIF Risk

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import cPickle 
import editdistance


def convertSentenceToHashMap(x1):

	mapOne= {} 
	for word in x1:
		word.lower() #put all words in lowercase
		if(word not in mapOne): #Make a map with individual words as keys that point to an integer of their frequency
			mapOne[word]= 1
		else:
			mapOne[word]+= 1
	return mapOne

def benchmark(mapOne, mapTwo):
	duplicates= []
	sentenceOneUnique= []
	sentenceTwoUnique= []
	
	for key in mapOne: #Return the sum of the number of word matches between two sentences.
		if(key in mapTwo): 
			duplicates.append(key)
		else:
			sentenceOneUnique.append(key)

	for key in mapTwo:
		if key not in mapOne:
			sentenceTwoUnique.append(key)

	return duplicates, sentenceOneUnique, sentenceTwoUnique


def main(filename1,filename2):
	# listOne= ['Aditya is a scum', 'The cat ate the dog', 'Han is a first year', 'Katy Perry ate the cat']
	# listTwo= ['Jeevan is a second year', 'Aditya is a scum', 'The cat ate the cat']

	numChanges=0
	listOne = cPickle.load(open(filename1, "rb"))
	listTwo= cPickle.load(open(filename2, "rb"))
	outputname=filename1+filename2+"matcher.txt"
	text_file=open(outputname,"w")

	listOneCount = 0 
	for sentenceOne in listOne:
		dups= []
		max= 0.0
		listTwoCount= 0
		listTwoBestCount = 0
		for sentenceTwo in listTwo: 
			result = fuzz.ratio(sentenceOne, sentenceTwo)
			if(result>max):
				max= result
				listTwoBestCount= listTwoCount
				dups= benchmark(convertSentenceToHashMap(sentenceOne.split()), convertSentenceToHashMap(sentenceTwo.split()))
			listTwoCount+=1

		if(max==100):
			text_file.write(listOne[listOneCount]+"is the same as"+listTwo[listTwoBestCount]+ "\n")

		else:
			text_file.write('SENT 1: ' + listOne[listOneCount] + "\n")
			text_file.write('is most similar to'+ "\n")
			text_file.write('SENT 2: '+ listTwo[listTwoBestCount]+ "\n")
			text_file.write("the benchmark is"+ str(max)+ "\n")
			text_file.write("words matched "+ str(dups[0])+ "\n")	
			text_file.write("unique to sentence one "+ str(dups[1])+ "\n")
			text_file.write("unique to sentence two "+ str(dups[2])+ "\n")
			numChanges=numChanges+editdistance.eval(listOne[listOneCount], listTwo[listTwoBestCount])
		listOneCount+=1
		text_file.write(""+ "\n")
	text_file.close()
	return numChanges	


if __name__ == "__main__":
	numChangesList=[]
	for x in range(2,16):
	    if x<10:
		    if x==9:
		    	txtfile1="List_AAPL_10K_2009.p"
		        txtfile2="List_AAPL_10K_2010.p"
		    else:
		    	txtfile1="List_AAPL_10K_200"+str(x)+".p"
	        	txtfile2="List_AAPL_10K_200"+str(x+1)+".p"
	    else:
	        txtfile1="List_AAPL_10K_20"+str(x)+".p"
	        txtfile2="List_AAPL_10K_20"+str(x+1)+".p"
	    #numChangesList is the list of all changes, the x-values
	    numChangesList.append(main(txtfile1,txtfile2))
	print(numChangesList)
	cPickle.dump(numChangesList, open("numChangesList.p", 'wb')) 
