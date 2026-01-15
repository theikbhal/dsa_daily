# microsoft_easy_dsa.py
# Microsoft Easy DSA Problems in Python

# 1. Two Sum
# Given an array of integers, return indices of two numbers that add up to target
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example: two_sum([2, 7, 11, 15], 9) → [0, 1]


# 2. Reverse a String
def reverse_string(s):
    return s[::-1]
    # Or: return ''.join(reversed(s))

# Example: reverse_string("hello") → "olleh"


# 3. Valid Palindrome
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example: is_palindrome("A man, a plan, a canal: Panama") → True


# 4. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 if l1 else l2
    return dummy.next


# 5. Valid Parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

# Example: is_valid_parentheses("()[]{}") → True


# 6. Maximum Subarray (Kadane's Algorithm)
def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Example: max_subarray([-2,1,-3,4,-1,2,1,-5,4]) → 6


# 7. Binary Search
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example: binary_search([1, 2, 3, 4, 5], 3) → 2


# 8. Reverse Linked List
def reverse_linked_list(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev


# 9. Find First and Last Position in Sorted Array
def search_range(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    return [find_bound(True), find_bound(False)]

# Example: search_range([5,7,7,8,8,10], 8) → [3, 4]


# 10. Missing Number
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example: missing_number([3, 0, 1]) → 2


# 11. Majority Element
def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Example: majority_element([2,2,1,1,1,2,2]) → 2


# 12. Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

# Example: remove_duplicates([1,1,2]) → 2, nums = [1,2,...]


# Test the functions
if __name__ == "__main__":
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("2. Reverse String:", reverse_string("hello"))
    print("3. Valid Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))
    print("4. Valid Parentheses:", is_valid_parentheses("()[]{}"))
    print("5. Max Subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
    print("6. Binary Search:", binary_search([1, 2, 3, 4, 5], 3))
    print("7. Search Range:", search_range([5,7,7,8,8,10], 8))
    print("8. Missing Number:", missing_number([3, 0, 1]))
    print("9. Majority Element:", majority_element([2,2,1,1,1,2,2]))
    print("10. Remove Duplicates:", remove_duplicates([1,1,2,2,3]))
