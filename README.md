# linux-ec2-learning

## First steps are to get some things installed:

I recommend getting a few things installed, like: 

* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) 
    * ~# if that didnt work please click [Here](https://www.putty.org)

* Within VSCode you may want to install the aws toolkit, simply search this extension ID in the extensions tab
```
amazonwebservices.aws-toolkit-vscode
```

# Lets get started
## The Network

You going to need 4 things for this network:

* 1. ### A VPC (Virtual Private Cloud)
    * To start with a VPC is required, we are setting up servers so we need to know where to point our traffic to. 
    lets navigate to VPC's in the AWs console and make a VPC with the IP Address :

    10.0.0.0/16

* 2. ### A Subnet
    * A subnet is required to place the ec2 inside so that should be our next step, add a Subnet with the ip address of:
    10.0.1.0/24

* 3. ### A Internet Gateway 
    * Lets make an Internet Gateway so that we can access the internet then attach that to our VPC.

* 4. ### A Route Table
    * Now finally we need to make a route table routing traffic from our Internet Gateway to our VPC.

### For making this in the CLI see code linked below 
Click [Here](./Console-README.md) for Code 

# Security Groups and Instances

## Launching an instance and doing it right! 

* 1. ### Names! 
    * You will need to name your instance, keep it appropriate, in this instance i recommend calling this "linux learning"

* 2. ### Your AMI (amazon machine image)
    * You need to make sure you are selecting the right AMI, in this instance i recommend using the Amazon Linux 2 AMI - Kernel 5.10, SSD Volume Type

* 3. ### Key Pairs!
    * You need to ensure you have a keypair active on this instance so i recommend making one. this has a few steps:
    * 1. Create a new keypair 
    * 2. I recommend keeping most of the settings the same but change the **.pem** to a **.ppk**
    * 3. Create key pair and ensure its selected
    # **Notice That a file will download you will need this do not delete it**

* 4. ### Network settings!!
    * You will need to change some network settings around!
    * Firstly you will need to choose the right VPC so use the VPC you made **NOT THE DEFAULT**
    * Next choose the subnet you made
    * Now you need to enable auto-assign public-IP
    * Then you need to create a security group:
        - Name: Linux-Learning-SG
        - Leave the SSH rule alone
        - Add a rule for HTTP and HTTPS making them anywhere (ipv4 anyone 0.0.0.0/0 rules should apply)

* 5. ### Storage!
    *  You should keep the size of your volume the same (8gb) but i recommend changing form a GP3 to a GP2

* 6. ### Advanced Details !!
    * Now for the advanced details the only real thing we need to change is the addition of some user data, so scroll to the berry bottom and add the following
```
#!/bin/bash

sudo yum install pip -y
sudo yum install tree -y
```
* 7. Launch instance!

# Putty Setup 

## In a few simple steps lets connect to that instance !

* 1. The key!
    * You will need to locate your **.ppk** key, this should be in your downloads folder
    * I recommend moving this to a secure location it will not be easily seen or located
    * once you have it stored safely you will need to open putty, in the left menu panel click the **+** next to **SSH** and then **Auth** respectively revealing the credentials tab. select that. This will give you the option to search for your private key with the browse button. 
    * Once you have your PPK key located head back to the main screen by clicking the session tab at the very top, by now you should have a public ip on your aws instance copy that IP address and paste it into the **Host Name (or IP address)**
    *  Now i recommend typing in the saved sessions input box "Linux Learning" the clicking the save button on the right hand side. finally pressing the open button at the bottom.
    * Finally i recommend clicking the accept button for any popups. 

# The Linux System !

## The Linux Quest !!

### Quest 1 Downloading The Quest!

Lets start by firstly downloading the Quest from this URL:
```
https://develop.charlyhudson.co.uk
```
There are afew ways to do so, lets find out how.

The Amazon Linux 2 AMI is based off of a [RedHat](https://developers.redhat.com/cheat-sheets/linux-commands-cheat-sheet) Distro, SO the Linux RedHat commands should work, here is a [Cheat Sheet](https://developers.redhat.com/cheat-sheets/linux-commands-cheat-sheet) for when you are stuck!

### Quest 2 Viewing the Quest

Now we have the quest, lets view it. You will notice its a .zip file, lets see how we can upzip that.

||
```
unzip linux-Quest.zip
```
||
