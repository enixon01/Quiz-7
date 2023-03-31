#Emily Nixon
string = "This is #awesome!!!"
def count_hashtag(string):
    index = 0
    total = 0
    while index<len(string):
        if  index == "#":
            total + 1
            index += 1
        else:
            index += 1
        return total
        
def hash_spam(string):
    index = 0
    total = 0
    while index<len(string):
        if chr == "#":
            total + 1
            index += 1
            return total
        else:
            index += 1
    if total > 4:
        print("This tweet will be considered as a spam!")
    else:
        return None

