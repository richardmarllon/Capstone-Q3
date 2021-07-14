# Record Lesse

table to get the record of the lesse

## Schemas

|    key     | type |       description        |
| :--------: | :--: | :----------------------: |
|     id     | int  |     id of the record     |
|  lesse_id  | int  |     id of the lesse      |
|   car_id   | int  |      id of the car       |
| avaliation | int  | car and lesse avaliation |
|  comment   | str  | user experience comment  |
|    date    | str  |       record date        |

## Get record lesse by id

-> URL

`GET https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

-> Example

Request: `GET https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

Response:

{
"id": 1,
"lesse_id": 1,
"car_id": 3,
"avaliation": 5,
"comment": "clean and comfortable car",
"date": "2021/07/13"
}

## Update record lesse by id

-> URL

`PATCH https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

-> Example

Request: `PATCH https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

Request Body:

{
"comment": "adorable lesse"
}

Response:

{
"id": 1,
"lesse_id": 1,
"car_id": 3,
"avaliation": 5,
"comment": "adorable lesse",
"date": "2021/07/13"
}

## Delete record lesse by id

-> URL

`DEL https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

-> Example

Request: `DEL https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

Response:

''

## Create record lesse

-> URL

`POST https://capstone-q3.herokuapp.com/rlesse/register_lesse`

-> Example

Request: `POST https://capstone-q3.herokuapp.com/rlesse/register_lesse`

Request Body:

{
"lesse_id": 5,
"car_id": 10,
"avaliation": 3,
"comment": "DIRTY CAR",
"date": "2021/07/15"
}

Response:

{
"id": 2,
"lesse_id": 5,
"car_id": 10,
"avaliation": 3,
"comment": "DIRTY CAR",
"date": "2021/07/15"
}
