#Given two strings, write a function that returns true if they are anagrams of each other and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another word.

s1 = "anagram"
t1 = "nagaram"
# Output:
# True

#s2 = "rat"
#t2 = "car"
#Output:
# False

#s3 = "stops"
#t3 = "pots"
#Output:
# False

def solution(s,t):
    # sorted_string1 = []
    # sorted_string2 = []
    # for char in s:
    #     sorted_string1.append(char)
    # for char in t:
    #     sorted_string2.append(char)
    # return sorted(sorted_string1) == sorted(sorted_string2)


    # or just use line 31

    return sorted(s) == sorted(t)

# print(solution(s1,t1))
# print(solution(s2,t2))
# print(solution(s3,t3))





# print(solution(s1,t1))
