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

#### Describe Route Table
```
aws ec2 describe-route-tables  
```

