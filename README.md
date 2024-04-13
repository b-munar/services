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
<td>N/A</td>
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

## 2. Post services 

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
<td>N/A</td>
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