Question 1
```
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
```

Hints:
```
Consider use range(#begin, #end) method
```

Solution using For Loop
```python
# Using For Loop and List
result=[]
for i in range(2300,3201):
  if i%7==0 and i%5!=0:
    result.append(str(i))
print(",".join(result))
```

Solution Using List Comprehension
```
#Using List Comprehension
result=[str(i) for i in range(2300,3201) if i%7==0 and i%5!=0]
print(",".join(result))
```

Output
```
2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,
2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,
2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,
2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,
2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,
2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,
2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,
3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
```
_______________________________________________________________________________________________________________


Question 2:
```
Write a program which can compute the factorial of a given numbers.
```
Hint:
```
Using Recursion
Using For Loop
Using Math Module
Using Stack
```
Solution Using Recursion
```python
#Factorial Using Recursion
def Fact(number):
  if number==0:
    return 1
  else:
    return number * Fact(number-1)
    
fact=5
print(Fact(fact))
```

Solution Using For Loop
```python
#Factorial Using For Loop
def Fact(number):
  if number==0:
    return 1
  else:
    fact=1
    for i in range(1,number+1):
      fact=fact*i
    return fact

fact=5
print(Fact(fact))
```

Solution Using Math Module
```python 
#Factorial using math
import math
def Fact(number):
  return math.factorial(number)

fact=5
print(Fact(fact))
```

Solution Using Stack
```python
#Factorial Using Stack
class STACKS:
  def __init__(self):
      #Initialize Empty Stack
      self.stack=[]
      
  def Push(self,data):
      '''This Will accept Element And Append to existing stack'''
      self.stack.append(data)

  def Pop(self):
      '''This will Remove the element from top of the stack'''
      return self.stack.pop()

  def Fact(self,number):
      '''Get The Factorial of Given Number'''
      self.Push(1)
      for i in range(1,number+1):
          self.Push(self.Pop()*i)
      return self.Pop()    

#Initialize The Stack Object    
s1=STACKS()
number=5
print(s1.Fact(number))
```
Output:
```
120
```
_______________________________________________________________________________________________________________


