#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
"""

import time

def job_scheduler(f, n):
	print("START OF JOB: " + str(time.ctime()))
	time.sleep(n/1000)
	print("END OF JOB: " + str(time.ctime()))
	return f
	pass

def print_message():
	print("Hello World")
	pass

def main():
	print("BEFORE JOB: " + str(time.ctime()))
	job_scheduler(print_message(), 5000)
	print("AFTER JOB: " + str(time.ctime()))
	pass

if __name__ == '__main__':
	main()


"""
As shown the function is callsed as soon as scheduler is called, not when f is returned.

OUTPUT: 

BEFORE JOB: Wed May  8 12:59:50 2019
Hello World
START OF JOB: Wed May  8 12:59:50 2019
END OF JOB: Wed May  8 12:59:55 2019
AFTER JOB: Wed May  8 12:59:55 2019
[Finished in 5.1s]
"""