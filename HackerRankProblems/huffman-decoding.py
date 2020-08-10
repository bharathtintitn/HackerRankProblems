import Queue

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()
    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT

def _decodeHuff(root, s, length, i, result):
	#Enter Your Code Here
    if not root:
        return True
    if length > len(s):
        return False

    if s[i] == '1':
        if _decodeHuff(root.right, s, length, i+1, result):
            return result + root.data
    else:
        if _decodeHuff(root.left, s, length, i+1, result):
            return result + root.data

def decodeHuff(root, s):
    import pdb
    pdb.set_trace()
    return _decodeHuff(root, s, len(s), 0, "")

ip = raw_input()
freq = {}#maps each character to its frequency

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object
dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
