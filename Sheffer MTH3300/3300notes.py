from math import *


def p(x, y=None, z=None): #print shortcut
    if y is None and z is None:
        print(x)
    elif z is None:
        print(x, y)
    else:
        print(x, y, z)

def convertKtoF():
    print("This program will receive a Kelvin value and convert it to Fahrenheit.")
    k=int(input("Please input a Kelvins to be converted to Fahreneheit: "))
    f=((k-273.15) * 9/5 + 32)
    print("The equivalent Fahrenheit value for ", k, " Kelvins is ", f, " degrees.")

def banana(x,y): #returns 
    x=y+1 
    y=x-1
    x=x
    return (x+y-1)
def coconut(x,y):
    x=x+y
    y=x-y 
    x=x-y
    return x
def papaya(a,b,c): 
    c=coconut(a,b) 
    b=banana(a,c) 
    return (b+c)/3

def printAsterisks(n):
    for i in range(1, n+1):
        num_asterisks = i
        num_spaces = n - i
        print(" " * num_spaces + "*" * num_asterisks)
    for i in range(n-1, 0, -1):
        num_asterisks = i
        num_spaces = n - i
        print(" " * num_spaces + "*" * num_asterisks)
        
def calcSum(n):
    if n % 2 == 0:
        sign = -1
    else:
        sign = 1
    result = 0
    factorial = 1
    for i in range(1, n+1):
        result += sign
        sign *= -1
        factorial *= i
        denominator = factorial
        if i % 2 == 0:
            denominator *= -1
        result += (sign * 1) / denominator
    return result

def isPrime(posInt):
    if posInt<1:
        return False
    for i in range(2,posInt):
        if (posInt%i == 0):
            return False
    return True
            
def sumOf2Primes(intOver2):
    for i in range(2,intOver2):
        if isPrime(i) and isPrime(intOver2-i) == True:
            print(intOver2 , " = " , i , " + " , intOver2-i)
            break

def prime3Combos(n):
    count=0
    for i in range (2,n):
        a=i
        for i in range (2, n):
            b=i 
            c=n-a-b
            if (c>1 and isPrime(a) and isPrime(b) and isPrime(c)):
                count=count+1
                print(a,b,c)
    return count

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fib(n): #another way of getting it
    if type(n)!=int or n<0:
        return "invalid"
    elif n==0 or n==1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1): #or (n-1)
            c = a + b
            a = b
            b = c
        return b

def dist(x1,y1,x2,y2):
    distx = (x1-x2)
    disty = (y1-y2)
    distance = sqrt((distx)**2+(disty)**2)
    return distance

def circleArea(centerx,centery,pointx,pointy):
    radius = dist(centerx,centery,pointx,pointy)
    area = pi * radius ** 2
    return area

def isPower(x,p):
    for i in range(x):
        print(p**i)
        if p**i == x:
            return True
    return False

def textEditor():
    print("Type 'done' to end the program")
    n = input("> ")
    while n != "done":
        n = input("> ")
        
def isPrime(posInt):
    if posInt<1:
        return False
    for i in range(2,posInt):
        if (posInt%i == 0):
            return False
    return True

def factorial(n):
    total = 1
    for i in range(n):
        print("(",n, " * ", i+1,")"," + " )
        total *= (n-i)
    return print("=",total)
        
def factorialWhile(n):#####NOT DONE
    x=1
    while total<n:
        total = total*(n)
        x=x-n
    return total
        
import time

def collatz(n):
    while n>0:
        print(n)
        if n%2==0:
            n=n/2
        elif n%2!=0:
            n=3*n+1
        time.sleep(.5)
    return n
            
def counter(n):
    x=0
    while n!=0:
        x=x+1
        n=int(n/10)
    return x
        
def threes(n):
    counter=0
    while n>0:
        if n%10==3:
            counter+=1
            n=int(n/10)
    return counter


def contains_x(text):
    for i in range(len(text)):
        if text[i]=="x":
            return True
    return False

def containsX(text):
    for char in text:
        if char == "x":
            return True
    return False

def contains_x_quant(text,ch):
    times = 0
    for char in text:
        if char == ch:
            times += 1
    return times

def firstWord(text):
    sent = ""
    for char in text:
        if char != " ":
            sent += char
        else: break
    return sent

def first_word(text):
    sent = ""
    for char in text:
        if char == " ":
            return sent
        sent += char            

# a 'slice' is a continuous/consec=utive subsequence of a string

def first_slice(text):
    for i in range(len(text)):
        if text[i] == " ":
           return text[:i]
       
def isPalindrome(text):
    for i in range(len(text)):
        if text[i]!=text[len(text)-1-i]:
            return False
    return True

