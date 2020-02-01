from bs4 import BeautifulSoup		
from pprint import pprint
import requests,time,json,os

os=os.path.exists("oppo.json")
if os:
	with open ("oppo.json","r") as thaman:
		a=json.loads(json.load(thaman))
		pprint(a)
else:
	flip=requests.get("https://www.flipkart.com/search?q=oppo&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")
	a=time.sleep(2)
	print(flip)
	soup=BeautifulSoup(flip.text,"html.parser")
	tbody=soup.find_all("div",class_="bhgxx2 col-12-12")
	dict1={}
	oppo=[]
	for i in tbody:
		names=i.find("div",class_="_3wU53n")
		if names!=None:
			name=names.text.split("(")
			dict1["NAME"]=name[0]
			name=name[1].split(",")
			dict1["ROM"]=name[1].strip(")")
			dict1["COLOR"]=name[0]
		pr=i.find("div",class_="_1vC4OE _2rQ-NK")
		if pr != None:
			dict1["RUPEES"]=pr.text
		ru=i.find("li",class_="tVe95H")
		if ru!= None:
			dict1["RAM"]=ru.text[:8]
			pprint(dict1)
			oppo.append(dict1)
	pprint(oppo)
	with open("oppo.json","w+") as thaman:
		a=json.dumps(oppo)
		b=json.dump(a,thaman)