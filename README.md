# Function to fetch the data from the github repo 


### This template will help us to fetch the details of the perticular resource. Suppose that we are working on the ADO pipeline and I have many ADO pipline and I want to run the perticular pipeline. So I can fetch the details from the yaml [in my case, I am fetching only the resource type so that i can trigger the perticular resource pipeline].

-------
### You just need to follow the below steps to run the code:-

#### 1. Define the required details for the code:

````
ref = "<branch name>"
filepath = "<file_path"
token = "<access_token_for_github>"
owner="<repo_owner>"
repo="<repo_name>"  

````

#### 2. Install the required packages in your system.

````
pip3 install -r requirements.txt
````

#### 3. Its time to run the main python code.

````
python3 fetch.py
````