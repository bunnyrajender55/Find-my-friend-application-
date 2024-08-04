from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pickle
import smtplib
import random
def gmail_otp(gmail):
	global otp
	print("Sending OTP to Gmail.....")
	try:
		msg=MIMEMultipart()
		msg["from"]="bunnyrajender77@gmail.com"
		msg["to"]=gmail
		msg["subject"]="WELCOM TO FIND YOUR FREIND APPLICATION"
		otp=random.randint(100000,999999)
		kmsg='Hello Welcome to...""Find Your Friend"" .... your One Time Password is--      '+str(otp)
		msg.attach(MIMEText(kmsg,"plain"))
		server=smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		lock='iyppdfbryvqXXXXX'
		server.login('bunnyrajenderXX@gmail.com',lock)
		server.send_message(msg)
		server.quit()
		print("OTP sented Successfully..")
	except:
		otp=0
		print("There is no internet connection... ")
		print("Plz check your data connection..")
def gmail_verification(gmail):
	gmail_otp(gmail)
	if(otp==0):
		assert 2%2==1,"*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nTHERE IS NO INTERNET\nPLZ TRY AGAIN\n*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*"
	i=0
	while(i<3):
		print("For enter otp Click -1\n For resend otp Click 2")
		while(1):
			g_opt=input("Enter your option:")
			if(g_opt.isdigit()):
				if(g_opt=="1" or g_opt=="2"):
					break
				else:
					print("Enter Correct option..")
			else:
				print("Enter ony digits..")
		if(g_opt=="1"):
			gg_otp=input("Enter OTP here:")
			break
		if(g_opt=="2"):
			gmail_otp(gmail)
			print("Successfully Resended")
		i=i+1
	else:
		print("Your Session is Expired..")
		assert 2%2==1,"*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nSESSTION EXPIRED\nPLZ TRY AGAIN\n*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*"
	if(otp==0):
		assert 2%2==1,"*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nSESSION EXPIRED\nPLZ TRY AGAIN\n*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*"
	else:
		i=0
		while(i<3):
			if(gg_otp==str(otp)):
				print("Successs...your gmail is working")
				break
			else:
				print("Invalid otp try again")
				gg_otp=input("Enter otp here:")
			i=i+1
		else:
			assert 2%2==1,"*-*-*-*-*-*--*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nSESSIOS IS EXPIRED\nPLZ TRY AGAIN\n*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*"
	
def unlock():
	xx=open("store_gmail.dat","rb")
	yy=pickle.load(xx)
	xx.close()
	i=3
	while(i>0):
		print("You have %d chances"%(i))
		i=i-1
		password=input("Enter possword to Unlock::")
		if(yy[0]==password):
			print("You successfully Unlocked\n*************************************")
			break
		else:
			print("Password is incorrect ...")
	else:
		print("If you forget your password Enter 1 else enter 0:")
		mmm=1
		while(1 and mmm):
			pass_forget=input("Enter your option:")
			if(pass_forget.isdigit()):
				pass_forget=int(pass_forget)
				if(pass_forget==1):
					fff=0
					nickname=input("Enter your nick name first to change password:")
					if(yy[1]==nickname):
						fff=1
						pass
					else:
						print("Incorrect nick name")
						print("YOU have to set set new password through GMAIL..")
						xm=open("store_gmail.dat","rb")
						xmm=pickle.load(xm)
						xm.close()
						print("Plz check your gmail that is-%s"%(xmm[2]))
						gmail_verification(xmm[2])
						print("Sussess ...")
					password1=input("Enter your new Password:")
					mkm=open("store_gmail.dat","rb")
					xmm=pickle.load(mkm)
					mkm.close()
					if(fff==0):
						nick_name=input("Enter your new NickName:")
					else:
						nick_name=xmm[1]
					mkm=open("store_gmail.dat","wb")
					
					
					pickle.dump([password1,nick_name,xmm[2]],mkm)
					mkm.close()
					print("Successfully password seted\n****************************************")
					break
						
						
								
				elif(pass_forget==0):
					print("Then ok")
					assert not(pass_forget==0),"****************************\n\n***************TRY AGAIN******************"
					break
				else:
					print("Enter correct option")
			else:
				print("Enter only digits")
