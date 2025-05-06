def intersection_of_arrays(arr1, arr2):
    count_map = {}
    for num in arr1:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    result = []
    for num in arr2:
        if num in count_map and count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1  # Decrease the count to handle duplicates

    return result

# Example Usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection_of_arrays(arr1, arr2))


def contains_duplicates(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True  # Found a duplicate
        seen[num] = True
    return False  # No duplicates found

# Example Usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(contains_duplicates(nums1))  # Output: True
print(contains_duplicates(nums2))  # Output: False


def first_non_repeating_char(s):
    char_count = {}
    # Count frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None  # If no non-repeating character found

# Example Usage:
s = "swiss"
print(first_non_repeating_char(s))
