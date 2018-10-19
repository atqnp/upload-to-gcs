from google.cloud import storage

def uploadtogcs(filename):
    """
    arg: filename
    upload the filename to Google Cloud Storage
    an account JSON file is required for authentication
    """
    path = 'path/to/file' + filename
    client = storage.Client.from_service_account_json('MY-ACCOUNT.json')
    bucket = client.get_bucket('MY-BUCKET')
    blob = bucket.blob(path)
    blob.upload_from_filename(filename)
   
upload = uploadtogcs("test_file.csv")
