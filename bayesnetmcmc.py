#Jacob Pawlak
#November 14th, 2017
#CS463G Intro to AI
#Bayesian Network MCMC


###################### IMPORTS ######################


from random import *
from math import *
from time import *


###################### MAIN FUNCTION ######################


'''
The tables given to us in the assignment

A	~A
0.6	0.4

A	B	~B
T	0.7	0.3
F	0.1	0.9

A       C       ~C
T       0.6      0.4
F       0.2      0.8

A       D       ~D
T       0.2      0.8
F       0.8      0.2

C	D	E	~E
T	T	0.1	0.9
T	F	0.9	0.1
F	T	0.7	0.3
F	F	0.3	0.7

I added the ~X parts just to make it more complete

Goal is to use MCMC to approx Pr(B | C = T)

'''
def main():

	print("Jacob Pawlak's MCMC")
	print()

	#Setting a random seed
	seed()

	#Conditional Probability calculations

	#Table A
	probA_BtCtDt = .8873239437
	probA_BfCtDt = .9921259843
	probA_BtCtDf = .2727272727
	probA_BfCtDf = .8571428571
	probNotA_BtCtDt = 1 - probA_BtCtDt
	probNotA_BfCtDt = 1 - probA_BfCtDt
	probNotA_BtCtDf = 1 - probA_BtCtDf
	probNotA_BfCtDf = 1 - probA_BfCtDf

	#Table B

	probB_At = .7
	probB_Af = .1
	probNotB_At = 1 - probB_At
	probNotB_Af = 1 - probB_Af


	#Table D

	probD_AtCtEt = .0270270270
	probD_AfCtEt = .3076923077
	probD_AtCtEf = .6923076923
	probD_AfCtEf = .9729729729
	probNotD_AtCtEt = 1 - probD_AtCtEt
	probNotD_AfCtEt = 1 - probD_AfCtEt
	probNotD_AtCtEf = 1 - probD_AtCtEf
	probNotD_AfCtEf = 1 - probD_AfCtEf

	#Table E

	probE_CtDt = .1
	probE_CtDf = .9
	probE_CfDt = .7
	probE_CfDf = .3
	probNotE_CtDt = 1 - probE_CtDt
	probNotE_CtDf = 1 - probE_CtDf
	probNotE_CfDt = 1 - probE_CfDt
	pronNotE_CfDf = 1 - probE_CfDf


	#init all of the states (we dont need C because it is a constant at 1)
	state_A = 1
	state_B = 1
	state_D = 1
	state_E = 1

	#a little var named tim, this is just for the output file name
	tim = localtime()
	#make an output file with the date and current time as the filename
	outfile = open(str(tim[1]) + "-" + str(tim[2]) + "-" + str(tim[0]) + "-" + str(tim[3]) + "-" + str(tim[4]) + "-" + str(tim[5]) + "outputfile.txt", 'w')

	#we are running 5 different tests because the assignment said so
	for i in range(0, 5):

		#This is the count of how many times b was used as true
		b_was_true = 0

		#we start by randomly assigning states to be True(1) or False(0)
		#I used the choice function because it is an easy way to do true/false
		state_A = choice([0,1])
		state_B = choice([0,1])
		state_D = choice([0,1])
		state_E = choice([0,1])

		#this is all for updating the user of the test number and starting state of the 5 states
		print()
		print("Test number:", i + 1)
		outfile.write("Test number:" + str(i + 1) + "\n")
		print("The starting state values are A:", state_A, "| B:", state_B, "| C:", 1, "| D:", state_D, "| E:", state_E)
		outfile.write("The starting state values are A: " + str(state_A) + " | B: " + str(state_B) +  " | C: 1 | D: " + str(state_D) + " | E: " + str(state_E) + "\n")
		print()

		#we start to loop 10000 times
		for j in range(0, 30000):

			#loop the extra 4 times to itterate over the non-const states A B D E
			for k in range(0, 4):

				#make a biased random number to use for set the state in the case that it needs
				# to be changed
				biased_rando = random()

				#Using Table A
				if(k == 0):

					#the path if B C D
					if(state_B and state_D):

						#check against the biased number and if the probability of changing is higher than
						# the biased number, change the state to True(1)
						if(biased_rando < probA_BtCtDt):
							state_A = 1

					#the path if !B C D
					elif((not state_B) and state_D):

						if(biased_rando < probA_BfCtDt):
							state_A = 1

					#the path if B C !D
					elif(state_B and (not state_D)):

						if(biased_rando < probA_BtCtDf):
							state_A = 1

					#the path if !B C !D
					elif((not state_B) and (not state_D)):

						if(biased_rando < probA_BfCtDf):
							state_A = 1

					else:
						state_A = 0

				#Using Table D
				elif(k == 1):

					#the path if A C E
					if(state_A and state_E):

						if(biased_rando < probD_AtCtEt):
							state_D = 1

					#the path if !A C E
					elif((not state_A) and state_E):

						if(biased_rando < probD_AfCtEt):
							state_D = 1

					#the path if A C !E
					elif(state_A and (not state_E)):

						if(biased_rando < probD_AtCtEf):
							state_D = 1

					#the path if !A C !E
					elif((not state_A) and (not state_E)):

						if(biased_rando < probD_AfCtEf):
							state_D = 1

					else:
						state_D = 0

				#Using Table E
				elif(k == 2):

					#the path if C D
					if(state_D):

						if(biased_rando < probE_CtDt):
							state_E = 1

					#the path if C !D
					elif((not state_D)):

						if(biased_rando < probE_CtDf):
							state_E = 1

					else:
						state_E = 0

				#using Table B
				else:

					#the path if A
					if(state_A):

						if(biased_rando < probB_At):
							state_B = 1
							#If b is true, I need to increment b_was_true counter
							b_was_true += 1

					#the path if !A
					elif(not state_A):

						if(biased_rando < probB_Af):
							state_B = 1
							#if b is true, I need to increment b_was_true counter
							b_was_true += 1

					else:
						state_B = 0

			#for the report and graphs, display the current ratio every 1000 steps
			if((j % 1000 == 0) and (not j == 0)):

				#used to calculate the ratio (B=T / loop#)
				ratio_B = float(b_was_true / j)
				print("Ratio of instances with B=T after", j, "passes:", ratio_B)
				outfile.write("Ratio of instances with B-T after " + str(j) + " passes: " + str(ratio_B) + "\n") 

	#close the file
	outfile.close()
main()
