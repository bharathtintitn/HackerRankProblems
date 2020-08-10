import pdb


def knap_snack(total_weigth, items):

    pdb.set_trace()
    memo = [[0]*(total_weigth + 1) for _ in xrange(len(items)+1)]
    for j in xrange(len(items)):
        weigth, number_of_items = items[j]
        for i in xrange(1, total_weigth + 1):
            if j == 4:
                pdb.set_trace()
            if weigth > i:
                memo[j+1][i] = memo[j][i]
            else:
                memo[j+1][i] = max(memo[j][i], number_of_items + memo[j][i-weigth])
    print memo

if __name__ == "__main__":

    items = [(1,1), (3,4), (4,5), (5,7)]
    total_weight = 7
    knap_snack(total_weight, items)
