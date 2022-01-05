import os
import sys
import argparse
from types import ClassMethodDescriptorType
from typing import Type
sys.tracebacklimit=0
file_list = "ip.txt"
checksum = 0

parser = argparse.ArgumentParser(description='Teste de PING')
parser.add_argument('--file-location', "-f", required=False, help="Lista de IPs a serem testados")
args = parser.parse_args()

if args.file_location:
  file_list = str(format(args.file_location))

print (args)

try:
  with open(file_list) as file:
    dump = file.read()
    dump = dump.splitlines()
    print ("Total de Hosts: "+ str(len(dump)))
except Exception as e:
  print("Erro:\nNenhum endereço IP informado\n\n")  

for ip in dump:
  res = os.popen(f"ping {ip}").read()
  if(("Host de destino inacess¡vel.") or ("unreachable") or ("Request time out")) in res:
    print(str(ip) + "\t" + "DOWN")
  else:
    checksum = checksum + 1
    print(str(ip) + "\t" + "UP")

print(str(checksum) + "/" + str(len(dump)) + "\t" + "Hosts UP" )

print ("\n"+ args)