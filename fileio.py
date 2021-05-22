# #             initially saved the file on desktop, hence this path
# jabber = open("C:\\Users\\rohit\\Desktop\\sample.txt",'r')  # ,'r' -> read only mode
# #             we add an extra "\" for the idea to interpret things correctly.
# #              \t, \n, \r etc are interpreted differently otherwise. that causes a problem.
# for line in jabber:
#     print(line)
# jabber.close()


#now copied the file in this project directory, so:
# jabber = open("sample.txt",'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end = "")
# jabber2.close()


# with open("sample.txt","r") as jabber:  # we don't need to close the file now
#     for line in jabber:                 # "with" takes care of that.
#         if "JAB" in line.upper():
#             print(line, end="")


# with open("sample.txt","r") as jabber:
#     line = jabber.readline()        #     ".readline" reads the file line by line
#     while line:
#         print(line,end = '')
#         line = jabber.readline()


with open("sample.txt","r") as jabber:
    lines = jabber.readlines()         #  ".readlines" reads all the lines in the text at once.
    #  *** IMPORTANT - It will return a LIST  of all the lines *****
print(lines,end = '')
print("\n"+ "="*45)

for line in lines:
    print(line,end="")
print("\n"+ "="*45)

for line in lines[::-1]:       # printing the lines of poem in reverse order, from readlines
    print(line,end="")         # this shows that "lines" from "readlines" was actually a list.
print("\n"+ "="*45)

with open("sample.txt","r") as jabber:
    lines = jabber.read()   # "Read" reads the whole file as a string in ONE single go.
    print(lines, end="\n")# NOTICE THE DIFFERENCE IN "READ" AND "READLINES"
print("\n"+ "*"*80)


for line in lines[::-1]:       # everything in reverse
    print(line,end="")         #
print("\n"+ "="*45)
