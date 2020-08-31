import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
query = input("Enter desired search term: ")
my_url = 'https://sfbay.craigslist.org/search/syp?query='+ query +'&srchType=T'
print(my_url)
#opening con / grab page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

filename ="product2.csv"
f = open(filename, "w")
headers = "brand, price, h_link, description\n"
f.write(headers)
#html parse
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("li",{"class":"result-row"})
#print(containers)
for container in containers:
	result_container = container.findAll("span",{"class":"result-price"})
	title_container = container.findAll("a",{"class":"result-title hdrlnk"})
	
	name = title_container[0].text
	price = result_container[0].text
	link = container.a["href"]
	url = link
	print(url)
	
	#opening con / grab page
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	discription_soup = soup(page_html, "html.parser")
	discription_containers = discription_soup.findAll("section",{"id":"postingbody"})

	
	d = discription_containers[0].text.replace("\n","")
	description = d.replace("QR Code Link to This Post","")
		#print(description)
	f.write(name.replace(",","|") + "," + price.replace(",","")+"," + link.replace(",","|") + ","+ description.replace(",","|") + "\n" )


	print(name)
	print(price)
	print(link)
	
	
f.close()


 
