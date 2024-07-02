''' Exercise #67. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def threebonacci_rec(n):
    if n < 3:
        return n
    return threebonacci_rec(n - 1) + threebonacci_rec(n - 2) + threebonacci_rec(n - 3)


#########################################
# Question 1.b - do not delete this comment
#########################################
def five_bonacci_mem(n, memo=None):
    if n < 5:
        return n
    if memo == None:
        memo = {}
    if n not in memo:
        memo[n] = five_bonacci_mem(n - 1, memo) + five_bonacci_mem(n - 2, memo) + five_bonacci_mem(n - 3, memo) + five_bonacci_mem(n - 4, memo) + five_bonacci_mem(n - 5, memo)
    return memo[n]


#########################################
# Question 2.a - do not delete this comment
#########################################
def climb_combinations(n):
    if n < 3:
        return n
    return climb_combinations(n - 1) + climb_combinations(n - 2)


#########################################
# Question 2.b - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n < 3:
        return n
    if memo == None:
        memo = {}
    if n not in memo:
        memo[n] = climb_combinations(n - 1) + climb_combinations(n - 2)
    return memo[n]


#########################################
# Question 3.a - do not delete this comment
#########################################
def catalan_rec(n):
    if n <= 1:
        return 1
    sum = 0
    for i in range(n):
        sum = sum + catalan_rec(i) * catalan_rec(n - i - 1)
    return sum


#########################################
# Question 3.b - do not delete this comment
#########################################
def catalan_memo(n, memo=None):
    if n <= 1:
        return 1
    if memo == None:
        memo = {}
    sum = 0
    if n not in memo:
        for i in range(n):
            memo[n] = catalan_rec(i) * catalan_rec(n - i - 1)
            sum = sum + memo[n]
    return sum


#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if len(lst) == 0:
        if n == 0:
            return 1
        elif n > 0:
            return 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    return find_num_changes_rec(n, lst[:-1]) + find_num_changes_rec(n - lst[-1], lst)
    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if len(lst) == 0:
        if n == 0:
            return 1
        elif n > 0:
            return 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo == None:
        memo = {}
    memo_key = find_num_changes_rec(n, lst[:-1]) + find_num_changes_rec(n - lst[-1], lst)
    if memo_key not in memo:
        memo[memo_key] = memo_key
    return memo[memo_key]



#########################################
# Question 5.a - do not delete this comment
#########################################
def isInTree(tree, val, idx=0):
    if idx in tree:
        if tree[idx] == val:
            return True
        elif tree[idx] > val:
            return isInTree(tree, val, idx * 2 + 1)
        elif tree[idx] < val:
            return isInTree(tree, val, idx * 2 + 2)
    else:
        return False

#########################################
# Question 5.b - do not delete this comment
#########################################
def create_sorted_binary_tree(lst, tree=None, idx=0):
    if len(lst) > 0 and tree is None:
        tree = {}
        tree[0] = lst[0]
    if len(lst) == 0:
        return tree
    if idx in tree:
        if lst[0] < tree[idx]:
            return create_sorted_binary_tree(lst ,tree , idx * 2 + 1)
        if lst[0] > tree[idx]:
            return create_sorted_binary_tree(lst ,tree ,idx * 2 + 2)
    else:
        tree[idx] = lst[0]
    return create_sorted_binary_tree(lst[1:] ,tree , 0)


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    

    print(threebonacci_rec(0) == 0)
    print(threebonacci_rec(5) == 11)
    print(threebonacci_rec(8) == 68)
    """
    #Question 1.b tests - you can and should add more
    """
    print(five_bonacci_mem(0) == 0)
    print(five_bonacci_mem(5) == 10)
    print(five_bonacci_mem(8) == 76)
    """
    #Question 2.a tests - you can and should add more
    """
    print(climb_combinations(4) == 5)
    """
    #Question 2.b tests - you can and should add more
    """
    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    """
    #Question 3.a tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    """
    #Question 3.b tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_memo(n) == res)
    """
    #Question 4.a tests - you can and should add more
    """
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)
    """
    #Question 4.b tests - you can and should add more
    """
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)
    """
    #Question 5.a tests - you can and should add more
    """
    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 11) == True)
    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 122121) == False)
    print(isInTree({0: 215, 1: 12, 4: 65, 9: 23}, 23) == True)
    """
    #Question 5.b tests - you can and should add more
    """
    print(create_sorted_binary_tree([2, 11, 5, 9, 8, 50, 10, 12, 1]) == {0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1})
    print(create_sorted_binary_tree([215, 12, 65, 23]) == {0: 215, 1: 12, 4: 65, 9: 23})
    print(create_sorted_binary_tree([1, 2, 66, 324, 3122]) == {0: 1, 2: 2, 6: 66, 14: 324, 30: 3122})
    pass
# ============================== END OF FILE =================================
