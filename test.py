import subprocess,os



cmd=["python","-m","http.server"]
p = subprocess.Popen(cmd)
print(p.pid)

