"""
Lab 8 - Set and Dict 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  <your name>
Due Date: This Friday (Mar. 13) 5pm.
Note: Try best to finish the lab exercises using what we've learnt about algorithms.
      Please do not rely on AI assistant too heavily for labs.

Objective:
1. Review how to write a good python docstring (started from lab7).
2. Review how to code simple Python functions and write unit tests using assert.
3. Practice how to operate on set and dict.
4. Review iterations using loop.
5. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, a set, a dict, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Here is one solution of Lab 7 exercise 3: Remove the duplicate characters in a string.
E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"
"""
def remove_duplicates(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"
    """
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res

# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

"""
Exercise 1 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Can you try to implement the above duplicates removal using data type set?

Hint: 1. We put the seen chars in the set while adding them to the res string;
      We also check if the new char is already in the set (more efficient than checking a string). If not seen, add it to the res string.
      2. To initialize an empty set: seen_set = set()
"""
def remove_duplicates_set(s):
    """
    This function removes duplicates in a string s by using an empty set and empty string.  
    For each character in the string, if the character is not yet in the set, then add it to the empty string and to the empty set. 

    Parameters:
    s (string): any string value 

    Returns:
    res (string): string containing the non duplicated characters
    """
    seen_set = set()
    res = ''
    for c in s:
        if c not in seen_set:
            res += c
            seen_set.add(c)
    return res 

    # OR
    # seen_set = set(s)
    # return ''.join(seen_set)

# Your unit tests
assert remove_duplicates_set('purple') == 'purle'
assert remove_duplicates_set('bottle') == 'botle'

"""
Exercise 2 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Assume you've collected many stones, 
and each character in the string stones represents a type of a stone. 
And each character in the string gems represents a type of a gem.

Write a function to calculate how many stones you've collected are actually jems. 
Requirement: Implement the function using data type set

E.g.,
gem_counting("abDFMdm", "admMQq") will return 4
gem_counting("abDFMdm", "af") will return 1
gem_counting("awCcM", "cQqW") will return 1
gem_counting("bFfL", "cQqW") will return 0
"""
def gem_counting(stones, gems):
    """
    This function finds how many stones are gems and uses a counter to count each time a stone is found as a gem.
    
    Parameters:
    stones (string): a string containing characters that represent stones
    gems (string): a string conataining characters that represent gems

    Returns:
    res (int): a variable referring to the number of stones that were also found to be gems
    """
    res = 0 #first step of accumulator algorithm is to initialize a variable 
    gem_set = set(gems) #create set, makes more efficient so doesnt have to traverse whole string gems 
    for stone in stones:
        if stone in gem_set:
            res += 1
    return res

# Your unit tests
assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("awCcM", "cQqW") == 1

"""
Exercise 3 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

CapU is planning to launch a shuttle bus between main campus 
and the students accomendation. (Fake news but best wishes 😄)

To determine how many buses are needed each day, 
CapU keeps track of the students who use the shuttle bus service.

Write a function students_id() that takes a list of student ids as its parameter, 
and returns the number of different students who use the shuttle service.

E.g.,
students_id(['002', '003', '001', '004', '012']) returns 5
students_id(['002', '003', '001', '012', '003', '001']) returns 4

Hint: 
Think about which data type we should use to ease the work of finding distinctive values from a list.

"""
def students_id(ids):
    """
    This function takes a list of students ids and returns a set of the students ids to remove duplicates. 

    Parameters:
    ids (list): list of string numbers representing student ids. 

    Returns:
    lenght of list of ids as a set
    """
    return len(set(ids))

# Your unit tests
assert students_id(['002', '003', '001', '012', '003', '001']) == 4
assert students_id(['002', '003', '001', '004', '012']) == 5

"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Similar as exercise 3, write a function called students_id_occurences() 
that takes a list of student ids as its parameter, 
and returns the occurences of each different student 
who uses the shuttle service in the form of dictionary data type.

E.g.,
students_id_occurences(['002', '003', '001', '004', '012']) 
returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}}

students_id_occurences(['002', '003', '001', '012', '003', '001']) 
returns {'002': 1, '003': 2, '001': 2, '012': 1}

Hint: To initialize an empty dict: id_dict = {}
"""
def students_id_occurrences(ids):
    """
    This fucntion turns list of ids into a dicrtionary and initializes an empty dictionary.
    For every id in the set of ids, if the id is in the dictionary, then the value for 
    that id key gets 1 added to it. 
    Else it gets the value 1.

    Parameters:
    ids (list): list of string values representing student ids 

    Returns:
    id_dict (dict): dictionary containing keys representing student ids and values referring 
    to number of times that id occurs in the list.
    """
    id_dict = {} 
    for id in ids:
        if id in id_dict:
            id_dict[id] += 1
        else:
            id_dict[id] = 1

    return id_dict 
# Your unit tests
assert students_id_occurrences(['002', '003', '001', '004', '012']) == {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}
assert students_id_occurrences(['002', '003', '001', '012', '003', '001']) == {'002': 1, '003': 2, '001': 2, '012': 1}

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to count 
the frequency of words in a given paragraph.

E.g.,
word_frequency("I am alive. I am happy.") 
returns {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}

word_frequency("I do not like water. I like fruits.") 
returns {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}

Hint: 
import Python's regular expression (pattern used to search for text patterns) module re. 
re.findall(r'\b\w+\b', s) returns list of words from s that matches the pattern of word.
"""
import re
def word_frequency(paragraph):
    """
    This fucntion can count the frequency of words in a given paragraph. It uses re module and 
    empty dictionary. It goes through the ids in words and if the id is in the dictionary 
    and if it is, then that dictionary key's value gets 1 added to it. Otherwise it remains 1.

    Parameters:
    paragraph (str): a string with similar sentences that re module can detect word pattern from.

    Returns:
    d (dict): returns dictionary containing word keys and values of occurences of those words 
    in paragraph.
    """
    words = re.findall(r'\b\w+\b', paragraph)
    d = {} 
    for id in words:
        if id in d:
            d[id] += 1
        else:
            d[id] = 1
    return d 
    
# Your unit tests
assert word_frequency("I am alive. I am happy.") == {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}
assert word_frequency("I do not like water. I like fruits.") == {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}

"""
Real-world Coding Question (optional): Extract Repository IDs and Names from GitHub API Data

The GitHub API allows you to search for repositories using different criteria. 
The following code sends a request to GitHub to find Python repositories with more than 300,000 stars.

The API response is converted into a Python dictionary called response_dict. 
Inside this dictionary, the key "items" contains a list of repository dictionaries,
where each repository includes information such as id, name, stars, and more.
"""

import requests 

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>300000"
# You can copy and paste the url into your browser to view the data.

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

# print(f"Status Code: {response.status_code}") 
# HTTP response status code 200 means The server processed the request and returned the requested data successfully.

response_dict = response.json() # Convert the response object to a dictionary


"""
Task: Write a function called id_name_repo_starred_300k(response_dict) that
takes response_dict as its parameter, 
traverses the list stored under the "items" key,
returns a dictionary containing all repository id → name pairs.

Ensure that your function passes the unit test provided below.
"""

# Save the repositories' id: name as a pair in a dict, and print them out.
def id_name_repo_starred_300k(response_dict):
    items = response_dict['items']
    repo_dict = {}
    for repo in items:
        repo_id = repo['id']
        repo_name = repo['name']
        repo_dict[repo_id] = repo_name

    return repo_dict

assert id_name_repo_starred_300k(response_dict) == {
    13491895: 'free-programming-books',
    54346799: 'public-apis',
    83222441: 'system-design-primer'
    }


"""
Congratulations on finishing your lab8. Hope you feel more comfortable now on the data type set and dict.

You just need to upload this lab to your GitHub repository, and copy the link to e-learn. That's all.
"""