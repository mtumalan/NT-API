# API de Cálculo de Número Faltante

Esta API en Django permite calcular el número faltante de un conjunto de los primeros 100 números naturales, del cual se ha extraído uno.

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalación y Ejecución

Sigue estos pasos para ejecutar la aplicación dentro de un contenedor Docker.

### 1. Clonar el Repositorio

```sh
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Construir y Ejecutar el Contenedor

```sh
docker-compose up --build
```
Esto iniciará el servidor Django dentro de un contenedor en el puerto 8000.

### 3. Acceder a la API

Una vez el contenedor esté corriendo, la API estará disponible en:

```sh
http://localhost:8000/api/missing-number/
```

Para probarla, puedes utilizar cURL o Postman.

## Uso

### Extraer un Número
Para extraer un número, realiza una petición POST con el número a eliminar:

```sh
curl -X POST http://localhost:8000/api/extract/ -H "Content-Type: application/json" -d '{"number": 42}'
```

Respuesta esperada:
```json
{
  "message": "Number 42 extracted successfully."
}
```

### Calcular Número Faltante
Para calcular el número faltante, realiza una petición GET:
```sh
curl -X GET http://localhost:8000/api/missing_number/
```

Respuesta esperada:
```json
{
  "missing_numbers": [42]
}
```

### Reiniciar el API
Para volver a iniciar el proceso y reiniciar la lista de números, Ingresar los siguientes comandos:

```sh
docker-compose down -v
docker-compose up --build
```