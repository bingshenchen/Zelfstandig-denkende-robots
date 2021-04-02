import sys
import randomit




afbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z']
Afbet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'U', 'W', 'X', 'Y', 'Z']

number = [i for i in range(-9,10)]
x = "zeae"

def isEng(n):
        if ((n in afbet )or (n in Afbet)):
                return True
        else:
                return False

def isupper(n):
        arr = []
        arror = []
        arrn = [i for i in n]
        l = len(n)
        for i in range(0, l):
                if arrn[i] in afbet:
                        arr.append(arrn[i])
                else :
                    arror.append(arrn[i])

        return len(arror)==0

def islarge(n):
        arr = []
        arror = []
        arrn = [i for i in n]
        l = len(n)
        for i in range(0, l):
                if arrn[i] in afbet:
                        arr.append(arrn[i])
                else :
                    arror.append(arrn[i])

        return len(arrn)==0


def isnumber(n):
        return n in [i for i in range(-99999,99999)]

def p(n):
	ti = 0
	mi = 1
	while(n>=0):
		n  = n - mi
		mi *= 2
		ti += 1
	return ti
      
def hi():
        arrinput = ["123"]
        while(True):
                prate = input("YOU:")
                arrinput.append(prate)
                if prate == "":
                        break
                elif prate =="123":
                        print(123)
                elif prate == "1":
                        print(isEng("a"))
                else:
                        prate = prate.replace("?","!")
                        prate = prate.replace("isnt","is")
                        prate = prate.replace("wasnt","was")
                        prate = prate.replace("bad","good")
                        print("Piqi:" + prate)
                        print(arrinput)

 
                
hi()
print(randomit.likeData("sd"))

