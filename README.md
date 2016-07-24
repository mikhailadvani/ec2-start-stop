ec2-start-stop
=========

Role to start/stop EC2 instance(s) and conditionally associate/disassociate elastic IP(s) to the same.  

Requirements
------------
- Python 2.7
- boto
- AWS access keys with EC2FullAccess privileges

Role Variables
--------------

- AWS_ACCESS_KEY_ID: Access key with EC2FullAccess privileges being set as environment variable as shown in the sample below
- AWS_SECRET_ACCESS_KEY: Corresponding secret access key to AWS_ACCESS_KEY_ID
- EC2_REGION: The AWS region of your infrastructure
- action: start/stop. Whether the instance(s) is/are to be started/stopped. **Default**: *start*
- reuse_existing_ip_allowed: yes/no. Re-use unassociated IP(s) allocated to your account. **Default**: *yes*
- release_on_disassociation: yes/no. Release the IP on disassociation. **Default**: *yes*
- roles_directory: roles. The directory in which the role is present. **Default**: *roles*
- instances.tags: Tags of the instance(s) you want to start/stop 
- instances.elastic_ip: yes/no. Whether you want an elastic_ip is to be associated or not. Elastic IP will be associated while starting and disassociated on stopping. Re-use & release are based on reuse_existing_ip_allowed & release_on_disassociation respectively.  


Example Playbook
----------------

`ansible-playbook ec2-start-stop.yml -e "action=start reuse_existing_ip_allowed=yes"`

`ansible-playbook ec2-start-stop.yml -e "action=stop release_on_disassociation=no"`

    
    - hosts: localhost
      connection: local
      environment:
        AWS_ACCESS_KEY_ID: "{{AWS_ACCESS_KEY_ID}}"
        AWS_SECRET_ACCESS_KEY: "{{AWS_SECRET_ACCESS_KEY}}"
        EC2_REGION: "{{EC2_REGION}}"
      roles:
      - {role: ec2-start-stop}

License
-------

MIT

Author Information
------------------

The role was created in 2016 by [Mikhail Advani](https://github.com/mikhailadvani "Github")

Twitter Handle: [@mikhail_advani](https://twitter.com/mikhail_advani "Twitter")
