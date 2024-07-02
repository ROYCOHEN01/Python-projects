''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def mult_residuals_of_k(lst, k):
    SUM = 1.0
    for element in lst:
        if element % k != 0:
            SUM= SUM * (element % k)
    return SUM


#########################################
# Question 2 - do not delete this comment
#########################################
def sum_even_digits(n):
    new_sum=0
    n=int(n)
    while n/10 > 0:
        i = n%10
        if i%2 == 0:
            new_sum=new_sum+i
        n = int(n/10)
    return new_sum



#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    s = str.upper(s)
    c = str.upper(c)
    k = s.count(c)
    if k == 0:
        return k
    else:

        while (c * k) not in s:
            k = k-1
        return k


#########################################
# Question 4 - do not delete this comment
#########################################
def lower_strings(lst):
    if type(lst) != list:
        return int(-1)
    else:
        for i in range(0,len(lst)):
            if type(lst[i]) == str:
                lst[i] = lst[i].lower()

#########################################
# Question 5 - do not delete this comment
#########################################
def mult_mat_by_scalar(mat, alpha):
    alpha = int(alpha)
    mat2 = []
    for i in range(0, len(mat)):
        elem = []
        for j in range(0, len(mat[i])):
            elem.append(mat[i][j] * alpha)
        mat2.append(elem)
    return mat2


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    mat5=[]
    column = len(mat[0])
    for i in range(0, column):
        elem=[]
        for j in range(0, len(mat)):
            elem.append(mat[j][i])
        mat5.append(elem)

    return mat5


    
#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == '__main__':  # Do not delete this line!
    print(mult_residuals_of_k([3, 6, 4, 11, 9], 3) == 2.0 )
    print(mult_residuals_of_k([45.5, 60, 74, 48], 4) == 3.0)


    print(sum_even_digits(5638) == 14)
    print(sum_even_digits(137) == 0)
    print(sum_even_digits(54984127) == 18)
    print(sum_even_digits(6) == 6)


    print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
    print(count_longest_repetition('cccccc','c') == 6)
    print(count_longest_repetition('abcde', 'z') == 0)


    vals = [11, 'Rick137', 3.14, 'moRTy']
    result=lower_strings(vals)
    print(vals == [11, 'rick137', 3.14, 'morty'])
    print(result == None)

    vals = [-5, None, True, [1, 'dont change me', 3]]
    lower_strings(vals)
    print(vals == [-5, None, True, [1, 'dont change me', 3]])

    print(lower_strings(42) == -1)
    print(lower_strings('im not a list') == -1)
    print(lower_strings(False) == -1)


    mat1 = [[2, 5], [6, 9]]
    mat2 = mult_mat_by_scalar(mat1, 2)
    print(mat1 == [[2, 5], [6, 9]])
    print(mat2 == [[4, 10], [12, 18]])

    print(mult_mat_by_scalar([[10,15], [-3,6]], -5) == [[-50, -75], [15, -30]])


    mat = [[1,2],[3,4],[5,6]]
    mat_T = mat_transpose(mat)
    print(mat == [[1, 2], [3, 4], [5, 6]])
    print(mat_T == [[1, 3, 5], [2, 4, 6]])

    mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    mat2_T = mat_transpose(mat2)
    print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])


# ============================== END OF FILE =================================
