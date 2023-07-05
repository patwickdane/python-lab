import sys

def add(num1, num2):
  try:
    sum = int(num1) + int(num2)
    return sum
  except (ValueError, TypeError):
    print('Invalid inputs')

if __name__ == '__main__':
  try:
    num1, num2 = sys.argv[1], sys.argv[2]
    print(add(num1, num2))
  except IndexError:
    print('Missing inputs')


