# Local buzz
This Django project offers an opportunity for the local community to share news in an informal setting. The website combines the features of a bulletin board with casual news sharing between neighbors, like a friendly chat on the street. Topics are not restricted, as long as they fall within the bounds of common sense and decency, which are overseen by the site administrator. Anyone can post news or an advertisement, express their opinions, or simply respond to a post by leaving a comment. However, to take an active part in the life of this online community, one must become a member by registering.

Attention! The website is currently not working with an ad blocker enabled.

![responsive mockup](https://res.cloudinary.com/duwv0smeo/image/upload/v1698793373/mockup_bmltxq.jpg)


[Link to live site](https://localtalks-944a783c443e.herokuapp.com/)

## Table of Contents
- [Site Goals](#site-goals)
- [UI/UX](#uiux)
    - [Agile Methodology](#agile-methodology)
    - [Wireframes](#wireframes)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)
        - [Colour Scheme](#colour-scheme)
        - [Images and Icons](#images-and-icons)
        - [Fonts](#fonts)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [Future Features](#future-features)
- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [CRUD](#crud)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validator Testing](#validator-testing)
    - [Fixed Bugs](#fixed-bugs)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment - Heroku](#deployment-heroku)
- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)
- [Languages](#languages)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Source Credits](#source-credits)
- [Acknowledgments](#acknowledgments)

### Site Goals
This website represents a compromise between real bulletin boards, live direct communication with neighbors, and the capabilities of modern technology. It expands the possibilities of messenger groups. Here, people can not only post or obtain the information they need, comment, edit, and delete it, but also search and sort it by keywords, author, and view all their published announcements on one page. In the basic version of the website, the administrator has the ability to remove inappropriate content. The developer plans to add the ability for private comments, visible only to the author of the announcement, which should make the atmosphere of information exchange on the site even more confidential (informal).

## UI/UX

The overall design of the website should create an atmosphere of casual, informal neighborly communication. To achieve this, minimal necessary features and interactivity are configured to avoid overwhelming the user with a large number of options. The general layout, navigation, and functionality are simple and intuitive, aligning with user expectations for any standard blog website.

### Agile Methodology and User Story

Agile was used from the initial planning stage for this project. You can find more information about my development planning as well as User Story in the project I created on GitHub [here](https://github.com/users/1101712/projects/1). In it, I employed the provided Kanban board method to divide project elements into user stories and manageable tasks. The plan presented in the project represents the optimal version with features, some of which I was unable to implement due to time constraints.

### Wireframes

The initial [wireframes in Figma](https://www.figma.com/file/w9czEkU8kcSVDod6AMa5Fu/Local-Talks?type=design&node-id=0%3A1&mode=design&t=OijBKnG8otwAM68t-1) serve as a simplified blueprint of the final product and are primarily intended for planning the website's core functionalities. You can view the wireframes by following this link and selecting the desired pages from the menu at the top left, next to the palm icon. The free version of the site offers only 3 pages for wireframe development.

Not all features are covered by these initial sketches. For a comprehensive list of existing features, please refer to the [Features](#features) section.

### 5 Planes of UX

#### Strategy

The goal is to meet the needs of local communities for a dedicated space where they can share news, advertisements, and general community information in an informal, yet organized manner. Unlike social media or e-commerce platforms, the focus here is on local, neighborly interaction.

#### Scope

The project aims to provide essential features that facilitate easy interaction among community members. These include:
- **User Authentication:**   
Sign up and login functionality.
- **News and Ads Posting:**   
CRUD operations for authenticated users.
- **Search and Sort:**  
Enables users to find posts by keywords, categories, and authors.
- **Profile Page:**  
A user-specific page where one can view all their posts.

For a comprehensive overview of all the features currently implemented, see [Existing Features](#existing-features). Additional functionalities that have not yet been implemented, primarily due to time constraints, are discussed under [Future Features](#future-features).


#### Structure

The site is modeled after a simple blog or bulletin board, offering intuitive navigation. Users can browse posts and perform advanced operations like searching and sorting. However, to post an ad or news, user authentication is required.

#### Skeleton
The initial outline of the project's skeleton can be viewed in Wireframes. The structure is designed to offer intuitive navigation through a familiar layout:

- The navbar provides quick access to all     primary features and varies according to user authentication status.
- The main content is displayed in a listview, and each post links to its details.
- Buttons and links are clearly labeled, and instructions are provided where necessary.

#### Surface

The visual design aims to create an atmosphere of informal, neighborly interaction. The layout is clean and straightforward, devoid of any elements that could potentially overwhelm the user. For more details on the visual planning, see [Visual Design Choices](#visual-design-choices).

### Visual Design Choices

### Colour Scheme:
Colour palette from [ASPOSE](https://products.aspose.app)

![Colour Palette](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508011/color_u9larf.jpg)
The colours chosen are quite neutral and calming. 

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility.

### Images and Icons

There is only four static images on the site. The rest of the imagery will be uploaded by users for their individual ads. 

The design of the site includes images and icons made in the style of children's drawings. This style was chosen intentionally. The aim of using such images and icons is to create an atmosphere of trust and openness. 

We want every visitor to our site to feel comfortable and not have the sensation that they are being manipulated or used for commercial purposes. The style of children's drawings contributes to a subconscious feeling of immediacy and sincerity, making the interaction with the site more pleasant and trustworthy.

### Fonts

[PT Font Family](https://company.paratype.com/pt-sans-pt-serif)

The fonts from the PT Family were chosed to make the website futureproof. As already mentioned, I plan on adding multilanguage support to this project, and the Paratype fonts are built around non-latin characters, such as the Cyrillic alphabet and special charachters used in post-Soviet countries, which are very rare to find in fonts produced in the anglophone world. While dealing with an impressive amount of letters from different language families, the PT font never compromises on aestetics - it has been created by the internationally acclaimed typeface designer [Alexandra Korolkova](https://en.wikipedia.org/wiki/Alexandra_Korolkova) and Olga Umpelova.

## Features

### Existing Features

#### Navigation
- Navbar with nav links and search
- Different links visible for authenticated and unauthenticated users
- Active link rendered bald
- Collapsible burger menu with drop-down on small to medium screens

![navbar](https://res.cloudinary.com/duwv0smeo/image/upload/v1698748926/nav1_c5cil7.jpg)

![navbar](https://res.cloudinary.com/duwv0smeo/image/upload/v1698748933/nav2_zpcyqg.jpg)

![burger menu](https://res.cloudinary.com/duwv0smeo/image/upload/v1698748957/nav3_fuwztk.jpg)

#### Сategory Panel
- Panel with links to ads by category
- The category that the mouse hovers over is    
  highlighted in purple
- Collapsible burger menu with drop-down on small to medium screens

![Categories navbar](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507999/categ-nav1_io7mic.jpg)

![Categories navbar](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508003/categ-nav2_qfwizy.jpg) 

#### Search Feature

- **The search functionality:**   
by the titles of the ads, categories, authors, and the text within the ads.

- **Highlighting:**  
The search results provide highlighted keywords to make it easier for you to find exactly what you're looking for. While the author names are searchable, they are not highlighted in the search results, as they are already displayed in bold text for easier recognition.  
For a glimpse of how this works, here's an example of search results for the query "al":

![Search](https://res.cloudinary.com/duwv0smeo/image/upload/v1698749421/search_ctlupo.jpg)

![Search Results](https://res.cloudinary.com/duwv0smeo/image/upload/v1698749428/search-results_kaebuu.jpg)

#### Ads by Categories Page

The page for all ads by categories is designed in a consistent style and displays all ads in the category selected by the user.

![Ads by categories page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507987/ads_by_categ_icltgv.jpg)

#### Home Page

Add Listing Button: Different text is displayed for authenticated and unauthenticated users. Unregistered users are informed that they need to register in order to post an ad.

Only the latest 6 listings are displayed. On their own ads, the user sees links to the option to edit or delete the ad. 

The ad title is an active link to the ad's individual page.
In the listing box, you can see the title, a mini-profile picture icon or a default image, information about the author, the publication date, and the category, as well as an image uploaded by the author or a default image. The ad is not limited in character count, but it is restricted in how much text is displayed in the listing field. To view the entire text, a scrolling feature is utilized.

Default images are included to maintain a consistent style.
Unlogged users cannot see the edit or delete ads buttons.
At the bottom of the main page, below the first 6 ads, there is a link to the page with all ads. It is designed in the  the same for all links way — purple in color and underlined when hovered over with the mouse.

![home page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698750024/home1_k9jvbv.jpg)

![home page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698750027/home2_ny440s.jpg)


#### Footer

In the footer, you can find contact information: the site admin's email, which is also a link styled in the same way — purple and underlined when hovered over with the mouse.  
As the website continues to develop, a contact form will be implemented instead of Email to prevent spam. If social media accounts are created, they will also be featured in the website footer.

![footer](https://res.cloudinary.com/duwv0smeo/image/upload/v1698750218/footer_csjh0w.jpg)

#### All Ads Page

In addition to the main page, which displays only the first 6 listings, we have created a dedicated 'All Ads' page. It has a design similar to the main page, with a few subtle differences.The purpose of this page is to provide users with access to the entire range of listings without any limitations. This way, users can explore more options and find exactly what they are looking for. 

Just like on the main page, this page also features an 'Add Listing' button, styled identically for a consistent user experience. 

The page starts with the heading 'All Ads' and displays 6 listings at a time, similar to the main page. To navigate through multiple listings, pagination is available at the bottom of the page. The current page in the pagination is highlighted in the same color as the category panel, for a unified visual experience.

From a development perspective, having a dedicated 'All Ads' page offers several advantages. First, it helps in optimizing performance; the main page can load faster as it only needs to fetch and display a limited number of listings. This is especially beneficial for users with slower internet connections. Secondly, it provides a more modular approach to development. Features like sorting, filtering, and advanced search can be implemented on the 'All Ads' page without cluttering the main page, making the codebase easier to manage and extend. Lastly, it allows for more targeted analytics. By tracking user interactions on the 'All Ads' page separately, developers can gain insights into user behavior that can be used for future improvements. Overall, the 'All Ads' page not only enhances the user experience but also provides a more manageable and scalable solution for developers.

![All ads page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507995/all-ads_jpskh9.jpg)

#### Registration Page

Here, the user is required to fill out an extended standard form with a username and email. The user must also choose a password and confirm it. Optionally, as a non-mandatory feature, the user can upload an image for their profile, which will then be automatically resized to fit specified parameters. Unlike other required fields, the form allows the user to skip the image upload. In this case, the system will use a default image.

#### Dynamic hints

In addition to the form fields, the registration page features dynamic hints to assist users in filling out their email and password. These hints serve as error prompts, helping users understand the requirements for each field. The hints are implemented using JavaScript and are displayed below the input fields.
Password Hints

- **For the password**,  
    the following conditions are displayed to the user as they type:

        The password must be at least 8 characters long.
        It should contain at least one uppercase letter.
        It should contain at least one lowercase letter.
        It should contain at least one number.
        It should contain at least one special character (such as @, $, !, %, *, ?, &, #).

    The hint text dynamically shrinks as the user meets each of these requirements.
    Confirm Password

    When the user is confirming their password, real-time validation occurs. The hint for this field operates on an error principle and will display a message until there is an exact match between the entered passwords.
    Email Hints

    ![registration hint](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751581/registr2_zctdnt.jpg)

- **For the email field**,   
    the following conditions are displayed:

        The email must contain an '@'.
        The email must contain a '.'.
        The email should be in a valid domain format.

    The hint text for the email also dynamically updates based on user input, guiding them to meet the email format requirements.

The hints are styled with a specific color (#76161eda) to ensure they are noticeable yet not too distracting. These interactive features make the registration process more user-friendly by providing immediate feedback and guidance.

![registration form](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751576/registr_r84b9k.jpg)

- **Email Already Exists Scenario:**  
    After the user submits the form, the back-end logic in Django checks whether the provided email already exists in the database. This is done in the RegisterView class within the form_valid method. If a user attempts to register with an email that already exists, a message will be displayed to inform them that a user with that email already exists. The user will then be redirected back to the registration page to correct this issue.

    ![email already exist](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751591/registr-email-exist_lvmyfr.jpg)

After successful registration, the user is redirected to the newly created profile page. where they will subsequently see all of their ads. Additionally, the user will see a confirmation message upon successful account creation. Otherwise, an error message will be displayed.

![account sucsess](https://res.cloudinary.com/duwv0smeo/image/upload/v1698778501/account-create-success_redgzp.jpg)

With these added features, the registration page becomes not only a gateway for new users but also a comprehensive, user-friendly interface that guides users through the process, helping them correct errors and understand requirements.

#### Login 

In the application, users can securely log in through an authentication process.   
If the user enters an incorrect Username or password, they will see an error message with a hint.

![login](https://res.cloudinary.com/duwv0smeo/image/upload/v1698779516/login-error_irlhmr.jpg)

Additionally, if a user forgets their password, the system provides a password reset functionality to help them regain access to their account.

Initially designed to send an email for password reset functionality, the feature has been adapted due to difficulties with sending emails from Gitpod. 

![login](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751916/login1_pd4twq.jpg)

![login reset](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751924/login-reset-pass_d0wjvq.jpg)

![reset email](https://res.cloudinary.com/duwv0smeo/image/upload/v1698751933/login-reset-message_dqa15r.jpg)

#### My Ads Page

User's Ads Page (also known as Profile Page)
This page is designed in a consistent style, but without Ad Category panel. The page is accessible only to registered and authenticated users. If a user is not authenticated, they will be prompted to log in or register. Authenticated users see a greeting with their name on their page, their rounded profile image links to edit or delete their profile, a link to add a new listing, and all the listings they have published with options to edit or delete each listing. All links are styled in the same way — purple and underlined when hovered over with the mouse — consistent with the overall site design.

![Profile page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698752085/profile_a05iyw.jpg)

#### Profile Editing Page

The user can change or delete their uploaded image. If the image is deleted, it will be replaced with a default image. After completing the editing process, the user will see a message indicating the successful completion of the profile edit. Otherwise, an error message will be displayed. The user will be redirected back to their profile page.

![Profile edit](https://res.cloudinary.com/duwv0smeo/image/upload/v1698780388/profile-edit_sjyp8u.jpg)

![Profile edit](https://res.cloudinary.com/duwv0smeo/image/upload/v1698780624/profile-edit-suc_vrd1ck.jpg)

#### Profile Deletion Page

The user can delete their profile. Before finalizing the deletion, the user will need to confirm their intent to delete the profile. After clicking the confirmation button again, the user will see a message stating that their profile has been deleted. Otherwise, an error message will be displayed. The user will be redirected to the Home Page.

![Profile delete](https://res.cloudinary.com/duwv0smeo/image/upload/v1698752430/profile-delete_azbeyb.jpg)

![Profile delete](https://res.cloudinary.com/duwv0smeo/image/upload/v1698752435/profile-delete-confirm_njnj8c.jpg)

#### Ad Creation
 
Only a registered and authorized user can create an ad. On the ad creation page, the user is prompted to come up with a title, create the text, optionally add an image, and select one or more categories.   
Text editing is not available in the current version, but it is a priority for future development of the website.  
The layout of the ad creation field follows the style of the ad itself. After the successful creation of the ad, the user is redirected to the page displaying all ads, where they can see their newly published ad, as well as receive a message confirming the successful creation of the ad. Otherwise, an error message will be displayed.

![Ad creation](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507954/ad-create_yufqh3.jpg)

![Ad Creation Confirmation](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507970/ad-create-confirm_ijxn9g.jpg)

#### Ad Editing

Only the authorized author of the ad can edit it. If necessary, the user can make changes to any previously selected fields. The layout of the ad editing field also follows the style of the ad itself. After successfully editing the ad, the user is redirected to their profile page, where they can see all of their ads and receive a message confirming the successful update of the ad. Otherwise, an error message will be displayed.

![Ad Editing](https://res.cloudinary.com/duwv0smeo/image/upload/v1698782257/ad-edit_jy4peh.jpg)

![Ad Editing Confirmation](https://res.cloudinary.com/duwv0smeo/image/upload/v1698507980/ad-edit-confirm_n6esnh.jpg)

#### Ad Deletion

 Only the authorized author of the ad can delete it. Before deleting, the user will need to confirm their intent. After confirmation and successful deletion, the user will see a confirmation message. Otherwise, an error message will be displayed.

 ![Ad deletion](https://res.cloudinary.com/duwv0smeo/image/upload/v1698783252/ad-delet-conf_u3z8bl.jpg)

 ![Ad deletion](https://res.cloudinary.com/duwv0smeo/image/upload/v1698783325/ad-del-confirm_giv9tr.jpg)

#### Ads Page with ad details and comments

The user is redirected to this page when they click on the title of the ad, which is an active link. The ads page is designed in a consistent style, but without Ad Category panel. Here, in addition to the ad itself, all comments on the ads are visible. Depending on whether the user is authenticated, they may or may not see text with links inviting them to log in or register in order to leave a comment, as well as links with the option to delete a comment.

This is how the page looks for a user who has left a comment:

![Ads page](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508016/comment1_cuw8ha.jpg) 

This is how the page looks for a user who is not authenticated:

![Comments](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508019/comment2_pgdpca.jpg)

This is how the page looks for a user who is neither the author of the ad nor the author of the comment:

![Comments](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508026/comment3_jeakm6.jpg)

#### Comment Edition and Deletion

On the page of the ad to which the user has left a comment, provided that the user is authenticated, the user can delete their comment and, if necessary, write a new one. Only the authorized author of a comment has the right to delete it. Before finalizing the deletion, the user will need to confirm their intent to delete the comment. After deleting the comment, the user will see a message confirming that their comment has been deleted. The user will be redirected back to the ad page to which the comment was just deleted. Otherwise, an error message will be displayed.

We intentionally did not add the ability to edit comments, as we fundamentally believe that editing should come with the ability to view comment history, which would take too much time within the scope of this educational project. However, such an option should definitely be implemented in the future.

![Comments deletion](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508034/comment-del-confirm_f5wg9h.jpg)

![Comments deletion](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508029/comment-del_tui21e.jpg)

#### How It Works Page

This page  introduces a comprehensive "How it Works" guide aimed at helping users navigate and make the most out of the "Local Buzz" platform. The guide covers everything from account creation and management, using default images, posting ads, to interacting with other users through comments. It explains how to use  default images for profiles and ads, categorized view for easier navigation, and efficient search functionality.

![Site rules](https://res.cloudinary.com/duwv0smeo/image/upload/v1698754438/rules_kly0x2.jpg)

### Security Features and Defensive Design

#### Authentication and Authorization:

- **Custom User Model:**      
    The application uses a custom user model CustomUser with unique email constraints.

- **Login Required:**  
    Several views like ProfileView, ProfileEditView, ProfileDeleteView, etc., are protected by Django's LoginRequiredMixin, ensuring that only authenticated users can access these views.
- **Ownership Checks:**   
    For example for deleting comments (CommentDeleteView), the application checks if the user attempting to delete the comment is indeed the author.

#### Database Security

- The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Due to an oversight, the database URL and secret key were initially committed to GitHub. However, all passwords and keys have since been regenerated. They are now stored in an env.py file, which is included in the .gitignore to prevent unwanted access to the database.

#### User Input Handling:

- **Form Validation:**  
    Django forms (CommentForm, AdForm, etc.) are used to validate user input before saving it to the database. 

- **Real-Time Form Validation:**  
    Dynamic Hints: The application provides real-time hints during the process of filling out the registration form. The hints are generated by JavaScript and displayed below the input fields for password and email.

- **Password Complexity:**  
    The JavaScript code enforces password complexity requirements, ensuring that the password contains a mix of uppercase letters, lowercase letters, numbers, and special characters. This helps improve the security of user accounts.

- **Password Confirmation:**  
    A real-time check is performed to make sure the confirmed password matches the initial password. This minimizes the risk of users setting unintended passwords.

- **Email Format Validation:**  
   The JavaScript code validates the email format in real-time, providing hints about missing '@' or '.' symbols or if the overall format does not match the required email format.

- **Escaping User Input:**  
   The function highlight_text is designed to highlight text in search results, which could help in preventing issues related to HTML injection if properly used.

#### File Handling:

- **Default Image:**  
    In the absence of a user-provided image, a default image is used.



#### Messages:

- **User Feedback:**     
    Uses Django's messaging framework for providing feedback like 'Profile updated successfully', etc., which is a good practice for UX but also can be seen as a security feature to confirm the action.

- **Error Feedback:**  
     Real-time feedback is not just a user experience feature but also a security measure, as it guides users to input data in a secure and correct format, thus reducing the chances of error or security vulnerability.


#### Signals:

- **Post-save and Post-delete Signals:**     
    Utilizes Django's signal mechanism to handle related activities post-save and post-delete, like creating a user profile or deleting associated images.

#### Others:

- **Pagination:**  
    The application uses Django's built-in pagination features to limit the number of displayed ads, which can prevent Denial of Service (DoS) attacks aimed at database exhaustion.

#### Notes:

Although the application has CSRF protection enabled by default (thanks to Django), it's not explicitly mentioned in the code. Database queries are generally well-parameterized to avoid SQL injection. The application uses Django's built-in password validators for increased security. 

While these practices enhance security, it's crucial to note that they are part of a layered security strategy and should not be relied upon as the only means of securing an application.

### Special Features:

#### Image Handling with Cloudinary

We use Cloudinary for image storage and manipulation. This ensures that all images are securely stored and optimally delivered.  
upload_image_to_cloudinary function takes a file and a default URL as parameters. If a file is provided, it uploads the file to Cloudinary, gets a secure URL, and adds an auto-format parameter to it.If no file is provided, the function returns a default URL. In case of any exception during the upload, an error message is printed and the default URL is returned.

#### Unique Email and Username Validation:

The application ensures that each user has a unique email address and Username. This validation is performed in the ExtendedUserCreationForm class via the clean_email method. The method checks the database for existing accounts with the same email and raises a validation error if a duplicate is found.

### CRUD

The CRUD principle served as the cornerstone for this project's design process. For a detailed overview of all CRUD functionalities, please refer to the [Features](#features) section.

**Create:**  
An authenticated user can create and save profiles, ads, and comments.

**Read:**  
Users can browse and read their own as well as other users' ads and comments.

**Update:**  
An authenticated user can edit and update their own saved profiles and ads.

**Delete:**  
An authenticated user has the capability to delete their own saved profiles, ads, and comments.

### 🚀 Future Features

#### For Users
- **Comment Edit History:**  
    Allow users to view the history of their edited comments.

- **Notification for Comments:**      
    Users will receive a notification when someone comments on their post.

- **Private Commenting:**  
    Enable the option for comments to be private, visible only to the author of the post.

- **Text Editing for Ads:**
    Implement a rich text editor for creating and editing ad content, offering users more formatting options.

- **User Bio:**
    Allow users to add a short bio or description about themselves on their profile page.

- **Clickable Profile Mini-Image:**
    The user's profile mini-image will serve as a clickable link leading to a page with more detailed information that the user wants to share about themselves.

#### For Admins
- **New Post Alerts:**  
    Admins will be notified of new posts.

- **User Management:**      
    Admins will have the ability to ban users and send them personal messages or warnings about undesirable actions.

#### General Enhancements

- **Location Mapping:**   
    Allow users to add a location related to the post on a map.

#### Security

Django provides a robust foundation for building secure web applications. However, there are additional measures that can further enhance security:


- **Two-Factor Authentication:**  
    Implement 2FA to enhance user security.

- **Rate Limiting:**   
    Implement rate limiting on API and user routes to improve security against brute-force attacks.
- **Two-Factor Authentication (2FA):**  
    Implementing 2FA can add an extra layer of security during user logins.

- **Rate Limiting:**  
    To safeguard against abuse, rate limiting can be applied to API and user routes.

- **Data Validation:**  
    It is advisable to validate data on both client and server sides for additional security.

- **Logging and Monitoring:**  
    Robust logging mechanisms can help in tracking unauthorized access or other security incidents.
    
- **Regular Updates:**  
    Keeping all packages up to date is essential for benefiting from the latest security patches.

With the use of class-based views and existing user authentication mechanisms, these security features can be seamlessly integrated into the current codebase.

## Database Design

### Database Model

- **CustomUser and UserProfile:**

One to One (OneToOneField). Each CustomUser has exactly one UserProfile. This extends the user information by adding additional fields such as bio.

- **CustomUser and Ad:**

One to Many (ForeignKey). A single user (CustomUser) can create multiple ads (Ad), but each ad belongs to only one user.

- **CustomUser and Comment:**

One to Many (ForeignKey). One user can leave multiple comments (Comment), but each comment belongs to only one user.

- **Ad and Category:**

Many to Many (ManyToManyField). One ad can belong to multiple categories, and one category can contain multiple ads.

- **Ad and Comment:**

One to Many (ForeignKey). One ad can have multiple comments, but each comment belongs to only one ad.

- **Signals**

After saving CustomUser, a UserProfile is automatically created.


The database model diagram was designed using [Drawio](https://app.diagrams.net/).
The first draft of the entity relationship diagram does not include all models and connections used in the final database.

![Database](https://res.cloudinary.com/duwv0smeo/image/upload/v1698508039/data-model_yzh68a.jpg)

## Testing

### Manual Testing

Testing and results can be found [here](/TESTING.md)

### Validator Testing

#### HTML [W3C validator](https://validator.w3.org/)

As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Bootstrap templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.

All HTML files have been verified with the above validator.

All files, except for 'Create New Ad,' yielded the same result:

"Document checking completed. No errors or warnings to show".

**Create New Ad**  
HTML Validation Issue on the Ad Creation Page  
Description:  

    Error: No p element in scope but a p end tag seen.

    From line 155, column 3; to line 155, column 6

      ↩    ↩  </p> <!--   

The HTML validator throws an error on the ad creation page. The error is related to an extra closing <p> tag in the generated form markup. This could lead to unpredictable rendering or behavior across various browsers.
Details:  

    Template file: create_ad.html
    Line with the issue: {{ form.as_p }}
    Validator error: "No p element in scope but a p end tag seen."

Solution:  
Created a custom Django template filter named render_as_list_items that renders the form fields as list items within an unordered list.  
Subsequent Issue:  
New validation errors emerged, stating that the <li> tags were not allowed as a child of the <form> element.  

Solution:  
Enclosed {{ form|render_as_list_items }} within a <ul> tag, which resolved the validation issue by making the <li> tags valid within the form.  

After fixing the code, the validator found no errors or warnings:  
Document checking completed. No errors or warnings to show.  


#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No error found.

#### JavaScript [JSHint](https://jshint.com/)

No error, no warnings found.

#### Python [CI Python Linter](https://pep8ci.herokuapp.com/)

All files with python code have been verified with the above validator.
All files yielded the same result - "All clear, no errors found".

### Fixed bugs


### Accessibility [axe DevTools Chrome Extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)

### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance. 

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| Desktop        |              |               |                 |     |
| Home           |           99 |            96 |              92 | 100 |
| All Ads        |           99 |            96 |              92 | 100 |
| My Ads         |           98 |            96 |              92 | 100 |
| How it works   |           99 |            96 |              92 | 100 |
| Register       |           99 |            96 |              92 | 100 |
| Login          |           99 |            96 |              92 | 100 |

![Accessibility](https://res.cloudinary.com/duwv0smeo/image/upload/v1698775956/accessibility-desk_mhffog.jpg)

### Browser Testing
- The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

### Device Testing
- The website was viewed on [a variety of devices](https://mobilemoxie.com/tools/mobile-page-test/) such as Desktop, Laptop, iPhone 8, iPhoneXR and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

## Unfixed Bugs
No Unfixed bugs  

## Deployment - Heroku

### Installing Required Libraries

Before deploying on Heroku, you'll need to install several libraries:

- Install **Gunicorn** (a server used to run Django on Heroku):  
pip3 install django gunicorn

- Install **pyscopg2** (connects to PostgreSQL):  
pip3 install dj_database_url pyscopg2  

- Install Cloudinary (hosts static files and images):  
pip3 install dj3-cloudinary-storage

- Install Whitenoise (prevents issues with Heroku not rendering custom stylesheet):  
pip3 install whitenoise

- Install dj-database-url (enables URL-based database configuration):  
pip3 install dj-database-url

### Create the Heroku App

- Log in to Heroku or create an account.
- Create a new app by clicking New > Create New App.
- Give your app a unique and meaningful name and select your region.

### Database Setup

#### ElephantSQL for PostgreSQL

- Log into [ElephantSQL](https://api.elephantsql.com) and create a new instance.
- Copy the DATABASE_URL from the instance details.

### Configuring Environment Variables

- Create an env.py file in your project root.
- Add your DATABASE_URL and SECRET_KEY to env.py
- Make sure env.py is in your .gitignore file to keep these sensitive details out of your repository.
- Add Cloudinary URL to env.py

### Update Django Settings

- Add the following to the top of your settings.py
import os
import dj_database_url
if os.path.exists('env.py'):
    import env

- Update your DATABASES settings to use dj_database_url  
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

- Replace the default SECRET_KEY with your environment variable:  
SECRET_KEY = os.environ.get('SECRET_KEY')

- Add Heroku to the ALLOWED_HOSTS list:  
ALLOWED_HOSTS = ['<your-heroku-app-name>.herokuapp.com', 'localhost']

### Additional Required Files

- Create a requirements.txt file to list all your Python dependencies.
- Create a Procfile in your project root and add:  
web: gunicorn <your-project-name>.wsgi:application

### Media Storage in the Project

In this project, we use a Cloudinary to storage media files.

### Update Heroku Config Vars

- Open your Heroku app's settings and add the following Config Vars:  
    SECRET_KEY
    DATABASE_URL
    EMAIL_HOST_PASSWORD
    EMAIL_HOST_USER
    CLOUDINARY_URL

### Deploying the App

- Make sure that DEBUG is set to False in your settings.py.
- Make sure to add X_FRAME_OPTIONS = 'SAMEORIGIN' in your settings.py.
- Go to the Deploy tab on Heroku, connect your GitHub repository, and either enable automatic deploys or deploy manually.

Your app should now be live and operational!

#### Deployin Isuues

During deployment to Heroku, it turned out that the basic structure of the Django project was compromised. A project folder was created within another folder of the same name. To fix this issue, we had to move the entire project up one level and delete the unnecessary folder. In the process, we also had to adjust all paths and settings.

However, we encountered limitations with Heroku's ephemeral filesystem, which does not support permanent storage of images. To address this, we transitioned to using Cloudinary for image storage.

Before Cloudinary

Originally, our application had a set of features for handling images:

    CustomUser Profile Pictures:
    Before saving an edited CustomUser with a new profile picture, the old profile picture was deleted from the server.

    Ad Images:
    Upon deleting an Ad, its associated picture was also deleted from the server.

    CustomUser Deletion:
    When a CustomUser was deleted, all of their associated pictures and ads were also deleted.

This architecture was designed to offer a flexible and scalable way to manage users, ads, and comments, as well as their interrelationships.

Now we use the Cloudinary Python library to upload images and return secure URLs, which are then stored in our database. Cloudinary also allows us to handle errors gracefully, ensuring a smooth user experience.

This transition has been a vital step in ensuring that our application remains robust and scalable, while also being compatible with cloud-based hosting services like Heroku.

## Development

### Fork

- Locate the repository at this link [Local buzz](https://github.com/1101712/Local-Talks).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

### Clone

To clone this repository follow the below steps: 

1. Locate the repository at this link [Local buzz](https://github.com/1101712/Local-Talks). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

### Download ZIP

- Log into GitHub and click on repository to download [Local buzz](https://github.com/1101712/Local-Talks])
- Select **Code** and click "Download Zip" file
- Once download is completed, extract ZIP file and use in your local environment

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
### Python Libraries

- [os](https://docs.python.org/3/library/os.html) - Standard Python library for interacting with the operating system.
- [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library for image manipulation.

### Django Modules

- [django.shortcuts](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/) - Utilities for handling HTTP shortcuts.
- [django.views](https://docs.djangoproject.com/en/4.2/topics/http/views/) - Base views for handling HTTP responses.
- [django.contrib.auth](https://docs.djangoproject.com/en/4.2/topics/auth/) - Authentication and user management.
- [django.http](https://docs.djangoproject.com/en/4.2/topics/http/) - Handling HTTP responses.
- [django.db.models](https://docs.djangoproject.com/en/4.2/topics/db/models/) - Object-relational mapping (ORM) for database queries.
- [django.forms](https://docs.djangoproject.com/en/4.2/topics/forms/) - Handling HTML forms.

### External Libraries and Packages

- [asgiref](https://pypi.org/project/asgiref/) - ASGI compatibility library.
- [backports.zoneinfo](https://pypi.org/project/backports.zoneinfo/) - Backports of the Python 3.9 zoneinfo module.
- [sqlparse](https://pypi.org/project/sqlparse/) - SQL query parser.
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter.
- [python-decouple](https://pypi.org/project/python-decouple/) - Strict separation of settings from code.

### Frontend Technologies

- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/): Framework for developing responsive and mobile-first web design.
- [Free Frontend](https://freefrontend.com/): Resource for ready-made frontend solutions and templates.
- [Google Fonts](https://fonts.google.com/): Library of free fonts.

### Code Validation and Styling

- [PEP 8 Checker](https://pep8ci.herokuapp.com/): Online service for checking code adherence to PEP 8 standards.
- [W3C HTML Validator](https://validator.w3.org/#validate_by_input): HTML validator by the W3C consortium.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator): CSS validator by the W3C consortium.
- [JSHint](https://jshint.com/): JavaScript code quality tool.
- [ESLint](https://eslint.org/): Linting utility for JavaScript.

### Design and Prototyping

- [ami.responsivedesign.is](http://ami.responsivedesign.is/): Tool for viewing your design on various devices.
- [Draw.io](https://app.diagrams.net/): Tool for creating data diagrams and charts.
- [Figma](https://www.figma.com/): Platform for UI/UX design prototyping.
- [Color Wheel](https://products.aspose.app/html/ru/color-wheel): Tool for color scheme selection.

### Database Management

- [SQL OnLine IDE](https://sqliteonline.com/): Online IDE for SQL.
- [ElephantSQL](https://www.elephantsql.com/): PostgreSQL database hosting service.

### Development and Deployment

- [GitHub](https://github.com/): Version control and code hosting platform.
- [GitPod](https://gitpod.io/): Online IDE for development.
- [Heroku](https://heroku.com/): Cloud platform for app hosting.

### Additional Tools

- [Markdown Live Preview](https://markdownlivepreview.com/): Online editor for Markdown file preview.
- [Guru99 on Web Testing](https://www.guru99.com/web-application-testing.html): Resource for manual web application testing guidelines.
- [Grammarly](https://www.grammarly.com/): Grammar and style checker.
- [Commit Message Generator](https://cbea.ms/git-commit/): Git commit message generator.
- [Chat GPT](https://openai.com/): Artificial intelligence for text generation.
- [Pythontutor](https://pythontutor.com/)
- [Website Screenshot API ](https://www.page2images.com/): site mockap generator


##  Source Credits

### Educational and Official Documentation

- [W3Schools](https://www.w3schools.com/): Used for HTML, CSS, and JavaScript references.
- [Django Docs](https://docs.djangoproject.com/en/4.1/): Official Django documentation was a go-to resource for backend functionalities.
- [Deployment checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/): Utilized for Bootstrap classes and components.
- [Mozilla Developer Network (MDN) Docs](https://developer.mozilla.org/): Comprehensive resource for web technologies.
- [Real Python](https://realpython.com/): In-depth Python tutorials and articles.
- [GeeksforGeeks](https://www.geeksforgeeks.org/): Useful for understanding algorithms and data structures.
- [FreeCodeCamp](https://www.freecodecamp.org/): Free coding bootcamp with interactive lessons.
- [LeetCode](https://leetcode.com/): For coding challenges and interview preparation.
- [Python Runtime Error](https://devcenter.heroku.com/articles/python-runtimes)

### Community Support

- [Stack Overflow](https://stackoverflow.com/): Community support for code troubleshooting.

### Media Content

- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com.
- [BBC Goodfood](https://www.bbcgoodfood.com/): All recipe content was sourced from BBC Goodfood.

### Tutorials and Examples

- [Update View](https://pytutorial.com/django-updateview-example): Tutorial on Django UpdateView.
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view): Used Django's own documentation for implementing pagination.
- [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html): Documentation for implementing AutoSlugField in Django.
  
### Projects and Repositories

- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog), [Code Institute](https://codeinstitute.net/ie/),  tutorials ["Hello Django"](https://github.com/ckz8780/ci-fsf-hello-django/tree/c13b414fd2e87a54b4f2788ceffec55be4ade925) and ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/Django3blog): Used as a reference for Django project structure.
  
### Custom Functions and Boilerplate

- [Ian Meigh - Custom Validator function](eateasy/validators.py): Custom validator function for specific use cases.
- [Code Institute's Django3blog source code](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/06_creating_our_first_view/templates/index.html) for adding conditional pagination, including page navigation links. Styling was customized.

## Acknowledgments
- To Kay Welfare, for providing great psyhological support and motivation.
- To Margarita Andrianova for helping to resolve the technical questions.
- I would like to mentions Openais ChatGPT, which gave me a huge opportunity to study quickly and very efficiently.
- To the Code Institute Slack community.

