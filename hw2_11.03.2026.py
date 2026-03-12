"""
Create a function called:

get_statistics
The function receives a list of numbers and returns a dictionary with the following statistics:

sum
average
minimum
maximum
length of the list
Function structure:

def get_statistics(numbers):
    pass
Demo code:

nums = [4, 8, 2, 10, 6]

result = get_statistics(nums)

print(result)
Possible output:

{
    'sum': 30,
    'avg': 6.0,
    'min': 2,
    'max': 10,
    'length': 5
}
"""
from pprint import pprint
def get_statistics(numbers) -> dict:
    """
    This function takes a list of numbers and returns a dictionary with the following statistics:
    :param numbers: the list of numbers
    :return: the dictionary with the following statistics (sum, average, min, max, length):
    """
    dictionary_numbers = \
{
    'sum': sum(numbers),
    'avg': sum(numbers) / len(numbers),
    'min': min(numbers),
    'max': max(numbers),
    'length': len(numbers)
}
    return dictionary_numbers

nums = [4, 8, 2, 10, 6]
result = get_statistics(nums)
#אופציה עם פפרינט
pprint(result, width=1, sort_dicts=False)

# אופציה 2 כמו הרווחים ששלחת
print('\n {')
for key, value in result.items():
    print(f'    {key}: {value}')
print('}')