alphabet = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'} 
print ("Type something you want to decode with <rot13> and press Enter:")
print("Type <stop> to end!")

a = raw_input() #pairnw eisodo apo to plhktrologio

while (a != "stop") : #while loop
	for i in a: #gia kathe gramma sthn eisodo
		if i in alphabet: #gia kathe xarakthra sto alphabet
			b += alphabet[i] #metavlhth b pou krataei to kwdikopoihmeno keimeno

	print(b)
	b = ""
	print ("what else?") #evgenikos 
	a = raw_input()

print("END OF DECODING! :)") #evgenikotatos