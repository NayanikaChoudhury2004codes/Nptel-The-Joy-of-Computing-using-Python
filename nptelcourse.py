# 2.1 Create a Python program that calculates the absolute value of a given number. The program should prompt the user to input a number, then compute and print the absolute value of that number.

# n = int(input("Input a number: "))
# absolute_value = abs(n)
# print(absolute_value)


# 2.2 Create a Python program to determine the nth element of an arithmetic sequence where the first term a is 7 and the common difference d is 11. The program should prompt the user to input the value of n, then compute and print the nth element of the sequence.

# a = 7
# d = 11
# n = int(input("input a Number: "))

# nth_element = a + (n - 1) * d
# print(nth_element)


# 2.3 Create a Python program to compute the sum of the first N natural numbers {1,2,3...N}. The program should prompt the user to input the value of N, then compute and print the sum of the first N natural numbers.

# n = int(input("Input no of Natural numbers: "))
# sum_of_natural_numbers = n * (n + 1) // 2
# print(sum_of_natural_numbers)


# 3.1 Create a Python program that finds the second largest number in a list of positive integers(includes zero). The program should prompt the user to input a list of numbers, then compute and print the second largest number in that list.

# def find_second_largest(Numbers):
#     first_largest = second_largest = None
    
#     for number in Numbers:
#         if first_largest is None or number > first_largest:
#             second_largest = first_largest
#             first_largest = number
#         elif (second_largest is None or number > second_largest) and number != first_largest:
#             second_largest = number
#     return second_largest

# input_number = list(map(int, input("Input numbers with space: ").split()))
# result = find_second_largest(input_number)
# print(result)   


# 3.2 Create a Python program that removes all duplicate positive integer numbers(includes zero) from a list and prints the unique numbers in the order they first appeared. The program should prompt the user to input a list of numbers, then process the list to remove duplicates and print the resulting list of unique numbers.             

# def find_and_remove_duplicates(numbers):
#     unique_numbers = []
#     seen = set()

#     for number in numbers:
#         if number > 0 and number not in seen:
#             unique_numbers.append(number)
#             seen.add(number)
#     return unique_numbers

# input_numbers = list(map(int, input("Enter numbers with space: ").split()))
# result = find_and_remove_duplicates(input_numbers)
# print(result)  


# 3.3 Create a Python program that takes a list of integers, reverses the list, adds the values at odd indices from both the original and reversed lists, and creates a new list with the result. The new list should be printed in the end.

# def processed_list(numbers):
#     reversed_numbers = numbers[::-1]
#     new_list = [ numbers[i] if i % 2 == 0 else numbers[i] + reversed_numbers[i]
#     for i in range(len(numbers))]
#     return new_list

# input_numbers = list(map(int, input("Enter number with space: ").split()))
# result = processed_list(input_numbers)
# print(" ".join(map(str, result)))           


# 5.1 Create a Python program that performs a binary search on a sorted list of integers using only loops. The program should prompt the user to input a sorted list of integers and a target number to search for. The program should then search for the target number in the list using the binary search algorithm and print the index of the target if found. If the target is not found, the program should print -1.

# def binary_search(arr, target):
#     left, right= 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = list(map(int, input("Enter sorted array elements (space-separated): ").split()))
# target = int(input("Target: "))

# result = binary_search(arr, target)
# print(result)


# 5.2 Create a Python program that merges two sorted lists into one sorted list. The program should prompt the user to input two sorted lists of integers. The program should then merge these two lists into one sorted list and print the result.

# def merge_sorted_list(list1, list2):
#     i, j = 0, 0
#     merged_list = []

#     while i < len(list1) and j < len(list2):
#         if list1[i] <list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     merged_list.extend(list1[i: ])
#     merged_list.extend(list2[j: ])

#     return merged_list

# list1 = list(map(int, input("Enter some no with space: ").split()))
# list2 = list(map(int, input("Enter some no with space: ").split())) 

# merged_list = merge_sorted_list(list1, list2)
# print("Merger shorted list: ", merged_list)


# 5.3 Create a Python program that finds the k-th largest and k-th smallest elements in a list of integers. The program should prompt the user to input a list of integers and a value `k`. The program should then find and print:
# 1 if the k-th largest and k-th smallest elements are the same and are at the middle of the sorted list.
#  -1 if the k-th largest and k-th smallest elements are the same but are not in the middle of the sorted list.
# 0 if the k-th largest and k-th smallest elements are different.

