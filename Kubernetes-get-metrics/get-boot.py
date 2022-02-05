import os
import subprocess
import pandas as ps


#ts = subprocess.check_output(["date"])

ts = os.popen("kubectl -n sandbox get pod  --output-watch-events --watch | awk '/nginx/ && /Running/'").read()


print("ts")