#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Stair Stepper
#   Daily Problem #: 12
#   Author: John Deisher
#   Date Started: 5/8/19
#   Date Finished: 5/8/19
#	Notes: Code pulled from my p7.py for decoding num strings
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

NOTE:
2 Solutions given, one returns the number of ways given any step size <= a given step
the other is what is asked for in the second part where given any set how many ways there are
"""

def count_ways_for_step_given_set(total_stairs, step_sizes = {1}):
	if total_stairs is 0 or len(step_sizes) is 0:
		return 0
	if max(step_sizes) is 0:
		return 0

	if max(step_sizes) > total_stairs:
		#remove any steps larger than the staircase
		step_sizes.remove(max(step_sizes))
		return count_ways_for_step_given_set(total_stairs, step_sizes)

	stairCount = [0]* (total_stairs+1)

	stairCount[0] = stairCount[1] = 1

	for i in range(2,total_stairs+1):
		for step_size in step_sizes:
			stairCount[i] += stairCount[i-step_size]
	return stairCount[total_stairs]


	pass

def count_ways_for_steps_less_than_max(total_stairs,largest_step = 2):
	if total_stairs is 0 or largest_step is 0:
		return 0

	if largest_step > total_stairs:
		#cant take a step bigger than the stair case
		return count_ways_for_steps_less_than_max(total_stairs,total_stairs)


	stairCount = [0]* (total_stairs+1)
	stairCount[0] = stairCount[1] = 1

	for i in range(2,total_stairs+1):
		for step_size in range(largest_step,0,-1):
			stairCount[i] += stairCount[i-step_size]
	return stairCount[total_stairs]

	pass

def main():
	#include a 0 stair in the count
	MAX_STAIRS = 6
	print("This data set is for largest steps <= a max step size")
	for largest_step_size in range(MAX_STAIRS):
		print("\nThe Largest Step is: " + str(largest_step_size))
		for num_of_stairs in range(MAX_STAIRS):
			print("#stairs: " + str(num_of_stairs) + ", ways to climb: " + str(count_ways_for_steps_less_than_max(num_of_stairs, largest_step_size)))

	testSets = list()
	testSets.append([0])
	testSets.append([1])
	testSets.append([1,2])
	testSets.append([1,3])
	testSets.append([1,2,3])	
	testSets.append([1,3,5])


	print("\nThis data set is for step sizes pulled from a set")
	for testSet in testSets:
		print("\nSteps that can be taken are: " + str(testSet))
		for num_of_stairs in range(MAX_STAIRS):
			print("#stairs: " + str(num_of_stairs) + ", ways to climb: " + str(count_ways_for_step_given_set(num_of_stairs, set(testSet))))
	pass

	assert count_ways_for_steps_less_than_max(MAX_STAIRS, 3) == count_ways_for_step_given_set(MAX_STAIRS, {1,2,3})

if __name__ == '__main__':
	main()

"""
OUTPUT:

This data set is for largest steps <= a max step size

The Largest Step is: 0
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 0
#stairs: 2, ways to climb: 0
#stairs: 3, ways to climb: 0
#stairs: 4, ways to climb: 0
#stairs: 5, ways to climb: 0

The Largest Step is: 1
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 1
#stairs: 3, ways to climb: 1
#stairs: 4, ways to climb: 1
#stairs: 5, ways to climb: 1

The Largest Step is: 2
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 3
#stairs: 4, ways to climb: 5
#stairs: 5, ways to climb: 8

The Largest Step is: 3
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 4
#stairs: 4, ways to climb: 7
#stairs: 5, ways to climb: 13

The Largest Step is: 4
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 4
#stairs: 4, ways to climb: 8
#stairs: 5, ways to climb: 15

The Largest Step is: 5
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 4
#stairs: 4, ways to climb: 8
#stairs: 5, ways to climb: 16

This data set is for step sizes pulled from a set

Steps that can be taken are: [0]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 0
#stairs: 2, ways to climb: 0
#stairs: 3, ways to climb: 0
#stairs: 4, ways to climb: 0
#stairs: 5, ways to climb: 0

Steps that can be taken are: [1]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 1
#stairs: 3, ways to climb: 1
#stairs: 4, ways to climb: 1
#stairs: 5, ways to climb: 1

Steps that can be taken are: [1, 2]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 3
#stairs: 4, ways to climb: 5
#stairs: 5, ways to climb: 8

Steps that can be taken are: [1, 3]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 1
#stairs: 3, ways to climb: 2
#stairs: 4, ways to climb: 3
#stairs: 5, ways to climb: 4

Steps that can be taken are: [1, 2, 3]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 2
#stairs: 3, ways to climb: 4
#stairs: 4, ways to climb: 7
#stairs: 5, ways to climb: 13

Steps that can be taken are: [1, 3, 5]
#stairs: 0, ways to climb: 0
#stairs: 1, ways to climb: 1
#stairs: 2, ways to climb: 1
#stairs: 3, ways to climb: 2
#stairs: 4, ways to climb: 3
#stairs: 5, ways to climb: 5
[Finished in 0.1s]
"""