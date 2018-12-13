
srcfile1665NT = 'output1665wordlist_short.txt'
srcfile1819 = 'output1819wordlist_short.txt'

with open(srcfile1665NT) as file1, open(srcfile1819) as file2:
    for line_from_file_1_raw, line_from_file_2_raw in zip(file1, file2):
        #line_from_file_1_strip = line_from_file_1_raw.strip()
        #line_from_file_2_strip = line_from_file_2_raw.strip()
        print(line_from_file_1_raw.strip())
        print(line_from_file_2_raw.strip())
        print()

        #set1819 = set(line_from_file_1_raw.strip())

        #open1665NT = open(srcfile1665NT, "r")
        #list1665NTRaw = open1665NT.read()
        #list1665NT = list1665NTRaw.split()

#different = [x for x in set1819 if not x in list1665NT]

#print(different)



#with open(srcfile1665NT, 'r') as file1665NT:
    #filedata1665NT = file1665NT.read()
    
#with open(srcfile1819, 'r') as file1819:
#    for fileline1819 in file1819:
#        #filelineStrip = fileline().strip()
#        print('1819', fileline1819.strip())        
#        with open(srcfile1665NT, 'r') as file1665NT:
#            for fileline1665NT in file1665NT:
#                print('1665', fileline1665NT.strip())
