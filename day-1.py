# Warmup 1 -----------------------------

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
  return (a + b) ==  10 or (a == 10 or b == 10)


# nearHundred(93) → true
# nearHundred(90) → true
# nearHundred(89) → false
  
def near_hundred(n):
  return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# posNeg(1, -1, false) → true
# posNeg(-1, 1, false) → true
# posNeg(-4, -5, true) → true

def pos_ned(a, b, negative):
  return (negative and (a < 0 and b < 0)) or (not negative and (a < 0 or b < 0))