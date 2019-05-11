---
layout: post
title: Review and solution for problem 1
subtitle: Find a Given Sum in a List of Numbers
gh-repo: DeisherJohn/DailyCodingProblems
gh-badge: [star, fork, follow]
categories: [list]
tags: [Python, Solutions, Lists]
comments: true
published: true
sticky: false
---

### Problem Review:

**Question**: This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given <b>[10, 15, 3, 7]</b> and <b>k=17</b>, return _true_ since 10 + 7 is 17.

_Bonus: Can you do this in one pass?_

**Answer One**

For this problem there are many ways to solve it, first being a brute force approch. 

```python
for i, num in enumerate(inputList, 1):
    for num2 in inputList[i:]:
        if num + num2 == k:
            return True
return False
```

This does check for the solution but is also very costly for time having _O(n<sup>2</sup>)_ time complexity. 

**Answer Two**

Assuming that the a space complexity of _O(n)_ is acceptable, a better option would be to remember the previous numbers as you iterate the list the first time. To meet the requirement of _O(n)_ however we need to store numbers we have seen in a way that is easy to recall. Python's set() data structures have a constant lookup and insertions time since they are based on hash tables. Using a set to store the complemetns of any numbers we check will allow us to make only one pass of the data. 

The following code runs in _O(n)_ time and has a space complexity of _O(n)_. 

```python
complementSet = set()

for num in inputList:
    if num in complementSet:
        return True
    elif (k - num) not in complementSet:
        complementSet.add(k - num)

return False
```

### Conclusion

- The brute force options is _O(n<sup>2</sup>)_ time complexity and _O(1)_ space complexity.
- The complement set searching options is _O(n)_ time complexity and _O(n)_ space complexity.

The set searching algorithm here is much better and in general if you are having to check for values in lists using sets can save time by having thier constant lookup costs. 

If you have any questions feel free to send me a message though my [LinkedIn](https://www.linkedin.com/in/john-deisher/) or email provided in the footer.
