

def mul_by_n(lst, n):
    return [i * n for i in lst]


def compare(a, b):
    digits_a = [int(d) for d in str(a)]
    digits_b = [int(d) for d in str(b)]

    common_digits = set(digits_a) & set(digits_b)
    
    similarity_percentage = len(common_digits) / 2 * 100
    if a == b:
        return "100%"
    else:

        return f"{int(similarity_percentage)}%"


def alternate(n, first_value,second_value):
    new_lis = []
    for i in range(n):
        if i % 2 == 0:
            new_lis.append(first_value)
        else:
            new_lis.append(second_value)
    return new_lis


def name_shuffler(str_):
    return " ".join((str_.split()[::-1])) 


def set_reducer(inp):   
    if len(inp) == 1:
        return inp[0]
    
    res = []
    count = 1
    for i in range(1,len(inp)):
        if inp[i] == inp[i-1]:
            count +=1
        else:
            res.append(count)
            count = 1
    res.append(count)
    
    return set_reducer(res)
       

def validate_hello(greetings):
    messages = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]

    for message in messages:
        if message in greetings.lower():
            return True
    return False


def find_average(numbers):
    return int(sum(numbers) / len(numbers)) if numbers else 0


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m


def domain_name(url):
    return url.split("//")[-1].replace("www.","").split(".")[0]


class Python:
    def __init__(self,name):
        self.name = name


def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    return "Odd"

def get_count(sentence):
    
    count = 0
    for x in sentence.lower():
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            count +=1
    return count

def disemvowel(string_):
    
    vowels = ["a","e","i","o","u"]
    return "".join(x for x in string_ if x.lower() not in vowels)

def square_digits(num: int) -> int:
    
    digits = [int(x) ** 2 for x in str(num)]
    squared_str = ''.join(map(str, digits))
    return int(squared_str)

def high_and_low(numbers):
    listing = [num for num in numbers.split() if num.isdigit() or (num.startswith("-") and num[1:].isdigit())]
    listing = sorted(listing, key=lambda x: (int(x) >= 0, int(x)))
    return str(listing[-1])+ " "+ str(listing[0])

def descending_order(num):
    each_digit = [int(digi) for digi in str(num)]
    return int("".join(map(str,(sorted(each_digit,reverse=True)))))

def get_middle(s):
    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:
        return s[middle_index - 1 : middle_index + 1]
    else:
        return s[middle_index]
    
def positive_sum(arr):
    return [sum(x for x in arr if x > 0)][0]

def is_square(num):
    if num < 0:
        return False
    for i in range(int(num ** 0.5) + 1):
        if i * i == num:
            return True
    return False

def capitals(word):
    
    return [index for index,x in enumerate(word) if x ==x.upper()]

def sorted_numbser(nums):
    return sorted(nums) if nums else []

def say_hello(name, city, state):
    name_ = " ".join(name)
    return f"Hello, {name_}! Welcome to {city}, {state}!"

def last_man_standing(n):
  
    numbers = list(range(1, n + 1))
    repeat = True
    while repeat:
        numbers = numbers[1::2]
        numbers = numbers[-1::-1]
        if len(numbers) == 1:
            repeat = False
    
    return numbers[0]