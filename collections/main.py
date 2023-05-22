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
    greetings = greetings.lower()

    for message in messages:
        if message in greetings:
            return True
    return False


def find_average(numbers):
    return int(sum(numbers) / len(numbers)) if numbers else 0


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m