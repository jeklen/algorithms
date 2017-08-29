### 用非迭代的方式来遍历BST，得到的是非降序排列的
```
def inorder_tree_walk(x):
    if x:
        inorder_tree_walk(x.left)
        print x.key
        inorder_tree_walk(x.right)
```

### TREE_SEARCH
```
def tree_search(x, k):
    if x == NIL or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

```

### 用while循环来展开循环，用一种迭代的方式重写这个过程
```
def iterative_tree_search(x, k):
    while x != NIL and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
```

### Minimum and Maximum
```
def tree_minimum(x):
    while x.left != NIL:
        x = x.left
    return x
    
def tree_maximum(x):
    while x.right != NIL:
        x = x.right
    return x
```
