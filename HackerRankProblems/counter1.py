from collections import Counter
def solution(S):
    # write your code in Python 3.6
    if not S:
        return 0
        
    freq_char = Counter(S)
    #print(freq_char)
    #freq = [value for key, value in freq_char.items()]
    freq = [value for value in freq_char.values()]
    #print(freq)
    freq.sort(reverse=True)
    #print(freq)
    removed_char = 0
    for i in range(1, len(freq)):
        while freq[i] >= freq[i-1]:
            if freq[i] > 0:
                freq[i] = freq[i] - 1
                removed_char = removed_char + 1
    #print("Removed char:", removed_char)
    return removed_char

print solution("ccaaffddecee")
