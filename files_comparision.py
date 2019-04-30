def text_files(file1, file2):
    file1_m = open(file1, 'r')
    file2_m = open(file2, 'r')
    num_lines1 = sum(1 for count1 in open(file1))
    num_lines2 = sum(1 for count2 in open(file2))
    for line1 in range(1, num_lines1+1):
        for line2 in range(1, num_lines2 + 1):
            line_text1 = file1_m.readline()
            line_text2 = file2_m.readline()
            if line_text1 == line_text2:
                print(end="")
            elif line_text1 != line_text2:
                try:
                    with open(file1) as f1: data = f1.readlines()
                    line_no = data.index(line_text1)
                    print("diff in line num: "+str(line_no+1)+" of file 1")
                except:
                    with open(file2) as f2: data = f2.readlines()
                    line_no1 = data.index(line_text2)
                    print("diff in line num: "+str(line_no1+1)+" of file 2")
                print(line_text1 + line_text2)
