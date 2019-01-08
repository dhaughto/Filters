''' 
	This function will filter two lists, removing duplicates from the first list
	It sums up the values of the removed duplicates and puts those in the new list
	Values in the first list and second list coorespond to each other

	-------------------
		Application
	-------------------
Can be used with data from finicial application
ß

'''	


def filter_sum(list1,list2):

	a = sorted(zip(list1,list2))
	b = list(zip(*a))
	list1 = b[0]
	list2 = b[1]

	c = Counter(list1)
	d = list(c.keys())
	counted = list(c.values())

	mega = []
	omega = []
	count = 0
	for i in counted:
		mega+=[list(list1[count:count+i])]
		omega+=[list(list2[count:count+i])]
		count += i

	new_list2 = []
	for i in omega:
		new_list2 += [sum(i)]

	return d,new_list2	