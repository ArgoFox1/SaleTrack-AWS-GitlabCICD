![white_background](https://github.com/user-attachments/assets/c367799f-c87e-4fe0-ad3d-23e6d6810b0f)

# SaleTrack-AWS-GitlabCICD
SaleTrack project automatically deployed on AWS EC2 instance using GitLab CI/CD pipeline with Docker.

* Create security group for ec2 instance

   ```shell
   aws ec2 create-security-group --group-name my-sg --description "My security group"
   ```
* Allow Port 80 (HTTP)
  
   ```shell
   aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp --port 80 --cidr 0.0.0.0/0
   ```
* Allow Port 5000 (FLASK)
  
   ```shell
   aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp --port 5000 --cidr 0.0.0.0/0
   ```
* Allow Port 22 (SSH)
  
   ```shell
   aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp --port 22 --cidr $(curl -s https://checkip.amazonaws.com)/32
   ```
* Create Keypair
  
   ```shell
  aws ec2 create-key-pair --key-name my-keypair --query 'KeyMaterial' --output text > my-keypair.pem
            
* Create EC2 Instance
   ```shell
   aws ec2 run-instances \
    --image-id ami-0090963cc60d485c3 \
    --count 1 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids $SECURITY_GROUP_ID \
   ```
* Connect EC2 Instance
   ```shell
   ssh -i yourkeypair.pem ec2-user@ec2publicip
   ```
![Screenshot 2025-03-08 130533](https://github.com/user-attachments/assets/4289fc03-cfb4-41ee-b860-5dd35aeaa3c1)

* Creating github webhook for gitlab 
   ```shell
   https://gitlab.com/api/v4/projects/(gitlab project id)/trigger/pipeline?token=(gitlab runner token)&ref=main
   ```
* Its must be look like this after entering payload url 
![Screenshot 2025-03-11 125543](https://github.com/user-attachments/assets/eae20375-e5e8-4f31-b297-201e07fe1e6f)

* After creating webhook its push every update you made in github repo to the gitlab ,  now you can access web server
   ```shell
   publicip:5000
   ```
* In server footages
![Screenshot 2025-03-11 130229](https://github.com/user-attachments/assets/8ba6e4b5-dbe6-49b3-a14d-5fb036f52784)

![Screenshot 2025-03-11 130256](https://github.com/user-attachments/assets/18d0c490-4f7a-4356-addb-86b4ef74f3eb)

