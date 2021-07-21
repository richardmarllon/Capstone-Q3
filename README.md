# HTTP status

201 -> Request was successful and that a new resource was created.

204 -> The request was successful and the user does not need to leave the current page

200 -> This request was successful.

401 -> User I don't have valid credentials to access the route

400 -> Server is unable to process the request due to a user error, either by syntax or any other reason

404 -> The server cannot find the requested resource.

403 -> The user does not have access rights to the content so the server is refusing to respond.

# Record Lesse

table to get the record of the lesse

## Schemas

|    key     | type |       description        |
| :--------: | :--: | :----------------------: |
|     id     | int  |     id of the record     |
| lessee_id  | int  |     id of the lesse      |
|   car_id   | int  |      id of the car       |
| avaliation | int  | car and lesse avaliation |
|  comment   | str  | user experience comment  |
|    date    | str  |       record date        |

## `Endpoints and methods:`

## Get record lessee by id

-> URL and method:

> GET: `https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

**Response example:**

Request: `GET https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

```JSON
{
"id": 1,
"lessee_id": 1,
"car_id": 3,
"avaliation": 5,
"comment": "clean and comfortable car",
"date": "2021/07/13"
}
```

## Update record lesse by id

-> URL

> PATCH `https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

-> Example

Request: `PATCH https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

**Body request example:**

```JSON
{
"comment": "adorable lesse"
}
```

**Response example:**

```JSON
{
"id": 1,
"lessee_id": 1,
"car_id": 3,
"avaliation": 5,
"comment": "adorable lesse",
"date": "2021/07/13"
}
```

## Delete record lesse by id

-> URL

> DEL `https://capstone-q3.herokuapp.com/rlesse/register_lesse/<id>`

-> Example

Request: `DEL https://capstone-q3.herokuapp.com/rlesse/register_lesse/1`

**Response example:**

```JSON
" "
```

## Create record lesse

-> URL

> POST `https://capstone-q3.herokuapp.com/rlesse/register_lesse`

-> Example

Request: `POST https://capstone-q3.herokuapp.com/rlesse/register_lesse`

**Body request example:**

```JSON
{
"lessee_id": 5,
"car_id": 10,
"avaliation": 3,
"comment": "DIRTY CAR",
"date": "2021/07/15"
}
```

**Response example:**

```JSON
{
"id": 2,
"lessee_id": 5,
"car_id": 10,
"avaliation": 3,
"comment": "DIRTY CAR",
"date": "2021/07/15"
}
```

# User locator

table to get the data of user locator

## Schemas

# User Lessee

Table to get the user lessee

## Schemas

|     key      | type |     description     |
| :----------: | :--: | :-----------------: |
|      id      | int  |   id of the user    |
|     name     | str  |      user name      |
|  last_name   | str  |  user's last name   |
| phone_number | str  | user's phone number |
|    email     | str  |    user's email     |
|     city     | str  |     user's city     |
|    state     | str  |    user's state     |
|     cnh      | str  |  user's CNH number  |
|     cpf      | str  |  user's CPF number  |
|   password   | str  |   user's password   |

## `Endpoints and methods:`

## Register

-> URL and method:

> POST:` https://capstone-q3.herokuapp.com/lessee/register`

**Body request example:**

```JSON
{
	"email": "email@email.com",
	"password": "123aA",
	"name": "user",
	"last_name": "test",
    "phone_number": "(44)99988-5544",
	"cpf": "111.222.333-44",
	"city": "Rio de Janeiro",
	"state": "RJ",
	"cnh": "12345678911"
}
```

Response: `status 201 - CREATED`

```JSON
{
    "id": 1,
    "name": "user",
    "last_name": "test",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "phone_number": "44999885544",
    "email": "email@email.com"
}
```

## Login

-> URL and method:

> POST:` https://capstone-q3.herokuapp.com/lessee/login`

**Body request example:**

```JSON
{
	"cpf": "111.222.333-44",
	"password": "123aA"

}
```

Response: `status 200 - OK`

```JSON
{
    "user": {
        "id": 1,
        "name": "user",
        "last_name": "test",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "email": "email@email.com",
        "phone_number": "44999885544"
    },
    "access_token": "eyJUzI1NiJ9.eyJmcmVzaCI6ZmFsc2Us2VyINnOSwiZXhwIjoxNjI2NTkxMTE5fQ.AOpSzar1EoWt2Uyp0jZM"
}
```

## Get user

-> URL and method:

> GET:` https://capstone-q3.herokuapp.com/lessee/user/<id>`

**Request example:**

GET without a body: `https://capstone-q3.herokuapp.com/lessee/user/1`

Response: `status 200 - OK`

```JSON
{
    "user": {
        "id": 6,
        "name": "user",
        "last_name": "test",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "phone_number": "44999885544",
        "email": "email@email.com"
    },
    "avaliations_received": [],
    "avaliations_give": []
}
```

## Update user

**You need to own the resource and be logged to update.**
You can change any key from your own user.

URL and method:

> PATCH: `https://capstone-q3.herokuapp.com/lessee/update/<id>`

**Request example:**

PATCH: `https://capstone-q3.herokuapp.com/lessee/update/1`

Authorization:

```javascript
{
    headers: {
        Authorization: "Bearer access_token";
    }
}
```

Body:

```JSON
{
	"email": "new@email.com",
	"password": "anotherPass"
}
```

Response: `status 200 - OK`

```JSON
{
    "id": 1,
    "name": "user",
    "last_name": "test",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "phone_number": "44999885544",
    "email": "new@email.com"
}
```

## Delete user

**You need to own the resource and be logged to delete.**

-> URL and method:

> DELETE:` https://capstone-q3.herokuapp.com/lessee/update/<id>`

