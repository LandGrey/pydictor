# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor) [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](http://www.gnu.de/documents/gpl-3.0.en.html)

**README.md [中文版](https://github.com/LandGrey/pydictor/blob/master/README_CN.md)**

##### pydictor —— A useful hacker dictionary builder for a brute-force attack

             _______                __   _          _
            |_   __ \              |  ] (_)        / |_
              | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
              |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
             _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
            |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                     \__.'


##### Email: LandGrey@qq.com
-
## Preface：
```
Q: Why pydictor was born ?
A: Writing an excellent password-generation security tool to help a large number of penetration testing researchers.

Q: Why I need to use pydictor ?
A: 1.it always can help you
      You can use pydictor to generate a general blast wordlist, a custom wordlist based on Web content, a social engineering wordlist, and so on;
      You can use the pydictor built-in tool to safe delete, merge, unique, merge and unique,  count word frequency to fillter the wordlist, and so on;

   2.highly customized
      You can generate highly customized and complex wordlist by modify multiple configuration files, add your own dictionary, using leet mode, pick by length, etc.
      and its very relevant to generate good or bad password dictionary with your custom rules;

   3.great compatibility
     whether you are using Python 2.7 version or Python 3.x version , pydictor can be run on Windows, Linux or Mac;

Q: What is the goal of pydictor?
A: A useful and better password-generator that helps plenty of penetration testers work better.
```

## Start:
```
git clone https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
python pydictor.py
```

## Overview：
#### terminal display 
```
pydictor.py [options]
           -base     [type]
           -char     [custom_char]
           -chunk    [chunk1] [chunk2] ...
           -plug     [pid6,pid8,extend,passcraper]
           -o        [output_path]
           -tool     [shredder,uniqifer,counter,combiner,uniqbiner] [args] ...
           --len     [minlen] [maxlen]
           --head    [prefix_string]
           --tail    [suffix_string]
           --encode  [none,b64,md5,md516,sha1,url,sha256,sha512]
           --conf    [config_file_path]
           --mode    [code]
           --pick
           --sedb

*[+] A Useful Hacker Dictionary  Builder. [+]*
 [+] Build by LandGrey    email:LandGrey@qq.com

optional arguments:
  -h, --help            show this help message and exit
  -base Type
                        Choose from  (d, L, c, dL, dc, Lc, dLc)
                            d     digital             [0 - 9]
                            L     lowercase letters   [a - z]
                            c     capital letters     [A - Z]
                            dL    Mix d and L         [0-9 a-z]
                            dc    Mix d and c         [0-9 A-Z]
                            Lc    Mix L and c         [a-z A-Z]
                            dLc   Mix d, L and dL     [0-9 a-z A-Z]
  -char character       Use Custom Character build the dictionary
  -chunk chunk [chunk ...]
                        Use the multi-chunk build the dictionary
  -plug plug [plug ...]

                        Choose from    (pid6, pid8, extend, passcraper)
                            pid6       [idcard_last_6_digit]   default sex:all
                            pid8       [idcard_last_8_digit]   default sex:all
                            extend     [file_path]
                            passcraper [url_or_file_path]
  -o output
                        Set the output directory path
                            default: pydictor/results
  -tool name [name ...]

                        Choose from    (shredder, uniqifer, counter,
                                        combiner, uniqbiner)
                            shredder   [file_or_dir]
                            uniqifer   [file_path]
                            counter    ['v','s','vs'] [file_path] [view_num]
                            combiner   [dir]
                            uniqbiner  [dir]
  --len minlen maxlen
                        [Minimun_Length]  [Maximun_Length]
                                            Default: min=1  max=4
  --head prefix         Add string head for the items
  --tail suffix         Add string tail for the items
  --encode encode
                        From (none, b64, md5, md516, sha1, url, sha256, sha512)
  --conf [file_path]
                        Use the configuration file build the dictionary
                            Default: pydictor/build.conf
  --mode code
                        Choose leet mode code
                            (0, 1, 2, 11-19, 21-29)      default: 0
  --pick
                        Use [minlen maxlen] to pick results
  --sedb                Enter the Social Engineering Dictionary Builder
```
#### pictures  
![passcraper](/screenshots/passcraper.png "passcraper")

![social engineering dictionary builder](/screenshots/sedb.png "sedb")

## Functions & Usage:
### 1. generate the base dictionary
##### cmd: -base
##### example 1: generating a dictionary that specifying length using pure digital,lowercase letters,or capital letters
    python pydictor.py -base d --len 6 6			generate six length dictionary base on pure digital

##### example 2: generating a dictionary that using two of digital,lowercase letters and capital letters
    python pydictor.py -base dL --len 1 3

##### example 3: generating a dictionary base on digital,lowercase letters and capital letters
    python pydictor.py -base dLc				default length: min=1 and max=4

### 2. generate the dictionary base on custom character
##### cmd: -char   
	python pydictor.py -char abc123._@ --len 1 3
  
