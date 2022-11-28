# Inline-6 Overnight

[View the live project here.]()

This is the e-Commerce website of Inline-6 Overnight, a company that specializes in the procurement, resale, shipment and delivery of specific, brand new straight-six combustion engines at the best available prices, delivering them the next business day. It provides engine solutions to professional tuning shops, automobile repair businesses, garages, workshops, car service specialists and private owners. It’s designed to be a very simple-to-use and functional website, and also responsive and accessible on a range of devices, making it easy to navigate for any potential customers.

![Am I Responsive]()

## User Experience (UX)

### • User Stories

#### As a user, I can:

o use the website's navbar so that I can click on its links and navigate the site

o access the cart page by clicking on the cart image on the navbar so that I can see what items are currently there, the quantities and the totals

o access the checkout page so that I can see my final order, add my details and pay for it

o view the store page so that I can see all products available, access their product information and add them to my cart if I want to purchase them

o view the image of any product so that I can decide if I want to purchase it or not

o add items to the cart so that I can easily shop around the website

o update the list of items in the cart so that I can change the quantity of items and remove items once the quantity goes below zero

o access a shipping address form on the checkout page so that I can fill it out depending on whether my cart contains an item that needs to be shipped or not

o use the website's footer so that I can click on its links, access the business' social media accounts and subscribe to the newsletter

o register on the website so that I can log into the site to add products to my cart, check out and pay for my order

o log out of the website so that I can no longer add products to my cart, check out or pay for my order

o log into the website so that I can start adding products to my cart, check out and pay for my order

o click on a product's view button so that I can see the product's details

o perform any action I'm allowed to when using the website and be informed each time so that I know if my actions were successful or not

o enter my payment information so that I can purchase my chosen products

o see a 404 page displayed when I try to access a URL that does not exist on the website so that I know that such page doesn't exist

o click on the Facebook link on the website's footer to access the site's Facebook account so that I can follow the business and be aware of any news related to it or any good prices

o click on a link on the footer and provide my email address to sign up for the website's newsletter so that I can be updated on any new products or good prices

o have access to the website's privacy policy so that I know how my data is being collected and processed

