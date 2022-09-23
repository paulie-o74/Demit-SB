<h1 align="center">Demit's Arthouse</h1>

<img src="media/">

### **Live Site**
[Demit Art Site](https://demit-sb.herokuapp.com/)

### **Repository:**
[Demit Art Repository](https://github.com/rashdogg74/Demit-SB)

# About
This is a full-stack e-commerce project built using Django, Python, HTML, CSS, and JavaScript. I have created this website for 'Demit', a real artist, based in NYC. It is a business that sells prints, one of one paintings on canvas as well as a contact point for commissioned pieces, murals and brand collaboration. The web application also doubles as a blog which allows fans to follow his work, keep up to date with recent shows and comment on recent work.

## Contents
+ [Aim](#aim)
+ [Databases](#database)
+ [Scope](#scope)
+ [Wireframes](#wireframes)
+ [Epics and User Stories](#user-stories)
+ [Agile Methodologies](#agile)
+ [Features](#features)
+ [Marketing](#marketing)
+ [Technologies Used](#tech)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

### Aim <a name="aim"></a>
Demit's Arthouse is an ecommerce web application inviting shoppers/fans/potential collaborators and patrons to engage with his brand, potentially buy his art, make contact relating to commissioned pieces, murals and professional collaborations.
The web application is developed for my final project as part of the Code Institute Diploma in Software Development (Full stack).

## Database Design <a name="database"></a>
[Database Schema](media/readme_images/)

#### **User Account**
This app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The `UserProfile` model has a one-to-one field that is linked to the Django AllAuth user account, upon logging in the model method `create_or_update_user_profile` creates the profile if it isn't already present in the model.

#### **Products App**

This app controls the products that are displayed and the categories that they fall under as well as whether or not the piece is an original. I have created two models to store the necessary data: `Category` & `Products`.

`Category` stores the various category types of artwork/vouchers on sale, this allows the user to filter the products by the category if they are looking for something specific.

`Products` enables individual products to be added to the database in order for them to be purchased via the online store. Only admin users are able to access this functionality and it can be done from the front end using the `add_product` view. This model has one FK which relates to the second model in this app, the category.

#### **Checkout**

The checkout app is used for the user to make purchases. This app contains three models, `Order`, `OrderItem` & `Coupon`. 

`OrderItem` contains all of the information regarding the products that have been purchased as part of a specific order. It has a foreign key to `Product` & `Order`, it also contains the quantity purchased of that product and then the item total. This information is used to calculate the total cost for the order. For the product FK I chose to use `on_delete=models.CASCADE`, using the 'original basket' field the admin can still see what the original purchase was.

`Order` contains all of the relevant address information for billing/shipping, a foreign key to the `UserProfile`, a foreign key to the `Coupon`, email & phone number. It also contains information regarding the payment itself, the stripe PID, original bag. Each order has an order number which is automatically generated when a new order is added to the database using `UUID`.

`update_total` calculates the overall total depending on the order items linked to the order, ensuring the value is always correct.

