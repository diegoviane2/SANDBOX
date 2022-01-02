import os

with open("ip.txt") as file:
  dump = file.read()
  dump = dump.splitlines()
  print(dump)

for ip in dump:
  res = os.popen(f"ping {ip}").read()
  print(res)