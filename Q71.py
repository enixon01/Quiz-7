#Emily Nixon
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
        
print(count_hashtag("#This is #hashtag #awesome"))
