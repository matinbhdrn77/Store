# Store
## Table of contents
- [Introduction](#introduction)
  * [Description and requirements](#description-and-requirements)
  * [Installation](#installation)
- [Apps Implementation](#apps-implementation)
  * [Core](#core)
    + [Models](#models)
    + [Admin Conf](#admin-conf)
    + [Serializers](#serializers)
    + [Signals](#signals)
  * [Likes](#likes)
    + [Models](#models-1)
  * [Store](#store-1)
    + [Models](#models-2)
    + [Admin Conf](#admin-conf-1)
    + [Serializers](#serializers-1)
    + [Signals](#signals-1)
    + [Views](#views)
    + [Permissions](#permissions)
    + [Tests](#tests)
    + [Other Features](#other-features)
  * [Tags](#tags)
    + [Models](#models-3)
    + [Admin Conf](#admin-conf-2)

# Introduction
## Description and requirements
Using Python, Django, Django Rest Framework complete the implementation of a Store that allows users to make carts, add item to carts, access to end point with permissions and ... . 

You must be registered to use options such as viewing some endpoints.

## Installation
To set up this project on your computer:
1. Clone the project
2. Install all necessary dependencies
    ```python
        pipenv install
    ```
3. Manage your database in storefront.settings.DATABASES
4. Make a migration
    ```python
        python manage.py migrate
    ```
5. Run server
    ```python
        python manage.py runserver
    ```
    
# Apps Implementation

## Core
plugable app to connect store app to another apps. so store app can work independently

### Models
Contains User Model extension with additional fields.

Classes:
* User : register with Email

### Admin Conf 
Classes:
* UserAdmin : add user with email, password, last and first name
* CustomProductAdmin : admin can add products with tag and image inlines
* TagInline : inline class for CustomProductAdmin and admin can search for tags

### Serializers
serializers for creating and retrieving users with djoser.

Clasess:
* UserCreateSerializer
* UserSerializer

### Signals 
create reciever signal handlers. recieve signal when an order create


## Likes
app that can handle liked items, ...

### Models
Classes:
* LikedItem : foreign key to django builtin content type so we can use it for any other models


## Store
our main app for project. all necessary configuration is here

### Models 
Classes:
* Product : a product is just in one collection and can be in multiple promotions
* Collection : every collection has a featured peoduct
* ProductImage : every product can have a multiple images
* Customer : 
    1. customer can be in gold, silver or bronze membership
    2. admin have access to customer first and last name through display decorator
    3. order customers base on user first name and last name
    4. add custom permission so customer can view history


### Admin Conf 
Classes:
* ProductAdmin :
    1. when user add product can search for products in line
    2. prepolate a slug for each product
    3. clear inventory for a specific product
    4. can filter base on collections, last update and inventory
* CollectionAdmin : display collections and number of products in it
* CustomerAdmin : 
    1. display customers with their member ship and orders (link to their orders)
    2. optimize searching for names
* OrderAdmin: admin user can add orders with items(products) in it

### Serializers
Classes:
* CollectionSerializer : serialize collections 
* ProductImageSerializer : crate ProductImage object in this serializer
* ProductSerializer : serialize products 
* ReviewSerializer : create Review object for products 
* SimpleProductSerializer : just for showing products in a simpler way in cart items endpoint
* CartItemSerializer : show items in cart with quantitiy and total price
* CartSerializer : show each items (CartItemSerializer) and total price for all items
* AddCartItemSerializer : a serializer for adding products to cart and if there is no cart for items, create a cart
* UpdateCartItemSerializer : just update quantity for items
* CustomerSerializer : serialize custommers
* CreateOrderSerializer : create cart add order and items in it then save items in database and delete cart (transaction atomic for integrity)

### Signals
create customer when a new user created

### Views
Classes:
* ProductViewSet : 
    1. model view set for handling products api
    2. search products base on title, description and unit price range
    3. order products base on unit price and updated time
    4. admin can't delete product if it's in ordering process
* CollectionViewSet :
    1. model vview set for handling collections api
    2. admin can't delete a collection if there is products in that collection
* ReviewViewSet : model view set for handling reviews for each product
* CartViewSet : generic view set for creating, retrieving and deleting cart
* CartItemViewSet : model veiw set for handling items in each cart
* CustomerViewSet : customer can see his profile and history
* OrderViewSet:
    1. model view set for handling orders
    2. just admin can delete and update orders
    3. admin can see all orders but each customer can just see his orders
* ProductImageViewSet : model view set for handling images

### Permissions
Classes:
* IsAdminOrReadOnly : normall user can just visit api's in safe method
* FullDjangoModelPermissions : 
* ViewCustomerHistoryPermission : customer can see just his history

### Tests
Classes:
* TestCreateCollection : test creating collections api
* TestRetrieveCollection :test retrieving colletion api

### Other Features
Fields:
* Pagination : show 10 item per page
* Management : add default data to your database
    ```python
        python manage.py seed_db
    ```
* Validators : file sizes must be at most 500 kb 


## Tags
app that can handle tags for products

### Models
Classes:
* TaggedItemManager : a model manager that returns tags for each item
* Tag : model with just 1 char field for name of the tag
* TaggedItem : every tagged item have tag label and product

### Admin Conf
Classes:
* TagAdmin : search base on label field
