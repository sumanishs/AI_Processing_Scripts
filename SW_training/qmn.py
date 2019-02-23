def toQmn(number, m, n):
	print "Number to convert:", number
	print "Qm.n","==>", m, ".", n
	prod = int(number * (2 ** n))
	print prod
	return prod

def bin2hex(binstr):
	#tmp = hex(int(binstr, 2))
	tmp = "{0:0>4X}".format(int(binstr, 2))
	tmp = tmp
	return tmp

def to16BitBin(number):
	print "Number to convert:", number
	binary = '{0:016b}'.format(number)
	print binary[:16]
	return binary[:16]

def twosComplementBin(number):
	binint = '{0:016b}'.format(number) #convert to binary
	tc = findTwoscomplement(binint)
	return tc

def findTwoscomplement(str): 
    n = len(str) 
    # Traverse the string to get first  
    # '1' from the last of string 
    i = n - 1
    while(i >= 0): 
        if (str[i] == '1'): 
            break
        i -= 1
    # If there exists no '1' concatenate 1  
    # at the starting of string 
    if (i == -1): 
        return '1'+str
    # Continue traversal after the  
    # position of first '1' 
    k = i - 1
    while(k >= 0): 
        # Just flip the values 
        if (str[k] == '1'): 
            str = list(str) 
            str[k] = '0'
            str = ''.join(str) 
        else: 
            str = list(str) 
            str[k] = '1'
            str = ''.join(str) 
        k -= 1
    # return the modified string 
    return str

