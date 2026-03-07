"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author:  <your name>
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    chars = ""
    for char in s:
        chars = char + chars 
    return chars
    
# Your unit tests 
assert reverse_str('kiana') == 'anaik'
assert reverse_str('apple') == 'elppa'
assert reverse_str('banana') == 'ananab'
"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1 
    return vowel_count 
# Your unit tests
assert count_vowels('kiana') == 3
assert count_vowels('pear') == 2
assert count_vowels('python') == 1
"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """
    This function removes duplicate charcters in a string. It removes duplicate letters in a word. The function considers 
    uppercase letters and lowercase letters as different. 

    Parameters: 
    - s (string): The inputted string in which vowels are counted.

    Returns:
    - chars: The variable that is continually reassigned using the accumulator algorithm and at the end of the function, 
    refers to the string with duplicate characters removed.

    Eg., 
    >>> remove_duplicates("Popsipple") == "Popsile" where 'P' and 'p' are considered different characters.
    """
    chars = ""
    for char in s:
        if char not in chars:
            chars += char       
    return chars 
                
# Your unit tests
assert remove_duplicates("kianna") == "kian"
assert remove_duplicates("lollipop") == "loip" 
assert remove_duplicates("brown") == "brown"
"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    This function finds the index of the first occurence of the character t in a string s. The function returns -1 if 
    the character t is not in the string. 

    Parameters:
    - s (string): The inputted values which is traversed to find the position of character t. 

    - t (character): The character that is looked for in the string. 

    Returns:
    - index of character t if it is in string s or -1 if t is not in s.

    Eg.,
    >>> find_index('red', 'd') == 2
    """
    for char in s: 
        if char == t:
            return s.index(char)
    return -1 

# Your unit tests
assert find_index("red", 'd') == 2
assert find_index("XYZ", 'z') == -1
assert find_index("pink", 'k') == 3
"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    This function finds the day of completion of a project when given the start date, day, and duration of project, days_to_completion. 
    It finds the index of day in the list called days_week and then adds this index with the days_to_completion and uses modulus operator. 
    It returns the day of the week that the project completes on. 

    Parameters: 
    - day (string): The variable referencing the day of the week that the project starts on. 
    - days_to_completion (int): The variable assigned to length of the project in number of days. 

    Returns:
    - days_week[project_complete] (string): Uses variable project_complete as an index of days_week to return the string value of date the 
    project will be finished. 
    """
    project_complete = (days_week.index(day) + days_to_completion) % 7
    return days_week[project_complete]

# Your unit tests
project_completion_day('Saturday', 4) == 'Thursday'
project_completion_day('Friday', 7) == 'Thursday'
project_completion_day('Monday', 2) == 'Wednesday'
project_completion_day('Wednesday', 4) == 'Sunday'


"""Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to implement two functions to parse and filter
these logs.

Log format - Each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

Sample log data:
log_string = "
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"

Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hint: str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']
"""
def parse_log_line(line):
    log = line.split()

    timestamp = (log[0] + " " + log[1])
    level = log[2][1:-1]
    module = (log[3])
    message = " ".join(log[4:])
    return (timestamp, level, module, message)

assert parse_log_line('2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s') == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

# Your unit tests
assert parse_log_line('2024-04-11 09:15:03 [ERROR] database.py Connection timeout after 45s') == ('2024-04-11 09:15:03', 'ERROR', 'database.py', 'Connection timeout after 45s')
assert parse_log_line('2024-04-11 09:15:07 [WARNING] api.py Slow query detected (3.1s)') == ('2024-04-11 09:15:07', 'WARNING', 'api.py', 'Slow query detected (3.1s)')
assert parse_log_line('2024-04-11 09:15:12 [INFO] server.py Server started on port 8080') == ('2024-04-11 09:15:12', 'INFO', 'server.py', 'Server started on port 8080')

# Use your parse_log_line() to parse all the lines in the sample data log_string,
# and store each tuple item in a list.
# Hint: log_string.split('\n') will return a list of lines.

"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository, and paste the link on e-learn. That's all.
"""