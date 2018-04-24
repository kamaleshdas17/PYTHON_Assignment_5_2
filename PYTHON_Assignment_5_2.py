## Implement a Python program to generate all sentences where subject is in
## ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
## ["Baseball","cricket"].

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

lst=[i+' '+j+' '+k for i in subjects for j in verbs for k in objects]

for item in lst:
	print (item)
	
"""
Americans  play Baseball
Americans  play Cricket
Americans  watch Baseball
Americans  watch Cricket
Indians play Baseball
Indians play Cricket
Indians watch Baseball
Indians watch Cricket

"""
