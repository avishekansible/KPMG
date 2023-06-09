import requests
import json

def get_azure_instance_metadata():
    url = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
    headers = {"Metadata": "true"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        metadata = response.json()
        return metadata
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve Azure instance metadata:", e)
        return None

# Example usage
metadata = get_azure_instance_metadata()
if metadata:
    # Print the entire metadata
    print(json.dumps(metadata, indent=4))

    # Retrieve a specific data key
    specific_key = "compute"
    if specific_key in metadata:
        print(json.dumps(metadata[specific_key], indent=4))
    else:
        print(f"Key '{specific_key}' not found in the metadata.")
