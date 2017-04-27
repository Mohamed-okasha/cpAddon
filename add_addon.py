#https://documentation.cpanel.net/display/SDK/cPanel+API+2+Functions+-+AddonDomain%3A%3Aaddaddondomain
import subprocess
import os
import sys

def excute(cmd):  
    p = subprocess.Popen(cmd.split(" "), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()


if len(sys.argv)!=4
   print "arguments error\n CALL Ex. python script.py <username for cpanel account> <addon domain> <sub domain> "
   return 

if not os.path.isdir(os.path.join(os.getcwd(), 'public_html')):
    print "please run script from home/<cpanel_account> directoy \neg. home/lsdemo "
    return 




user_name=sys.argv[1]
addon_domain=sys.argv[2]
subdomin_domain=sys.argv[3]


cmd_cpanel_api="cpapi2 --user=<username> AddonDomain addaddondomain dir=<addondomain> newdomain=<addondomain> subdomain=<subdomain>"
try:
  excute(cmd_cpanel_api.replace("<username>",user_name).replace("<addondomain>",addon_domain).replace("<subdomain>",subdomin_domain))

  excute("wget "+ source_domain+ "/etc.zip"  )
  excute("wget "+ source_domain+ "/mail.zip"  )
  excute("wget "+ source_domain+ "/public_html.zip")

  excute("mkdir "+"etc/"+source_domain)
  excute("mkdir "+"mail/"+source_domain)


  excute("unzip -j etc.zip -d etc/"+source_domain)
  excute("unzip -j"+"mail.zip -d mail/"+source_domain)
  excute("unzip -j"+"public_html.zip -d public_html/"+source_domain)
except Exception as e:
  print "error massage:"+str(e)

