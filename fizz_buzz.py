# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:38:19 2021

@author: Henry
"""

#FizzBuzzDict

#func to return true if a given number is divisible by another given number'
def is_modulo(num, factor):
  if(num % factor == 0):
    return True
  else:
    return False

#some improvements ofer conventional FizzBuzz: 
#1. rather than the if.. else for creating the return clause, a str is iteratively built
#2. The Fizz and Buzz values and sring outputs are no longer hard-coded, and are now
#default values in a dict. This can thus be extended to change the values or stings
#and add more values if required.

def e_fizz_buzz(x, y, terms = {'Fizz': 3, 'Buzz': 5}):
  ls = []
  for i in range(x, (y + 1)):
    build_str = ''
    for x in terms:
      if is_modulo(i, terms[x]):
         build_str += x
    if (build_str == ''):
       build_str = (str(i))
    ls.append(build_str)
  return ', '.join(ls)
  
print("FizzBuzz, 1 to 15:")
print(e_fizz_buzz(1, 15))

print("FizzBuzz, 10 to 30:")
print(e_fizz_buzz(10, 30))

new_dict = {'Fizz': 3, 'Buzz': 5, 'Jazz': 7}
print("FizzBuzzJazz (7), 1 to 21:")
print(e_fizz_buzz(1, 21, new_dict))

new_dict = {'Oak': 2, 'Birch': 3, 'Willow': 5, 'Ash': 7} 
print("Entirly different FizzBuzz, 20 to 45")
print( e_fizz_buzz(20, 45, new_dict))