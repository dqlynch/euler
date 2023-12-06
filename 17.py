prefix = {
    2: len("twen"),
    3: len("thir"),
    4: len("for"),
    5: len("fif"),
    6: len("six"),
    7: len("seven"),
    8: len("eigh"),
    9: len("nine"),
}

mapping = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
}

def len_tens(tens_place):
    return prefix[tens_place] + len("ty")

def num2count(num):
    if num >= 0 and num < 20:
        return mapping[num]

    if num >= 20 and num < 100:
        ones_place = (num % 10)
        tens_place = (num % 100) // 10
        return len_tens(tens_place) + num2count(ones_place)


    if num >= 100 and num < 1000:
        hundreds_place = (num % 1000) // 100
        return num2count(hundreds_place) + len("hundredand") + num2count(num % 100) if num % 100 > 0 else num2count(hundreds_place) + len("hundred")

    if num == 1000:
        return len("onethousand")


if __name__ == '__main__':
    print(num2count(999))
    print(len("ninehundredandninetynine"))

    print(sum(num2count(i) for i in range(1, 1001)))

