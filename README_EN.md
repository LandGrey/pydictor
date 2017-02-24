# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor) [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](http://www.gnu.de/documents/gpl-3.0.en.html)

**README.md [中文版](https://github.com/LandGrey/pydictor/blob/master/README.md)**

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

Q: Why I need to use pyictor ?
A: Too many reasons, whether you are using Python 2.7 version or Python 3.x version , pydictor can be run on Windows, Linux or Mac;
   you can use pydictor to generate common blasting password dictionary, custom password dictionary based on web content ,
   social engineering password dictionary, a series of advanced dictionary and etc., it can help you almost all works
   that relevant generate a password dictionary in pentesting.

Q: What is the goal of pydictor?
A: A useful and better password-generator that helps plenty of penetration testers work better.
```

## Start:
```
git clone https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
./pydictor.py
```

## Overview：
#### terminal display 
```
pydictor.py [options]
           -o        output_path
           -base     type
           -char     custom_char
           -chunk    <chunk1> <chunk2> ...
           -plug     [pid6,pid8,extend,passcraper]
           -tool     [shredder,uniqifer,counter,combiner,uniqbiner] <arguments ...>
           --len     minlen maxlen
           --sex     [m, f, all]
           --head    prefix_string
           --tail    suffix_string
           --encode  [none,b64,md5,md516,sha1,url,sha256,sha512]
           --conf    config_file_path
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
  -char Character       Use Custom Character build the dictionary
  -chunk Chunk [Chunk ...]
                        Use the string [Chunk Multiplication] build the dictionary
  -plug Plug [Plug ...]

                        Choose from    (pid6, pid8, extend, passcraper)
                            pid6       [id_card_post_6_number]     default sex:all
                            pid8       [id_card_post_8_number]     default sex:all
                            extend     [file_path]
                            passcraper [url_or_file_path]
  -o Output
                        Set the directory output path
                            default: pydictor\results
  -tool Tool [Tool ...]

                        Choose from    (shredder, uniqifer, counter, combiner, uniqbiner)
                            shredder   [file_or_dir]
                            uniqifer   [file_path]
                            counter    ['v','s','vs'] [file_path] [view_num]
                            combiner   [dir]
                            uniqbiner  [dir]
  --sex Sex
                        Choose from  (m, f, all)
                            m: Male        f: Female   all: Male and Female
  --len Minlen Maxlen
                        [Minimun_Length]  [Maximun_Length]
                                            Default: min=2  max=4
  --head Prefix         Add string head for the items
  --tail Suffix         Add string tail for the items
  --encode Encode
                        Choose from [none, b64, md5, md516, sha1, url, sha256, sha512]
  --conf [Conf_file_path]

                        Use the configuration file build the dictionary
                            Default: pydictor\build.conf
  --sedb                Enter the Social Engineering Dictionary Builder
```
#### pictures  
![passcraper](https://github.com/LandGrey/pydictor/raw/master/screenshots/passcraper.png "passcraper")  
![social engineering dictionary builder](https://github.com/LandGrey/pydictor/raw/master/screenshots/sedb.png "sedb")
## Functions & Usage:
### 1. generate the base dictionary
##### cmd: -base
##### example 1: generating a dictionary that specifying length using pure digital,lowercase letters,or capital letters
    python pydictor -base d --len 6 6			generate six length dictionary base on pure digital

##### example 2: generating a dictionary that using two of digital,lowercase letters and capital letters
    python pydictor -base dL --len 1 3

##### example 3: generating a dictionary base on digital,lowercase letters and capital letters
    python pydictor -base dLc					default length: min=2 and max=4

### 2. generate the dictionary base on custom character
##### cmd: -char   
	python pydictor -char abcABC123456._@ --len 6 8
  
**note**:  When you need spaces and other special characters, double quotation marks surround all custom characters, Such as:"abc ABC123."

### 3. chunk multiply dictionary
##### cmd: -chunk
	python pydictor -chunk abc ABC 666 . _ @			generating all  possible permutations and combinations base on 'abc'、'ABC'、'666' 、'.'、'_'、'@'
  
**note**:  When you need spaces and other special characters, double quotation marks surround all custom characters, such as:abc " " 123 asdf

### 4. add prefix and suffix:
##### cmd: --head,--tail
	python pydictor.py -base L --len 1 4 --head a --tail 123
**note**:  prefix and suffix exclude from --len option,it's extra length

### 5. encode every item
##### cmd: --encode
    python pydictor.py -chunk abc ABC 123 123456 . @ _ --encode b64

### 6. specify output path
##### cmd: -o
    python pydictor.py -base d -o D:\output

### 7. special function plugins
##### cmd: -plug
##### example 4: using pid6 plugin generate post six length Chinese citizen id card number blasting dictionary
	python pydictor -plug pid6

##### example 5: using pid8 plugin generate post eight length Chinese citizen id card number blasting dictionary
	python pydictor -plug pid8 --sex m

**note**:   default sex ='all', and 'm' is Male, 'f' is Female

##### example 6: using extend plugin expand the raw word into a blasting dictionary base on the built-in rules 
	python pydictor -plug extend D:\word.txt

##### example 7: using passcraper plugin crawl website generating password dictionary based on plain text found
    python pydictor -plug passcraper								using default file scraper.site as multi-input
	python pydictor -plug passcraper http://www.example.com

### 8. handle dictionary's tools
##### cmd: -tool
##### example 8: safe delete tool shredder
	python pydictor.py -tool shredder 			delete the currently specified output path(default:results) files and all its dictionary files
    python pydictor.py -tool shredder base 		delete the files of it's prefix is "BASE" in currently specified output path

prefix(case insensitive) range in 12 items:base,char,chunk,conf,sedb,idcard,extend,uniqifer,counter,combiner,uniqbiner,passcraper

  besides，you can safe shred files or whole directory as following:

    python pydictor.py -tool shredder /data/mess
    python pydictor.py -tool shredder D:\mess\1.zip

  for improving the security delete speed, the default uses 1 times to erase and rewrite，you can modify lib\data.py file's file_rewrite_count and dir_rewrite_count value

##### example 9: remove duplicates tool uniqify
	python pydictor.py -tool uniqify /tmp/my.dic

##### example 10: word frequency statistics tool counter
	python pydictor.py -tool counter vs /tmp/mess.txt 100		select 100 words in /tmp/mess.txt file that appear in the most times and output to the terminal and saved to file

  **note**: default choose 10 items to print or save；default separator is:"\n",you can modify counter_split value in lib\data.py file

##### example 11: merge dictionary tool combiner
	python pydictor.py -tool combiner /my/messdir

##### example 12: remove duplicates after merging tool uniqbiner
	python pydictor.py -tool uniqbiner /my/messdir

### 9. using configuration file build dictionary
##### cmd: --conf
   this function contains all of "-base" and "-char" capacities，and more precise control

    python pydictor.py --conf				    		using default file build.conf build the dictionary
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

### 10. social engineering dictionary
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
    ----------------------------------[ command ]------------------------------------
    [+]help desc     (View the description) |  [+]show name     (Show current settings)
    [+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)
    [+]run           (Build the dictionary) |
                                            |
    Usage Exp :show  (Show all of settings) |  help desc   (view all of descriptions)

    -------------------------------[ setting options ]--------------------------------
    [+]cname      [+]ename      [+]sname    |  [+]birth      [+]usedpwd    [+]phone
    [+]uphone     [+]hphone     [+]email    |  [+]postcode   [+]nickname   [+]idcard
    [+]jobnum     [+]otherdate  [+]usedchar |
                                            |
    Usage Exp :sname zhang wei zw zwell     |  * Each setting supports multiple values
    pydictor SEDB>>

##### command:
    help				reload sedb help
	help desc			view the meaning for each items
	show				view the current settings
	run					run sedb
	cls/clear			clear screen
	quit/exit			exit the program

##### Destination is just a point of departure，It's your show time.