try:
	xx=open("store_gmail.dat","rb")
	xx.close()
except:
	print("First set your password")
	password2=input("Enter password:")
	print("Enter your nick name:")
	nick=input("Enter nick name :")
	while(1):
		gmail=input("Enter your working Gmail here:")
		if(gmail.islower()):
			if(gmail.endswith("@gmail.com")):
				break
			else:
				print("Enter valid Gmail")
		else:
			print("Enter lower case letters only..")
	gmail_verification(gmail)
	
	xx=open("store_gmail.dat","wb")
	pickle.dump([password2,nick,gmail],xx)
	xx.close()
	print("Successfully password Seted")
unlock()
try:
	x=open("store_friends.dat","rb")
except:
	x=open("store_friends.dat","wb")
	a=[]
	b=["STATE","DISTRICT","MONDAL","VILLAGE","NAME","PHONE_NUMBER"]
	a.append(b)
	pickle.dump(a,x)
x.close()
x=open("store_friends.dat","rb")
m=pickle.load(x)
x.close()
def deletelast():
	try:
		e=m[1]
		f=m.pop()
	except:
		print("There is no any record")
		return
	x=open("store_friends.dat","wb")
	pickle.dump(m,x)
	x.close()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print("Successfully deleted last record")
	print("-------That is-------")
	for i in f:
		print(i,end="  ")
def search_phone():
	while(1):
		phone=input("Enter phone Number:")
		if(phone.isdigit()):
			if(len(phone)==10):
				break
			else:
				print("Enter 10 digits number")
		else:
			print("Enter only digits")
	print("%s\t\t%s\t\t%s"%("VILLAGE","NAME","PH_NO"))
	for i in m:
		for j in i:
			if(j==phone):
				global f123
				global k
				global s123
				s123=1
				global full_d
				full_d=i
				f123=i
				k=1
				print("%s\t\t%s\t\t%s"%(i[3],i[4],i[5]))
def search_name():
	while(1):
		o=0
		name=input("Enter Name:")
		for b in range(10):
			if(name.startswith(str(b))):
				o=1
		if(o==1):
			print("Digits are not allowed at starting")
		else:
			break
	print("%s\t\t%s\t\t%s"%("VILLAGE","NAME","PH_NO"))
	name=name.capitalize()
	for i in m:
		e=i[4].find(".")
		if(e==-1):
			t=i[4]
		else:
			t=i[4][e+1:]
		if(name==i[4] or name==i[4][1:].capitalize() or name==t.capitalize()):
			global k
			k=1
			print("%s\t\t%s\t\t%s"%(i[3],i[4],i[5]))
def search_village():
	while(1):
		village=input("Enter Village Name:")
		if(village.isalpha()):
			break
		else:
			print("Enter aplhabets only")
	print("%s\t\t\t\t%s\t\t%s\t\t%s"%("MONDAL","VILLAGE","NAME","PH_NO"))
	village=village.capitalize()
	for i in m:
		if(village==i[3]):
			global k
			k=1
			print("%s\t\t%s\t\t%s\t\t%s"%(i[2],i[3],i[4],i[5]))
	
def search_mondal():
	district()
	mondal()
	print("%s\t\t-\t%s\t-\t%s\t-\t%s"%("Mondal","Village","Name","Ph_no"))
	for i in m:
			if(Mondal==i[2]):
				global k
				k=1
				print()
				print("%s\t-\t%s\t-\t%s\t-\t%s"%(i[2],i[3],i[4],i[5]))	
def search_district():
	district()
	print("%s\t- %s\t- %s\t- %s\t- %s"%("District","Mondal","Village","Name","Ph_no"))
	for i in m:
		if(District==i[1]):
			global k
			k=1
			print()
			print("%s\t- %s\t- %s\t- %s\t- %s"%(i[1],i[2],i[3],i[4],i[5]))
	
