from flask import Flask, jsonify, request
import boto3
import botocore.exceptions

app = Flask(__name__)

# Replace this with the name of the S3 bucket you create manually
BUCKET_NAME = "buckettfortestt"

# Create an S3 client
s3_client = boto3.client('s3')


@app.route('/', methods=['GET'])
def index():
    """Return a simple message at the root of the application."""
    return jsonify({"message": "Welcome to the S3 Bucket Service! Use '/list-bucket-content/<path>' to get bucket content."})


@app.route('/list-bucket-content/<path:path>', methods=['GET'])
@app.route('/list-bucket-content/', defaults={'path': ''}, methods=['GET'])
def list_bucket_content(path):
    """
    Endpoint to list the content of an S3 bucket for the specified path.
    If no path is specified, the top-level content is returned.
    """
    try:
        # Ensure the path ends with a trailing slash if it's a directory
        if path and not path.endswith('/'):
            path += '/'

        # Fetch objects and directories at the specified path
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path, Delimiter='/')

        # Check if contents exist
        dirs = [prefix['Prefix'] for prefix in response.get('CommonPrefixes', [])]
        files = [content['Key'] for content in response.get('Contents', []) if content['Key'] != path]
        content = dirs + files

        return jsonify({"content": content}), 200

    except botocore.exceptions.ClientError as e:
        # Log the error details for debugging
        error_code = e.response.get("Error", {}).get("Code", "Unknown")
        print(f"AWS ClientError: {error_code}, {e}")
        return jsonify({"error": f"Unable to access the bucket. AWS Error: {error_code}"}), 500

    except Exception as e:
        # Log the generic error
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
