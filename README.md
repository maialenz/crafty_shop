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
- Colour Scheme
- Typography
- Imagery

### 3. [Database Model](#database-model)

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

