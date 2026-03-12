#How to work with texts - "strings"
name = "Sally"
print(name)

#Playing with positions
print(name[0]) #0 is the firs position of the string, which is the letter "S"
print(name[1]) #1 is the second position of the string, which is the letter "a"
print(name[2]) #2 is the third position of the string, which is the letter "l"
print(name[3]) #3 is the fourth position of the string, which is the letter
print(name[4]) #4 is the fifth position of the string, which is the letter "y"

#Put positions together
print(name[1:4])
print(name[0:3])

#Working with longer texts and breaking them into different lines
sentence = "I am learning Python programming language, \n since I am studying IT."
print(sentence)

#Breaking texts with quotation marks
sentence = """\"I am learning Python
programming language,
since I am studying IT.\""""
print(sentence)

#Another way to use quotation marks
sentence = '"I am learning Python programming language, since I am studying IT."'
print(sentence)

#Now breaking lines
sentence = '''
"I am learning Python programming language, 
since I am studying IT."'''
print(sentence)