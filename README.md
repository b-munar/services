# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/services

2. 

```bash
docker compose build
docker compose up
```


El servicio de Servicios de terceros.

## 1. Get services 

Retorna servicios.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6750/services</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td> "Authorization": "Bearer eyJ0eXAiOiJKV1QiL..."/td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "services": [
        {
            "id": "971df62f-dc42-481b-b320-2d090ef5aaa1",
            "name": "service 1",
            "description": "description 1",
            "cost": 20.0,
            "taxes": 5.0,
            "address": "direction",
            "details": "details",
            "updateAt": "2024-04-13T16:33:15",
            "createdAt": "2024-04-13T16:33:15"
        },
        {
            "id": "1a848fa7-decb-4a81-9b9f-bdf5d5a39a30",
            "name": "service 1",
            "description": "description 1",
            "cost": 20.0,
            "taxes": 5.0,
            "address": "direction",
            "details": "details",
            "updateAt": "2024-04-13T16:35:25",
            "createdAt": "2024-04-13T16:35:25"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Crear services 

Permite realizar creación de servicios.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6750/services</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td> "Authorization": "Bearer eyJ0eXAiOiJKV1QiL..."</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
 "name": "service 1",
 "description": "description 1",
 "cost": 20.0,
 "taxes": 5.0,
 "address": "direction",
  "details": "details"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "1a848fa7-decb-4a81-9b9f-bdf5d5a39a30",
    "name": "service 1",
    "description": "description 1",
    "cost": 20.0,
    "taxes": 5.0,
    "address": "direction",
    "details": "details",
    "updateAt": "2024-04-13T16:35:25",
    "createdAt": "2024-04-13T16:35:25"
}
```
</td>
</tr>
</tbody>
</table>

## 3. Post Agendar servicios 

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6750/services/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td> "Authorization": "Bearer eyJ0eXAiOiJKV1QiL..."</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
 {
 "service_id": "51d7ea07-bb98-4000-9a10-b60bfcf5c848",
 "amount": 2
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
  "id": "6c697c2f-bb1f-4298-a5b3-ec67bbae42e4",
  "service_id": "51d7ea07-bb98-4000-9a10-b60bfcf5c848",
  "amount": 2,
  "service": {
    "name": "service 3",
    "description": "description 3",
    "cost": 20.0,
    "taxes": 5.0,
    "address": "direction",
    "details": "details"
  }
}
```
</td>
</tr>
</tbody>
</table>


## 4. Listar servicios agendados 

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6750/services/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td> "Authorization": "Bearer eyJ0eXAiOiJKV1QiL..."</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>
NA
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
  "services": [
    {
      "id": "3e1bacc2-6bd5-4365-a804-f8f54c45dfe7",
      "service_id": "06adb3d5-f9fe-4b20-acfe-62b50e9e0f80",
      "amount": 2,
      "service": {
        "name": "service 1",
        "description": "description 1",
        "cost": 20.0,
        "taxes": 5.0,
        "address": "direction",
        "details": "details"
      }
    },
    {
      "id": "6c697c2f-bb1f-4298-a5b3-ec67bbae42e4",
      "service_id": "51d7ea07-bb98-4000-9a10-b60bfcf5c848",
      "amount": 2,
      "service": {
        "name": "service 3",
        "description": "description 3",
        "cost": 20.0,
        "taxes": 5.0,
        "address": "direction",
        "details": "details"
      }
    },
    {
      "id": "6a8b2b5a-6825-44cb-aea1-5b602bd8280b",
      "service_id": "51d7ea07-bb98-4000-9a10-b60bfcf5c848",
      "amount": 2,
      "service": {
        "name": "service 3",
        "description": "description 3",
        "cost": 20.0,
        "taxes": 5.0,
        "address": "direction",
        "details": "details"
      }
    }
  ]
}
```
</td>
</tr>
</tbody>
</table>