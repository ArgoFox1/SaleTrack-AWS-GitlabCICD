![white_background](https://github.com/user-attachments/assets/c367799f-c87e-4fe0-ad3d-23e6d6810b0f)

# SaleTrack-AWS-GitlabCICD
SaleTrack project automatically deployed on AWS EC2 instance using GitLab CI/CD pipeline with Docker.

* Create security group for ec2 instance

   ```shell
   aws ec2 create-security-group --group-name my-sg --description "My security group"
   ```
* Make Acessable port 80
  
   ```shell
   aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp --port 80 --cidr 0.0.0.0/0
   ```
* Make Acessable port 5000
  
   ```shell
   aws ec2 authorize-security-group-ingress \
    --group-id $SECURITY_GROUP_ID \
    --protocol tcp --port 5000 --cidr 0.0.0.0/0
   ```
* Make Acessable port 22
  
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
   https://gitlab.com/api/v4/projects/(gitlab project id)/trigger/pipeline?token=      (gitlab runner token)&ref=main
   ```
