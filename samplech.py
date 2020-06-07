# Ingreso de credenciales y subida y bajada de archivos con S3 Bucket a AWS
import boto3
from botocore.client import Config



# Ingreso de credenciales.
print("Ingrese credenciales.")
access_key_id = input("Acces key id: ")
secret_access_key = input("Secret Key: ")
nbucket =  input("Nombre del bucket: ")

# Logueo con las keys ingresadas
s3 = boto3.resource(
        's3', 
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        config=Config(signature_version='s3v4')
    )

# Se le solicita al usuario el código de la acción que desea realizar
acc = input("1. Subir un archivo. 2. Descargar un archivo. Otra tecla. salir -> ")

if int(acc) == 1 : #Upload
    file = input(str("ingrese archivo que desea subir: ")) # Pedimos el nombre del archivo a subir
    data = open(file, 'rb')
    s3.Bucket(nbucket).put_object(Key = file,Body = data)
    print("Subido.") # Informamos al usuario que la acción se realizó
elif int(acc) == 2 : #Download
    file = input(str("ingrese archivo que desea descargar: ")) # Pedimos el nombre del archivo a bajar
    s3.Bucket(nbucket).download_file(file,"manu")
    print("Descargado.") # Informamos al usuario que la acción se realizó
else :
    print("Sale del programa.")
    exit()
