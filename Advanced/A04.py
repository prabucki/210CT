'''
TASK OBJECTIVE:

Write the pseudocode for a recursive program to generate the Cartesian product (product
set, direct product, cross product) of n sets.
'''

'''
------PSEUDO CODE------

// VARIABLES:
// lists = list of lists containing integers to process
// CurrentPair =  Printed pair of cartesian product (initially start as empty list)
// N = iteration over the sets list (initially starts as 0)

CARTESIAN(CurrentPair, lists, n)
	if n < length(lists)
		FOR i <-  0 to length[lists[n]]
			CARTESIAN(CurrentPair + (lists[n][i]), lists, n+1)
	else:
	    PRINT CurrentPair
'''