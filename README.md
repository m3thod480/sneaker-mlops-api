# Sneaker MLOps API

Proyecto personal para practicar el despliegue de modelos de Machine Learning en AWS utilizando herramientas habituales del ecosistema DevOps/MLOps.

La idea del proyecto es sencilla: entrenar un modelo capaz de clasificar imágenes de zapatillas y exponerlo mediante una API para realizar inferencias. Además del modelo, el objetivo principal era trabajar todo el proceso de despliegue y automatización en la nube.

## Tecnologías utilizadas

* Python
* TensorFlow
* FastAPI
* Docker
* AWS ECS Fargate
* Amazon ECR
* Terraform
* GitHub Actions

## Objetivos del proyecto

Con este proyecto he querido practicar varios conceptos:

* Entrenamiento de un modelo de visión por computador.
* Creación de una API para servir predicciones.
* Contenerización con Docker.
* Despliegue en AWS utilizando ECS Fargate.
* Infraestructura como código con Terraform.
* Automatización mediante pipelines CI/CD.

## Arquitectura

El flujo general es el siguiente:

1. El modelo se entrena y se empaqueta junto con la aplicación.
2. La API FastAPI expone un endpoint para realizar inferencias.
3. La aplicación se ejecuta dentro de un contenedor Docker.
4. La imagen se almacena en Amazon ECR.
5. Terraform crea la infraestructura necesaria en AWS.
6. GitHub Actions automatiza el proceso de despliegue.

## Estado actual

Proyecto desarrollado con fines formativos para seguir aprendiendo sobre Machine Learning, Cloud y MLOps.

Hay varios aspectos que podrían ampliarse en el futuro, como monitorización de métricas del modelo, gestión de versiones de modelos o despliegues más avanzados.

## Autor

Juan José Collado
