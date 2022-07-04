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
    + [Models](#models)
  * [Store](#store)
    + [Models](#models)
    + [Admin Conf](#admin-conf)
    + [Serializers](#serializers)
    + [Signals](#signals)

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
3. Make a migration
    ```python
        python manage.py migrate
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

### user_profile
(only for logged-in users)

Here you can:
* View user's bio
* View all user's posts
* Edit posts (if you are the post's creator)
* Delete posts (if you are the post's creator)
* Like them 
* View all comments on user's posts
* Create a comment
* Delete a comment (if you are the comment's creator)
* Edit a comment (if you are the comment's creator)
* Follow the user (if you are not this user)
* Click on edit profile button (if you are this user)

### edit_profile
(only for logged-in users)

Here you can:
* Change your *name*
* Change your *birthdate*
* Change your *about info*
* Change your *profile picture*
* Change your *country*

### like
(only for logged-in users)

Controls all actions regarding liking:
* Add a new like
* Change a like's emoji

### following
(only for logged-in users)

Here you can:
* View all posts created by followed users
* Like them
* View all comments
* Create a comment
* Delete a comment (if you are the comment's creator)
* Edit a comment (if you are the comment's creator)

### follow_unfollow
(only for logged-in users)

Controls following/unfollowing users (only POST method allowed).

### login_view
Controls logging in.

### logout_view
Controls logging out.

### register
Controls registration.

## Tests
There are 4 main test cases:
* ModelsTestCase - checks database integrity
* FormsTestCase - makes sure that forms work correctly
* ViewsTestCase - makes sure that all views work correctly and give proper responses
* FrontEndTestCase - uses Selenium to simulate user interaction with every element on the page

Test requirements can be viewed in [test requirents.md](https://github.com/serwatka-w-proszku/CS50-Network/blob/master/test%20requirements.md)

---
Special thanks to Brian and the entire CS50 team for making learning easy, engaging, and free.