**Request example:**

DELETE without a body: `https://capstone-q3.herokuapp.com/lessee/update/1`

Authorization:

```javascript
{
    headers: {
        Authorization: "Bearer access_token";
    }
}
```

Response: ` status 204 - NO CONTENT`

# Car

Table to get the car

## Schemas

|       key        | type |         description         |
| :--------------: | :--: | :-------------------------: |
|        id        | int  |        id of the car        |
|       year       | int  |       year of the car       |
|  license_plate   | str  |     license_plate plate     |
|      model       | str  |          car model          |
|   trunk_volume   | int  |     car trunk capacity      |
|     insurer      | str  | car insurance company name  |
|  insurer_number  | str  | car insurance company phone |
|   review_date    | str  |   date of last car review   |
| withdrawal_place | str  |    car withdrawal place     |
|       city       | str  |          car city           |
|      state       | str  |          car state          |
|     user_id      | int  |      id of the locator      |

## `Endpoints and methods:`

---

## Every route needs authorization

Authorization:

```javascript
{
    headers: {
        Authorization: "Bearer access_token";
    }
}
```

---

## Routes that need permission

## Register

**You need be the locator user and be logged in to register**

-> URL and method:

> POST:` https://capstone-q3.herokuapp.com/car/register`

**Body request example:**

```JSON
{
	"year": 2019,
	"license_plate": "abc123",
	"model": "Prisma",
	"trunk_volume": 54,
	"insurer": "Teste Seguros",
	"insurer_number": "(12) 1234-56789",
	"review_date": "2001-07-12",
	"withdrawal_place": "Shopping Curitiba",
	"city": "Curitiba",
	"state": "pr"
}
```

Response: `status 201 - CREATED`

```JSON
{
    "id": 1,
    "year": 2019,
    "model": "PRISMA",
    "trunk_volume": 54,
    "insurer": "TESTE SEGUROS",
    "insurer_number": "12123456789",
    "review_date": "Thu, 12 Jul 2001 00:00:00 GMT",
    "withdrawal_place": "SHOPPING CURITIBA",
    "city": "CURITIBA",
    "state": "PR"
}
```

## Update car

**You need to own the resource to update.**
You can change any key from your own user.

URL and method:

> PATCH: `https://capstone-q3.herokuapp.com/car/update/<id>`

**Request example:**

PATCH: `https://capstone-q3.herokuapp.com/car/update/1`

Body:

```JSON
{
	"review_date": "2021-07-12",
	"withdrawal_place": "Shopping Palladium"
}
```

Response: `status 200 - OK`

```JSON
{
    "id": 1,
    "year": 2019,
    "model": "PRISMA",
    "trunk_volume": 54,
    "insurer": "TESTE SEGUROS",
    "insurer_number": "12123456789",
    "review_date": "Mon, 12 Jul 2021 00:00:00 GMT",
    "withdrawal_place": "SHOPPING PALLADIUM",
    "city": "CURITIBA",
    "state": "PR"
}
```

## Delete user

**You need to own the resource to delete.**

-> URL and method:

> DELETE:` https://capstone-q3.herokuapp.com/car/delete/<id>`

**Request example:**

DELETE without a body: `https://capstone-q3.herokuapp.com/car/delete/1`

Response: ` status 204 - NO CONTENT`

---

## Routes don't that need permission

**All GET Routes don't need permission.**

In response header are the information about total cars quantity, pagination, next_page that access the next page and prev_page that access the previous page

Response header:

```JSON
{
    "info": {
    "count": 11,
    "pages": 1,
    "next_page": null,
    "prev_page": null
  },
```

## Get cars

-> URL and method to get all cars:

> GET:` https://capstone-q3.herokuapp.com/car/cars`

Response: `status 200 - OK`

```JSON
{
  "result": [
    {
       "id": 1,
       "year": 2019,
       "model": "PRISMA",
       "trunk_volume": 54,
       "insurer": "TESTE SEGUROS",
       "insurer_number": "12123456789",
       "review_date": "Thu, 12 Jul 2001 00:00:00     GMT",
       "withdrawal_place": "SHOPPING CURITIBA",
       "city": "CURITIBA",
       "state": "PR"
    },
  ]
}
```

-> URL and method to get cars with parameters:

> GET:` https://capstone-q3.herokuapp.com/car/cars?<parameters=values>`

**Request example:**

GET without a body: `https://capstone-q3.herokuapp.com/car/cars?model=prisma&withdrawal_place=curitiba`

Response: `status 200 - OK`

```JSON
  "result": [
    {
      "id": 1,
      "year": 2019,
      "model": "PRISMA",
      "trunk_volume": 54,
      "insurer": "TESTE SEGUROS",
      "insurer_number": "12123456789",
      "review_date": "Thu, 12 Jul 2001 00:00:00 GMT",
      "withdrawal_place": "SHOPPING CURITIBA",
      "city": "CURITIBA",
      "state": "PR"
    }
  ]
```

## Get cars by id

-> URL and method to get by id:

GET:` https://capstone-q3.herokuapp.com/car/<id>`

**Request example:**

GET without a body: `https://capstone-q3.herokuapp.com/car/1`

Response: `status 200 - OK`

```JSON
{
    "car": {
    "id": 1,
    "year": 2019,
    "model": "PRISMA",
    "trunk_volume": 54,
    "insurer": "TESTE SEGUROS",
    "insurer_number": "12123456789",
    "review_date": "Thu, 12 Jul 2001 00:00:00 GMT",
    "withdrawal_place": "SHOPPING CURITIBA",
    "city": "CURITIBA",
    "state": "PR"
  },
  "date_ocupied": [],
  "avaliations": []
}
```
