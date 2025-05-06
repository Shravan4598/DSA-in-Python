hashmap = {}

hashmap['one'] = 1


def count_frequency(nums):
    ans = {}

    for eachNumber in nums:
        if eachNumber in ans:
            ans[eachNumber] +=1
        else:
            ans[eachNumber]= 1
    
    return ans


nums = [1,2,2,3,3,1,1,4,2]
ans = count_frequency(nums)

ans = {'key1':1,'key2':2}





def group_anagrams(words):
    anagrams ={}

    for eachWord in words:
        sorted_word = ''.join(sorted(eachWord))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(eachWord)
        else:
            anagrams[sorted_word] = [eachWord]

    return list(anagrams.values())

words = ['eat','tea','tan','ate','nat','bat']
dict1 = group_anagrams(words)






