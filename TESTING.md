# Demit's Arthouse Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Accessibility](#accessibility)
  - [Accessibility Validation](#accessibility-validation)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)

# Performance

## Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. There are a couple of issues due to Bootstrap, Stripe and general Heroku slowness.

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="/">
</details>
<details><summary>Products</summary>
<img src="/">
</details>
<details><summary>Product Detail</summary>
<img src="/">
</details>
<details><summary>Producers</summary>
<img src="/">
</details>
<details><summary>Profile</summary>
<img src="">
</details>
<details><summary>Bag</summary>
<img src="">
</details>
<details><summary>Checkout</summary>
<img src="/">
</details>
<details><summary>Order Confirmation</summary>
<img src="">
</details>
<details><summary>Privacy Policy</summary>
<img src="">
</details>
<details><summary>Terms & Conditions</summary>
<img src="">
</details>

*Go back to the [top](#table-of-contents)*

---

# Accessibility

## Accessibility Validation

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards. All pages pass with 0 errors, except for the checkout page that has a contrast error. This is only for placeholder text.

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Products</summary>
<img src="">
</details>
<details><summary>Product Detail</summary>
<img src="">
</details>
<details><summary>Producers</summary>
<img src="">
</details>
<details><summary>Profile</summary>
<img src="">
</details>
<details><summary>Bag</summary>
<img src="">
</details>
<details><summary>Checkout</summary>
<img src="">
</details>
<details><summary>Order Confirmation</summary>
<img src="">
</details>
<details><summary>Privacy Policy</summary>
<img src="">
</details>
<details><summary>Terms & Conditions</summary>
<img src="">
</details>

*Go back to the [top](#table-of-contents)*

---

# Code Validation

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. For logged in pages, the page source was copied and pasted into the validator. All pages pass with 0 errors and 0 warnings. Except for the profile and checkout pages, which have an error due to a placeholder attribute in a select element. This looks to be coming from the `CountryField` class from `django-countries`.

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Products</summary>
<img src="">
</details>
<details><summary>Product Detail</summary>
<img src="">
</details>
<details><summary>Producers</summary>
<img src="">
</details>
<details><summary>Profile</summary>
<img src="">
</details>
<details><summary>Bag</summary>
<img src="">
</details>
<details><summary>Checkout</summary>
<img src="">
</details>
<details><summary>Order Confirmation</summary>
<img src="">
</details>
<details><summary>Privacy Policy</summary>
<img src="">
</details>
<details><summary>Terms & Conditions</summary>
<img src="">
</details>

*Go back to the [top](#table-of-contents)*

---

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.

![CSS validation](/media/readme_images/css1.png)
![CSS validation](/media/readme_images/css2.png)

*Go back to the [top](#table-of-contents)*

---

## JS Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript/Jquery of the website. No issues were found.


*Go back to the [top](#table-of-contents)*

---

## PEP8 Validation

A combination of the following Python packages was used to ensure the code is PEP8 compliant: flake8, autopep8 and black. After which `flake8 --statistics` was ran in VSCode terminal and the final flagged files were checked in [PEP8 Online](http://pep8online.com). The only issues found were a few longer lines in the base project's settings.py and migrations files due to HTML blocks.

*Go back to the [top](#table-of-contents)*

---

# Testing

## Manual Testing (BDD)

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

User Story | BDD Test | Pass
--- | --- | :---:
As a Shopper<br>I want to be able to view past work, artists evolution, endorsements and current projects<br>So that I can evaluate the artists quality/reputation and make a decision about a purchase | Given that I'm a new visitor to the website<br>When I view/scroll down the homepage<br>Then I should see what they sell and what they care about | :white_check_mark:
As a Shopper<br>I want to be able to view a list of products<br>So that I can select some to purchase | Given that I am interested in making a purchase<br>When I click the "Shop now" button or the Shop button<br>Then I should see a product page with all products | :white_check_mark:
As a Shopper<br>I want to be able to view individual product details<br>So that I can identify the price, the size (if applicable), description & product image | Given that I am interested in making a purchase<br>When I click on a product image or name<br>Then I should see the details of the product on a new page | :white_check_mark:
As a Shopper<br>I want to be able to easily view the total of my purchases at any time<br>So that I can review the total amount of my order and reflect on whether I want to buy or not | Given that I'm on any page on the site<br>When I click on the shopping bag icon<br>Then I should be taken to the shopping bag page where I can see all of the products in the bag and the total price | :white_check_mark:
As a Shopper<br>I want to be able to view the artists journal chronologically<br>So that I can connect with the individual behind the work and understand their process | Given that I'm on any page on the site<br>When I click on the blog link<br>Then I should only see the artists journal posts chronologically | :white_check_mark:
As a user<br>I want to be able to view any comments on a particular journal post<br>So that I can understand why people enjoy the artists work & better understand them | Given that I'm on the blog page<br>When I click on a blog post<br>Then I expect to see hte entire post and any user comments below it | :white_check_mark:
As a user<br>I want to be able to easily register a profile<br>So that I can save my information for purchases, delivery & commenting site-wide | Given that I want to sign up to the site<br>When I click the user icon<br>Then I should see an option to sign up or log in and clicking sign up will bring me to a registration page where upon completion I will receive an email confirmation link | :white_check_mark:
As a user<br>I want to be able to easily login/log out<br>So that I can access my information and make a purchase without filling in forms every time | Given that I'm not logged in<br>When I click on the user icon and click login<br>Then I should see a form to add my username/password and be given feedback upon submission as to whether I was successful or not | :white_check_mark:
As a user<br>I want to be able to easily recover my password if I forget it<br>So that I can recover access to my account | Given that I am not logged in and have forgoten my password<br>When I click on forgot password link<br>Then I expect to be redirected to a page where I can fill in my email and receive a link to reset it | :white_check_mark:
As a user<br>I want to be able to receive a confirmation email after registering<br>So that I can verify that my registration was successful | Given that I have just filled in the registration details<br>When I open my email <br>Then I should see I have an email confirmation link | :white_check_mark:
As a user<br>I want to be able to have a personalised user profile<br>So that I can view order history, confirmations and payment/delivery information | Given that I'm on any page, I can click the user icon and select my profile<br>When I arrive at the page<br>Then I should see a form where I can enter my details to start the checkout process | :white_check_mark:
As a shopper<br>I want to be able to sort the list of available products<br>So that I can identify products based on featured, best selling, price, date added | Given that I'm on the products page<br>When I select a sort method<br>Then I should see all products sorted accordingly | :white_check_mark:
As a shopper<br>I want to be able to sort a specific category of product<br>So that I can identify specific products and not waste time looking at other categories' products | Given that I'm on the products page<br>When I select a category<br>Then I should see all products sorted in that category | :white_check_mark:
As a shopper<br>I want to be able to search for a product by name or description<br>So that I can find a specific product I'd like to purchase | Given that I am on any page and enter data into the search bar<br>When I click the search button<br>Then I should see all relevent search details | :white_check_mark:
As a shopper<br>I want to be able to see a list of search results & number of results<br>So that I can decide quickly if the products are of interest or not | Given that I am on any page and enter data into the search bar<br>When I click the search button<br>Then I should see all relevent search details | :white_check_mark:
As a shopper<br>I want to be able to easily select the product I want and quantity/size if applicable<br>So that I can be sure the product is the one that I want and add to bag quickly | Given that I've navigated to my desired product<br>When I click the add to bag button<br>Then I should see confirmation that the product has been added and if the piece is not an original then I can add more instances of the product | :white_check_mark:
As a shopper<br>I want to be able to view items added to the bag <br>So that I can identify the total cost of my order and all the items I will receive | Given that I have clicked the shopping bag icon<br>When I scroll down<br>Then I should see all the items currently in the bag | :white_check_mark:
As a shopper<br>I want to be able to adjust the quantity of individul items in my bag<br>So that I can easily make quick changes before checkout | Given that I am on the shopping bag page<br>When I click + or - buttons<br>Then I should see the quantity change (except if it is an original piece) | :white_check_mark:
As a shopper<br>I want to be able to easily enter payment information<br>So that I can check out quickly and easily | Given that I've navigated to the Checkout page<br>When I enter payment details<br>Then I should see visual confirmation that all is well | :white_check_mark:
As a shopper<br>I want to be able to pay for items quickly and securely<br>So that I can keep my credit card and delivery information safe and secure | Given that I've entered my personal details and card details on the Secure Checkout page<br>When I click the "Pay Now" button<br>Then I should see confirmation that all is well and my order has been received | :white_check_mark:
As a shopper<br>I want to be able to view order confirmation after checkout<br>So that I can be secure in the knowledge that the payment went through & order is confirmed | Given that I've entered my personal details and card details on the Secure Checkout page and clicked pay now<br>When the payment has been processed<br>Then I should see confirmation that the order has been successful and all the transaction details | :white_check_mark:
As a store owner<br>I want to be able to add a product<br>So that I can add new items to the store | Given that I'm logged in as a superuser<br>When I click the user icon<br>Then I should see a link to product management where I can add poriducts to the site | :white_check_mark:
As a store owner<br>I want to be able to edit/update a product<br>So that I can change product prices, images, descriptions | Given that I'm logged in as a superuser<br>When I navigate tot he products page or to any product detail page<br>Then I should see an icon to edit the product | :white_check_mark:
As a store owner<br>I want to be able to delete a product<br>So that I can remove items that are no longer for sale | Given that I'm logged in as a superuser<br>When I navigate tot he products page or to any product detail page<br>Then I should see an icon to delete the product | :white_check_mark:
As a store owner<br>I want to be able to review all journal comments before they are posted<br>So that I can only allow genuine comments & avoid potentially harmful comments to the store | Given that I'm logged in as a superuser<br>When I navigate to the admin page<br>Then I should see all comments waiting for approval | :white_check_mark:
As a store owner<br>I want to be able to add a journal post (with date, image, text)<br>So that I can share with patrons/customers what the current projects are | Given that I'm logged in as a superuser<br>When I click the user icon<br>Then I should see a link to the journal where there is a working form to add blog posts | :white_check_mark:
As a store owner<br>I want to be able to edit/update a post<br>So that I can update a current project/ fix errors| Given that I'm logged in as a superuser<br>When I navigate to any blog post<br>Then I should see a link to edit the post which brings me to a form which upon submission updates the product | :white_check_mark:
As a store owner<br>I want to be able to delete a post<br>So that I can remove posts that are no longer relevant/part of the brand. | Given that I'm logged in as a superuser<br>When I navigate to any blog post<br>Then I should see a link to delete the post | :white_check_mark:
As a shopper<br>I want to be able to comment on a journal post (anonamously or if signed in)<br>So that I can interact with other buyers/the artist or share thoughts and engage in debate| Given that I am a shopper and have navigate to a blog post<br>When I enter a comment into the comment form<br>Then I should see confirmation that the comment has been received and is up for approval | :white_check_mark:
As a shopper<br>I want to be able to (if signed in) delete a comment<br>So that I can change my mind and take a comment back | Given that I am a shopper and have navigate to a blog post which I have commented on<br>When I look at my previous comment<br>Then I should see an option to delete the comment which works | :white_check_mark:


*Go back to the [top](#table-of-contents)*

---