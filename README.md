# py-macchanger
<a href="https://docs.python-guide.org/starting/install3/linux/" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/61SA0Wq1P1L.png" width="80"> </a>

### Features Version 1.01
- Python 3
- Linux only (at the moment)
- super user needed

### Instructions
**1.** Download the repository, you can use the command below if you have git installed:

<code>git clone https://github.com/peleon02/py-macchanger</code>


**2.** Make sure that you have python 3 installed, just type python3 in your terminal
and you will see an interpreter if it is installed, if you don't have it, click in the python logo at the beginning

**3.** Go to the folder where you have the repository cloned, make sure you are in the folder which the repository is and use (of course it must be unziped, if you used git clone it should be already unziped)

<code>cd py-macchanger-master</code>

**4.** Now you have to run the program like <code>sudo python3 py-macchanger.py</code> and the arguments (check the section below)

### Arguments
######   You can use the short one with one "-" or you can use the long one with two "--"

| Argument| Help |
| ------ | ------ |
| -a / --about |Use it alone to know about me and the program |
| -m / --mac |Pass your new MAC (must be 6 pairs of alphanumerics characters) separated with ":" example <code>00:11:22:33:44:55</code> |
| -i / --interface |Pass the interface which you wanna change the MAC, to know your interface use ifconfig (if you can't run it install <code>net-tools</code>) |
| -r / --random |Pass it to generate random MACs  |

#### Combination of arguments
  **(examples only with short version but you can use long too)**

- -a

   <code>sudo python3 py-macchanger -a</code>

- -r -i  example:

  <code>sudo python3 py-macchanger -r -i eth0</code> (remember this is my interface it might not be the same as yours)
- -m -i example:

  <code>sudo python3 py-macchanger -m 00:14:22:91:56:37</code> (remember this a random mac as example)<code> -i eth0 </code>(remember this is my interface it might not be the same as yours) the whole code below:

  <code>sudo python3 py-macchanger -m 00:14:22:91:56:37 -i eth0 </code>
