import sys

def print_name(name):
  print('Your name is {}'.format(name))


if __name__ == '__main__':
  print_name(sys.argv[1])
