


def lcs(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    memory = [[0]*(length2+1) for _ in xrange(length1+1)]
    print memory

    for i in xrange(1, length1+1):
        character1 = str1[i-1]
        for j in xrange(length2+1):
            character2 = str2[j-1]
            if character1 == character2:
                value = max(1, memory[i-1][j-1]+1)
            else:
                value = max(memory[i-1][j], memory[i][j-1])
            memory[i][j] = value
    print memory


if __name__ == "__main__":

    lcs('acdbdwe', 'adgccddwe')
