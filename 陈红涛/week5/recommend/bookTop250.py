fixed = open('./top250Book_comments.txt', 'w', encoding='utf-8')
lines = [line for line in open('./doubanbook_top250_comments.txt', 'r', encoding='utf-8')]
num = 0;
for (i, line) in enumerate(lines):

    if i == 0:
        fixed.write(line)
        prev_line = ""
        continue
    terms = line.split('\t')
    
    if terms[0] == prev_line.split('\t')[0]:

        if len(prev_line.split('\t')) == 6:
            fixed.write(prev_line + '\n')
            prev_line = line.strip()
        else:
            
            prev_line = ""
    else:
        if len(terms) == 6:
            
            num+=1
            prev_line = line.strip()
        else:
            prev_line += line.strip()
print(num)
fixed.close()