# text[-1] means the last char in string
# method written as variable.method() like fruit.upper() or find()
    
def isReverse(w1,w2):
        if len(w1) != len(w2):
            return False
        i = 0
        j = len(w2)-1
        while j>=0:
            if w1[i]!= w2[j]:
                return False
            i+=1
            j-=1
        return True
    
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True
    
def any_lowercase1(s): #checks if first letter in s are lowercase
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s): #checks if literal "c" is lowercase, and thats it
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
def any_lowercase3(s): #checks if last letter is lowercase
    for c in s:
        flag = c.islower() #loop does not localize variable inside of it
    return flag

def any_lowercase4(s): #####
    flag = False
    for c in s:
        flag = flag or c.islower() ##didnt know you could do or in assignment
    return flag

def any_lowercase5(s): #checks if all lowercase letters (no characters or spaces)
    for c in s:
        if not c.islower():
            return False
    return True

def ceaserCrypto(text): #.isalpha() checks if letter
    newtext = ''
    for ch in text:
        if ch == 'y' or ch == 'z':
            newtext += chr(ord(ch)-24)
        elif ch == ' ' or ch == '.' or ch == '(' or ch == ')':
            newtext += ch            
        elif ch != ' ' or ch != '.':
            newtext += chr(ord(ch)+2)
    print(newtext)
            
def tenthword(sentence):
    tenth = ""
    spaces = 0
    for ch in sentence:
        if ch == " ":
            spaces += 1
        if spaces == 9:
            if ch != " ":
                tenth += ch
    if spaces <= 9:
        return tenth
    else:
        return "Not enough words!"

#print(tenthword("one two three four five six seven eight ni ne ten"))

def rsa(text):
    decrypt = ""
    for ch in text:
        if ch == 'e' or ch == 'w' or ch == 'l':
            decrypt += ch
        else:
            decrypt += chr((pow(ord(ch),19)%201))
    return decrypt
            
#print(rsa("h:a°vÅvha]eÅ3%ÅuÅ­hei]ÅDWÅwi­hÅBa°a°av¦"))
#print(rsa('Di¾ÅÇuÅY°uw¥Å6u:a­uevÅha²eÅ:u]eÅde°evÅ­ha°Åh:a°v'))

def password():
    print("\nYour password must include at least one lowercase and uppercase letters, six characters minimum, no '$', and 3 or fewer digits.\n")
    pWord = (input('ENTER: '))
    pLower = False
    pUpper = False
    pChars = 0
    pMoneySign = False
    pDigits = 0
    def error():
        print("\nTry again by meeting the conditions.\n")
    for ch in pWord:
        char = ch
        if char.islower() == True:
            pLower = True
        elif char.isupper() == True:
            pUpper = True
        elif char == '$':
            pMoneySign = True
        elif char in '01234567889':
            pDigits += 1
        pChars +=1 
    if pLower == False:
        return error()
    elif pUpper == False:
        return error()
    elif pChars < 6:
        return error()
    elif pMoneySign == True:
        return error()
    elif pDigits < 3:
        return error()       
    print("Password Accepted!!")
    
#password() #doesnt say anything about char == " "

words = open("words.txt")
def firstwords():
    for text in words:
        text = text.strip()
        if len(text)>=20:
            print(text)

def notLetter(letter):
    for ch in words:
        if letter not in ch:
            ch = ch.strip()
            print(ch.strip())
        
def not_Letter(letter):
    for text in words:
        text = text.strip()
        flag = False
        for char in text:
            if char == letter:
                flag = True
            if not flag:
                print(text)

def percentLetter(letter):
    letterCount = 0
    totalCount = 0
    for ch in words:
        totalCount += 1
        if letter not in ch:
            ch = ch.strip()
            letterCount += 1
    for total in words:
        totalCount += 1
    print(((letterCount/totalCount)*100),"%")
    
def sameLetters(letters):
    for word in words:
        flag = True
        word.strip()
        for ch in letters:
            if not ch in word:
                flag = False
        if flag:
            print(word)

def occurrence(finder,pointer):
    Occurrences = []
    counter = 0
    for k in range(len(finder)):
        if finder[k] == pointer:
            Occurrences.append(finder.find(pointer,counter))
        #print(finder[k])
        counter += 1
    print(f"The positions of '{pointer}' in '{finder}' are ",end="")
    for l in range(len(Occurrences)):
        print(Occurrences[l],end="  ")
        
def isAlpha(specialch):
    chars = ''
    for line in specialch:
        for ch in line:
            if ord(ch) >= 65 and ord(ch) <= 122 and not (ord(ch) >= 91 and ord(ch) <= 96):
                chars += ch
    print(chars)
   
    
  
