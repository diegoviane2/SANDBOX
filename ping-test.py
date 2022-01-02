import os
import csv

with open("ip.csv") as file:
  dump = file.read()
  dump = dump.splitlines()
  print(dump)

    
for ip in dump:
  res = os.popen(f"ping {ip}").read()
  if(("Host de destino inacess¡vel.") or ("unreachable") or ("Request time out")) in res:
    print(str(ip) + " Is DOWN" +"\n")
   
  else:
    print(str(ip) + " Is UP" +"\n")