#Dockerfile

#Para que la base del dockerfile sea Ubuntu.
FROM ubuntu

#Uso de python.
FROM python:3.10.13

#Guardando el archivo httpCliente.py en /opt/.
ADD httpCliente.py /opt/

