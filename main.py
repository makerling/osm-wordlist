import unicodedata
import re

srcfile1665NT = 'output1665wordlist.txt'
srcfile1819 = 'output1819wordlist.txt'
srcfileExclude = 'master_exclude_list_1665-1819.txt'
output = 'output.txt'
log = 'log.log'

with open(output, 'w') as clearfile:
	print('clearing ' + output + ' file')
with open(output,'a') as f:
    f.write('COMPARISON of 1665NT with 1819\n')
    f.write('Num@Ref@1665 Words@1819 Words@Notes\n')

with open(srcfile1665NT) as file1, open(srcfile1819) as file2:
    for i, (line_from_file_1_raw, line_from_file_2_raw) in enumerate(zip(file1, file2)):

        f1 = open(srcfileExclude, "r") 
        file1_raw = f1.read() 
        #file1_lowercase = file1_raw.lower()
        #file1_normalized = unicodedata.normalize('NFD',file1_lowercase)
        #shaved = ''.join(c for c in file1_normalized if not unicodedata.combining(c))
        #final = unicodedata.normalize('NFC', shaved)
        file1_words = file1_raw.split()
        file1_set = set(file1_words)

        #line_from_file_1_raw_lowercase = line_from_file_1_raw.lower()
        #line_from_file_1_raw_normalized = unicodedata.normalize('NFD',line_from_file_1_raw_lowercase)
        #shaved = ''.join(c for c in line_from_file_1_raw_normalized if not unicodedata.combining(c))
        #final = unicodedata.normalize('NFC', shaved)        
        list1819 = line_from_file_1_raw.split()
        ref = list1819[0]
        list1819Pop = list1819.pop(0)
        set1819 = set(list1819)
        #line_from_file_2_raw_lowercase = line_from_file_2_raw.lower() 
        #line_from_file_2_raw_normalized = unicodedata.normalize('NFD',line_from_file_2_raw_lowercase) 
        #shaved = ''.join(c for c in line_from_file_2_raw_normalized if not unicodedata.combining(c))
        #final = unicodedata.normalize('NFC', shaved)         
        list1665NT = line_from_file_2_raw.split()
        list1665NTPop = list1665NT.pop(0)
        set1665NT = set(list1665NT)
        
        print (set1665NT)
        print (set1819)
        
        different1beforeExclude = [x for x in list1665NT if not x in set1819]
        different1 = [x for x in different1beforeExclude if not x in file1_set]
        
        different2beforeExclude = [x for x in list1819 if not x in set1665NT]
        different2 = [x for x in different2beforeExclude if not x in file1_set]
        
        different1String = ', '.join(different1)
        different1StringStripped = re.sub(r'[A-ZÂÇÎİȮÖÛÜĖĠŞ\-][^,]+?\b', '', different1String)
        print(different1String)
        print(different1StringStripped)        
        
        different2String = ', '.join(different2)
        different2StringStripped = re.sub(r'[A-ZÂÇÎİȮÖÛÜĖĠŞ\-][^,]+?\b', '', different2String)        
     
        if different1String != different2String:
            finalString = str(i)+'@'+str(ref)+'@'+str(different1StringStripped.strip())+'@'+str(different2StringStripped)+'@\n'
            #finalString = str(i)+'@'+str(ref)+'@'+str(different1String.strip())+'@'+str(different2String)+'@\n'            
            checkContainsAlpha = re.search('[a-z]',finalString)
            if checkContainsAlpha:
                checkContainsAlphaStripped = re.sub(r'(, , , )|(@, , )|(@ ,)|(@\ʿ )|(, , @)|(, @)|(@ʿ, )|(@, )|(, , )', '@', finalString)
                with open(output,'a') as f:
                    f.write(checkContainsAlphaStripped)
                with open(log,'a') as f:                    
                    f.write(str(set1665NT))
                    f.write(str(set1819))                    
                    f.write(str(different1String))                    
                    f.write(str(different1StringStripped))                    
        print (i)
print('done')


#for all words in list that begin with capital letter
 #   if not exist in the other project list
  #      if exist with case ignore
   #         make element lowercase