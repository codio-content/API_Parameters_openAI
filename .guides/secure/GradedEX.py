import os
import subprocess
import sys

sys.path.append('/usr/share/codio/assessments')
from lib.grade import send_partial_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT



# opens files , creates flag, and empty list
f = open("ktest1.py", "r")
flag=0
respline=[]
#using flag we look for everthing with completion.create
for x in f:
  if "Completion.create" in x:
    flag=1
  if ")" in x and flag ==1:
    flag=2
  if flag>0:
    respline.append(x.strip()) # remove white spaces
  if flag==2:
    flag=0
#print (respline)
f.close()

feedback=''
global points 
points = 100

#use the following lines to only have the argument in the string
respline=' '.join(respline)
firstP=respline.find('(')
lastP=respline.rfind(')')
respline=respline[firstP+1:lastP]
d=dict(x.split("=") for x in respline.split(","))
print(d)
total=5
for a,b in d.items():
  if "temperature" in a:
    if int(b)!=1:
      total-=1
      feedback+="Please check your randomness variable"
  if "max_tokens" in a:
    if int(b)!=25:
      total-=1
      feedback+="Completion token limit should be set 25"
  if "best_of" in a:
    if int(b)!= 6:
      total-=1
      feedback+="Generate 6 responses and pick the best among them"


# this can check for right values associated with arguments
def check_variable1():
  if total !=5:
    return False
  return True 

# this makes sure they are using the right number of arguments
def check_variable2():
  global feedback
  if len(d) > 5 :
   feedback+=" Do not include any argument that are not necessary to the requirements"
   return False
  if len(d) < 5:
    feedback+=" You are missing some arguments"
    return False 
  return True

# this is not needed for chapter 3 here but here is a function to test the count of  a certain word 
# put the word needed  in the word variable. and change the count . for the example it is set to 3 

def check_variable_counter():
  global feedback
  try: 
    import ktest1 
    return True
  except:
    feedback+="Please make sure your code is not generating any error before submission"
    return False

# you can check add additional check by copy and pasting other check_variable fucntion just add another number and we can 
# please note we start points at 100 and remove points from there  base on the function that came out false. 
if not check_variable1():
  points -= 30
  feedback+= ("<h2>Test did not pass</h2>")
  
  
if not check_variable2():
  points -= 30
  feedback+=("<h2>Test did not pass</h2>")
 
  
# this is not needed for chapter 3 here but here is a function to test the count of  a certain word 
# put the word needed  in the word variable. and change the count . for the example it is set to 3 

if not check_variable_counter():
  points -= 40
  feedback+=("<h2>Test did not pass</h2>")
  feedback+=('Please make sure to fix code')  
  


# partial point last part 
if feedback == "":
  feedback = "<h2>Test passed</h2>"
res = send_partial_v2(points, feedback, FORMAT_V2_HTML)
exit(0 if res else 1)

''' non partial point last part
if check_variable1(contents) and check_variable2(contents) :
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)
'''