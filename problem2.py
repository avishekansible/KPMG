import requests
import json
import base64   

proxies = {
    "http": None,
    "https": None
}

def get_azure_instance_metadata():
    url = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
    headers = {"Metadata": "true"}

    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        metadata = response.json()
        return metadata
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve Azure instance metadata:", e)
        return None

#def print_json_obj_to_terminal(json_obj):
#   print(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': ')))

metadata = get_azure_instance_metadata()
if metadata:
    # Print the entire metadata
    print(json.dumps(metadata, sort_keys=True, indent=4, separators=(',', ': ')))

    # Retrieve a specific data key
    specific_key = "compute"
    if specific_key in metadata:
        print(json.dumps(metadata[specific_key], sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print(f"Key '{specific_key}' not found in the metadata.")
