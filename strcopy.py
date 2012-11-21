def strlen(string):
  return len(string)

def empty_list():
  return []

def add_to_list(new_list, item):
  new_list.append(item)
  
def get_n_item(list, index):
  return list[index]
  
def array_range(string):
  return range(1, strlen(string))

def combine_array(arr):
  return ''.join(arr)

def identity(item):
  return item

def strcopy(string):
  new_string_arr = empty_list()
  for index in array_range(string):
    add_to_list(new_string_arr, get_n_item(string, index))
  new_string = identity(combine_array(new_string_arr))
  return new_string

if __name__ == '__main__':
  arr = 'Test_string'
  new_arr = strcopy(arr)
  print arr
  print new_arr
  print str(arr == new_arr)