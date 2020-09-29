import pdb


def bfs(right, left, paren, num, result):

    if right == num and left == num:
        print('Found', paren)
        result.append(paren)
        return

    if right < num:
        right += 1
        paren += '('
        bfs(right, left, paren, num, result)

    if left < num:
        left += 1
        paren += ')'
        bfs(right, left, paren, num, result)

    return

def generate_valid_parentheses(num):
  result = []
  # TODO: Write your code here
  bfs(0, 0, '', num, result)
  print('Result:', result)
  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
