from os.path import join
from glob import glob
tragic_path = join('tempdata', 'tragedies', '*')
tragic_filenames = glob(tragic_path)

for fname in tragic_filenames:
    # open the file to count the lines
    txtfile = open(fname, 'r')
    total_lines = 0
    for line in txtfile:
        total_lines += 1
    txtfile.close()    
    # print out the filename this one time, with the line count
    print(fname, "has", total_lines, "lines")
    # calculate the line from which to start printing text
    starting_line_num = total_lines - 5
    # reopen the file again
    txtfile = open(fname, 'r')
    for line_num in range(total_lines): 
        line = txtfile.readline()
        if line_num >= starting_line_num:
            # print the final lines
            the_line = str(line_num + 1) + ": " + line.strip()
            print(the_line) 
    txtfile.close()