import requests
import base64
import yaml

ref = "<branch name>"
filepath = "<file_path"
token = "<access_token_for_github>"
owner="<repo_owner>"
repo="<repo_name>"  

def fetch_github_file(owner, repo, ref, filepath, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filepath}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.json()
        if content.get("type") == "file":
            return content["content"]
        else:
            print(f"Error: {filepath} is not a file.")
    else:
        print(f"Error: Failed to fetch file {filepath} (Status Code: {response.status_code})")
    return ""



# function to decode the output from the above function
def decode_base64(content):
    decoded_content = base64.b64decode(content).decode("utf-8")
    return decoded_content




# fucntion to get the data from the deine path

def get_resource_types_list(content):
    resources = []

    for component in content:
        resources.append(component['type'])

    return resources

# calling fucntion  to get the file from the github repo

file_content = fetch_github_file(owner, repo, ref, filepath, token)

if file_content:
    # calling the Decode fucntion to decode content
    decoded_content = decode_base64(file_content)

    try:
        decoded_data = yaml.safe_load(decoded_content)
        if isinstance(decoded_data, dict):
            resource_type = get_resource_types_list(decoded_data.get('shared-resources', []))
            print(f"Resource types: {resource_type}")
        else:
            print("Error: Failed to parse YAML file. Content is not a dictionary.")
    except Exception as e:
        print(f"Error: Failed to parse YAML file. {str(e)}")
