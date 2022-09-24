<h1 align="center">Demit's Arthouse</h1>


![Am I responsive](/media/readme_images/amiresponsive.png)

### **Live Site:**
[Demit Art Site](https://demit-sb.herokuapp.com/)

### **Repository:**
[Demit Art Repository](https://github.com/rashdogg74/Demit-SB)

### **Developer:**
Paul Thomas O'Riordan

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
+ [Bugs](#bugs)
+ [Technologies Used](#tech)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

### Aim <a name="aim"></a>
Demit's Arthouse is an ecommerce web application inviting shoppers/fans/potential collaborators and patrons to engage with his brand, potentially buy his art, make contact relating to commissioned pieces, murals and professional collaborations.
The web application is developed for my final project as part of the Code Institute Diploma in Software Development (Full stack).

## Database Design <a name="database"></a>
[Database Schema](media/readme_images/erd.webp)

#### **User Account**
This app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The `UserProfile` model has a one-to-one field that is linked to the Django AllAuth user account, upon logging in the model method `create_or_update_user_profile` creates the profile if it isn't already present in the model.

#### **Products App**

This app controls the products that are displayed and the categories that they fall under as well as whether or not the piece is an original. I have created two models to store the necessary data: `Category` & `Product`.

`Category` stores the various category types of artwork/vouchers on sale, this allows the user to filter the products by the category if they are looking for something specific.

`Product` enables individual products to be added to the database in order for them to be purchased via the online store. Only admin users are able to access this functionality and it can be done from the front end using the `add_product` view. This model has one FK which relates to the second model in this app, the category.

#### **Checkout**

The checkout app is used for the user to make purchases. This app contains two models, `Order`, `OrderLineItem`. 

`OrderLineItem` contains all of the information regarding the products that have been purchased as part of a specific order. It has a foreign key to `Product` & `Order`, it also contains the quantity purchased of that product and then the item total. This information is used to calculate the total cost for the order. For the product FK I chose to use `on_delete=models.CASCADE`.

`Order` contains all of the relevant address information for billing/shipping, a foreign key to the `UserProfile`, email & phone number. It also contains information regarding the payment itself, the stripe PID, original bag. Each order has an order number which is automatically generated when a new order is added to the database using `UUID`.

`update_total` calculates the overall total depending on the order items linked to the order, ensuring the value is always correct.

## Scope <a name="scope"></a>

 * A simple, straightforward, intuitive UX experience;
 * Explicit content;
 * An easy navigation for the user through all the pages and features;
 * A site that is visually appealing on all screen sizes.

### Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have an enjoyable browsing experience.
* Navbar is auto-hidden and shown on scroll up on top to facilitate users easily navigating through pages. Mobile navigation is the same on all pages to ensure easy navigation.
* Footer is fixed on the bottom with links to social media and newsletter subscription.

## Skeleton <a name="wireframes"></a>

### UI/UX

Design inspiration came from various google searches for arthouses and art websites as well as https://www.shopify.com/ templates.

The project was developed from initial wireframes by hand and then these were expanded digitally.
Each subsequent page after the home page has the same structure to ensure uniformity accross the site.

Click to see wireframes:

[1](/media/readme_images/home_pc4.webp)<br>
[2](/media/readme_images/home_pc3.webp)<br>
[3](/media/readme_images/home_pc2.webp)<br>
[4](/media/readme_images/home_pc.webp)<br>
[5](/media/readme_images/footer.webp)<br>
[6](/media/readme_images/home_pc4.webp)<br>
[7](/media/readme_images/home_mobile.webp)<br>
[8](/media/readme_images/home_mobile2.webp)<br>
[9](/media/readme_images/home_mobile3.webp)<br>
[10](/media/readme_images/home_mobile4.webp)<br>
[11](/media/readme_images/home_mobile5.webp)<br>
[12](/media/readme_images/home_mobile6.webp)<br>
[13](/media/readme_images/footer_mb.webp)<br>

## User Experience

### User Stories <a name="user-stories"></a>

* EPIC: Viewing and navigation of the web app works as expected

1. As a... Shopper I want to be able to... view past work, artists evolution, endorsements and current projects So that I can... evaluate the artists quality/reputation and make a decision about a purchase.
2. As a ... Shopper I want to be able to... view a list of products so that I can... select some to purchase.
3. As a... Shopper I want to be able to... view individual product details so that I can... identify the price, the size (if applicable), description & product image.
4. As a ... Shopper I want to be able to... easily view the total of my purchases at any time so that I can... review the total amount of my order and reflect on whether I want to buy or not.
5. As a ... Shopper I want to be able to... view the artists journal chronologically so that I can... connect with the individual behind the work and understand their process.
6. As a... Site User I want to be able to... view any comments on a particular journal post	so that I can... understand why people enjoy the artists work & better understand them.

* EPIC: Registration & User accounts work as expected

7. As a ... Site User I want to be able to... easily register a profile so that I can... save my information for purchases, delivery & commenting site-wide.
8. As a... Site User... I want to be able to... easily login/log out so that I can... access my information and make a purchase without filling in forms every time.
9. As a ... Site User I want to be able to... easily recover my password if I forget it so that I can... recover access to my account.
10. As a... Site User I want to be able to... receive a confirmation email after registering so that I can... verify that my registration was successful.
11. As a Site User... I want to be able to... have a personalised user profile so that I can... view order history, confirmations and payment/delivery information.

* EPIC: Sorting and searching of products work as expected

12. As a Shopper I want to be able to... sort the list of available products so that I can... identify products based on featured, best selling, price, date added.
13. As a... Shopper I want to be able to... sort a specific category of product	so that I can... identify specific products and not waste time looking at other categories' products.
14. As a... Shopper I want to be able to... search for a product by name or description so that I can... find a specific product I'd like to purchase.
15. As a... Shopper I want to be able to... see a list of search results & number of results so that I can... decide quickly if the products are of interest or not.

* EPIC: Purchasing & Checkout work as expected

16. As a... Shopper I want to be able to... easily select the product I want and quantity/size if applicable so that I can... be sure the product is the one that I want and add to bag quickly.
17. As a... Shopper I want to be able to... view items added to the bag so that I can... identify the total cost of my order and all the items I will receive.
18. As a ... Shopper I want to be able to... adjust the quantity of individual items in my bag	so that I can... easily make quick changes before checkout.
19. As a... Shopper I want to be able to... easily enter payment information so that I can... check out quickly and easily.
20. As a... Shopper I want to be able to... pay for items quickly and securely so that I can... keep my credit card and delivery information safe and secure.
21. As a ... Shopper I want to be able to... view order confirmation after checkout	so that I can... be secure in the knowledge that the payment went through & order is confirmed.
22. As a... Shopper I want to be able to... receive an email confirmation after checkout so that I can... have reference to the order and financial details if needed for reference.

* EPIC: Admin and store management work as expected

23. As a ... Store Owner I want to be able to... add a product so that I can... add new items to the store.
24. As a ... Store Owner I want to be able to ... edit/update a product so that I can... change product prices, images, descriptions.
25. As a... Store Owner I want to be able to ... delete a product so that I can... remove items that are no longer for sale.
26. As a ... Store Owner I want to be able to ... review all journal comments before they are posted so that I can... only allow genuine comments & avoid potentially harmful comments to the store.

* EPIC: Journal & commenting work as expected

27. As a... Store Owner I want to be able to ... add a journal post (with date, image, text) so that I can... share with patrons/customers what the current projects are.
28. As a ... Store Owner I want to be able to... edit/update a post so that I can... update a current project/ fix errors.
29. As a ... Store Owner I want to be able to ... delete a post so that I can... remove posts that are no longer relevant/part of the brand.
30. As a ... Shopper I want to be able to... comment on a journal post so that I can... interact with other buyers/the artist or share thoughts and engage in debate.
32. As a ... Shopper I want to be able to ...(if signed in) delete a comment so that I can... change my mind and take a comment back.

### Agile methodology <a name="agile"></a>

* All functionality and development of this project will be managed through GitHub issues, milestones and projects, along with google sheets for initial conception. 

<summary>All sprints are described here.</summary>

* Sprint 1 - 10/08/2022 - 16/08/2022 (Finished at 18/08/2022)

  + Initial setup
    - Install django
    - Install Allauth
    - Add Allauth templates to project templates
    - Create base.html
    - Create Home app
    - Create index.html, view and style
    - Create responsive navigation
    - Add to README.md file
  
* Sprint 2 - 18/08/2022 - 24/08/2022 (Finished on 25/08/2022)

  + Add Product app
    - Set up all products view
    - Set up product dteail view
  + Add bag app
    - Set up add to bag
    - Set up adjust bag
    - Set up remove from bag
  + Add Responsive footer
    - Add mailchimp form
    - Create footer layout

* Sprint 3 - 25/08/2022 - 31/08/2022 (Finished on 01/09/2022)

  + Add Checkout app
    - Set up Models
    - Set up admin
    - Set up Signals
    - Set up templates
  + Add Stripe to project
    - Set up webhooks
  + Add Product form
    - Add Create product form
    - Set up create product view
    - Set up Update Product view
    - Set up Delete Product view
  + Add Contact Us
   - Create HTML
   - Set up Email functionality
   - Add link to footer

  * Sprint 4 - 01/09/2022 - 11/09/2022 (finished 11/09/2022)

    + Add Profile app
    - Set up Models
    - Set up admin
    - Set up views
    - Set up templates
    + Customise allauth templates
    - Set up templates
    - Add CSS
    + Add Toasts
    - Set up notifications with toasts

* Sprint 5 - 11/09/2022 - 24/09/2022 (Finished on 24/09/2022)

  + Add Facebook Business link
    - Create FB busness page
    - Add link in footer (not to deployed site but will be once deployed)
  + Add site policy
    - Generated a site policy with a generator site
    - Added link to the Footer
  + Add Subscription (mailchimp)
    - Form already in place for mailchimp
    - Created mailchimp account (Site is not deployed at this point)
    - Moved css to custom file
    - Moved js to bottom of base.html

## Business Model

+ A nontraditional model has been chosen, due to the volatility of the sector with a straightforward and user-friendly responsive interface.

+ This online store offers products/services to the final customer as well as services to businesses and to brands. The five main art business models are tailored to in the one web app (Direct to customer original works, Gallary sales, prints, commissions, licensing).

### Features <a name="features"></a>
* Responsive design.
* Website title and information on the site's purpose.
* Navigation Menu (Site Wide).
* Postgress databases to store information and user login/profile information.
* CRUD Functionality
* Login functionality.
* Logout functionality.
* Ability to view all products.
* Ability to view product details.
* Ability to add and remove product to the bag to purchase.
* Ability to Update quantity of or remove items in bag.
* Ability to review a product.
* Ability to sign up to a newsletter.
* Ability to view a site policy.
* Ability to contact the site owners.
* Ability to follow the site owners built in blog "journal"
* Ability to comment on blog posts and delete comments
* Ability to checkout and receive confirmation of purchase.
* Admin creation and management of products.

**Importance and Difficulty**

|       Feature         |   Difficulty   |   Importance   |
|:--------------------  |--------------- |--------------- |
|Postgress databases to |       5        |       5        |
|store information and  |                |                |
|user login/profile     |                |                |
|information            |                |                |
|:--------------------  |--------------- |--------------- |
|CRUD Functionality     |       5        |       5        |
|:--------------------  |--------------- |--------------- |
|Admin creation and     |       5        |       5        |
|management of Products |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view all    |       2        |       5        |
|products.              |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view        |       2        |       5        |
|product details        |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to add and     |       2        |       5        |
|remove a product from  |                |                |
|favourites.            |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to add and     |       2        |       5        |
|remove a product from  |                |                |
|the bag to purchase.   |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to update the  |       3        |       5        |
|quantity or remove a   |                |                |
|product from the bag.  |                |                |
|:--------------------  |--------------- |--------------- |
|Registered user can    |       5        |       5        |
|review a product.      |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to signup to   |       2        |       5        |
|a newsletter.          |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view a site |       2        |       5        |
|policy.                |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to contact the |       2        |       5        |
|site owners.           |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to checkout and|       2        |       5        |
|receive confirmation   |                |                |
|of purchase.           |                |                |
|:--------------------  |--------------- |--------------- |
|Login functionality    |       3        |       5        |
|:--------------------  |--------------- |--------------- |
|Navigation Menu        |       3        |       5        |
|(Site Wide)            |                |                |
|:--------------------  |--------------- |--------------- |
|Responsive design      |       2        |       5        |
|:--------------------  |--------------- |--------------- |
|Website title and      |       1        |       5        |
|information on the     |                |                |
|the site purpose       |                |                |
|:--------------------  |--------------- |--------------- |
|Logout functionality   |       1        |       5        |

### Future Features
As this is an educational project, it will not be maintained in the future. However, if it were a live site, some features that I would like to implement are listed below.
* Allow for admin to create discount codes and manage on site.
* Allow for the use of social sign ins.
* Allow users to edit their comment on a journal post.
* Stock control.
* Better form validation.
* User permissions / groups to allow staff to have non-breaking access to the CMS.
* Link up user profiles and subscription list.
* Further improve user experience.
* Add a FAQs section.

## Marketing <a name="marketing"></a>

+ Due to the sector this site will rely heavily on an Instagram Page with a link on the page footer. It can be viewed here:
[Instagram Page](https://www.instagram.com/bouquet/)
[Facebook Page Images](media/readme_images/instagram%20page.png)

+ This site has a Facebook Business Page with a link on the page footer. It can be viewed here:
[Facebook Page](https://www.facebook.com/)
[Facebook Page Images](media/readme_images/facebook%20page.png)

+ Users can subscribe to our newsletter to receive all offers in their email box. Subscription links are available on the footer on all pages. 

+ Upon registering, the user is shown a message confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.

+ I have searched similar websites and googled key words to apply to the site for SEO purposes:

- I have used the meta description and keywords to improve the SEO

* There are no sponsored or paid links on this site.

* Colours

The Colour scheme was generated using the eyedropper plugin to get one colour from the logo image and [colours](https://coolors.co/) to create the colour palette.

[View Pallet Here](media/readme_images/pallette.png)

* Font Selection
 
Two complimentary fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The chosen fonts were Gloria Hallelujah for the logo and titles and Raleway for everything else on the site.


## Bugs <a name="bugs"></a>

| **Bug** | **Fix** |
| ----------- | ----------- |
| .| . |
|  |  |
|   |  |
|  |  |
|  |  |
|  |  |


## Technologies Used <a name="tech"></a>

* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used on multiple pages to manipulate the DOM.
* [Python](https://www.python.org/)
    * This projects core was created using Python, the back-end logic and the means to run/view the Website.
    * Python Modules used (These can be found in the requirements.txt project file):
    * asgiref==3.5.2
    * backports.zoneinfo==0.2.1
    * boto3==1.24.75
    * botocore==1.27.75
    * dj-database-url==1.0.0
    * Django==3.2.14
    * django-allauth==0.41.0
    * django-countries==7.3.2
    * django-crispy-forms==1.14.0
    * django-storages==1.13.1
    * gunicorn==20.1.0
    * jmespath==1.0.1
    * oauthlib==3.2.0
    * Pillow==9.2.0
    * psycopg2-binary==2.9.3
    * python-dateutil==2.8.2
    * python3-openid==3.2.0
    * pytz==2022.2.1
    * requests-oauthlib==1.3.1
    * s3transfer==0.6.0
    * sqlparse==0.4.2
    * stripe==4.1.0
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
    * This project was created using the Django framework, the back-end logic and the means to run/view the Website.
* [Bootstrap](https://getbootstrap.com/)
    * The Bootstrap framework was used through the website for layout and responsiveness.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used in the project to import the fonts for the site.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website, as well as github projects to manage the planning and implementation of all functionality using a kanban board. 
* [Gitpod](https://gitpod.io/)
	* Gitpod is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [AWS S3 Buckets](https://aws.amazon.com/s3/)
	* AWS S3 Buckets provides the storage for the deployed sites static and Media files.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Am I Responsive](http://ami.responsivedesign.is/#)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README

## Testing <a name="testing"></a>

Testing is required on all features and user stories documented in the TESTING.md file linked from this README below as the testing is a large section. 
All clickable links must redirect to the correct pages. All forms linked to the database
must be tested to ensure they insert all given fields into the correct collections.

HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri).

CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code must pass through the [JSHint Validator](https://jshint.com/).

Python Code must pass through [PEP8 Validator](http://pep8online.com/)

The website was extensively tested as it was developed using:
* print().
* The terminal by printing the expected outcome.
* Testing User Stories.
* Testing scenarios manually.
* Testing functionallity manually.

This project has been tested throughout its inception. Each input has been thoroughly tested to make sure that any invalid inputs are handled correctly and a response is shown to the user.

Full test results can be found [here](TESTING.md)

## Deployment on Heroku <a name="deployment"></a>

This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
* In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
* Create your Procfile and insert the following code: ```web: ``` and make sure there is no additional blank line after it. 
* Push these files to your repository.

### Creating Heroku App
* Log into Heroku
* Select 'Create New App' from your dashboard
* Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
* Select the appropriate region based on your location
* Click 'Create App'

### Connecting to GitHub
* From the dashboard, click the 'Deploy' tab towards the top of the screen
* From here, locate 'Deployment Method' and choose 'GitHub'
* From the search bar newly appeared, locate your repository by name
* When you have located the correct repository, click 'Connect'

### Environment Variables
* Click the 'Settings' tab towards the top of the page
* Locate the 'Config Vars' and click 'Reveal Config Vars'
* Enter all variables needed.

### Heroku Postgres Database
* AWS S3 Buckets
* Paste variable in to Heroku config vars.

### Heroku Postgres Database
* Go to the resources tab in Heroku.
* In the Add-ons search bar look for Heroku Postgres & select it.
* Choose the Hobby Dev-Free option in plans.
* Click submit order form.
* Go back to the build environment and install 2 more requirements:
  * ```pip3 install dj_databse_url```
  * ```pip3 install psycopg2-binary```
  make sure to add these to the requirements file using ```pip3 freeze > requirements.txt``` 

### Set up Emails

## I used Gmail for the email on the contact page. Others can be used but will need a few changes**

* Go to settings.py and change the EMAIL_HOST_USER to your chosen email address.
* If you want to set up a new Gmail account for the site, this is the time to do so.
* Go to the Gmail account and open the 'Settings' tab.
* Go to 'Accounts and Imports' > 'Other Google Account Settings'.
* Go to the 'Security' tab and open 'Signing in to Google'.
* Click on '2-step Verification', click 'Get Started' and turn on 2-step verification following their instructions.
* Go to 'Security' > 'Signing in to Google' > 'App Passwords'.
* (You may have to input your account password again) Set 'App' to 'Mail', 'Device' to Other, and name it Django.
* The passcode that appears will be used in your Heroku variables.

## Deploy
* In Heroku, once all the variables are in place, locate 'Manual Deploy' > choose the master branch and click 'Deploy Branch'.
* Once the app is built (it may take a few minutes), click 'Open App' from the top of the page.
* Go back to the 'Deploy' tab and you can now click 'Enable Automatic Deployment'. Changes automatically deploy when you make a git push.

## Forking the Repository
* Log in to GitHub and locate the GitHub Repository.
* At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
* You will have a copy of the original repository in your GitHub account.
* You will now be able to make changes to the new version and keep the original safe. 

## Making a Local Clone
* Log into GitHub.
* Locate the repository.
* Click the 'Code' dropdown above the file list.
* Copy the URL for the repository.
* Open Git Bash on your device.
* Change the current working directory to the location where you want the cloned directory.
* Type ```git clone``` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  * ```$ git clone https://github.com/```
* Press Enter to create your local clone.

You will need to install all of the packages listed in the requirements file you can use the following command in the terminal ```pip install -r requirements.txt``` which will do it for you. 

## Credits <a name="credits"></a>

### Code
* The project is broadly based on the Boutique Ado project by the Code Institute and was used as a basse for my project (https://github.com/Code-Institute-Solutions/boutique_ado_v1/)
* The hover underline animation was built using references from (https://www.30secondsofcode.org/css/s/hover-underline-animation)
* The navbar was built using references from (https://www.w3schools.com/css/css_navbar.asp)
* The blog was built using references from (https://djangocentral.com/building-a-blog-application-with-django/)
* The card hover effects were built using references from (https://codingyaar.com/bootstrap-card-hover-effect-zoom/)
* The footer was built using references from (https://mdbootstrap.com/docs/standard/navigation/footer/)

### Media
* Images - One image used is taken from google images. All other images were taken from https://www.fleurshop.co/ with permssion from the artist himself.

### Acknowledgments
* My mentor Spence for his advice and guidance.
* Code Institutes Tutor support for their help and guidance.
* My wife Ashley for her unwaivering support and advice.
* Students of Code Institute on slack that helped with certain bugs.