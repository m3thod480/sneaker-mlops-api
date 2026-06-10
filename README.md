# Sneaker MLOps API

Proyecto personal donde se despliega un modelo de Machine Learning en AWS utilizando herramientas habituales del ecosistema DevOps/MLOps.

La idea del proyecto consistió en exponer un modelo capaz de clasificar imágenes de zapatillas mediante una API para realizar inferencias. Además del modelo, el objetivo principal era trabajar todo el proceso de despliegue y automatización en la nube.

![Diagrama de arquitectura](Diagrama.png)

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

Se ha tratado de llevar un modelo que se entrenó hace un año a una idea de e-commerce real, donde se propone un modelo de búsqueda a través de visión artificial en un portal web. De este modo he podido cubrir todo el apartado de despliegue en AWS y algunos de los muros con los que uno se encuentra cuando intenta exponer un modelo de inteligencia artificial en el cloud
