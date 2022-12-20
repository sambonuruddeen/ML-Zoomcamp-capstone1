# ML Zoomkcamp Capstone Project 1

The Dataset for this work is from [Zindi Africa](zindi.africa) Financial Inclusion in Africa [Challenge](https://zindi.africa/competitions/financial-inclusion-in-africa)

The objective of the competition is to create a machine learning model to predict which individuals are most likely to have or use a bank account. 

You are asked to predict the likelihood of the person having a bank account or not (Yes = 1, No = 0).

#
**Please note that all the code in this repository is written and tested on a Linux 
machine**

- OS:  Ubuntu 20.04 LTS
- Python: 3.10
- pip: 22.2.1
- Docker version: 20.10.17, build 100c701

# Setup
**Follow the setup instructions below**


Build Docker Image

- `docker build --tag capstone-project .`

Run image as a container

To locate our image with the tag you created above, run the command below

- `docker images`

Choose the image you want to run and execute the docker `run command` followed by the image name

- `docker run -it --rm -p 8080:8080 capstone-project:latest`

After succesfully runing the command above, you will see that docker is running.

## Test 

Open a new terminal window with the app by running in another window and run the command below:

- `python3 test.py`

- Finally, Upload the docker image to DockerHub or Amazon ECR using the `docker push <image_name>` command

#
## Deployment on AWS Lambda
- Go to AWS Console and Lambda
- Create a function
- Choose `container image` and fill in the necessary details
- Select **browse image** to choose from our list of images
- Finally, choose **create function**

The lambda function will now be created, we can go ahead to start testing it. Follow the instructions in this [video](https://youtu.be/kBch5oD5BkY?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR) to learn how to deploy a docker image to AWS Lambda
#
## Deployment on Kubernetes
You can learn how to deploy kubernetes service using by following this [ML Zoomcamp Video](https://youtu.be/PPUCVRIV9t8?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR)

**Setup local Kubernetes cluster by installing kubectl & kind**

#### create deployment
-  Deployment configuration can be found in the [deployment.yaml](deployment.yaml) file
- `kind load docker-image <image_name> `
- `kubectl apply -f deployment.yaml`
- `kubectl get deployment`
- `kubectl port-forward <port_name>`

#### Create Service
- configuration can be found in the [service.yaml](service.yaml) file
- `kubectl apply -f service.yaml`
- `kubectl get service`
- `kubectl port forward service/<service_name> 8080:80`


### **Files**

- Dataset: [Train.csv](Train.csv), [Test.csv](Test.csv), [SampleSubmission.csv](SampleSubmission.csv), [VariableDefinition.csv](VariableDefinition.csv)
- Model: [zindi-fi.bin](zindi-fi.bin), [dv.bin](dv.bin)
- Prediction: [lambda_fucntion.py](lambda_fucntion.py), [test.py](test.py)
- Jupyter Notebook: [Zindi_Financial_Inclusion.ipynb](Zindi_Financial_Inclusion.ipynb), [predict-test.ipynb](predict-test.ipynb)
- Other: [Dockerfile](Dockerfile) [deployment.yaml](deployment.yaml) [service.yaml]([service.yaml])

