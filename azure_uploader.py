import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()

# Azure connection string .env se aayegi ya directly pass kar sakte hain
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "server-logs-archive"

def upload_log_to_azure(local_file_path, destination_blob_name=None):
    if not AZURE_CONNECTION_STRING:
        print("[!] Azure connection string nahi mili. Skipping Azure upload.")
        print("[*] (Local mode me file safe hai aur code verified hai)")
        return False

    if destination_blob_name is None:
        destination_blob_name = os.path.basename(local_file_path)

    try:
        print(f"[*] Uploading {local_file_path} to Azure Blob Storage...")
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        
        # Container exist karta hai ya nahi, check/create karein
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        if not container_client.exists():
            container_client.create_container()

        # Blob upload karein
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=destination_blob_name)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"[+] Successfully uploaded to Azure container: {CONTAINER_NAME}/{destination_blob_name}")
        return True
    except Exception as e:
        print(f"[!] Azure upload error: {e}")
        return False