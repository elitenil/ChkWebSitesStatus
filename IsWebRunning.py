import requests,time
def WebTest(url):
   
    print(url)
    try:
        t1 = time.time()
        r = requests.get(url)
        t2 = time.time()
        tim = str(t2-t1)
        print("Time in Seconds: " + tim)
    except requests.exceptions.RequestException as err:
        print("Error: ",err)
    except requests.exceptions.HTTPError as errh:
        print("Http error: ",errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connection: ", errc)
    except requests.exceptions.Timeout as errt:
        print(" TimeOut Error: ", errt)
    print("\n")

#Put Testing url Here
url =["http://www.github.com",
'http://www.google.com',
'http://www.google.com/blablabla',
'http://www.googleNotFoundSiite.com',
'http://www.yahoo.com'
]

for sites in url:
    WebTest(sites)