/*#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Job Scheduler
#   Daily Problem #: 10
#   Author: John Deisher
#   Date Started: 5/8/19
#   Date Finished: 5/8/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

"""
Found this code at https://repl.it/@jeweells/DailyCoding10
it does not take a function as the argument though
it is basically what I have come up with the problem is when it is done as my code shows it calls
the function immediatly and not on the return

import time

def jobscheduler(f, n):
	time.sleep(n/1000)
	return f()

print(time.ctime())
print(jobscheduler(lambda: "Hi! " + time.ctime(), 2000))
"""*/
