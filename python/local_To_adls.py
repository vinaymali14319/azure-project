
from azure.storage.filedatalake import DataLakeServiceClient

account_name = "devopssavinay"
account_key = "K1PhR06p/Wzl91pMVWp9h4D27j4CFv1dAU43YAsyl4Q+OHFUW0zeGygGF4lT"
file_system_name = "project"  #container name
directory_name = "raw"  # directory name
local_file_path = "./sourcefiles/PLANE.pdf" 
destination_file_name = "PLANE.pdf" 

# Function to upload a file to ADLS
def upload_file_to_adls():
    # Create the service client
    service_client = DataLakeServiceClient(
        account_url=f"https://{account_name}.dfs.core.windows.net",
        credential=account_key
    )

    # Get a client for the file system (container)
    file_system_client = service_client.get_file_system_client(file_system=file_system_name)

    # Get a directory client
    directory_client = file_system_client.get_directory_client(directory_name)

    # Get a file client
    file_client = directory_client.create_file(destination_file_name)

    # Read the local file and upload its content
    with open(local_file_path, "rb") as file:
        file_contents = file.read()
        file_client.upload_data(file_contents, overwrite=True)

    print(f"File '{local_file_path}' uploaded successfully to ADLS as '{destination_file_name}'.")

# Call the function to upload the file
upload_file_to_adls()
