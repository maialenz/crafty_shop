# Mai's Crafty Shop

## Introduction

The Crafty Shop is an e-commerce website offering personalized and handmade products. 

-   [View the Crafty Shop Heroku App](https://[appname].herokuapp.com/)
-   [View the repository on GitHub](https://github.com/maialenz/crafty_shop/)

![](MOCKUP IMAGE)

This is Milestone N.4 of teh Full-Stack Web Development Diploma Course by UCD and Code Institute. 

The Crafty Shop is a fully functionioning e-commerce Django web application, built in using Python and backed by PostgreSQL (and SQLite3 for development mode) database, and Deployed using Heroku. It allows users to purchase products and register an account with full CRUD functionality. For styling Bootstrap was used and the shop has the posibility to take real payments on a future. 

**ATTENTION!** At this moment the website is set up for educational purposes, and the Stripe Payments is not taking real cards. To test the card payments, first create an account and use the following card number: 4242 4242 4242 4242 ; expiry date: 42 42 and CVC: 424.

[Click here to view the project live.](https://.herokuapp.com/)
  
---

## Table of Contents

### 1. [UX](#ux) 

#### 1.1. [Goals](#goals)
##### 1.2.1. [Visitor Goals](#visitor-goals)   
##### 1.2.2. [Business goals](#business-goals)

#### 1.2. [User Stories](#user-stories)

#### 1.3. [User Centered Design](#user-centered-design)
- Strategy 
- Scope 
- Structure 
- Wireframes

### 2. [Design](#design)
- Colours
- Typography
- Icons
- Logo
- Imagery

### 3. [Database Structure](#database-structure)
#### 3.1. [Database Choice](#database-choice)
#### 3.2. [Data Models](#data-models)

### 4. [Features](#features)

### 5. [Technologies Used](#technologies-used)
- Syntax
- Frameworks, Libraries & Programs

### 6. [Testing](#testing)
- [Testing Document](TESTING.md)

### 7. [Deployment](#deployment)
- [Deployment Document](DEPLOYMENT.md)

### 8. [Credits](#credits)
- Resources
- Code 
- Media

----

# UX

## Goals

As the Covid-19 pandemic has forced businesses around the world to have to close their doors for months and mothns, many have been left with no choice but to adapt quickly and take the goods and services online.

As most of us found ourselves in this position and were forced to work/study from home, we started finding other ways to entretain and keep busy in our homes. We started crafting, baking, cooking, and now they are a large part of our daily rutines. We have also started appreciating hand made things and supporting small and community businesses that received a big push back due to the situtation.

So it's understandable when many have decided to move from traditional retail to e-commerce. 
This website wants to offer those who appreciate the handmade crafts and the quality that comes with it.

### Visitor Goals

The target audience for The Crafty Shop are:
- People who value handmade items
- People searching for unique gifts
- People that enjoy art

User Goals:
- Get inspiration
- Find a gift
- Be able to navigate the shop easily, find what they need and make a secure purchase
- Buy from a small shop

### Business Goals

The goals of The Crafty Shop business are;
- To provide a professional online shop.
- To sell homemade and handmade crafts to its users
- Build brand awareness.
- Build an online pressence

---

## User Stories

![Image of User Stories table](docs/Readme/user-stories.png)

---

## User Centered Design

### Strategy

- The main goal of this website is to convert visitors into frequent customers. As the items shown in this website are handcrafted items, the products will be shown in a very minimalistic way, with minimum imagery and clutter to show that the products are made in the most professional manner, clean and tidy. To show the customers the type of crafts that are offered on the website, all products will be displayed together, with the option to sort them by name, price, ... as well as having the option to go directly to the category they would like to search.

- To achieve the goals pointed on the goals section, the information will be diplayed to the user inside each item, not to overwhelm the possible customer. The website will show a light but light-in-color palette to give the sense of delicacy and care by the creator.

The steps a new user would idealy take when arriving into the website would be the following:
- Expore the website's landing page, where the information will introduce the user to the products offered within the shop.
- Follow the call to action buttons directing the user either to all the products or the selected category.
- Select the product of their choice and choose the quantity needed
- Following the secure checkout call to action button go to the checkout page and purchase the product/s selected following the instructions on the following pages (delivery information, card information)
- On the delivery instruction page, choose to save the information and create an account 
- Go to the personal account to see their delivery information where they can update personal details, see their latest order.
- Remain a regular user to the shop due to an positive website experience and crafted items.

This will all be achieved through creating a clear, tidy and strong UI focusing on well structured content. Having a creat hirearchy of information and well placed call to action buttons will allow the user to navigate and use the functionalities of the website without the need of instructions

- Technical capabilities:
    - To use this website the user needs to have acces to some internet connection within the chosen device.
    - They also need to have basic understanding on how to select and navigate the page.
    - This page will be done using the Bootstrap framework to create a responsive structure and implement sections that the user needs. The website will be separated in 8 (Landing, Products, Product information, Register, Login, Bag, checkout, Payments). Only registered users will be allowed to access the personal account to see their details. The admin/superuser will be allowed to edit/delete products (accessed under the product name) as well as adding new products.

---

### Scope | Trade Off

- Features within the desing plan with highest priority:
    - Minimal but appealing homepage
    - Navigation links clearly visible on the top of the website
    - Responsive navigation bar
    - Only allow registered users to access and manage their personal accounts
    - Only allow superusers to add/edit/delete new products
    - Detailed information under each product
    - A secured payment system
    - Validated and error free forms
    - Search and sorting functionalities
    - The posibility for the user to check the selected products and to have CRUD functionalities to control their bags.

- Lower priority features that may not be included in the initial release of the website:
    - Contact section to send messages to the Creator
    - A comment section that allows all users to write their own feedback
    - A rating option for products
    - A gallery section connected to customers instagram accounts
    - The functionality to add personalized options for some products
    - Related/recommended products to be displayed under the product choice
    - Footer with social media links, contact information and Links to different categories for easy access

---

### Structure

- The structure of the site will be layed out in ----------- pages. The landing page(homepage) will welcome new and returning users to the page, where they'll see a call to action button that will direct them to the shop where they'll be able to select and purchase different items. Anonymous users wi8ll be allowed to make purchases and will be able to not to make an account, but these will not be able to access the personal accounts where they can see their latest purchases. Normal users are not able to access the full CRUD functionality of the database, being this only accessible for the Admin/Superusers. The latest, will have an extra page where they will be able to insert/edit/delete products. Logged in users will have the logout option to stop their session cookies. The basic structure of the website is:
    - Header/Navigation - *Top Level*
        - The navigation bar will be a hamburger/bars menu icon on smaller screen sized. It is not sticky as there will be a back to top icon throught the site for UX purposes.
        - The navigation menu will feature a search bar allowing users fast and immediate search of the site to quickly find the products they are looking for. 
        - Categories will be displayed in button/link form to access same category products in a faster way.
    - Body - *Main Page Elements*
        - The product page overview will show a typical webshop layout including cards with product images, product name, price and a button to direct the user to the detailed page of the selected product for further inspection.
        - The individual product page will include the product's image, a description, price and add to bag button.
        - The bag page will show the summary of the product selection with the extra prices added with the grand total showing at the bottom of all products added to the bag for the consideration of the customers before the purchase.
        - The order confirmation page will display all the users details to confirm the order was successfully delivered.
    - Footer - *Bottom level*
        - A repeated navigation menu to help the users change categories if they are at the bottom of the page.
        - Social media links so the users can follow and see the shops creations.
        - Copyright information
        - Contact information

---

### Wireframes

The wireframes were created using [Balsamiq](https://balsamiq.com/) to design and plan the project
- [Mobile Wireframes ](docs/Readme/wireframes/mobile-wireframes.png)
- [Ipad Wireframes ](docs/Readme/wireframes/ipad-wireframes.png)
- [Desktop Wireframes ](docs/Readme/wireframes/desktop-wireframes.png)

---

# Design

The Crafty Shop website will have an overall simplistic and minimalist feeling, to emphasis a clean and high quality crafts and items on sale. 

### Colors

- The color scheme for this webshop will contain three main colors: A primary color, secondary and accent colors. In the places where accessibility requires a darker tone, this will be achieved with darker tones of the same colors.
- For the success and error colors red and green will be used, as these are obvious to everybody. 
- The colors will be taken from the brand logo, to keep a professional and pull the site together.
- Chosen colors:
    - 
    - 
    - 

### Typography

- There will be four fonts used throughout the website. Fredericka the Great and Shadows Into Light will only be used for the logo and main header as they are fun and easy to see. They give a sense of handpainted/handmade sense to the user, which goes very well along the theme of the website. Quicksand will be used and the main font for the mayority of the website, using different weights and sizes to fit the circumstances of the use. Sans-serif will be used as a fallback alternative in case of unsuported font.
    - Fredericka the Great: Main Header/Logo
    - Shadows Into Light: Main Header/Logo
    - Quicksand: Rounded but simple font. It has a informal but professional style, suited for a shop were users are spending their money but they may feel closer to the artist/creator
    - Sans-Serif: used as a fallback font
- All fonts were taken from [Google Fonts](https://fonts.google.com/) to avoid unsuported browser/systems. 

### Icons

- To keep a simplistic and minimalistic feeling only the most necessary icons were used. The icons were taken from [Fontawesome](https://fontawesome.com/v6.0)
    - Search icon
    - Shopping cart icon
    - User icon
    - Facebook, Instagram, and Social media icons
    - 

### Logo

- The logo has been created using [Canva]() for a personalized and custom brand. It displays ... according to the products created and offered on this website
******** MISING LOGO ***********

### Imagery

- Imagery will be used but will be used only when necessary, like to show product images to users. There might be used as a landing page image as an introduction to the shop to welcome the user to the store and increase expectation of what they will find along the website. 
- The images representing the products, will be as simple as possible, just representing the product on a single images. 

---

# Database Structure

## Database Choice
- This project uses two different types of databases, one for local development and one for the production version. As the Crafty Shop was built on Djnago, during the local development the standard Django's built in **MySQL** (sqlite3) database was used. On deployment on Heroku, the database was changed to **PostgreSQL** database, which is provided by Heroku as an add-on for production.

## Data Models

### User

The Django’s default user model for authorization is has been used, which allows the project to meet one of the main requirements of separating features by anonymous users, users in session and superusers. This User model is the standard `django.contrib.auth.models`.

**NOTE**: The structure of the Checkout and Products apps have been inspired by *Boutique Ado*, which was previously creaded following videos created by Code Institute.

### Profiles App

**UserProfile Model**

| **Name** | **Database Key** | **Validation** | **Field Type** |
--- | --- | --- | --- 
User | user | on_delete=models.CASCADE | OneToOneField 'User'
Phone number | default_phone_number | max_length=20, null=True, blank=True | CharField
Address Line1 | default_street_address1 | max_length=80, null=True, blank=True | CharField
Address Line2 | default_street_address2 | max_length=80, null=True, blank=True | CharField
Postcode | default_postcode | max_length=20, null=True, blank=True | CharField
Town/City | default_town_or_city | max_length=40, null=True, blank=True | CharField
County | default_county | max_length=80, null=True, blank=True | CharField
Country | default_country | blank_label='Country', null=True, blank=True | CountryField

### Products App

**Product Model**

| **Name** | **Database Key** | **Validation** | **Field Type**|
--- | --- | --- | --- 
Category | category | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey 'Category'
Sku | sku | max_length=254, null=True, blank=True | CharField 
Name | name | max_length=254 | CharField 
Description | description | max_length=700 | TextField
Image URL | image_url | max_length=300, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField
Price | price | max_digits=6, decimal_places=2 | DecimalField 

**Category Model**

| **Name** | **Database Key** | **Validation** | **Field Type** |
--- | --- | --- | ---
Name | name | max_length=254 | CharField 
Friendly Name | friendly_name | max_length=254, null=True, blank=True | Charfield 

### Checkout App

**Order Model**

| **Name** | **Database Key** | **Validation** | **Field Type** |
--- | --- | --- | --- 
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'| ForeignKey 'UserProfile' 
Full Name | full_name | max_length=50, null=False, blank=False | CharField 
Email | email | max_length=254, null=False, blank=False | EmailField 
Country | country | blank_label='Country*', null=False, blank=False | CountryField
Postcode | postcode | max_length=20, null=True, blank=True | CharField 
Town/City | town_or_city | max_length=40, null=False, blank=False | CharField
Phone number | phone_number | max_length=20, null=False, blank=False | CharField 
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address2 | max_length=80, null=False, blank=True | CharField 
County | county | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Total Price | total_price | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Stripe Pid | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField 

**OrderLineItem Model**

| **Name** | **Database Key** | **Validation** | **Field Type** |
--- | --- | --- | --- 
Order | order | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey 'Order'
Product | product | null=False, blank=False, on_delete=models.CASCADE | ForeignKey 'Product' 
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Lineitem Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField 

---

# Features

## Existing Features

### Elements on every page

**Navbar:**
- The navbar features on every page except on the checkout/payment pages. This is standard for webshops, as it avoids accidental clicks or distractions and makes the customer focus on the payment.
- The navbar has a logo on the left, linking the homepage. This will remain the same in tablet and mobile view as it is expected to be. 
- In mobile view, the navigation will collapse into a burger icon situated on the right hand side, as most users will be right handed and it is easier to access it with a single hand.
- It will be responsive on most devices.
- The shopping bag will be placed on the right hand side making sure is easy to spot.
- The shopping cart works even for users not registered or logged in.
- Logged out users will be able to see the options to log in, register and product pages.
- Logged in users will be able to see their account page and the possibility to loggout and end their session.
- Search bar will be located in the navbar

**Footer:**
- Will not appear on the checkout page for the same reasons as the navbar
- The footer will contain the copyright information as well as the contact details and the posibility to include some of the future release features if there is enough time to incorporate them. 
- The social media links will be placed in the right side as it will be easier to access them with a single hand

**Back to Top Button:**
- All long pages will be provided with an arrow to scroll to the top to automatically bring the user to the top of the page. This avoids the need for the user to manually have to scroll all the way up.

**Home/Landing Page:**
- The home page will feature a hero image taking most of the page as a welcome page. Inside it will have the name of the shop and a brief description with a CTA button that will redirect the user to the main product page where they'll be able to start their shopping journey.

**Products/Shop Page:**
- *Categories* button under the navbar for easy access to different categories of products/items
- *Sort* option will allow to sort the products on the page by price (high to low and low to high), name (a-z or z-a)
- *Products* list
    - The products in the shop they'll be represented by an image. The name, category and price will be placed under the image
    - The products will be placed using card class from bootstrap
    - Each product will have a button under at the bottom, which opens the product individually, showing the description and the options to increase the quantities to be added to the cart

**Product Detail Page:**
- This page can be accessed from the CTA button under each product card on the Shop page.
- In this page the users can find the Image, Title or name of the product, description of the item, the category it belongs to and the price of the item.
- The users will have the option to select the amount of items they would like to add to the cart.

**Profile Page:**
- Non-Logged or non-registered users will have the options to LogIn or Register for an account.
- *My Account*: This page will be accessible to *Registered* users **only**
    - Users that have registered and logged in will be able to access their individual page where they can see and edit their delivery/billing information
    - Here logged users can see their past orders, if there were any.

**Bag Page:** 
- This follows already well know e-commerce style for shopping carts. 
- The users will be able to see the items they have added to the shopping basket
- The information for each items will be displayed for the users review. They will have the option to remove an item from the cart or update it (qty, adding more items by going to the main product page again)
- A checkout button will invite the users to confirm the order by finishing the payment.
- The shipping price will be updated depending if the user has met the necessary requirements for a free delivery or not. This will be added to the card automatically.

**Checkout Page:**
- This can be accessed from the bag page.
- Users will be asked to introduce their delivery/billing information.
    - Registered and Logged in Users will find this information prefiled for them. They can change any fields here.
- Users will have the option to save the details introduced on the form on their profile for future purchases. This makes the shopping experience nicer as the customer doesn't have to constantly introduce personal detail.
- Card details are not saved.
- A Secure Checkout button will allow the user to end the payment, confirming the order.
- The payment will be created using Stripe's payment method. This avoids the need to write all the code manually and instead reuse the already available code.
- The user will be prompted with validation messages handled by Stripe.

**Order Confirmation/Success Page:**
- This page is only accessible when the payment has been completed. It can also be accessed from the profile page by clicking on top of the Past order numbers. 
- The user is able to see their details as well as the order number for their reference.
- A confirmation email is sent to the user when the payment is successfull.

