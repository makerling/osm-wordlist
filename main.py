##print('hello world')
srcfile1665NT = 'output1665wordlist_short.txt'
srcfile1819 = 'output1819wordlist_short.txt'

#with open(srcfile1665NT, 'r') as file1665NT:
    #filedata1665NT = file1665NT.read()
    
with open(srcfile1819, 'r') as file1819:
    for fileline1819 in file1819:
        #filelineStrip = fileline().strip()
        print('1819', fileline1819.strip())        
        with open(srcfile1665NT, 'r') as file1665NT:
            for fileline1665NT in file1665NT:
                print('1665', fileline1665NT.strip())
