import requests

url = ""
hd = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

fromdata = ""

res = requests.post(url, data=fromdata, headers=hd)

res_header = res.headers
set_cookie = res_header['Set-Cookie']


