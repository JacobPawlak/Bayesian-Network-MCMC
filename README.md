# Bayesian-Network-MCMC
# Jacob Pawlak
## November 16th, 2017

## CS463G Bayes Net Project

## ------------------------

This will be my deliverables report I think. My project description, pattern
description, conditional probability tables,and what I learned statements will all be in here.

### Description in English

	This project uses the bayes net diagram given to us, and using the MCMC model discussed in class,
		so I had to calculate the Conditional Probabilities for each state not including C (C was 
		fixed to be true)
	From there, I initialized all of the states (again not including C because it is a constant 1)
	I start the 5 tests, each with 10000 checks each, and set a count up for the number of times
		state B was used as True
	I randomly assign the states their truth conditions and then display those to the user, along with 
		the test number.
	Now comes the 10000 loops, with 4 loops each (the inner loops are for checking the non-evidence 
		variables like described in the assignment, and a new random number called 'biased_rando' 
		that acts according to the row of your conditional probability table corresponding to the 
		current values of the other variables in its Markov blanket.
	On the first of the four sub loops, I try to assign A with the biased_rando checking agianst the
		conditional probability that the state would transition. Each permutation of the markov 
		blanket for the state_X gets checked with the corresponding value in the table.
	The second is for state_D, the third for state_E, and the fourth for state_B 
	When I get to state_B, we want to add to the counter when the above states result in state_B being
		assigned true
	After every 1000 steps, I want to update the user with the calculated ratio of B=T
	And that's it, I close the output file and quit the program

### Noticed Patterns

	I noticed that even though I seeded the random number generator, I have always converged around .7 
		or .69
	It was hard to see obscure paterns just becuase of the sheer number of data points, but I did
		notice a little bit of noise around the mean value of the ratio B=T

### Conditional Probability calculations

        #### Table A
        probA_BtCtDt = .8873239437
        probA_BfCtDt = .9921259843
        probA_BtCtDf = .2727272727
        probA_BfCtDf = .8571428571
        probNotA_BtCtDt = 1 - probA_BtCtDt
        probNotA_BfCtDt = 1 - probA_BfCtDt
        probNotA_BtCtDf = 1 - probA_BtCtDf
        probNotA_BfCtDf = 1 - probA_BfCtDf

        #### Table B

        probB_At = .7
        probB_Af = .1
        probNotB_At = 1 - probB_At
        probNotB_Af = 1 - probB_Af

	#### Table D

        probD_AtCtEt = .0270270270
        probD_AfCtEt = .3076923077
        probD_AtCtEf = .6923076923
        probD_AfCtEf = .9729729729
        probNotD_AtCtEt = 1 - probD_AtCtEt
        probNotD_AfCtEt = 1 - probD_AfCtEt
        probNotD_AtCtEf = 1 - probD_AtCtEf
        probNotD_AfCtEf = 1 - probD_AfCtEf

        #### Table E

        probE_CtDt = .1
        probE_CtDf = .9
        probE_CfDt = .7
        probE_CfDf = .3
        probNotE_CtDt = 1 - probE_CtDt
        probNotE_CtDf = 1 - probE_CtDf
        probNotE_CfDt = 1 - probE_CfDt
        pronNotE_CfDf = 1 - probE_CfDf


### What I learned

	I learned a bit more about Markov models and how to apply them. I know I am
		going to use this kind of bayesian network approach to some speech
		generation stuff for my final project, although I am probably going
		to need HMMs instead of MCMC. 
	I learned a bunch more about conditional probability, which is good because 
		I needed a refresher. Going over the equations in class was really helpful
		and I learned that I need to take better notes on math topics in class.
	This whole topic of porbabilistic modeling is really interesting, and I wish we could
		spend a little more time on it. I think learning about MCMC and MDP is not
		only good for the CS curriculum, but we are learning about the same things
		in my Computational Linguistics class and I love the parallels from the
		classes. 
	Sorry if i tried to talk about NLP too much, I just get really excited about NLP
		and when my Compliers, AI, and Compling classes all run together its hard
		to contain ideas to their respective classes.
		
