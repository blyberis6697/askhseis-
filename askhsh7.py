from datetime import date, timedelta
now = datetime.datetime.now()
shmera = datetime.date.today()
day = now.day #1-31
onoma_hmeras = datetime.date.today().weekday() #arithmos hmeras: ( kyriakh(0) - savvato(6) )
a = 0

dd = [shmera + timedelta(days=i) for i in range(0, 10*365+3 ,7)] #oles oi meres pou thelw ta epomena 10 xronia(10*365), vhma 7 giati thelw tis idies meres!
for d in dd:
	if day == d.day : 
		print d
		a += 1 

print "Number of same dates from now to 10 years later:", a