#Write a Python program to reverse a string
def reverse(object):
	x=''
	rev=len(object)
	while(rev>0):

		x=x+object[rev-1]
		rev=rev-1
	return x
    
print(reverse(('lloojjjjjj')))
