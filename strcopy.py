def strlen(string):
  return len(string)

def empty_list():
  return []

def strcopy(string):
  pass

if __name__ == '__main__':
  arr = 'Test_string'
  new_arr = strcopy(arr)
  print arr
  print new_arr
  print str(arr == new_arr)