def district():
	global d
	d={1:"hanmakonda",2:"warangal",3:"karimnagar",4:"siddipeta",5:"khammam"}
	j=1
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	for i in d.values():
		print("%d-%s"%(j,i))
		j=j+1
	while(1):
		global district
		district=input("SELECT DISTRICT:")
		if(district.isdigit()):
			district=int(district)
			if(district<=5 and district>=1):
				break
			else:
				print("Enter correct option")
		else:
			print("Enter only digits")
	global District
	District=d[district]
def mondal():
	global mo
	if(district==1):
		mo={1:"Hanamkonda",2:"Khaazipet",3:"Inavole",4:"Hasanparthy",5:"Velair",6:"Dharmasagar",7:"Elkathurthi",8:"Bheemadevarapalli",9:"Kamalapur",10:"Parkal",11:"Nadikuda",12:"Athmakur",13:"Damera",14:"Shayampet"}
	elif(district==2):
		mo={1:"Chennaraopet",2:"Duggondi",3:"Anantharam",4:"Khanapur",5:"Khila Warangal",6:"Nallabelly",7:"Narsampet",8:"Nekkonda",9:"Parvathagiri",10:"Raiparthy",11:"Sangem",12:"Warangal",13:"Wardhannapet"}
	elif(district==3):
		mo={1:"karimnagar",2:"kothapally",3:"karimnagar Rural",4:"Manakondur",5:"Thimmapur",6:"Ganneruvaram",7:"Gangadhara",8:"Ramadugu",9:"Choppadandi",10:"Chigurumamidi",11:"Huzurabad",12:"Veenavanka",13:"V.Saidapur",14:"Jammikunta",15:"Ellandakunta",16:"Shankarapatnam"}
	elif(district==4):
		mo={1:"Siddipet Rural",2:"Siddipet Urban",3:"Narayanaraopet",4:"Chinnakodur",5:"Nangnoor",6:"Dubbak",7:"Mirdoddi",8:"Thoguta",9:"Doulthabad",10:"Raipole",11:"Kondapak",12:"Gajwel",13:"Jagadevapur",14:"Markook",15:"Wargal",16:"Mulugu",17:"Cherial",18:"Komuravelly",19:"Maddur",20:"Husnabad Urban",21:"Akkannapeta",22:"Koheda",23:"Bejjenki",24:"Dhoolmitta",25:"Akbarpet-Bhoompally",26:"Kukunoorpally"}
	elif(district==5):
		mo={1:"Vemsoor",2:"Yerrupalem",3:"Madhira",4:"Bonakal",5:"Wyra",6:"Thallada",7:"Chinthakani",8:"Nelakondapalle",9:"Mudigonda",10:"Khammam Rural",11:"Kusumanchi",12:"Thirumalayapalem",13:"Penuballi",14:"Sathupalle",15:"Dammapeta",16:"Aswaraopeta",17:"Mulakalapalle",18:"Chandrugonda",19:"Julurpad",20:"Singareni",21:"Garla",22:"Bayyaram",23:"Gundala",24:"Yellandu",25:"Tekulapalle",26:"Kothagudem",27:"Palawancha",28:"Burgampadu",29:"Kukunoor",30:"Vararamachandrapuram",31:"Chintur",32:"Kunavaram",33:"Bhadrachalam",34:"Dummugudem",35:"Aswapuram",36:"Manuguru",37:"Cherla",38:"Venkatapuram",39:"Khammam",40:"Kalluru",41:"Kamepalle"}
	
	j=1
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	for i in mo.values():
		print("%d-%s"%(j,i))
		j=j+1
	while(1):
		global mondal
		mondal=input("SELECT MONDAL:")
		if(mondal.isdigit()):
			mondal=int(mondal)
			try:
				global Mondal
				Mondal=mo[mondal]
			except:
				print("Enter correct option")
			else:
				break
		else:
			print("Enter only digits")
