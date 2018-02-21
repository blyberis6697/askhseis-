import random
list = []
list2 = []
list3 = []
t = 0

for i in range(0,30):
	#gia na apofygw na exw sth lista mou to stoixeio 0!
	list.insert(i , random.choice([-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))	
print "Afth einai h lista me 30 tyxaious THETIKOUS h ARNHTIKOUS arithmous: "
print list	

for i in range(0,29):
	for j in range(0,29):
		for k in range(0,29):
			if (list[i] + list[j] + list[k] == 0):	 
				list2.insert(t,[list[i],list[k],list[j]])
				t+=1

for x in list2:  
	#gia na apofygw tis idies 3ades me diaforetikh seira!
	if sorted(x) not in list3:
		list3.append(sorted(x))	
print "Oi diaforetiks 3ades ths listas pou exoyn athroisma 0: "
for x in list3:
	print x, "\n"