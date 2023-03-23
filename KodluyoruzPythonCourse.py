def flatten(list):
  myList_1 = []
  for i in list:
    if isinstance(i, list):
      myList_1.extend(flatten(i))
    else:
      myList_1.append(i)
  return myList_1



def reverse(list):
  myList_2 = []
  for i in list:
    if isinstance(i, list):
      myList_2.append(reverse(i))
    else:
      myList_2.append(i)
  return myList_2[::-1]
