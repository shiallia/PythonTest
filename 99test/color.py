from colorama import init, Fore, Back
init(autoreset=True)
 #通过使用autoreset参数可以让变色效果只对当前输出起作用，输出完成后颜色恢复默认设置
print(Fore.RED + 'welcome to www.jb51.net')
print('automatically back to default color again')
print(Fore.GREEN + 'welcome to www.jb51.net')
print(Fore.BLUE + Back.WHITE + 'welcome to www.jb51.net')
a = input()


