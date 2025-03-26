n = 762.95
n_str = str(n)
for i in n_str:
    print(i)
    
    
n = 567
n_str = str(n)
sq_sum = 0
for d in n_str:
    sq_sum += int(d)**2
print('Sum of squared digits:', sq_sum)


def remove_all_whitespaces(s):
    s_list = s.split()
    s = ''.join(s_list)
    return s



import string

def reverseWithoutReversing(s):
    '''Returns the input string with all words in reverse order but whithout
        reversing the single words, and removing all extra spaces.
        Words are separated by spaces and there
        might be multiple and/or lead/train spaces that need to be removed.
        E.g., " Hello  I like this   course " should be retuned as
        "course this like I Hello".
    '''
    s = s.strip()
    word_list = s.split()
    word_string = ' '.join(word_list[-1::-1])
    return word_string


def isPangram(s):
    '''Check if ALL the letters of the alphabet appears at least once in
        the string s. Upper or lower case doesn't matter''' 
    for letter_code in range(ord('a'), ord('z')):
        letter = chr(letter_code)
        if letter.upper() not in s and letter.lower() not in s:
            return False
    return True

def is_valid_filename(s):
    if s.count('.') != 1:
        print("Error: there's more the one dot")
        return False
    elif len(s) - s.find('.') != 4:
        print("Error: the extension has more than three characters")
        return False
    elif s.find(' ') > 0:
        print("Error: there are white spaces")
        return False
    elif len(s) < 4:
        print("Error: the name is shorter than one character")
        return False
    elif s[0].isdigit():
        print("Error: the name doesn't start with a letter")        
        return False
    elif not s[0:len(s)-4].isalnum():
        print("Error: the name contains non alphanumeric characters")
        return False
    else:
        return True
