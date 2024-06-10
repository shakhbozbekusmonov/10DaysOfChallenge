"""
  https://codingbat.com/python 

  1. Warmup-1 - Day 1
  Solver: Shakhbozbek Usmonov (Miracle)
  --
  
  1. sleep_in
  2. monkey_trouble
  3. sum_double
  4. diff21
  5. parrot_trouble
  6. makes10
  7. near_hundred
  8. pos_neg
  9. not_string
  10. missing_char
  11. front_back
  12. front3
  13. back_around
  14. or35
  15. front22
  16. start_hi
  17. icy_hot
  18. in1020
  19. has_teen
  20. lone_teen
  21. del_del
  22. mix_start
  23. start_oz
  24. int_max
  25. close10
  26. in3050
  27. max1020
  28. string_e
  29. last_digit
  30. end_up
  31. every_nth
"""

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


def sleep_in(weekday, vacation):
    return not weekday or vacation


# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    return a + b

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0


def diff21(n):
    if n > 21:
        return abs(21 - n) * 2
    return 21 - n


# parrotTrouble(true, 6) → true
# parrotTrouble(true, 7) → false
# parrotTrouble(false, 6) → false

def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))


# makes10(9, 10) → true
# makes10(9, 9) → false
# makes10(1, 9) → true

def makes_10(a, b):
    return (a + b) == 10 or (a == 10 or b == 10)


# nearHundred(93) → true
# nearHundred(90) → true
# nearHundred(89) → false

def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# posNeg(1, -1, false) → true
# posNeg(-1, 1, false) → true
# posNeg(-4, -5, true) → true


def pos_neg(a, b, negative):
    return (negative and (a < 0 and b < 0)) or (not negative and (a < 0 or b < 0))


# notString("candy") → "not candy"
# notString("x") → "not x"
# notString("not bad") → "not bad"

def not_string(input_str):
    if len(input_str) >= 3 and input_str[:3] == "not":
        return input_str
    return "not " + input_str


# missingChar("kitten", 1) → "ktten"
# missingChar("kitten", 0) → "itten"
# missingChar("kitten", 4) → "kittn"

def missing_char(str, n):
    return str[:n] + str[n+1:]


# frontBack("code") → "eodc"
# frontBack("a") → "a"
# frontBack("ab") → "ba"

def front_back(str):
    if len(str) < 2:
        return str
    return str[-1:] + str[1:-1] + str[:1]


# front3("Java") → "JavJavJav"
# front3("Chocolate") → "ChoChoCho"
# front3("abc") → "abcabcabc"

def front3(str):
    return str[:3] * 3


# backAround("cat") → "tcatt"
# backAround("Hello") → "oHelloo"
# backAround("a") → "aaa"

def back_around(str):
    return str[-1:] + str + str[-1:]


# or35(3) → true
# or35(10) → true
# or35(8) → false

def or35(n):
    return n % 3 == 0 or n % 5 == 0


# front22("kitten") → "kikittenki"
# front22("Ha") → "HaHaHa"
# front22("abc") → "ababcab"

def front22(str):
    return str[:2] + str + str[:2]


# startHi("hi there") → true
# startHi("hi") → true
# startHi("hello hi") → false

def start_hi(str):
    return str.startswith('hi')


# icyHot(120, -1) → true
# icyHot(-1, 120) → true
# icyHot(2, 120) → false

def icy_hot(temp1, temp2):
    return (temp1 < 0 and temp2 > 100) or (temp1 > 100 and temp2 < 0)


# in1020(12, 99) → true
# in1020(21, 12) → true
# in1020(8, 99) → false

def in1020(a, b):
    return 10 <= a <= 20 or 10 <= b <= 20


# hasTeen(13, 20, 10) → true
# hasTeen(20, 19, 10) → true
# hasTeen(20, 10, 13) → true

def has_teen(a, b, c):
    return 13 <= a <= 19 or 13 <= b <= 19 or 13 <= c <= 19


# loneTeen(13, 99) → true
# loneTeen(21, 19) → true
# loneTeen(13, 13) → false

def lone_teen(a, b):
    return (13 <= a <= 19 and b != 13) or (13 <= b <= 19 and a != 13)


# delDel("adelbc") → "abc"
# delDel("adelHello") → "aHello"
# delDel("adedbc") → "adedbc"

def del_del(str):
    if len(str) < 4:
        return str
    if str[:3] == 'del':
        return str[3:]
    return str


# mixStart("mix snacks") → true
# mixStart("pix snacks") → true
# mixStart("piz snacks") → false

def mix_start(str):
    if len(str) < 3:
        return False
    if str[1:3] == 'ix':
        return True
    return False


# startOz("ozymandias") → "oz"
# startOz("bzoo") → "z"
# startOz("oxx") → "o"

def start_oz(str):
    result = ''
    if str[0] == 'o':
        result += str[0]
    if str[1] == 'z':
        result += str[1]
    return result


# intMax(1, 2, 3) → 3
# intMax(1, 3, 2) → 3
# intMax(3, 2, 1) → 3

def int_max(a, b, c):
    return max(a, b, c)


# close10(8, 13) → 8
# close10(13, 8) → 8
# close10(13, 7) → 0

def close10(a, b):
    return (abs(10 - a) <= abs(10 - b)) * a + (abs(10 - b) > abs(10 - a)) * b


# in3050(30, 31) → true
# in3050(30, 41) → false
# in3050(40, 50) → true

def in3050(a, b):
    return 30 <= a <= 40 or 30 <= b <= 40 or 40 <= a <= 50 or 40 <= b <= 50


# max1020(11, 19) → 19
# max1020(19, 11) → 19
# max1020(11, 9) → 11

def max_1020(a, b):
    return 10 <= max(a, b) <= 20


# stringE("Hello") → true
# stringE("Heelle") → true
# stringE("Heelele") → false

def string_e(str):
    return str.count('e') > 1


# lastDigit(7, 17) → true
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def last_digit(a, b):
    return a % 10 == b % 10


# endUp("Hello") → "HeLLO"
# endUp("hi there") → "hi thERE"
# endUp("hi") → "HI"

def end_up(str):
    return str[:-2] + str[-2:].upper()


# everyNth("Miracle", 2) → "Mrce"
# everyNth("abcdefg", 2) → "aceg"
# everyNth("abcdefg", 3) → "adg"

def every_nth(str, n):
    return str[::n]