o (and though I'm a person with disabilities) use the website's features so that I can access the site as easily as users who do not have special needs do

#### As a developer, I can:

o get the project set up so that I can start creating code for it

o create a templates folder so that I can store the project's templates

o create the views and URL paths so that I can render the templates

o configure the static files so that I can use images, CSS and JavaScript on the project

o design the main template so that I can have an HTML base for the project

o create the necessary models so that I can set up the project's database

o add in some user data in the admin area so that I can render it on the cart and checkout pages

o hide the user fields when the user is logged in so that I can prevent the logged in user from seeing them; and I can hide the shipping form altogether if the items don't need shipping so the user can go straight to the payment option

o build out a view in the backend that will take the checkout form data so that I can use the fetch API to send POST data from the submitFormData function and add logic to the view to process orders

o design the store page so that I can start adding functionality, style and product information to it

o click on a link on the navbar so that I can access the admin area through the frontend without the need to open the /admin URL and enter my superuser login details

o use Heroku as a cloud-hosting solution so that the website can be used accessed by any user that is connected to the Internet

o create an AWS S3 Bucket and an IAM user so that I can store the website's static and media files

o create a sitemap.xml file so that I can list the website’s important page URLs and make sure that search engines can crawl/navigate through them

o create a robots.txt file so that I can tell search engines where they are not allowed to go on the website

o test all features of the website so that any bugs are found and fixed before submitting the project

o create the website's README.md file so that all details of its creation are documented

### • Design

#### o Color Scheme

Black (#000000) and white (#FFFFFF) together is the best color scheme for e-Commerce. It's practical, professional and versatile, and it's the perfect contrast for great readability and accessibility. Grey was also used throughout the website, tweaked to make sure that, in bright light, the lighter shades of grey don't disappear (grey is only used on the h1/h2/h3/h4/h5/h6 tags for headings and the buttons on the body, so it's not used for small text). HSL, RGBA and Hex colors are used to tweak a few of the white (like "hsl(0, 0%, 98%)", "hsl(0, 0%, 80%)", "rgba(214,214,214,1)" and "#ececec") and grey (like "hsl(0, 0%, 30%)" for Hex color hex #666666) colors, as they're the websafe versions of such colors. The cart total on the cart image on the navbar is red (#FF0000), making it very readable/visible on the navbar's black background (only the circular shape for the cart total is red, so it's not used for red or small text). And Bootstrap's dark button color (#292B2C) is used for the all buttons on the website's body, making it very visible/readable. The color used for the body text was #212529 (a very dark shade of cyan-blue, which looks great on a white background). The main photo at the top of the store/main page obeys the chosen color scheme, and the product images unavoidably provide a different mix of colors.

Please see the results for the body's text color contrast check [here](docs/color-contrast-check-body-text.png).

Please see the results for the navbar's and the footer's color contrast check [here](docs/color-contrast-check-navbar-and-footer-text.png).

Please see the results for the cart total's color contrast check [here](docs/color-contrast-check-cart-total-container.png).

Please see the results for the headings "h" tags' color contrast check [here](docs/color-contrast-check-h-tags-for-headings.png).

Please see the results for the body's buttons' color contrast check [here](docs/color-contrast-check-body-buttons.png).

#### o Typography

The Roboto font makes it perfect for short pieces in all caps, and it's also effective in lowercase as paragraphing text. This is the best choice when e-Commerce products are described in long paragraphs or provided with technical specifications, as it’s the case with Inline-6 Overnight. It suits the layout and the style of this website and provides clear reading and accessibility for the user, so it was used as part of a [system font stack already available on the user's machine](docs/system-font-stack.png), which is believed to be a useful and elegant solution that eliminates the need to fetch a font elsewhere and makes load times faster (fonts are usually one of the heaviest resources loaded on any app). It matches what the current Operating System uses, so it lends a comfortable look to this project. It was imported along with the Bootstrap code used throughout the website.

#### o Imagery

Very much on purpose, there are not many images on this e-Commerce website. The main image used - [the one on the Store/main page](static/images/home-image.png) does much of the work helping the user identifying what this project is about and providing color/style to the first page the user sees when he/she lands on this e-Commerce website (it's an inline-6 engine, and there's a Nissan Skyline R34 GT-R in the background). The other images are of the engines/products sold on Inline-6 Overnight (AWS is the image-hosting service used to store the images for this project). And, of course, there's [the favicon image](static/images/favicon-engine.png) used for this website (very appropriately, an engine).

### • Wireframes

o Desktop wireframe (Store/Home 1 - user logged out) - [View](docs/wireframes/store-home-1-user-logged-out-desktop.png)

o Desktop wireframe (Store/Home 1 - user logged in) - [View](docs/wireframes/store-home-1-user-logged-in-desktop.png)

o Desktop wireframe (Store/Home 2 - user logged out) - [View](docs/wireframes/store-home-2-user-logged-out-desktop.png)

o Desktop wireframe (Store/Home 2 - user logged in) - [View](docs/wireframes/store-home-2-user-logged-in-desktop.png)

o Desktop wireframe (Store/Home 3 - user logged out) - [View](docs/wireframes/store-home-3-user-logged-out-desktop.png)

o Desktop wireframe (Store/Home 3 - user logged in) - [View](docs/wireframes/store-home-3-user-logged-in-desktop.png)

o Desktop wireframe (Footer - user logged out) - [View](docs/wireframes/footer-user-logged-out-desktop.png)

o Desktop wireframe (Footer - user logged in) - [View](docs/wireframes/footer-user-logged-in-desktop.png)

o Desktop wireframe (Sign up) - [View](docs/wireframes/sign-up-desktop.png)

o Desktop wireframe (Log in) - [View](docs/wireframes/log-in-desktop.png)

o Desktop wireframe (Product detail - user logged out) - [View](docs/wireframes/product-detail-user-logged-out-desktop.png)

o Desktop wireframe (Product detail - user logged in) - [View](docs/wireframes/product-detail-user-logged-in-desktop.png)

o Desktop wireframe (Cart) - [View](docs/wireframes/cart-desktop.png)

o Desktop wireframe (Check out - before payment) - [View](docs/wireframes/check-out-before-payment-desktop.png)

o Desktop wireframe (Check out - payment) - [View](docs/wireframes/check-out-payment-desktop.png)

o Desktop wireframe (Check out - payment - only digital products on cart) - [View](docs/wireframes/check-out-payment-only-digital-products-on-cart-desktop.png)

o Mobile wireframe (Store/Home 1 - user logged out) - [View]()

o Mobile wireframe (Store/Home 1 - user logged in) - [View]()

o Mobile wireframe (Store/Home 2 - user logged out) - [View]()

o Mobile wireframe (Store/Home 2 - user logged in) - [View]()

o Mobile wireframe (Store/Home 3 - user logged out) - [View]()

o Mobile wireframe (Store/Home 3 - user logged in) - [View]()

o Mobile wireframe (Footer - user logged out) - [View]()

o Mobile wireframe (Footer - user logged in) - [View]()

o Mobile wireframe (Sign up) - [View]()

o Mobile wireframe (Log in) - [View]()

o Mobile wireframe (Product detail - user logged out) - [View]()

o Mobile wireframe (Product detail - user logged in) - [View]()

o Mobile wireframe (Cart) - [View]()

o Mobile wireframe (Check out - before payment) - [View]()

o Mobile wireframe (Check out - payment) - [View]()

o Mobile wireframe (Check out - payment - only digital products on cart) - [View]()

### • Data Model

The data model for this project was built using Excel. A screenshot of the spreadsheet was then converted into an image file and has been made available on this README.md file. It makes extensive use of Django's built-in User model.

![Model Diagram]()

### • Agile Project Planning

This project was planned and carried out using an Agile approach. 48 User Stories were created based on the idea of building this e-Commerce website by the creator of this project, and the planning of each step in the Agile plan of action used was done based on Dennis Ivy's video tutorial on how to create an e-Commerce website with Django on YouTube (it can be found [here](https://www.youtube.com/watch?v=_ELCMngbM0E&list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)) - it greatly helped organizing the thinking and prioritization of the User Stories and tasks that led to the final product that is Inline-6 Overnight. Of course there were a lot more functionalities added to the project, with their own user stories, but Dennis Ivy's video tutorial was a huge help.

Each User Story was created on GitHub using a User Story template created for this purpose (each step of this Agile plan was created on GitHub, for that matter). The User Stories were then transferred to a Product Backlog, created using the "Milestones" tab, and refined/re-prioritized as needed.

The MoSCoW technique (MUST-have, SHOULD-have, COULD-have, WON'T-have) was then used to add one of these specific labels to each of the User Stories based on the User Story's importance to the project - these labels were also created using the "Milestones" tab.

Then, a Project called "Inline-6 Overnight User Stories" was created and, inside it, a Kanban Board, where all the User Stories were again transferred to. This simple Kanban Board has three columns - "Todo", "In Progress" and "Done" - and the User Stories would go from the "Todo" column to the "In Progress" column when they were being worked on. This was a huge help when tracking progress of what had been done and what still needed to be done throughout the project. When the User Story's tasks were performed and the User Story functionality was implemented (each User Story has its own set of tasks, and each of these were ticked and marked when completed), it would be finally moved to the "Done" column. This was basically how this project was planned and built. The Kanban Board for this project can be found [here](https://github.com/users/PedroMiguelFerreira/projects/5) - eleven User Stories were not implemented on this iteration, but they might be in the future (at the moment, they're all labelled as WON'T-have).

## Features

• 

o 

• 

o 

o 

o 

**When the user is logged out:**

**When the user is logged in:**

## Features Left to Implement

• 

• 

• 

• 

• 

• 

• 

## Technologies Used

### Languages Used

• 

• 

• 

• 

### Frameworks, Libraries, Programs, Databases & Other Tools Used

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

## Testing

### Validation Testing

The W3C Markup Validator Service, the W3C CSS Validator Service, the JSHint Static Code Analysis Tool for JavaScript and the PEP8 Online Checker were used to validate every page of this project to ensure there were no syntax errors.

• W3C Markup Validator (results)

• W3C CSS Validator - [Results]()

• JSHint - [Results]()

• PEP8 Online Checker (results)

### Testing User Stories from the User Experience (UX) Section

### Further Testing

• 

• 

• 

• 

### Security

• 

• 

• 

• 

• 

• 

• 

• 

### Known Bugs

#### Fixed Bugs

Countless bugs were found and fixed during the creation of this blog - the list is long, but here are the most memorable ones:

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

• 

#### Unfixed Bugs

• 

• 

## Deployment

GitHub is not built to handle backend languages like Python or frameworks like Django, so Heroku was used to deploy this project (all code was pushed to GitHub as normal, but the website was deployed using Heroku). DEBUG was set to False and the database, Stripe and AWS secret keys were hidden in the env.py file. The project was deployed using the following steps...

1.	Log in to Heroku.
2.	Click on New in the top-right corner and select Create New App. A unique app name must be entered. Then, select the region and click on Create App.
3.	Go to the Resources tab and add a Heroku Postgres database.
4.	On the Deploy tab, click on Settings, scroll down to Config Vars and add:

    a.  CLOUDINARY_URL (followed by the Cloudinary key)

    b.	DATABASE_URL (followed by the URL of the Heroku Postgres database)

    c.  PORT (followed by 8000)

    d.	SECRET_KEY (followed by the project's secret key)

    e.	DISABLE_COLLECTSTATIC (followed by 1) - this is during development only; this field must be removed when deploying to production

5.	On the Deploy tab, connect to GitHub (search for the repository name and click on the connect button).
6.	Scroll to the bottom of the deployment page and select the preferred deployment type: click on Enable Automatic Deploys (for automatic deployment when you push updates to GitHub) or select the correct branch for deployment from the dropdown menu and click on Deploy Branch for manual deployment (this was the option chosen for this project).

### Forking the GitHub Repository

By forking the GitHub repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1.  Log in to GitHub and locate the GitHub repository.

2.  At the top of the repository (not at the top of the page), just above the "Settings" button on the menu, locate the "Fork" button.

3.  You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1.	Log in to GitHub and locate the [GitHub repository](https://github.com/PedroMiguelFerreira/inline-6-overnight).
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash.
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/PedroMiguelFerreira/inline-6-overnight
7.	Press Enter. Your local clone will be created.

$ git clone https://github.com/PedroMiguelFerreira/inline-6-overnight

> Cloning into `CI-Clone`...

> remote: Counting objects: 10, done

> remote: Compressing objects: 100% (8/8), done

> remove: Total 10 (delta 1), reused 10 (delta 1)

> Unpacking objects: 100% (10/10), done

Click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

• 

• 

• 

• 

• 

• 

• 

• 

### Content

• 

• 

### Media

• 

• 

• 

### Acknowledgements

The creator of this blog would like to thank:

• 

• 

• 

• 
