import boto3
from botocore.retries import bucket


# CREAMOS EL CLIENTE DE S3
client = boto3.client('s3')


# Crear un Bucket
response = client.create_bucket(
    ACL= 'private'|'public-read'|'public-read-write'|'authenticated-read',
    Bucket='bucket_name', # Nombre del bucket,
    CreateBucketConfiguration={
        "LocationConstraint":"region_location" # 
    }
)
# vemos la respuesta
print(response)


# Get a list of buckets in s3
# Obtener una lista de los buckets en el s3
response = client.list_buckets()
for b in response.get("Buckets",None):
    print(b.get("Name",None))


# UPLOAD  FILES 
# Subir archivos a un bucket de AWS
# debemos leer el archivo en modo binario
with open("file","rb") as f:
    data = f.read()
# defenimos el cliente
response = client.put_object(
    'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
    Body= data,
    Bucket = "bucket_name",
    Key="file_name"
)


# Delete a file from s3
# Eliminar un archivo del s3
response = client.delete_object(
    Bucket="bucket_name",
    Key="file_name"
)


# Get the list of objects in s3
# Obtener una lista de los objetos del s3
response = client.list_objects(
    Bucket = "bucket_name"
)
# iteramos en los nombres
for i in response.get("Contents",None):
    print(i.get("Key",None))
# Usamos .get("key",None) para que si no encuntra la llava
# no nos devuelva error sino None


# DOWNLOAD A FILE FROM S3
# Descargar un archivo del s3
#how to dowonload single file
client.download_file(Bucket="bucket_name",
    Key="file_name",
    Filename="path/file_name")