**note**:  When you need spaces and other special characters, double quotation marks surround all custom characters, Such as:"abc ABC123."

### 3. chunk multiply dictionary
##### cmd: -chunk
	python pydictor.py -chunk abc ABC 666 . _ @		generating all  possible permutations and combinations base on 'abc'、'ABC'、'666' 、'.'、'_'、'@'
  
**note**:  When you need spaces and other special characters, double quotation marks surround all custom characters, such as:abc " " 123 asdf

### 4. add prefix and suffix:
##### cmd: --head,--tail
	python pydictor.py -base L --len 1 4 --head a --tail 123
**note**:  prefix and suffix exclude from --len option,it's extra length

### 5. encode each items
##### cmd: --encode
    python pydictor.py -chunk abc ABC 123 123456 . @ _ --encode b64

### 6. specify output path
##### cmd: -o
    python pydictor.py -base d -o D:\output

### 7. special function plugins
##### cmd: -plug
##### example 4: using pid6 plugin generate post six length Chinese citizen id card number blasting dictionary
	python pydictor.py -plug pid6

##### example 5: using pid8 plugin generate post eight length Chinese citizen id card number blasting dictionary
	python pydictor.py -plug pid8

**note**:   default sex ='all', it decided by lib/data/data.py default_sex, and 'm' is Male, 'f' is Female

##### example 6: using extend plugin expand the raw word into a blasting dictionary base on the built-in rules 

1.  extend plug mainly directed against web application administrator to generate password
2.  You can put your own weak password wordlist in wordlist/Web，extend plug will auto unique them，new wordlist will contains them
3.  You can modify the directory of funcfg, extend_prefix.cfg、extend_suffix.cfg and extend_headtail.cfg arguments，set prefix, suffix, prefix + suffix when extended
4.  extend plug support leet mode and pick by lenght function，you can learn more in the following   

```
python pydictor.py -plug extend D:\word.txt -o D:\awesome\wordlist
```
##### example 7: using passcraper plugin crawl website generating password wordlist based on plain text found and extend rules

1.  the rules of passcraper plug and extend plug are the same
2.  passcraper plug will generate two wordlist，preffix with SCRATCH is raw wordlist by website plain text，
    and if you feel that there are a lot of unrelated words in the SCRATCH wordlist, 
    you can remove them, and then use the extend plugin to specify the new file to generate dictionary again.
3.  you can modify the funcfg/passcraper_blacklist.cfg file，add or delete useless words that need to be filtered out，also can modify lib/data/data.py file passcraper_filter argument，change the filter regular expressions
4.  with same extend plugin，you can put your weak password in /wordlist/Web，new wordlist will contains them

```
python pydictor.py -plug passcraper				using default file scraper.sites as multi-input file
python pydictor.py -plug passcraper http://www.example.com
```
### 8. handle wordlist's tools
##### cmd: -tool
##### example 8: safe delete tool shredder
	python pydictor.py -tool shredder 		delete the currently specified output path(default:results) files and all its dictionary files
    python pydictor.py -tool shredder base 		delete the files of it's prefix is "BASE" in currently specified output path

prefix(case insensitive) range in 13 items:base,char,chunk,conf,sedb,idcard,extend,uniqifer,counter,combiner,uniqbiner,scratch,passcraper

  besides，you can safe shred files or whole directory as following:

    python pydictor.py -tool shredder /data/mess
    python pydictor.py -tool shredder D:\mess\1.zip

  for improving the security delete speed, the default uses 1 times to erase and rewrite，you can modify lib/data/data.py file's file_rewrite_count and dir_rewrite_count value

##### example 9: remove duplicates tool uniqifer
	python pydictor.py -tool uniqifer /tmp/my.dic

##### example 10: word frequency statistics tool counter
	python pydictor.py -tool counter vs /tmp/mess.txt 100		select 100 words in /tmp/mess.txt file that appear in the most times and output to the terminal and saved to file

  **note**: default choose 100 items to print or save；default separator is:"\n",you can modify counter_split value in lib/data/data.py file

##### example 11: merge dictionary tool combiner
	python pydictor.py -tool combiner /my/messdir

##### example 12: remove duplicates after merging tool uniqbiner
	python pydictor.py -tool uniqbiner /my/messdir

### 9. using configuration file build dictionary
##### cmd: --conf
   this function contains all of "-base" and "-char" capacities，and more precise control

    python pydictor.py --conf				using default file build.conf build the dictionary
    python pydictor.py --conf /my/other/awesome.conf	using /my/other/awesome.conf build the dictionary

**note**: parsing rules details as following，besides referred to build.conf file

