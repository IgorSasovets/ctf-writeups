# Warm Up challenges

## Read The Rules

```
5 points
Please follow the rules for this CTF!
Connect here: http://ctf.virseccon.com/rules.
```
### Solution
Navigate to the http://ctf.virseccon.com/rules and review the page source

```
<!-- Thank you for reading the rules! Your flag is: -->
<!--         LLS{you_are_ready_to_HACK_THE_PLANET}         -->
```

## Believe Your Eyes
```
10 points
You would not believe your eyes...

Download the file below.
believe_your_eyes.rar
```
### Solution

Let's see what the file data actually is using `file` command
```
> file believe_your_eyes.rar
believe_your_eyes.rar: PNG image data, 600 x 200, 8-bit grayscale, non-interlace
```

It seems that we need to change the file extension to `png` to get more info

```
> cp believe_your_eyes.rar believe_your_eyes.png
```

Open the image and we get the flag!
```
LLS{if_ten_million_fireflies}
```

## Yarn
```
25 points
I found this ball of... yarn?

Download the file below.
yarn
```

### Solution
At first, let's try to use `strings` command with the file 

```
> strings yarn | grep LLS
yLLS{it_was_just_a_ball_of_strings}j

```

Easy one :)

## Puppo
```
25 points
Awww, isn't this puppo so cute??? I can almost hear him barking... what does he say?

Download the file below.
woofer.jpg 
```

### Solution
We will start we the `file` command
```
> file woofer.jpg
woofer.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "b'TExTe2RvZ2dvX3NheXNfc3VjaF9iYXNlNjRfdmVyeV93b3d9'", baseline, precision 8, 537x529, components 3
```

Hmmm, it looks like comment should hold some base64 encoded stuff. Check it out!
```
> echo e2RvZ2dvX3NheXNfc3VjaF9iYXNlNjRfdmVyeV93b3d9 | base64 -d
{doggo_says_such_base64_very_wow}
```
A little transformation: `LLS{doggo_says_such_base64_very_wow}` and we got it

## DotCom Scavenger Hunt
```
25
It’s a website scavenger hunt!

Download the file below.
dotcom_scavenger_hunt.zip
```

### Solution
Unzip the file
```
> unzip dotcom_scavenger_hunt.zip
```
* After that, we can analyze the files with grep or just open the index.html in Chrome browser and review `Page sources`
using the Developer tools.
* Open `jquery-1.3.1.min.js` file
* Use search with the term `LLS` and we got the flag
```
LLS{just_find_it_with_grep}
```

## Ssh, quiet!
```
35 points
Ssssh, don't wake the flag!

(Yes, that is intended behavior.)

Connect with:
ssh user@jh2i.com -p 50035 # password is 'userpass'
```

### Solution
Plain connection to the target host doesn't give us something juicy:
```
> ssh user@jh2i.com -p 50035
user@jh2i.com's password: 
Last login: Sat Apr  4 07:43:07 2020 from 167.172.141.127
Connection to jh2i.com closed.
```

Let's try to execute `ls` command on the remote host
```
> ssh user@jh2i.com -p 50035 ls
user@jh2i.com's password: 
flag.txt
```

Hmmm, there is smth interesting, we should definitely print it out!!!!
```
> ssh user@jh2i.com -p 50035 cat flag.txt
user@jh2i.com's password: 
LLS{automate_ssh_like_a_boss}
```
LIKE A BOSSSSSS!!!!!!! Check out this [tutorial](https://phoenixnap.com/kb/linux-ssh-commands) for linux ssh commands

## Pack'd
```
40 points
I checked the mailbox, and I found this bundled up package! Can you make any sense of it?

Download the file below.
packd
```
### Solution
After we downloaded the file, execute the `file` command on it
```
> file packd
packd: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, no section header
```
Now let's check if we can to grab the flag without reversing the executable
```
> strings packd_original | grep LLS
LLS{
```
It seems that we need to use UPX unpacker for this. Let's give it a try
```
> sudo apt install upx
> upx -d packd
```
Nice!!! Now execute `strings` on the unpacked file
```
> strings packd | grep LLS
LLS{packing_an_executable_can_hide_some_data}
```

## Capture the Flag
```
50 points
Are you ready to play Capture the Flag?

This is a stupid challenge, and it is dumb, and stupid.
https://www.youtube.com/watch?v=Nh23tQ8MD-Q
```
### Solution
Just change the video speed to be able to catch as many frames as you can an on the one of them you will see the flag!
```
LLS{flags_in_frames_forever}
```
