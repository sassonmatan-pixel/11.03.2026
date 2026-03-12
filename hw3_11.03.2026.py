"""
Create a function that receives two dictionaries.

Each dictionary has:

key → string
value → string
The function should create and return a third dictionary that combines both dictionaries.

Rules:

If a key appears in only one dictionary, add it normally
If the same key appears in both dictionaries, choose the value with the longer string
If both strings have the same length, keep the value from the first dictionary
Example:

dict1 = {
    "name": "Dan",
    "city": "Tel Aviv",
    "job": "Dev"
}

dict2 = {
    "name": "Daniel",
    "city": "TA",
    "country": "Israel"
}
Possible result:

{
    "name": "Daniel",
    "city": "Tel Aviv",
    "job": "Dev",
    "country": "Israel"
}
"""
from pprint import pprint
dict1 = {
    "name": "Dan",
    "city": "Tel Aviv",
    "job": "Dev"
}
dict2 = {
    "name": "Daniel",
    "city": "TA",
    "country": "Israel"
}
def combine_dicts(dict1, dict2) -> dict:
    """
    Combine two dictionaries.
    :param dict1:
    :param dict2:
    :return: If a key appears in only one dictionary, add it normally
             If the same key appears in both dictionaries, choose the value with the longer string
             If both strings have the same length, keep the value from the first dictionary
    """
    result = {}
    for key in dict1.keys():
        if key in dict2:
            if len(dict2[key]) > len(dict1[key]):
                result[key] = dict2[key]
            else:
                result[key] = dict1[key]
        else:
            result[key] = dict1[key]
    for key in dict2.keys():
        if key not in dict1:
            result[key] = dict2[key]
    return result

pprint(combine_dicts(dict1, dict2), width=30, sort_dicts=False)