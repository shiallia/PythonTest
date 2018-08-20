import platform

sysstr = platform.system()
print(sysstr)
if sysstr == "Windows":
    print("Windows")
else:
    print("others")