from binarytree import  tree, bst, Node, build

a= tree (height=4, is_perfect=False)
print(a)

b = bst(height=3, is_perfect=True)
print(b)

c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
print(c)

d = build([7, 3, 11, None,5])
print(d)

