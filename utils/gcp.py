#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import os
import pandas as pd

from google.cloud import bigquery
from google.cloud import storage


# In[3]:


class GCPUtils():
    
    def __init__(self, key_path):

        # Set the environment variable programmatically
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        
        self.storage_client = storage.Client()
        
    def pandas_to_gcs(self, df, blob_name, bucket_name=None):

        # Get the bucket object
        bucket_obj = self.storage_client.bucket(bucket_name)

        # Create a blob object
        blob_obj = bucket_obj.blob(blob_name)

        # Convert the DataFrame to CSV format
        csv_data = df.to_csv(index=False)

        # Upload the CSV data to the blob
        blob_obj.upload_from_string(csv_data, content_type='text/csv')

        print(f"DataFrame saved to {bucket_name}/{blob_name}")


# In[ ]:





# In[ ]:


# def bq_to_pandas(query):
    
#     return None


# In[ ]:


# def pandas_to_bq(df):
    
#     return None


# In[ ]:


# def _get_blob_(client, bucket_name, blob_name):

#     # Get a reference to a bucket
#     bucket = client.bucket(bucket_name)
    
#     # Download the file to a local temporary file
#     blob = bucket.blob(blob_name)
    
#     return blob

# def gcs_to_pandas(df):
    
#     # Define storage client & source paths
#     storage_client = storage.Client.from_service_account_json(key_path)
    
#     src_blob = get_blob(storage_client, src_bucket_name, src_blob_name)
#     # Download the blob to a BytesIO object
#     data = io.BytesIO()
#     blob.download_to_file(data)
#     data.seek(0)

#     # Read the data from the BytesIO object into a Pandas DataFrame
#     df = pd.read_csv(data)
    
#     return df


# In[ ]:


# def pandas_to_gcs(df):
    
#     # Define client
#     client = storage.Client.from_service_account_json(key)
    
#     # Get the bucket object
#     bucket = client.bucket(bucket)

#     # Create a blob object
#     blob = bucket.blob(blob)

#     # Convert the DataFrame to CSV format
#     csv_data = df.to_csv(index=False)

#     # Upload the CSV data to the blob
#     blob.upload_from_string(csv_data, content_type='text/csv')

#     print(f"DataFrame saved to {bucket}/{blob}")


# In[ ]:


# def create_table(client, table_ref, schema):

#     table = bigquery.Table(table_ref, schema=schema)
#     table = client.create_table(table)
#     print("Created table {}.".format(table.full_table_id))

