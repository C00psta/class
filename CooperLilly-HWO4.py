#Cooper Lilly
#Lab Section 13
#Submission Date 11/12/24
#Sources, help given to/received from

def get_lines(filename):
    with open(filename, 'r') as input_file:
        line_list = []
        for line in input_file:
            line_list.append(line.strip())
        return line_list
    
def clear_or_create(filename):
    with open(filename, 'w') as input_file:
        pass

def add_string(filename, string):
    with open(filename, 'a') as f:
        if f.tell() == 0:
            f.write(string)
        else:
            f.write("\n" + string)

clear_or_create("out.txt")
lines = get_lines("prompt.txt")

for line in lines:
    assembled_string = ""
    pairs = line.split("\t")
    for pair in pairs:
        if pair != "":
            sp = pair.split(":")
            c = sp[0]
            a = sp[1]
            if c == "w":
                c = " "
            assembled_string += (c*int(a))
    add_string("out.txt", assembled_string)