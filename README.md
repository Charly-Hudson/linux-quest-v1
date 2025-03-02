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

* 1. A VPC (Virtual Private Cloud)
    * To start with a VPC is required, we are setting up servers so we need to know where to point our traffic to. 
    lets navigate to VPC's in the AWs console and make a VPC with the IP Address :

    10.0.0.0/16

* 2. A Subnet
    * A subnet is required to place the ec2 inside so that should be our next step, add a Subnet with the ip address of:
    10.0.1.0/24

* 3. A Internet Gateway 
    * Lets make an Internet Gateway so that we can access the internet then attach that to our VPC.
    
* 4. A Route Table
    * Now finally we need to make a route table routing traffic from our Internet Gateway to our VPC.
