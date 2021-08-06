# Find 512 in 2 loops.
def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512"

print(find_512())


# Substring in string.
def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index: index + len(substring)] == substring:
            return True
        index += 1
    return False


print(is_substring('izz', 'izzbazzfizz'))
print(is_substring('bad', 'abracadabra'))
print(is_substring('dab', 'abracadabra'))


# Characters and Substrings.
def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return f"Characters count: {total}"


def count_substring(string, substring):
    index = 0
    total = 0
    while index < len(string):
        if string[index: index + len(substring)] == substring:
            total += 1
            index += len(substring)
        else:
            index += 1
    return f"Substrings count: {total}"


print(count_character('love, love, love, all you need is love', 'l'))
print(count_substring('love, love, love, all you need is love', 'love'))
print(count_substring('AAddaAAAAAAA', 'AA'))

#  Location of substring.
def locate_first(string, count):
    index = 0
    matches = []
    while index < len(string):
        if string[index: index + len(count)] == count:
            matches.append(index)
            index += len(count)
        else:
            index += 1
    return f"Locate index: {matches}"

print(locate_first('cookbook', 'ook'))
