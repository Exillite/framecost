# **FrameCost**
---
# Pages

### Home
list of all shops, wich user can administrate

### Shop
tabs: products, templtates, orders, settings
- products - list of all products from shop, add new product or item of product
- templates - list of all templates from shop
- orders - list of all orders from shop
- settings - shop settings (change title, add/remove admins, etc)

### Template
see/edit template

### Order
see/edit order

### Login
login page

### Registeration
registeration page

---

# API DOCUMENTATION

## Methods

### Registeration
- method: POST
- path: /api/v1/register
- request body: 
```json
{
    "name": "string",
    "surname": "string",
    "login": "string",
    "email": "string",
    "password": "string"
}
```
- response body: 
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Login
- method: POST
- path: /api/v1/login
- request body: 
```json
{
    "email": "string",
    "password": "string"
}
```
- response body:
```json
{
    "status": "int",
    "tocken": "string", // if status == 200
    "user_id": "string",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get user info
- method: GET
- path: /api/v1/user
- response body:
```json
{
    "stattus": "int",
    "user": {
        "id": "string",
        "name": "string",
        "surname": "string",
        "email": "string",
        "role": "string",
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Update user info
- method: PUT
- path: /api/v1/user/{user_id}
- request body:
```json
{
    "name": "string",
    "surname": "string",
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Create new shop
- method: POST
- path: /api/v1/shop
- request body:
```json
{
    "title": "string",
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get shop
- method: GET
- path: /api/v1/shop/{shop_slug}
- response body:
```json
{
    "status": "int",
    "shop": {
        "id": "string",
        "title": "string",
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get user shops
- method: GET
- path: /api/v1/user/shops
- response body:
```json
{
    "status": "int",
    "shops": [
        {
            "id": "string",
            "title": "string",
        }
    ]
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error

### Create new product
- method: POST
- path: /api/v1/product
- request body:
```json
{
    "title": "string",
    "category": "string",
    "price": "float",
    "shop_id": "string",
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get all products from shop
- method: GET
- path: /api/v1/shop/{shop_slug}/products
- response body:
```json
{
    "status": "int",
    "products": [
        {
            "id": "string",
            "title": "string",
            "category": "string",
            "price": "float",
            "slug": "string",
            "shop_id": "string",
        }
    ]
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get product
- method: GET
- path: /api/v1/product/{product_slug}
- response body:
```json
{
    "status": "int",
    "product": {
        "id": "string",
        "title": "string",
        "category": "string",
        "price": "float",
        "slug": "string",
        "shop_id": "string",
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Update product
- method: PUT
- path: /api/v1/product/{product_slug}
- request body:
```json
{
    "title": "string",
    "category": "string",
    "price": "float",
}
```
- response body:
```json
{
    "status": "int",
}
```


### Get item
- method: GET
- post: /api/v1/item/{item_id}
- response body:
```json
{
    "status": "int",
    "item": {
        "id": "string",
        "product_id": "string",
        "params": "string", // {cnt: 2, a: 1, b: 2}
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Create new item
- method: POST
- path: /api/v1/item
- request body:
```json
{
    "product_id": "string",
    "params": "string", // {cnt: 2, a: 1, b: 2}
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Update item
- method: PUT
- path: /api/v1/item/{item_id}
- request body:
```json
{
    "params": "string", // {cnt: 2, a: 1, b: 2}
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get all items of product
- method: GET
- path: /api/v1/product/{product_slug}/items
- response body:
```json
{
    "status": "int",
    "items": [
        {
            "id": "string",
            "product_id": "string",
            "params": "string", // {cnt: 2, a: 1, b: 2}
        }
    ]
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Create new template
- method: POST
- path: /api/v1/template
- request body:
```json
{
    "title": "string",
    "shop_id": "string",
    "products": "string", // { products: [{ "product_id": "string" }, { "product_id": "string" }]}
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get all templates from shop
- method: GET
- path: /api/v1/shop/{shop_slug}/templates
- response body:
```json
{
    "status": "int",
    "templates": [
        {
            "id": "string",
            "title": "string",
            "shop_id": "string",
            "slug": "string",
            "products": "string", // { products: [{ "product_id": "string" }, { "product_id": "string" }]}
        }
    ]
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get template
- method: GET
- path: /api/v1/template/{template_id}
- response body:
```json
{
    "status": "int",
    "template": {
        "id": "string",
        "title": "string",
        "shop_id": "string",
        "slug": "string",
        "products": "string", // { products: [{ "product_id": "string" }, { "product_id": "string" }]}
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Create new order
- method: POST
- path: /api/v1/order
- request body:
```json
{
    "shop_id": "string",
    "items": "string", // {cnt: 2, items: [{"item_id": "string", cnt: 2, a: "float", b: "float"}, {"item_id": "string", cnt: 1, a: "float"}]}
}
```
- response body:
```json
{
    "status": "int",
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get order
- method: GET
- path: /api/v1/order/{order_id}
- response body:
```json
{
    "status": "int",
    "order": {
        "id": "string",
        "shop_id": "string",
        "price": "float",
        "products": "string", // {cnt: 2, items: [{"item_id": "string", cnt: 2, a: "float", b: "float"}, {"item_id": "string", cnt: 1, a: "float"}]}
        "created_at": "datetime",
    }
}
```
- status codes:
    - 200: success
    - 400: bad request
    - 500: internal server error


### Get all orders from shop
- method: GET
- path: /api/v1/shop/{shop_id}/orders
- response body:
```json
{
    "status": "int",
    "orders": [
        {
            "id": "string",
            "shop_id": "string",
            "price": "float",
            "products": "string", // {cnt: 2, items: [{"item_id": "string", cnt: 2, a: "float", b: "float"}, {"item_id": "string", cnt: 1, a: "float"}]}
            "created_at": "datetime",
        }
    ]
}
```