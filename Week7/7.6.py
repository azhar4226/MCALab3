def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()
    
def write_file(filename,lines):
    with open(filename,'w') as file:
        file.writelines(lines)

def swap_lines(file1,file2):
    lines_file1=read_file(file1)
    lines_file2=read_file(file2)

    if len(lines_file1) % 2 == 0 :
        print("The first file must have an odd number of lines.")
        return
    
    mid_index=len(lines_file1) // 2 
    last_index=len(lines_file2) -1

    (lines_file1[mid_index], lines_file2[last_index] )= (lines_file2[last_index], lines_file1[mid_index])

    write_file(file1,lines_file1)
    write_file(file2,lines_file2)


file1="/Users/apple/Downloads/MCALab3/Week7/file1.txt"
file2="/Users/apple/Downloads/MCALab3/Week7/file2.txt"

swap_lines(file1, file2)