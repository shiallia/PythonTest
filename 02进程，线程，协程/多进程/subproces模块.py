import subprocess

cmd = "ping www.baidu.com -n 3"
config = ""

proc = subprocess.Popen(cmd)
a = proc.wait()
print(f"done!函数返回值是{a}")
