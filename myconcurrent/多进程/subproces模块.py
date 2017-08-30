import subprocess

cmd = "ping www.baidu.com -n 3"
config = ""

output_byte = subprocess.check_output(cmd)
print(output_byte.decode('GBK'))
#print(f"done!函数返回值是{a}")
