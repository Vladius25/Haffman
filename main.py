from collections import Counter
import heapq
import pickle
import __hello__


class Forest:
    def __init__(self, weight=-1, root=-1):
        self.weight = weight
        self.root = root

    def __repr__(self):
        return "({}, {})".format(self.weight, self.root)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight


class Tree:
    def __init__(self, left=-1, right=-1, parent=-1):
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return "({}, {}, {})".format(self.left, self.right, self.parent)


def get_min():
    return heapq.heappop(forest), heapq.heappop(forest)


def make_tree():
    while len(forest) > 1:
        left, right = get_min()
        root = len(tree)
        heapq.heappush(forest, Forest(left.weight + right.weight, root))
        tree.append(Tree(left.root, right.root, -1))
        tree[left.root].parent = tree[right.root].parent = root


def make_codes(root, code=''):
    left, right = tree[root].left, tree[root].right
    if -1 in (right, left):
        codes[roots[root]] = code
        return
    make_codes(left, code + '0')
    make_codes(right, code + '1')


def make_binstring():
    str = ''
    for ch in input:
        str += codes[ch]
    return str


def encode():
    pickle.dump(tree, f2)

    output = make_binstring()
    #f2.write(bytes(int(output[i: i + 8], 2) for i in range(0, len(output), 8)))


# def encode2():
#     write_tree()
#
#     sym, length = 0, 0
#     bytes_list = []
#     for ch in input:
#         for bit in codes[ch]:
#             sym = (sym << 1) + int(bit)
#             length += 1
#             if length == 8:
#                 bytes_list.append(sym)
#                 sym, length = 0, 0
#     if(length < 8):
#         bytes_list.append(sym)
#     f2.write(bytes(bytes_list))



if __name__ == "__main__":
    f1 = open("input.txt", "rb")
    f2 = open("input.rar", "wb")
    # f1.write('a'*12+'b'*40+'c'*15+'d'*8+'e'*25)

    forest, roots, codes = [], {}, {}

    input = f1.read()
    vals = Counter(sorted(input)).items()
    for root, syms in enumerate(vals):
        forest.append(Forest(weight=syms[1], root=root))
        roots[root] = syms[0]

    tree = [Tree() for _ in range(len(forest))]
    heapq.heapify(forest)

    make_tree()
    make_codes(len(tree) - 1)
    encode()

