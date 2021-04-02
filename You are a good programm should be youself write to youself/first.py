def a0():
    writefile.write("""
filename = input()
writefile = open(filename, "w")
savefile = open(filename, "a")
            """)


def a1():
    writefile.write("""
def a1():
    writefile.write()
        """)


def a2():
    savefile.write("""
def a2():
    savefile.write()
        """)


filename = input()
openfile = open("first.py", "r")
writefile = open(filename, "w")
savefile = open("twee.py", "a")

# writefile.write("")
# writefile.close()

# for i in openfile:
#    print(i)
print(openfile.readline(2))

a0()
a1()
a2()


writefile.close()
savefile.close()
