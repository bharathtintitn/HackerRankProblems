
def orientation(row_number, row, crossword):
    word_present = False
    for i, j in enumerate(row):
        if j == '-':
            word_present = True
            break
    count = 0
    is_horizantal = True
    for k in xrange(i, len(row)):
        if row[k] == '-':
           count += 1
        else:
            break
    if count == 1:
        count = 0
        for k in xrange(row_number, 10):
            if crossword[k][i] == '-':
                count +=1
                is_horizantal = False
            else:
                break
    return count, is_horizantal, word_present, i

def place_word(row, crossword, info, words):

        if len(words) == info[0]:
            for i in xrange(info[0]):
                if info[1]:
                    crossword[row][info[3] + i] = words[i]
                else:
                    crossword[row+i][info[3]] = words[i]
            return

def backtrack(info, row, crossword):
    for i in xrange(info[0]):
        if info[1]:
            crossword[row][info[3] + i] = '-'
        else:
            crossword[row+i][info[3]] = '-'


def list_of_words(words, count):

    words_list = [i for i in words if len(i) == count]
    print words_list
    return words_list

def crosswordPuzzle(crossword, words):

    for i in xrange(0, 10):
        place_info = orientation(i, crossword[i], crossword)
        if place_info[2]:
            words_list = list_of_words(words, place_info[0])
            for word in words_list:
                place_word(i, crossword, place_info, word)
                backtrack(place_info, i, crossword)
                return_value = crosswordPuzzle(crossword, words_list)
                if return_value:
                    return True

if __name__ == "__main__":

    import pdb
    crossword = []
    for _ in xrange(10):
        crossword_item = raw_input().strip()
        crossword.append(crossword_item)
    #pdb.set_trace()
    words = raw_input().split(';')
    pdb.set_trace()
    result = crosswordPuzzle(crossword, words)