def candles(): #REWATCH ON THE ZOOM!
    letters = open('specials.txt') 
    word = ''
    for line in letters:
        for i in range(4,len(line)-4):
            before = line[i-3:i]
            after = line[i+1:i+4]
            if line[i].islower() and before.isupper() and after.isupper():
                word += line[i]
    print(word)
            
def recursiveFactorial(n):
    if n == 1:
        return 1
    return n * recursiveFactorial(n-1)

def recursiveSum(n):
    if n == 1:
        return n
    sum = n + (n-1)
    return n + recursiveSum(n-1)   

def recursiveDigits(n):
    if n < 10:
        return 1
    return 1 + recursiveDigits(n//10)

def recursiveDigitSum(n):
    if n < 10:
        return n
    return n%10 + recursiveDigitSum(n//10)

def recursiveCollatz(n):
    print(n)
    if n != 1:
        if n!=1:
            if n%2==0:
                recursiveCollatz(int(n/2))
            else:
                recursiveCollatz(3*n+1)
                    
def secondCypher(text):
    decrypt = ''
    thisNum = ''
    for ch in range(len(text)):
        if ch == 0 and ch not in (' ','\n',','):
            thisNum += text[ch]
            print(ch)
        elif (text[ch-1] in (' ','\n',',')) and (text[ch] not in (' ','\n',',')):
            thisNum += text[ch]
            print(ch)
        if ch in (' ','\n',','):
            decrypt += thisNum
            return decrypt
        
def findLineOfWord():
    cervantes = open('Cervantes.txt',errors='ignore')
    word = input(str("Enter the word who's line # you would like to find: "))
    count = 0
    for line in cervantes:
        count += 1
        if word in line:
            print(count)
            return 0
    print(-1)
#findLineOfWord()

def firstLetter(n):
    declaration = open('declaration.txt',errors='ignore')
    wordCount = 0
    isWord = False
    nthWord = ''
    for line in declaration:
        for ch in line:
            if isWord == False:
                if ch not in (' ','\n',','):
                    isWord = True
                    wordCount += 1
            elif isWord == True:
                if ch in (' ','\n',','):
                    isWord = False
            if wordCount == n:
                nthWord += ch.lower()    
    return nthWord[0]
#print(firstLetter(72)) #72nd word is 'We'

def secondCypher(text):
    decrypt = ''
    thisNum = ''
    for ch in text:
        if ch not in (' ', '\n', ',') and ch.isnumeric():
            thisNum += ch
        if ch in (' ', '\n', ','):
            if thisNum:
                decrypt += firstLetter(int(thisNum))
                thisNum = ''
    if thisNum:
        decrypt += firstLetter(int(thisNum))
    return decrypt
#print(secondCypher('115, 73, 24, 807, 37, 52, 49, 17, 31, 62, 647, 22, 7, 15,'))
        
def calculator():
    ops = '+,*,-,/,//,%,**'

    try:
        val1 = int(input("Enter val 1: "))
    except ValueError:
        print("Must be an integer.")
        return

    try:
        op = input("Enter +, *, -, /, //, %, **: ")
    except ValueError:
        print("Error")
        return

    try:
        val2 = int(input("Enter val 2: "))
    except ValueError:
        print("Error: Please enter a valid integer for val 2.")
        return

    result = None

    if op in ops:
        if op == '+':
            result = val1 + val2
        elif op == '*':
            result = val1 * val2
        elif op == '-':
            result = val1 - val2
        elif op == '/':
            result = val1 / val2
        elif op == '//':
            result = val1 // val2
        elif op == '%':
            result = val1 % val2
        elif op == '**':
            result = val1 ** val2
        print(f"{val1} {op} {val2} = {result}")
    else:
        print("Invalid operator. Please use one of the following: +, *, -, /, //, %, **")
#calculator()

def listsDouble():
    nums = [1,2,3,4,5]
    for i in range(len(nums)):
        nums[i] *= 2
        
def listsSum():
    nums = [1,2,3,4,5]
    return sum(nums)

import urllib.request


    
def square_info(side_length):

    perimeter = 4 * side_length
    area = side_length ** 2
    answer = (perimeter, area)
    return answer

def fn(*args):
    counter = 0
    total = 0
    for num in args:
        total += num
        counter+= 1
    return total/counter

def fnz(*args):
    first, second, *third, fifth = args
    print(third)
       
from random import *
    
    
def randomz(*args):
    t = []
    for s in args:
        t.append((randint(1,100),s))
    answer = []
    t.sort()
    for (a,b) in t:
        answer.append(b)
    return answer
        

        
t = (1,2,3,4)

first, *secondthird, fourth = t

print(secondthird)
        
        
        
        
        
        
        
        
        


    