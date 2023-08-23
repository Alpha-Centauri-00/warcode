

def mul_by_n(lst, n):
    '''mutiply a givin number to each number in a list'''
    return [i * n for i in lst]


def compare(a, b):
    '''it checks if a is equal to b then returns 100% and if a one number in a is also in b then it returns 50% otherwise it will return 0%'''
    digits_a = [int(d) for d in str(a)]
    digits_b = [int(d) for d in str(b)]

    common_digits = set(digits_a) & set(digits_b)
    
    similarity_percentage = len(common_digits) / 2 * 100
    if a == b:
        return "100%"
    else:

        return f"{int(similarity_percentage)}%"


def alternate(n, first_value,second_value):
    '''in this function it will return first_value and second_value times n'''
    new_lis = []
    for i in range(n):
        if i % 2 == 0:
            new_lis.append(first_value)
        else:
            new_lis.append(second_value)
    return new_lis


def name_shuffler(list_strings):
    '''this function will reverse last name with surname'''
    return " ".join((list_strings.split()[::-1])) 


def set_reducer(inp):   
    '''This function takes in an array of integers from 0-9, and returns a new array:'''
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
    '''This should check if a word in a list is a valid greeting'''
    messages = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]

    for message in messages:
        if message in greetings.lower():
            return True
    return False


def find_average(numbers):
    '''Find the avarage from a givin numbers'''
    return int(sum(numbers) / len(numbers)) if numbers else 0


def paperwork(n, m):
    '''This task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.'''
    return 0 if n < 0 or m < 0 else n * m


def domain_name(url):
    '''Get the domain name from a link'''
    return url.split("//")[-1].replace("www.","").split(".")[0]


class Python:
    def __init__(self,name):
        self.name = name


def even_or_odd(number):
    '''if a number is even returns Even else Odd'''
    if number %2 == 0:
        return "Even"
    return "Odd"

def get_count(sentence):
    '''Count the vowel letters in a given sentence'''
    count = 0
    for x in sentence.lower():
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            count +=1
    return count

def disemvowel(string_):
    '''Remove the vowel letters in a given string_'''
    vowels = ["a","e","i","o","u"]
    return "".join(x for x in string_ if x.lower() not in vowels)

def square_digits(num: int) -> int:
    '''Sequare a given number'''
    digits = [int(x) ** 2 for x in str(num)]
    squared_str = ''.join(map(str, digits))
    return int(squared_str)

def high_and_low(numbers):
    '''Get the highst number and lowest from numbers'''
    listing = [num for num in numbers.split() if num.isdigit() or (num.startswith("-") and num[1:].isdigit())]
    listing = sorted(listing, key=lambda x: (int(x) >= 0, int(x)))
    return str(listing[-1])+ " "+ str(listing[0])

def descending_order(num):
    '''Descending num order from left to wright, big to small'''
    each_digit = [int(digi) for digi in str(num)]
    return int("".join(map(str,(sorted(each_digit,reverse=True)))))

def get_middle(s):
    '''Get the middle 2 letters from a sentence'''
    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:
        return s[middle_index - 1 : middle_index + 1]
    else:
        return s[middle_index]
    
def positive_sum(arr):
    '''Sum only positive numbers in arr'''
    return [sum(x for x in arr if x > 0)][0]

def is_square(num):
    '''Given an integral number, determine if it's a square number'''
    if num < 0:
        return False
    for i in range(int(num ** 0.5) + 1):
        if i * i == num:
            return True
    return False

def capitals(word):
    '''Return an index of a capital letter in a word'''
    return [index for index,x in enumerate(word) if x ==x.upper()]

def sorted_numbser(nums):
    '''Sorting numbers small number to big'''
    return sorted(nums) if nums else []

def say_hello(name, city, state):
    '''Return a hello name with a given city and state'''
    name_ = " ".join(name)
    return f"Hello, {name_}! Welcome to {city}, {state}!"

def last_man_standing(n):
    '''Find the last number between 1 and n (inclusive) that survives the elimination process'''
    numbers = list(range(1, n + 1))
    repeat = True
    while repeat:
        numbers = numbers[1::2]
        numbers = numbers[-1::-1]
        if len(numbers) == 1:
            repeat = False
    
    return numbers[0]

def tail_swap(list_strings):
    '''return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.'''
    lis = []
    for x in list_strings:
        colon = x.split(":")
        lis.extend(colon)
    return [lis[0]+ ":"+lis[3],lis[2]+ ":"+lis[1]]