import sys
from datetime import datetime

def get_current_date():
  date_string = datetime.today().strftime('%m/%d/%Y')
  return date_string

def print_current_date():
  date_string = get_current_date()
  print('Today is {}'.format(date_string))
 
if __name__ == '__main__':
 print_current_date() 
