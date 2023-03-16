# save only 5 letter words and sort them with radix sort
import copy

from english_words import english_words_lower_set

english_words = []
for val in english_words_lower_set:
    if len(val) == 5 and '.' not in val and '"' not in val and "'" not in val:
        english_words.append(val+'\n')

newdata = ["" for i in range(len(english_words))]
# radix sort for letters in a 5 letter words
data = copy.deepcopy(english_words)
for i in range(4, -1, -1):  # goint from last letter to first letter
    # first step stable counting sort
    letters = [0 for i in range(26)]
    for word in data:
        letters[ord(word[i]) - ord('a')] += 1
    # a part of stable counting sort add each index
    for j in range(len(letters)-1):
        letters[j+1] = letters[j] + letters[j+1]
    # a part of stable counting sort go through the list backwards and add to a new list each item
    # in the index from the conting array and sub 1 from the counting array
    for word in data[::-1]:
        temp = ord(word[i]) - ord('a')
        newdata[letters[temp]-1] = copy.copy(word)
        letters[temp] -= 1
    data = copy.deepcopy(newdata)

with open("words5.txt", "w") as file5:
    file5.writelines(newdata)
