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






def descargar_prefix(prefix):
    """
    Esta función obtiene todos un listado de todos los files 
    que contienen cierto prefijo, los descarga, 
    los extrae en una carpeta llamada "unpack"
    Y luego elimina los archivos.
    """
    # listado de los files con el prefijo:
    paginator = client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket='u-wigo-events',Prefix='production/2021/01')
    count = 1
    for page in pages:
        for obj in page['Contents']:
            nombre_file = obj.get("Key",None)
            client.download_file(Bucket=bucket,Key=nombre_file,Filename=path+'/descargas/file{}.json.gz'.format(count)) 
            print(f"Archivo {nombre_file} descargado como file{count}")
            count = count + 1 
            if count >= 500: 
                continue

        
    # rescatamos todos los files con el prefijo
    #os.chdir("descargas")
    lista_files = os.listdir()
    print(lista_files)
    for archivo in lista_files:
        patoolib.extract_archive(archivo,outdir="unpack")
        if os.path.exists(archivo):
            os.remove(archivo)
            
            