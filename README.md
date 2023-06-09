# KPMG
Problem 2. In this code, the get_azure_instance_metadata function sends an HTTP GET request to the Azure Metadata service URL http://169.254.169.254/metadata/instance?api-version=2021-02-01 to retrieve the instance metadata. The Metadata header is set to true to indicate that metadata is being requested.

If the request is successful, the JSON response is parsed, and the entire metadata is printed using json.dumps with an indentation of 4 spaces. You can modify this behavior according to your needs.

To retrieve a specific data key, you can provide the key name (e.g., "compute") and check if it exists in the metadata dictionary. If found, the corresponding value is printed as JSON.

Please note that this code assumes you are running it within an Azure instance with the Azure Metadata service available at the given IP address. Make sure to install the requests library if it's not already installed (pip install requests).
