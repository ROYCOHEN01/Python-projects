''' Exercise #5. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def rixum(file_name):
    f = open(file_name, 'r')
    lines = []
    for line in f:
        lines.append(line)
    numbers = str(lines).split()
    new=[]
    for word in numbers:
        d = "".join(c for c in word if c.isdigit())
        new.append(d)
    newsum = 0
    for elem in new:
        newsum = int(elem) + newsum
    f.close()
    return newsum


#########################################
# Question 2 - do not delete this comment
#########################################
def rickounter(f_document, f_rick_identifiers):
    f = open(f_document, 'r')
    g = open(f_rick_identifiers, 'r')
    r = f.read()
    d = {}
    for line in g:
        elem=str(line.rstrip())
        d[elem] = r.count(line.rstrip())
    f.close()
    g.close()
    print(d.items())
    return d

#########################################
# Question 3 - do not delete this comment
#########################################
def twin_pricks(num, out_file_name):
    if num <= 0:
        raise ValueError(f"Illegal value num={num}")
    else:
        try:
            f = open(out_file_name, 'w')
            count = 0
            c = 3
            new = []
            d = {}
            while num > count:
                for i in range(2, c):
                    if c % i == 0 or (c + 2) % i == 0:
                        break
                    elif c % i != 0 and (c + 2) % i != 0 and i == c - 1:
                        new.append(c)
                        new.append(c + 2)
                        d[c] = c + 2
                        count += 1
                        f.write(str(c) + ',' + str(c+2) + '\n')

                c += 1
            f.close()
        except IOError:
            raise ValueError(f'Could not write to {out_file_name}')



#########################################
# Question 4 - do not delete this comment
#########################################
def rickode(in_file):
    try:
        f = open(in_file, 'r')
        s = f.read()
        new_file =''
        f.close()
        for i in s:
            if i.isupper():
                if i == 'Z' or i == 'Y':
                    new_file = new_file + chr(ord(i) - 24)
                else:
                    new_file = new_file + chr(ord(i) + 2)
            elif i.islower():
                if i == 'z' or i == 'y':
                    new_file = new_file + chr(ord(i) - 24)
                else:
                    new_file = new_file + chr(ord(i) + 2)
            else:
                new_file = new_file + i
            newtitle = in_file[:-4] + '_decipherick.txt'
            t = open(newtitle, 'w')
            t.write(new_file)
            t.close()
    except IOError:
        raise ValueError(f'could not decipher {in_file} due to an IO Error')
    return newtitle

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    NO_EXC_MSG="Exception must be raised for this input (NOT pass)."
    WRONG_EXC_MSG="Wrong message in raised exception (NOT pass). \nExpected: {}\nGot: {}\n"
    NOT_PASS_MSG="Unexpected result (NOT pass.)"

    PASS_MSG="Got expected results (pass)."
    EXPECTED_EXC_MSG="Got corrent error and error message (pass)."
    

    print('==== Q1: Basic tests/output====')
    q1_input_file_name = "q1_input_1.txt"
    expected_result=137
    actual_result=rixum(q1_input_file_name)
    print("q1t1:", f'{PASS_MSG if expected_result==actual_result else NOT_PASS_MSG}')
    print("TBD: Write more tests here")
    
    print('==== Q2: Basic tests/output====')
    expected_result={'Hello_word9': 0, 'CoolRick11': 1, 'C-137': 2, 'c-132': 1, 'Z0Zo0': 1, 'TestMeRick123': 1}
    actual_result=rickounter("q2_f_document_1.txt", "q2_f_rick_identifiers_1.txt")
    print("q2t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: {expected_result}')
        print(f'Got: {actual_result}')

    print('==== Q3: Basic tests/output====')
    twin_pricks(4, "q3_output_1_res.txt")
    twin_pricks(20, "q3_output_2_res.txt")
    # Compare your output files with the correct output files

    try:
        num = 0
        twin_pricks(num, "q3_output_2_res.txt")  # this line should raise an exception
        print("q3t1", NO_EXC_MSG)
    except ValueError as ex:
        expected_result="Illegal value num={}".format(num)
        actual_result=ex.args[0]
        print(f'{EXPECTED_EXC_MSG if expected_result == actual_result else WRONG_EXC_MSG.format(expected_result , actual_result)}')

    print('==== Q4: Basic tests/output====')
    q4_input_file_name = "q4_input_1.txt"
    deciphered_text="There's a lesson here, and I'm not going to be the one to figure it out\n\nAnd...\n\nThere'Z a lesson here, and I'm not going to be the one to figure it out!!\n"
    with open(rickode(q4_input_file_name),'r') as f:
        print(f'{PASS_MSG if f.read() == deciphered_text else NOT_PASS_MSG}')



   

# ============================== END OF FILE =================================
