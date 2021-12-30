q1 = """who developed the python language?
a)gudio van rossum
b)dennis ritchie
c)larry page
d)ken"""
q2 = """which type of programming does python support?
a)object-oriented programming
b)structured programming
c)functional programming
d)all of the mentioned"""
q3 = """Is python case sensitive when dealing with indentifiers?
a)no
b)yes
c)machine department
d)none of the mentioned"""
q4 = """which of the is correct extension of the python file?
a).python
b).pl
c).py
d).p"""
q5 = """Is python code compiled or interpreted?
a)python code is both compiler and interpreted
b)python code is neither compiled nor interpreted
c)python code is only compiled
d)python code is only interpreted"""

questions = {q1:"a",q2:"d",q3:"a",q4:"c",q5:"b"}

name = input("enter your name:")
print("hello",name,"welcome to the master minds")

for i in questions:
    print(i)
    ans = input("enter the answers (a/b/c/d) :")
    if ans==questions[i]:
        print("correct answer,you got 1 point")
        score = ('score+1')
    else:
        print("wrong answer,you lost 1 point")
        score = ('score-1')

print("good try",name)
print("keep on try")
print("closing")

