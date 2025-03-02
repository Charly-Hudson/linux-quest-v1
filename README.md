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

### For making this in the CLI see code below 

#### Creating a VPC
```
aws ec2 create-vpc --cidr-block "10.0.0.0/16" --instance-tenancy "default" --tag-specifications '{"resourceType":"vpc","tags":[{"key":"Name","value":"linux-learning"}]}' 
```

#### Modify VPC attribute
```
aws ec2 modify-vpc-attribute --vpc-id "preview-vpc-1234" --enable-dns-hostnames '{"value":true}' 
```

#### DescribeVPC's
```
aws ec2 describe-vpcs --vpc-ids "preview-vpc-1234" 
```

#### Create Subnet
```
aws ec2 create-subnet --vpc-id "preview-vpc-1234" --cidr-block "10.0.0.0/20" --availability-zone "us-east-1a" --tag-specifications '{"resourceType":"subnet","tags":[{"key":"Name","value":"linux-learning-subnet-public1-us-east-1a"}]}' 
```

#### Create an Internet Gateway
```
aws ec2 create-internet-gateway --tag-specifications '{"resourceType":"internet-gateway","tags":[{"key":"Name","value":"linux-learning-igw"}]}' 
```

#### Attach IGW
```
aws ec2 attach-internet-gateway --internet-gateway-id "preview-igw-1234" --vpc-id "preview-vpc-1234" 
```

#### Create Route Table
```
aws ec2 create-route-table --vpc-id "preview-vpc-1234" --tag-specifications '{"resourceType":"route-table","tags":[{"key":"Name","value":"linux-learning-rtb-public"}]}' 
```

#### Create Route
```
aws ec2 create-route --route-table-id "preview-rtb-public-0" --destination-cidr-block "0.0.0.0/0" --gateway-id "preview-igw-1234" 
```

#### Associate IGW
```
aws ec2 associate-route-table --route-table-id "preview-rtb-public-0" --subnet-id "preview-subnet-public-0" 
```

#### Describe ROute Table
```
aws ec2 describe-route-tables  
```