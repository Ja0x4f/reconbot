from masscan import masscan
import os, time, sys

domain = str(sys.argv[1])

masscan.scansubs(domain)
masscan.portscanner(domain)
masscan.crawling(domain)
masscan.vulnsearch(domain)
masscan.xsshunt(domain)
