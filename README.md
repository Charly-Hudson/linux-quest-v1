# linux-ec2-learning

## First steps are to get some things installed:

I recommend getting a few things installed, like: 

* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) 
    * ~# if that didnt work please click [Here](https://www.putty.org)

* Within VSCode you may want to install the aws toolkit, simply search this extention ID in the extensions tab
```
amazonwebservices.aws-toolkit-vscode
```

# Lets get started
## The Network

You going to need 4 things for this network:

* 1. A VPC (Virtial Private Cloud)
    * To start with a VPC is required, we are setting up servers so we need to know where to point our traffic to. 
    lets navigate to VPC's in the AWs console and make a VPC with the IP Address :
    
    10.0.0.0/16

* 2. A Subnet
    * 
* 3. A Internet Gateway 
* 4. A Route Table
