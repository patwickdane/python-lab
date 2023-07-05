import sys
import random
from functools import reduce

def generate_random_numbers(size):
  def reducer(acc, curr):
    random_number = random.randint(0,100)
    return acc + [random_number]

  random_numbers = reduce(reducer, range(0, size), [])
  return random_numbers


def get_min_max(num_list):
  def find_min_max(acc, curr):
    curr_min, curr_max = acc

    if curr < curr_min:
      return curr, curr_max

    if curr > curr_max:
      return curr_min, curr

    return acc
      
  return reduce(find_min_max, num_list, (num_list[0], num_list[0]))
