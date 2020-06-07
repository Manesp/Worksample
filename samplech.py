# Ingreso de credenciales y subida y bajada de archivos con S3 Bucket a AWS
import boto3
from botocore.client import Config



# Ingreso de credenciales.
print("Ingrese credenciales.")
access_key_id = "AKIAVVLED4RIT567M4TQ" #input("Acces key id: ")
secret_access_key = "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" #input("Secret Key: ")
nbucket = "demo.challenge" #input("Nombre del bucket: ")

s3 = boto3.resource(
        's3', 
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        config=Config(signature_version='s3v4')
    )


acc = input("1. Subir un archivo. 2. Descargar un archivo. Otra tecla. salir -> ")

if int(acc) == 1 : #Upload
    file = "test.png" #input(str("ingrese archivo que desea subir: "))
    data = open(file, 'rb')
    s3.Bucket(nbucket).put_object(Key = file,Body = data)
    print("Subido.")
elif int(acc) == 2 : #Download
    file = input(str("ingrese archivo que desea descargar: "))
    s3.Bucket(nbucket).download_file(file,"manu")
    print("Descargado.")
else :
    print("Sale del programa.")
    exit()
