''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def least_popular_characters(my_string):
    charcounter = {}
    for char in my_string:
        charcounter[char]=charcounter.get(char , 0) + 1
    sortedchar = sorted(charcounter, key=charcounter.get)
    count=charcounter.get(sortedchar[0])
    d=[] # לראות אם אפשר לעשות במילון
    for char in charcounter:
        if charcounter.get(char) == charcounter.get(sortedchar[0]):
            d.append(char)
    newlist=" ".join(sorted(d))#לא מימשתי את הצעד שאמרו לאסוף לפי סדר
    return newlist


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_sparse_matrices(lst):
    newmach = {}
    mach = lst[0]
    for d in range(1,len(lst)):
        for i in lst[d]:
            if i in mach:
                mach[i] = mach[i] * lst[d].get(i)
                newmach[i] = mach[i]
    return newmach


#########################################
# Question 3 - do not delete this comment
#########################################
def fill_substring_dict(s, d, k):
    new={}
    for key in d.keys():
        if len(key) <= k:
            for i in range(0,len(s)):
                if s[i:len(s)].find(key) == 0:
                    d[key].append(i)
    return d


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    dt={}
    for elem in tuples_lst:
        if elem[0].lower() not in dt.keys():
            dt[elem[0].lower()] = [elem[1].lower()]
        else:
            dt[elem[0].lower()].append(elem[1].lower())
    return dt


def num_courses_per_student(stud_dict):
    for course in stud_dict:
        stud_dict[course] = len(stud_dict[course])
    return stud_dict

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__':  # Do not delete this line!
    # Q1
    print(least_popular_characters('aabbAA') == 'A a b')

    # Q2
    print(mult_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): 12})

    # Q3
    print(fill_substring_dict('TTAATTAGGCGCTA', {'TA': [], 'G': [], 'K': [], 'TTAA': [], 'tat': [], 'TTA': []}, 3) == {
        'TA': [1, 5, 12], 'G': [7, 8, 10], 'K': [], 'TTAA': [], 'tat': [], 'TTA': [0, 4]})

    # Q4
    stud_dict = courses_per_student(
        [('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])

    print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})

    num_courses_per_student(stud_dict)
    print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