# def find_kth_element(arr, k):
#     arr.sort()
#     n = len(arr)

#     kth_smallest = arr[k - 1]
#     kth_largest = arr[-k]

#     if kth_smallest == kth_largest:
#         middle_index = (n-1) // 2
#         if (k == middle_index + 1) or (k == n - middle_index):
#             return 1
#         else:
#             return -1
#     else:    
#         return 0

# arr = list(map(int, input("Enter no with space: ").split()))
# k = int(input("Input k value: "))

# result = find_kth_element(arr, k)
# print(result)


# 6.1 Write a Python program that takes two positive integers a and b as input and returns their product using a recursive function. The function should only use the + and - operators to calculate the product.

# def multiply(a, b):

#     if b == 0:
#         return 0
#     return a + multiply(a, b - 1)

# a, b = map(int, input("Enter a, b: ").split())
# result = multiply(a, b)
# print(result)


# 6.2 Write a Python program that takes a positive integer x as input and returns the logarithm of x to the base 2 using a recursive function. The logarithm of x to the base 2, denoted by log₂(x), is the number of times 2 has to be multiplied by itself to get x. Assume that x is a power of 2

# x = int(input())

# def log2(x):
#     if x == 1:
#         return 0
#     return 1 + log2(x // 2)

# result = log2(x)
# print(result)


# 6.3 Write a Python program that includes a recursive function named non_decreasing which takes a non-empty list L of integers as input. The function should return True if the elements in the list are sorted in non-decreasing order from left to right, and False otherwise.

# def non_decreasing(L):

#     if len(L) <= 1:
#         return True
#     return L[0] <= L[1] and non_decreasing(L[1: ])

# L = list(map(int, input("Enter no with space: ").split()))
# result = non_decreasing(L)
# print(result) 


# 7.1 You are given a board game scenario with ladders and snakes. A player starts at a given position on the board, and you are provided with the result of a die roll. You need to determine whether the player lands on a ladder, a snake, or a normal block after moving. Write a Python function named move_player that takes four inputs:

# def move_player(ladders, snakes, current_position, die_roll):
#     new_position = (current_position + die_roll)

#     if new_position in ladders:
#         return 1
#     elif new_position in snakes:
#         return -1
#     return 0

# ladders = list(map(int, input("Enter Value for ladders: ").split()))
# snakes = list(map(int, input("Enter Value for Snakes: ").split()))
# current_position = int(input("Enter your position: "))
# die_roll = int(input("Enter diece no: "))

# print(move_player(ladders, snakes, current_position, die_roll))


# 7.2 Write a Python program that includes a recursive function named is_palindrome which takes a non-empty string s as input. The function should return 1 if the string is a palindrome (reads the same backward as forward), and 0 otherwise.

# def is_palindrome(S):

#     if len(S) <= 1:
#         return 1
#     if S[0] != S[-1]:
#         return 0
#     return is_palindrome(S[1:-1])

# S = input("Input a Word: ")
# result = is_palindrome(S)
# print(result)


# 8.1 Write a function that takes an integer n followed by n lines of space-separated integers, where each line represents a tuple. The function should return the sum of the first elements of all tuples.

# def sum_of_first_elements(tuples):
#     return sum(t[0] for t in tuples)

# n = int(input("Enter no of tuples: "))
# tuples = [tuple(map(int, input("Enter value for tuple: ").split())) for _ in range (n)]

# print(sum_of_first_elements(tuples))   


# 8.2 Write a function that checks if two given strings are anagrams of each other considering only alphabetic characters and ignoring case. Additionally, the function should handle cases where the strings may contain spaces or punctuation, and should return the result as 1 or 0.

# def clean_string(s):
#     return ''.join(char.lower() for char in s if char.isalpha())

# def are_anagram(str1, str2):
#     clean_str1 = clean_string(str1)
#     clean_str2 = clean_string(str2)

#     return sorted(clean_str1) == sorted(clean_str2)

# str1 = input("Input a String: ").strip()
# str2 = input("Input a String: ").strip()

# if are_anagram(str1, str2):
#     print(1)
# else:
#     print(0)   


# 8.3 Write a function that takes a list of integers and an integer k. The function should multiply each integer in the list by k and then return the maximum value from the resulting list  

# def find_max_after_multiplication(lst, k):
#     max_value = float('-inf')

