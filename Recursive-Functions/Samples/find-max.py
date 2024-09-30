def find_max(lst, index=0):
    if index == len(lst) - 1:
        return lst[index]

    max_in_rest = find_max(lst, index + 1)
    return lst[index] if lst[index] > max_in_rest else max_in_rest
  
