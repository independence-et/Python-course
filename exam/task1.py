__author__ = 'Independence'

file0 = open("yazkora.txt", "r")
file1 = file0.read()
file2 = file1.split('.')
file_ans = open("answer.txt", "w")
for i1 in range(len(file2)):
    file1_1 = str()
    file3 = file2[i1].split(' ')
    for i2 in range(len(file3) - 1):
        if '\n' in file3[i2]:
            file4 = file3[i2].split('\n')
            if file4[0][len(file4[0]) - 2:] == 'yo':
                file1_1 = file1_1 + file4[0].strip() + ' '
            if file4[1][len(file4[1]) - 2:] == 'yo':
                file1_1 = file1_1 + file4[1].strip() + ' '
        elif file3[i2][len(file3[i2]) - 2:] == 'yo':
            file1_1 = file1_1 + file3[i2].strip() + ' '
    file1_1 += '\n'
    file_ans.write(file1_1)
