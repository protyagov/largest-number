# Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number. The result may be very large, so you need to return a string instead of an integer. 


*Examples:*
```
  Input : [3,30,34,5,9]
  Output: "9534330"
 
  Input : [0,0,0]
  Output: "0"

  Input : [3432312, 3432]
  Output: "34323432312"
```
<br><br><br>

**Observation**

Solution appears simple, - sort input array largest to smalles and then join numbers into result string. Interesting part is the compare func for the sorting. 
Simple solution for compare function is 
```
def __lt__(self, other):
   return int(self.value + other.value) < int(other.value + self.value)
```
More interesting solution is where you do not convert joined strings to number.
<br><br><br>


**Compare Algorithm** 

We take 2 string, A and B, and need to figure if AB or BA be the largest number. Strings with equal length are easy, - just compare them. Challenging are strings that start with the same numbers, ex: [3432312, 3432]. Simple compare would not work here. What we need to do is recurcively remove common part from the start of the largest string until we find first difference.
```
So, [A,B] = [**3432**312, 3432] -> [**3**12, **3**432] -> [12, 432] -> second number should go first = BA is largest number 
```
<br><br><br>


**Runtime** 

We have soring, which is n•log(n). Compare function best case is O(1) and worsed case O(k) where k is number of digits in one of the numbers. So, we get therefore 
**k•n•log(n)**

LeetCode says my solution runs about average, 50% of all online submissions which is expected because faster would be to convert AB and BA to numbers and compare but it would not be that interesting.

![Image of Yaktocat](https://github.com/protyagov/largest-number/blob/master/leetcode.png)
