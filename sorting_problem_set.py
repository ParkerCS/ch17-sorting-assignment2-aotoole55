# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]

temp = my_list[2]
my_list[2] = my_list[7]
my_list[7] = temp
print(my_list)


# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]

def selection(list):
    for pos in range(len(sort_me)):
        min_pos = pos
        for scan_pos in range(min_pos, len(sort_me)):
            if sort_me[scan_pos] < sort_me[min_pos]:
                min_pos = scan_pos
        temp = sort_me[pos]
        sort_me[pos] = sort_me[min_pos]
        sort_me[min_pos] = temp
    return list

print(selection(sort_me))


# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]

def insertion(sort_me2):
    for pos in range(1, len(sort_me2)):
        key_pos = pos
        scan_pos = key_pos - 1
        key_value = sort_me2[key_pos]

        while sort_me2[scan_pos] > key_value and scan_pos >= 0:
            sort_me2[scan_pos + 1] = sort_me2[scan_pos]
            scan_pos -= 1
        sort_me2[scan_pos + 1] = key_value
    return sort_me2


insertion(sort_me2)
print(sort_me2)
# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the list below.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]

sort_me4 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]

print('Selection.')
def selection_counter(sort_me3):
    big = 0
    small = 0
    for pos in range(len(sort_me3)):
        big += 1
        min_pos = pos
        for scan_pos in range(min_pos, len(sort_me3)):
            small += 1
            if sort_me3[scan_pos] < sort_me3[min_pos]:
                min_pos = scan_pos
        temp = sort_me3[pos]
        sort_me3[pos] = sort_me3[min_pos]
        sort_me3[min_pos] = temp
    print("Function iterates through big loop", big," times.")
    print("Function iterates through small loop", small," times.")
    return sort_me3

print(selection_counter(sort_me3))

print('Insertion.')
def insertion_counter(sort_me4):
    big = 0
    small = 0
    for pos in range(1, len(sort_me4)):
        big += 1
        key_pos = pos
        scan_pos = key_pos - 1
        key_value = sort_me4[key_pos]
        while sort_me4[scan_pos] > key_value and scan_pos >= 0:
            small += 1
            sort_me4[scan_pos + 1] = sort_me4[scan_pos]
            scan_pos -= 1
        sort_me4[scan_pos + 1] = key_value
    print("Function iterates through big loop", big," times.")
    print("Function iterates through small loop", small," times.")
    return sort_me4


print(insertion_counter(sort_me4))