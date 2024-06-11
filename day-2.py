"""
  https://codingbat.com/python 

  1. Warmup-2 - Day 2
  Solver: Shakhbozbek Usmonov (Miracle)
  --
  
  1. string_times
  2. front_times
  3. count_xx
  4. double_x
  5. string_bits
  6. string_splosion
  7. last2
  8. array_count9
  9. array_front9
  10. array123
  11. string_match
  12. string_x
  13. alt_pairs
  14. string_yak
  15. array667
  16. no_triples
  17. has271
"""

# stringTimes("Hi", 2) → "HiHi"
# stringTimes("Hi", 3) → "HiHiHi"
# stringTimes("Hi", 1) → "Hi"


def string_times(str, n):
    return str * n


# frontTimes("Chocolate", 2) → "ChoCho"
# frontTimes("Chocolate", 3) → "ChoChoCho"
# frontTimes("Abc", 3) → "AbcAbcAbc"

def front_times(str, n):
    return str[:3] * n


# countXX("abcxx") → 1
# countXX("xxx") → 2
# countXX("xxxx") → 3

def count_xx(str):
    return str.count('xx')


# doubleX("axxbb") → true
# doubleX("axaxax") → false
# doubleX("xxxxx") → true

def double_x(str):
    for i in range(len(str) - 1):
        if str[i] == 'x' and str[i + 1] == 'x':
            return True
    return False


# stringBits("Hello") → "Hlo"
# stringBits("Hi") → "H"
# stringBits("Heeololeo") → "Hello"

def string_bits(str):
    return str[::2]


# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i + 1]
    return result


# last2("hixxhi") → 1
# last2("xaxxaxaxx") → 1
# last2("axxxaaxx") → 2

def last2(str):
    if len(str) < 2:
        return 0
    last = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last:
            count += 1
    return count


# arrayCount9([1, 2, 9]) → 1
# arrayCount9([1, 9, 9]) → 2
# arrayCount9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    return nums.count(9)


# arrayFront9([1, 2, 9, 3, 4]) → true
# arrayFront9([1, 2, 3, 4, 9]) → false
# arrayFront9([1, 2, 3, 4, 5]) → false


def array_front9(nums):
    return 9 in nums[:3]


# array123([1, 1, 2, 3, 1]) → true
# array123([1, 1, 2, 4, 1]) → false
# array123([1, 1, 2, 1, 2, 3]) → true

def array123(nums):
    return 1 in nums and 2 in nums and 3 in nums


# stringMatch("xxcaazz", "xxbaaz") → 3
# stringMatch("abc", "abc") → 2
# stringMatch("abc", "axc") → 0

def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count


# stringX("xxHxix") → "xHix"
# stringX("abxxxcd") → "abcd"
# stringX("xabxxxcdx") → "xabcdx"

def string_x(str):
    return str.replace('x', '')


# altPairs("kitten") → "kien"
# altPairs("Chocolate") → "Chole"
# altPairs("CodingHorror") → "Congrr"

def alt_pairs(str):
    return str[0::2] + str[1::2]


# stringYak("yakpak") → "pak"
# stringYak("pakyak") → "pak"
# stringYak("yak123ya") → "123ya"

def string_yak(str):
    return str.replace('yak', '')


# array667([6, 6, 2]) → 1
# array667([6, 6, 2, 6]) → 1
# array667([6, 7, 2, 6]) → 1

def array_667(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 6:
            if nums[i + 1] == 6 or nums[i + 1] == 7:
                count += 1
    return count


# noTriples([1, 1, 2, 2, 1]) → true
# noTriples([1, 1, 2, 2, 2, 1]) → false
# noTriples([1, 1, 1, 2, 2, 2, 1]) → false

def no_triples(nums):
    for i in range(len(nums) - 2):
        if nums[i] == nums[i + 1] == nums[i + 2]:
            return False
    return True


# has271([1, 2, 7, 1]) → True
# has271([1, 2, 8, 1]) → False
# has271([2, 7, 1]) → True

def has_271(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 7:
            return True
    return False
