#0( log n) time complexity – half the search range each iteration
#0(1) space - not storing extra things in memory (just two pointer variables)

#Givens
sorted_list = [1, 4, 6, 9, 11, 14, 15, 16, 18, 19, 20]
target = 15

#Our function - algorithm
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    
    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2) #cast to integer make 5.0 to 5 w/ int () in

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1


    return -1 #if the value isn't in the list, return -1

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)