def add():
	while(1):
			state=input("ENTER STATE:")
			if(state.isalpha()):
				break
			else:
				print("Enter only Alphabets")
	district()
	mondal()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		village=input("ENTER VILLAGE:")
		if(village.isalpha()):
			break
		else:
			print("Enter only Alphabets")
	village=village.capitalize()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		o=0
		name=input("ENTER NAME:")
		for b in range(10):
			if(name.startswith(str(b))):
				o=1
		if(o==1):
			print("Digits are not allowed at Starting")
		else:
			break
	name=name.capitalize()
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	while(1):
		ph_no=input("ENTER PH_NO:")
		if(ph_no.isdigit()):
			if(len(ph_no)==10):
				if(int(ph_no[0])<=5):
					print("Must be first digit is greatet than 5")
				else:
					break
			else:
				print("Enter 10 digits number")
		else:
			print("Enter only digits")
	if(s123==1):
		pass
	else:
		for i in m:
			for j in i:
				if(ph_no==j):
					print("*-*-*-*-*-*-*-*-*-*-*-*-*")
					print("The Record/Ph_no already exits")
					return
	print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
	a=[state,District,Mondal,village,name,ph_no]
	global v123
	v123=a
	m.append(a)
	x=open("store_friends.dat","wb")
	pickle.dump(m,x)
	x.close()
	print("successfully added\n")
	print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
def search():
	print("1-SEARCH BY DISTRICT")
	print("2-SEARCH BY MONDAL")
	print("3-SEARCH BY VILLAGE")
	print("4-SEARCH BY NAME")
	print("5-SEARCH BY NUMBER")
	print("6-SEARCH VIA RANDOM")
	global k
	k=0
	while(1):
		search=input("SELECT OPTION:")
		if(search.isdigit()):
			search=int(search)
			if(search>=1 and search<=6):
				break
			else:
				print("Enter correct option")
		else:
			print("Enter only digits")
	if(search==1):
		search_district()
	if(search==2):
		search_mondal()
	if(search==3):
		search_village()
	if(search==4):
		search_name()
	if(search==5):
		search_phone()
	if(search==6):
		while(1):
			random=input("Enter random one:")
			if(random.isdigit()):
				if(len(random)==10):
					break
				else:
					print("Enter 10 digits Number")
			elif(random.isalpha()):
				break
			else:
				print("Enter properly")	
		print("VILLAGE\t\t\tNAME\t\t\tPH_NO")
		for i in m:
			for j in i:
				if(random.capitalize()==j):
					k=1
					print(i[3],"\t\t",i[4],"\t\t",i[5])
	print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
	if(k==0):
		print("No record is founded")
	print("Searching ended")
def Full_details():
	search_phone()
	if(s123==1):
		print("Full details Are---")
		iii=["STATE","DISTRICT","MONDAL","VILLAGE","NAME","PHONE_NUMBER"]
		for iiii in range(len(iii)):
			print("  %s            \t       :: %s"%(iii[iiii],full_d[iiii]))
	else:
		print("No record is Founded")
def edit():
	search_phone()
	if(s123==1):
		q=open("store_friends.dat","rb")
		r=pickle.load(q)
		for t in range(len(r)):
			if(r[t]==f123):
				global i123
				i123=t
				print("Enter now updated details")
				add()
				r[t]=v123
				ff=r
				q=open("store_friends.dat","wb")
				pickle.dump(ff,q)
				break
		q.close()
		print("Sussessfully edited")
	else:
		print("No record Founded")
		
		
	
print("For add a Friend enter 1")
print("For Search a Friend enter 2")
print("For delete last record enter 3")
print("For edit a record enter 4 ")
print("For Get Full details of a Friend Enter 5")
f123=[]
v123=[]
s123=0
i123=0
otp=1
full_d=[]
def enter():
   while(1):
    n=input("enter your option:")
    if(n.isdigit()):
    	break
    else:
    	print("enter only digits")
   n=int(n)
   if(n==1):
   	add()
   elif(n==2):
   	search()
   elif(n==3):
   	deletelast()
   elif(n==4):
   	edit()
   elif(n==5):
   	Full_details()
   else:
   	print("enter correct option")
   	enter()
enter()