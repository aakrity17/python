#WAP to get a string when all occurence of its first charcater have been changed to $ except the first char itself

def replaceChar(str):
	char=str[0]
	str=str.replace(char,'$')
	str=char+str[1:]
	return str
print(replaceChar('shrishty'))
