# HTTP Service for S3 Buckets  

A Python-based HTTP service to interact with Amazon S3 storage using simple REST APIs. This service allows you to list the contents of an S3 bucket, navigate through directories, and view the files stored in your S3 bucket. It's an easy way to explore and manage the contents of your S3 storage without directly interacting with the AWS console.

## Repository Name: **http-service-python-s3**  

## Features  
- List top-level content in your S3 bucket.  
- Browse through specific directories in your S3 bucket.  
- Fetch file details and directory structure.  
- Simple, lightweight REST API with Flask.  

## Requirements  
Before running the application, make sure you have the following installed and configured:  

1. **Python** (version 3.7 or newer)  
2. **AWS CLI** (to configure your AWS credentials)  

Additionally, the application relies on external libraries which you can install via pip.  

## How to Set Up and Use  

### Step 1: Clone the Repository  

Start by cloning the repository to your local machine:  

```bash  
git clone https://github.com/your-akashsilam/http-service-python-s3.git  
cd http-service-python-s3

### Step 2: Create a Virtual Environment
Create a virtual environment to isolate the project dependencies:

bash
Copy code
python -m venv env  
Now, activate the virtual environment:

On Windows:
bash
Copy code
env\Scripts\activate  
On macOS/Linux:
bash
Copy code
source env/bin/activate  
Step 3: Install Required Dependencies
Install all the required libraries listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt  
Step 4: Configure AWS Credentials
The application uses AWS SDK (boto3) to interact with your S3 bucket. To authenticate the application with your AWS account, you need to configure AWS credentials using the AWS CLI:

bash
Copy code
aws configure  
This command will prompt you to enter your AWS Access Key ID, Secret Access Key, Region, and Output Format. Make sure to provide the correct information.

You can get these credentials from your AWS IAM (Identity and Access Management) console.

Step 5: Set Your S3 Bucket Name
Open the main.py file and replace the BUCKET_NAME variable with the name of your S3 bucket:

python
Copy code
BUCKET_NAME = "your-s3-bucket-name"  
Step 6: Run the Application
Start the Flask application by running the following command in your terminal:

bash
Copy code
python main.py  
This will start a local development server, and you will be able to access the service at http://127.0.0.1:5000.

Step 7: Make API Requests
Now that your service is running, you can interact with it through HTTP requests. You can use your browser or an API tool like Postman to send GET requests.

1. Get top-level content of the bucket:
Send a GET request to http://127.0.0.1:5000/list-bucket-content/ to list the contents of the S3 bucket.

Example Request:

http
Copy code
GET http://127.0.0.1:5000/list-bucket-content/
Example Response:

json
Copy code
{
  "content": ["dir1", "dir2", "file1", "file2"]
}
This will return all top-level files and directories in the bucket.

2. Get content of a specific directory (e.g., dir1):
Send a GET request to http://127.0.0.1:5000/list-bucket-content/dir1 to see the contents of dir1.

Example Request:

http
Copy code
GET http://127.0.0.1:5000/list-bucket-content/dir1
Example Response:

json
Copy code
{
  "content": []
}
This will return the content inside dir1. If the directory is empty, it will return an empty array.

3. Get content of another directory (e.g., dir2):
Send a GET request to http://127.0.0.1:5000/list-bucket-content/dir2 to see the contents of dir2.

Example Request:

http
Copy code
GET http://127.0.0.1:5000/list-bucket-content/dir2
Example Response:

json
Copy code
{
  "content": ["file1", "file2"]
}
This will return the files inside dir2. If there are any files stored in the directory, they will be shown.

Example Use Cases
View S3 Bucket Contents: Quickly list the files and directories in your S3 bucket.
Explore Folders and Files: Navigate through folders in your S3 bucket to check the stored files.
Automation: Integrate this service with other automation tools to interact with your S3 bucket.
Why Use This Service?
Ease of Access: Provides an HTTP interface to interact with S3, which is simple to use and doesn't require logging into AWS.
REST API: Built using Flask, which makes it easy to integrate with other applications or services.
Simple Setup: Easy to set up on your local machine and requires minimal configuration.


