def swap(seznam, x, y):
    seznam[x], seznam[y] = seznam[y], seznam[x]

def my_permutations_inner(array, position, all_list):
    if position >= len(array):
        all_list.append(array[:])
        # print(array)
    else:
        for i in range(position, len(array)):
            swap(array, i, position)
            my_permutations_inner(array, position + 1, all_list)
            swap(array, i, position)
    return all_list

def permutations(array):
  all_list = []
  return my_permutations_inner(array, 0, all_list)




# def permutations(array):
#   all_list = []
#   my_permutations_inner(array, 0, all_list)
#
#     if position >= len(array):
#         all_list.append(array[:])
#         # print(array)
#     else:
#         for i in range(position, len(array)):
#             swap(array, i, position)
#             permutations(array, position + 1)
#             swap(array, i, position)
#     return all_list

# print(permutations([1,2,3]))
# print(permutations([1]))








# swap(seznam, i, i+1)
# swap(array[i], array[pos])









