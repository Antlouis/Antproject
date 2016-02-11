#!/usr/bin/python
# -*- coding: latin-1 -*-

import matplotlib.pyplot as plt
import numpy as np

fichier=open('data.txt')
M=fichier.readlines()

totalist1=[]
totalist2=[]
totalist3=[]
totalist4=[]
meanlist=[]
error=[]



for i,line in enumerate(M):
	words=line.split()
	if not words: continue
	if words[3] == "photocellPin1":
		totalist1.append(float(words[4])
#		totalist.append([])
#		totalist.append([])
#		totalist.append([])
	if words[3] == "photocellPin2":
    totalist2.append(float(words[4])
#		totalist[-3].append(float(words[4]))
#		totalist[-2].append(float(words[2]))
#		totalist[-1].append(float(words[3]))
	if words[3] == "photocellPin3":
		totalist3.append(float(words[4])
		
  if words[3] == "photocellPin4":
		totalist4.append(float(words[4])



#totalist.pop(0)
#totalist = np.array(totalist)


#for i in range(len(totalist)):
#	error.append(np.std(totalist[i]))

#for i in range(len(totalist)):
#	meanlist.append(np.mean(totalist[i]))
	
#print (meanlist)

#finalist, errorlist = [], []

#for i in range(4):
#	finalist.append([meanlist[0+i],meanlist[4+i],meanlist[8+i],meanlist[12+i],meanlist[16+i]])
#	errorlist.append([error[0+i],error[4+i],error[8+i],error[12+i],error[16+i]])

#print (finalist)

#all=[]
#for l in totalist:
#	all += list(l)
#all=np.array(all)
#print all
#print np.mean(all), np.std(all)

#print meanlist
#print error
#print np.mean(meanlist)

#colorlist = ['#4d7f17', '#6bb120', '#8ae429', '#9afe2e']




#a = np.arange(len(finalist[0]))
#width = 0.15
 
 
 
#for i in range(len(finalist)):
#	plt.bar(a + i*width, finalist[i], width, yerr = errorlist[i], ecolor = 'k', color = colorlist[i], edgecolor = 'none')
#plt.title('')
#plt.show()