#     for num in lst:
#         product = num * k
#         if product > max_value:
#             max_value = product
#     return max_value

# lst = [int(x) for x in input().strip().split()]    
# k = int(input())

# print(find_max_after_multiplication(lst, k))


# 9.1 Write a function that takes a string and counts the number of vowels in it. The function should return the total number of vowels.

# def count_vowels(s: str) -> int:
#     vowels = set("aeiouAEIOU")
#     count = 0

#     for char in s:
#         for char in vowels: 
#             count += 1
#     return count

# if __name__ == "__main__":
#     input_string = input("Enter a string: ").strip()
#     print("Number of Vowels: ", count_vowels(input_string))


# 9.2 Write a function that takes a string and determines if the average length of the words in the string is greater than 4. If the average word length is greater than 4, the function should return 1; otherwise, it should return 0.

# def avg_word_length_check(s: str) -> int:
#     words = s.split()

#     if not words:
#         return 0
    
#     total_sum = sum(len(word) for word in words)
#     avg_length = total_sum / len(words)

#     return 1 if avg_length > 4 else 0
        
# if __name__ == "__main__":
#        input_string = input().strip()
#        print(avg_word_length_check(input_string))


# 9.3 Write a function that takes an integer n representing the number of nodes in a complete graph and returns the total number of edges in the graph. A complete graph is a graph in which every pair of distinct nodes is connected by a unique edge.
# def count_edges_in_a_complete_graph(n: int) -> int:
#     return n * (n - 1) // 2

# if __name__ == "__main__":
#     n = int(input("Number of nodes: ").strip())
#     print(count_edges_in_a_complete_graph(n))


# 10.1 Write a program that accepts the string `para` and a positive integer `n` as input. The program should print `1` if there is at least one word in `para` that occurs exactly `n` times, and `0` otherwise.

# def count_words(para, n):
#     words = para.split()
#     word_count = {}

#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1

#     if any(count == n for count in word_count.values()): 
#         print(1)
#     else:
#         print(0)

# para = input("Input word where at least one word in `para` that should occurs exactly `n` times: ")
# n = int(input("Input value of n: "))
# count_words(para, n)     


# 10.2 Write a program that accepts a string of space-separated float numbers. The program should print the number of long tail numbers, where a float number is said to have a long tail if the number of digits after the decimal point is greater than the number of digits before the decimal point.

# def count_long_tail_count(numbers):
#     count = 0
    
#     for num in numbers.split():
#         before_decimal, after_decimal = num.split('.')
#         if len(after_decimal) > len(before_decimal):
#             count +=1
#     return count

# numbers = input()
# print(count_long_tail_count(numbers))        


# 10.3 Write a program that accepts a space-separated string of integers representing a sequence of even length. The program should determine whether the sequence is left-heavy, right-heavy, or balanced. It should print:
# -1 if the sequence is left-heavy (left half sum > right half sum).
# 1 if the sequence is right-heavy (right half sum > left half sum).
# 0 if the sequence is balanced (both sums are equal).

# def analysis_integers(sequence):
#     number = list(map(int, sequence.split()))
#     n = len(number)

#     left_sum = sum(number[:(n // 2)])
#     right_sum = sum(number[(n // 2):])

#     if left_sum > right_sum:
#         print(-1)
#     elif right_sum > left_sum:
#         print(1) 
#     else:
#         print(0)

# sequence = input()
# print(analysis_integers(sequence))


# 11.1 Write a program that accepts a date in MM/DD/YYYY format as input and prints the date in DD-MM-YY format. The program should retain only the last two digits of the year, replace the forward slash (/) with a dash (-), and swap the order of the month and date.

# def convert(date_str):
#     month, day, year = date_str.split('/')
#     year = year[-2:]

#     return f"{day}-{month}-{year}"

# date_str = input("Input your date of birth: ")
# print(convert(date_str))


# 11.2 Write a program that accepts a sequence of numbers separated by colons as input, and prints the common factors of all the numbers in ascending order.

# import math

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def find_gcd_of_list(numbers):
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = gcd(result, num)
#     return result

# def find_common_factor(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors

# input_data = input()
# numbers = list(map(int, input_data.split(':')))
# gcd_value = find_gcd_of_list(numbers)
# common_factors = find_common_factor(gcd_value)

# print(" ".join(map(str, common_factors)))