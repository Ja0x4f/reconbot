import os,time
class masscan():

    def scansubs(domain):
        global subfile
        subfile = f"{domain.split('.')[0]}_subdomains.txt"
        print("Starting subdomain discovery.")
        os.system(f"echo {domain} | subfinder -all -silent | gauplus | anew {subfile}")
        print("Subfinder OK")
        print("Starting haktrails")
        #time.sleep(5)
        os.system(f"echo {domain} | haktrails subdomains | anew {subfile}")
        time.sleep(5)
        print("Recon de subdominios completo.")
        print(f"Output file -> {subfile}")
        time.sleep(5)

    def portscanner(domain):
        global portscan
        portscan = f"{domain.split('.')[0]}_portscan.txt"
        global http200
        http200 = f"{domain.split('.')[0]}_http200.txt"
        allports = "80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672"
        time.sleep(5)
        print("\n\nIniciando busca por portas on Naabu.")
        os.system(f"cat {subfile} | naabu -silent -p {allports} | anew {portscan}")
        os.system(f"cat {portscan} | httpx -silent | anew {http200}")
        print(f"\nNaabu completo.\nTodos links foram validados.\nOutput file -> {http200}")
        time.sleep(5)

    def crawling(domain):
        global crawKatana
        crawKatana = f"{domain.split('.')[0]}_crawKatana.txt"
        blacklist = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"
        katanalist = "js,jsp,json,php,aspx,asp"
        unfullDomains = f"{domain.split('.')[0]}_unfullDomains.txt"
        global fullDomains
        fullDomains = f"{domain.split('.')[0]}_fullDomains.txt"
        global full200
        full200 = f"{domain.split('.')[0]}_full200.txt"
        crawKatanaJS = f"{domain.split('.')[0]}_crawKatanaJS.txt"
        print("\nStarting crawling with Katana.")
        time.sleep(5)
        os.system(f"cat {http200} | katana -d 10 -silent -o {crawKatana} -ef {blacklist} -em {katanalist}")
        os.system(f"cat {crawKatana} | unfurl domains | anew {unfullDomains}")
        os.system(f"cat {unfullDomains} {subfile} | anew {fullDomains}")
        os.system(f"cat {fullDomains} | httpx -silent | anew {full200}")
        print(f"\nCrawling com Katana completo.\nTodo links validados com httpx.\nOutput file -> {full200}")
        print(f"Iniciando JS crawling.")
        time.sleep(5)
        os.system(f"cat {full200} | katana -d 10 -silent -em {katanalist} -o {crawKatanaJS}")
        print(f"\n\nJS Crawling completo.\nOutput file -> {crawKatanaJS}")

    def vulnsearch(domain):
        UserAgent = "User-Agent: kommandos"
        nucleiResp = f"{domain.split('.')[0]}_nuclei.txt"
        print("\n\nInicinado scan com Nuclei.")
        time.sleep(5)
        os.system(f"cat {full200} | nuclei -severity low,medium,high,critical -silent -o {nucleiResp} -H {UserAgent} | notify --silent")
        print(f"Scan com nuclei completo.\nOutput file -> {nucleiResp}")


    def xsshunt(domain):
        xssCrawling = f"{domain.split('.')[0]}_xssCrawling.txt"
        craw1xss = f"{domain.split('.')[0]}_craw1xss.txt"
        xssResults = f"{domain,split('.')[0]}_xssResults.txt"
        #os.system(f"echo {domain} | subfinder -silent | gauplus | grep \"=\" | uro | gf xss | anew {craw1xss}")
        os.system(f"cat {full200}| grep \"=\"| uro | gf xss | anew {xssCrawling}")
        os.system(f"python3 /home/john/Tools/Knoxnl/knoxnl.py -i {xssCrawling} -X BOTH | anew {xssResults}")

