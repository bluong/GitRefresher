def strlen(string):
  return len(string)

def empty_list():
  return []

def add_to_list(new_list, item):
  new_list.append(item)
  
def array_range(string):
  return range(1, strlen(string))

def combine_array(arr):
  return ''.join(arr)

def identity(item):
  return item

def strcopy(string):
  pass

if __name__ == '__main__':
  arr = 'Test_string'
  new_arr = strcopy(arr)
  print arr
  print new_arr
  print str(arr == new_arr)