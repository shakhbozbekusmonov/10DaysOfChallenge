"""
  https://codingbat.com/python 

  1. String-1 - Day 3
  Solver: Shakhbozbek Usmonov (Miracle)
  --
  
  1. hello_name
  2. make_abba
  3. make_tags
  4. make_out_word
  5. extra_end
  6. first_two
  7. first_half
  8. without_end
  9. combo_string
  10. non_start
  11. left2
  12. right2
  13. the_end
  14. without_end2
  15. middle_two
  16. endsly
  17. n_twice
  18. two_char
  19. middle_three
  20. has_bad
  21. at_first
  22. last_chars
  23. con_cat
  24. last_two
  25. see_color
  26. front_again
  27. min_cat
  28. extra_front
  29. without2
  30. de_front
  31. start_word
  32. without_x
  33. without_x2
"""


def hello_name(name):
    return f"Hello {name}!"


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


def make_out_word(out, word):
    return out[:2] + word + out[-2:]


def extra_end(str):
    return str[-2:] * 3


def first_two(str):
    return str[:2]


def first_half(str):
    return str[:len(str) // 2]


def without_end(str):
    return str[1:-1]


def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    return b + a + b


def non_start(a, b):
    return a[1:] + b[1:]


def left2(str):
    return str[2:] + str[:2]


def right2(str):
    return str[-2:] + str[:-2]


def the_end(str, front):
    if front:
        return str[-1]
    return str[0]


def without_end2(str):
    return str[1:-1]


def middle_two(str):
    return str[:len(str) // 2 - 1] + str[len(str) // 2 + 1:]


def endsly(str):
    return str[-2:] == "ly"


def n_twice(str, n):
    return str[:n] + str[-n:]


def two_char(str, index):
    return str[:index] + str[index:index + 2]


def middle_three(str):
    return str[:len(str) // 2 - 1] + str[:len(str) // 2 + 2]


def has_bad(str):
    return str[:3] == "bad" or str[1:4] == "bad"


def at_first(str):
    if len(str) < 2:
        return str + "@"
    return str[:2]


def last_chars(a, b):
    return a[:1] + b[-1:]


def con_cat(a, b):
    if a[-1:] == b[:1]:
        return a[:-1] + b
    return a + b


def last_two(str):
    return str[:-2] + str[-1:] + str[-2:-1]


def see_color(color):
    if color[:3] == "red":
        return "red"
    if color[:4] == "blue":
        return "blue"
    return ""


def front_again(str):
    return str[:2] == str[-2:]


def min_cat(a, b):
    if len(a) > len(b):
        return a[-len(b):] + b
    if len(b) > len(a):
        return a + b[-len(a):]
    return a + b


def extra_front(str):
    return str[:2] * 3


def without2(str):
    if str[:2] == str[-2:]:
        return str[2:]
    return str


def de_front(str):
    if str[0] == "a":
        return str[0] + str[2:]
    if str[0] == "b":
        return str[0] + str[1]
    return str
