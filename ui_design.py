import os
color=lambda num:os.system("tput setaf {}".format(num))
background=lambda num:os.system("tput setab {}".format(num))
blink_text=lambda: os.system("tput blink")
reset=lambda: os.system("tput sgr0")
bold=lambda: os.system("tput bold")
underline=lambda o: os.system("tput {}mul".format(o))