#### configuration parsing rules details:
```
 1. the basic unit of parsing is called an parsing element, an parsing element includes five elements, namely: head, character set, length range, encoding, tail, which can be omitted both head and tail;
A standard parsing element:head[characters]{minlength:maxlength}<encode-type>tail，a example parsing element：a[0-9]{4:6}<none>_
Its meaning build a dictionary that  prefix is "a" , character set is 0—9, don't encode,length range is 4—6 and  suffix is "_"
 2. current is support parsing one line
 3. one line can contains 10 parsing elements
such as:[4-6,a-c,A,C,admin]{3:3}<none>_[a,s,d,f]{2:2}<none>[789,!@#]{1:2}<none>,it contains three parsing elements
 4. if annotator "#" in first place, program won't parse this line
 5. conf function can build more precise dictionary up to single char

about character sets：
				   You can add the "-" in the middle of character sets beginning and ending to  join them
				   and can also use "," to separate multiple character sets, or a single character, or a single string, as an element of the character set;

supported encoding:
			   none    don't encode
			   b64     base64
			   md5     md5 digest algorithm output 32 char
			   md516   md5 digest algorithm output 16 char
			   sha1    sha1 digest algorithm
			   url     urlencode
			   sha256  sha256 digest algorithm
			   sha512  sha512 digest algorithm
```

### 10. pick by length function
##### cmd: --pick

1.  this function is currently only support extend, passcraper, Social Engineering Dictionary Builder
2.  it can be use --len to choose length to pick，and SEDB function can set it in SEDB interface   

##### example 13: only select the the password between the length 6-16    

	python pydictor -plug extend /awesome/ext.txt --pick --len 6 16

### 11. use leet mode
##### cmd: --mode

1.  this function is currently only support extend, passcraper, Social Engineering Dictionary Builder
2.  extend plug and passcraper plug default enable leet mode，and sedb default unable to use leet mode
3.  SEDB can enable leet mode and set code in SEDB interface
4.  enable leet mode cannot make wordlist decrease，it will increase wordlist on the basis of unable to use the leet mode


##### default leet table
	leet char = replace char

```
a = 4
b = 6
e = 3
l = 1
i = 1
o = 0
s = 5
```

##### code
```
0			default，replace all
1			left-to-right, replace all the first encountered leet char
2               	right-to-left, replace all the first encountered leet char
11-19			left-to-right, replace the first encountered leet char to maximum code-10 chars   
21-29			right-to-left, replace the first encountered leet char to maximum code-20 chars
```


##### code effection table

| code| old string         | new string        |
|:---:| :----------------: |:----------------: |
| 0   | as a airs trees    | 45 4 41r5 tr335   |
| 1   | as a airs trees    | 4s 4 4irs trees   |
| 2   | as a airs trees    | a5 a air5 tree5   |
| 11  | as a airs trees    | 4s a airs trees   |
| 12  | as a airs trees    | 4s 4 airs trees   |
| 13  | as a airs trees    | 4s 4 4irs trees   |
| 14  | as a airs trees    | 4s 4 4irs trees   |
| ... | as a airs trees    | 4s 4 4irs trees   |
| 21  | as a airs trees    | as a airs tree5   |
| 22  | as a airs trees    | as a air5 tree5   |
| 23  | as a airs trees    | a5 a air5 tree5   |
| 24  | as a airs trees    | a5 a air5 tree5   |
| ... | as a airs trees    | a5 a air5 tree5   |


besides,you also can:   

```
modify /funcfg/leet_mode.cfg, add or delete leet table items;   
modify /lib/lib/data.py, extend_leet、passcraper_leet、sedb_leet arguments, choose some functions whether default use leet mode;
modify /lib/data/data.py,leet_mode_code argument, choose default mode code;
```


### 12. social engineering dictionary
##### cmd: --sedb
    python pydictor.py --sedb
#
         _______                __   _          _
        |_   __ \              |  ] (_)        / |_
          | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
          |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
         _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
        |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                 \__.'


               Social Engineering Dictionary Builder
                                            Build by LandGrey
    --------------------------[ command ]--------------------------
    [+]help desc            [+]ls/show  option     [+]rm option
    [+]exit/quit            [+]clear/cls           [+]run
    [+]set option arguments [+]pick minlen maxlen  [+]mode code

    --------------------------[ option ]---------------------------
    [+]cname                [+]ename               [+]sname
    [+]birth                [+]usedpwd             [+]phone
    [+]uphone               [+]hphone              [+]email
    [+]postcode             [+]nickname            [+]idcard
    [+]jobnum               [+]otherdate           [+]usedchar
    pydictor SEDB>>

##### command:
```
help				reload interface
help desc			view the meaning for each items
ls or show			view the current settings
clear or cls		clear screen
exit or quit		exit the program
set					set option value
rm					remove option value
pick                select the length range
mode                enable leet mode and choose code
run					run Social Engineering Dictionary Builder
```

note:  
1. you can modify funcfg/sedb_tricks.cfg file，change the word transform prefix, suffix and prefix+suffix rules
2. you can put your own individual weak password wordlist in wordlist/SEDB, 
3. SEDB some little rules contains extend plugin function

##### Destination is just a point of departure，It's your show time.
