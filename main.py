srcfile1665NT = 'output1665wordlist_short.txt'
srcfile1819 = 'output1819wordlist_short.txt'
output = 'output.txt'

with open(output, 'w') as clearfile:
	print('clearing ' + output + ' file')
with open(output,'a') as f:
    f.write('COMPARISON of 1665NT with 1819\n')
    f.write('Num@Ref@1665 Words@1819 Words@Notes\n')

with open(srcfile1665NT) as file1, open(srcfile1819) as file2:
    for i, (line_from_file_1_raw, line_from_file_2_raw) in enumerate(zip(file1, file2)):

        list1819 = line_from_file_1_raw.split()
        ref = list1819[0]
        list1819Pop = list1819.pop(0)
        set1819 = set(list1819)
        list1665NT = line_from_file_2_raw.split()
        list1665NTPop = list1665NT.pop(0)
        set1665NT = set(list1665NT)
        
        different1 = [x for x in list1665NT if not x in set1819]
        different2 = [x for x in list1819 if not x in set1665NT]
        
        different1String = ', '.join(different1)
        different2String = ', '.join(different2)
        
        if different1String != different2String:
            finalString = str(i)+'@'+str(ref)+'@'+str(different1String.strip())+'@'+str(different2String)+'@\n'
            with open(output,'a') as f:
                f.write(finalString)