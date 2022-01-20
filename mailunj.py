import os,requests,bs4,json,convertapi
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor as thread
os.system("clear")

GR = "\033[90m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
P = "\033[95m"
C = "\033[96m"
W = "\033[m"
F = "\033[47;30m"
O = "\033[37m"
print("Email UNJ\n")
nim = input("Nim  > ")
pw=nim
#pw = input("Pass > ")
ses = requests.Session()

print("\nLogin...")
url = "http://siakad.unj.ac.id/index.php/login/getlogin"
capca = "http://103.8.12.212:36880/siakad_api/api/as400/captcha"
raw = ses.get(capca).text
cap = json.loads(raw)
login = ses.post(url, headers={ 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Referer':'http://siakad.unj.ac.id/login' }, data={ "username":nim, "password":pw, "captcha_id":cap['data']['id'], "captcha":cap['data']['ans'] }, verify=False).text  
if "Selamat Datang" in login:
	print("Berhasil Login...")
	email = bs4.BeautifulSoup(login, 'html.parser').find("div",{"class":"col-md-12 alert alert-info"}).text.split("@mhs.unj.ac.id")[2].split(":")[2].replace(" ","") +"@mhs.unj.ac.id"
	email = email.lower()
	password = bs4.BeautifulSoup(login, 'html.parser').find("div",{"class":"col-md-12 alert alert-info"}).text.split("@mhs.unj.ac.id")[3].split("Silahkan")[0].replace(" ","").split(":")[1].replace("\n","")
	print(f"""
Nim     : {nim}
Email   : {email}
Pass    : {password}
""")
	ksks = bs4.BeautifulSoup(ses.get("http://siakad.unj.ac.id/index.php/krs").text,'html.parser').find("select",{"id":"kodeSMS"}).findAll("option")[1]["value"]
	ran = bs4.BeautifulSoup(ses.post("http://siakad.unj.ac.id/krs/showData",data={"ksks":ksks}).text,'html.parser').findAll("button")[0]["onclick"].split("=")[2].split("'")[0]
	pdf = f"http://siakad.unj.ac.id/index.php/krs/cetakKRS?k={ksks}&ran={ran}"
	pdf = ses.get(pdf)
	try:os.mkdir("krsunj")
	except:pass
	open('krs.pdf', 'wb').write(pdf.content)
	convertapi.api_secret = 'djgyPYWre02chA0m'
	convertapi.convert('png', {
	    'File': 'krs.pdf'
	}, from_format = 'pdf').save_files(f'krsunj/{nim}.png')
	os.remove('krs.pdf')
	print(f"File krs tersimpan di krsunj/{nim}.png")
else:
	exit("Gagal Login...")
	