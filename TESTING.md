# Testing

## Table of Contents

- [Navigation](#navigation)

- [Categories](#categories)

- [Search](#search)

- [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)

- [Login](#login)

- [Logout](#logout)


## Navigation

All navigation links can be found in navbar or on small to medium screens in the burger drop-down menu on all pages. This feature is available to all users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on homepage, click icon. | Icon shrinks and expands. User is redirected back to homepage. |
| **"All Ads" Link** | While not on All Ads page, click "Search". | User is redirected to All Ads page. |
| **"My Ads" Link** | While authenticated, click "My Ads". | Renders list view of authenticated user's ads page. |
| **"My Ads" Link** | While not authenticated, click "My Ads". | User is directed to Login form. |
| **"How It Works" Link** | While not on How It Works page, click "How it works". | User is redirected to How it works page. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Register" Link** | While not authenticated, click "Register". | User is directed to Sign Up form. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to homepage. |
| **"Search" Link** | Every user click "Search". | User is directed to All Ads page with highlited search result by titles, authors, categories and ads context. |


## Filter by Categories Option

All existing categories can be found in navbar or on small to medium screens in the burger drop-down menu on the Home and All Ads pages. This feature is available to all users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **"Every of Categories** | Click on every of the buttons with Category's name. | Renders list view of all submitted ads with this category. In case of no submitted ads with chosen key, there is an empty page. |

## CRUD

The full CRUD functionality is only available to authenticated users.

### Create
Create Profile, Ads and comments is only available to authenticated users.

#### User Registration

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Username** | Select field with placeholder "Username" and start typing. | Typing is disabled after reaching 150 characters. |
| **Email** | Select field with placeholder "Email" and start typing. | Shows validation hints based on the input: "Please include an '@' in the email address", "Please include a '.' in the email address", "Please use a valid domain for email address". |
| **Duplicate Email** | Enter an email that already exists in the database and click the "Register" button. | User is redirected back to the "Registration" page with a message stating "A user with that email already exists." |
| **Password** | Select field with placeholder "Password" and start typing. | Shows validation hints based on the input: "Password should be at least 8 characters long", "Password should contain at least one uppercase letter", "Password should contain at least one lowercase letter", "Password should contain at least one number", "Password should contain at least one special character (@, $, !, %, *, ?, &, #)". |
| **Password Confirmation** | Select field with placeholder "Confirm Password" and start typing. | Shows validation hint if the passwords do not match: "Passwords do not match". |
| **Profile Picture** | Click "Choose File" to select a profile picture file. | Selected file's name displays next to the "Choose File" button. |
| **Incomplete Form** | Failing to fill out all form fields, click the "Register" button. | User remains on the "Registration" page and is prompted to complete the missing fields. |
| **Successful Registration** | After completing all form fields accurately, click the "Register" button. | User is redirected to the newly created profile page, which includes a greeting with the username, the uploaded profile image in a circular frame, "Edit Profile" and "Delete Profile" links, a "My Ads" heading, an "Add Ad" link, and a list of the user's ads if any exist. |

#### Create Ad

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Add Ad Button** | Click "Add Ad" button. | TRedirects to the ad creation page. |
| **Title** | Select field with placeholder "Title" and start typing. | User can input the title of the ad. |
| **Description** | Select field with placeholder "Description" and start typing. | User can input the description of the ad. |
| **Categories** | Select one or multiple categories from the drop-down. | Selected categories will be associated with the ad. |
| **No Category Selected** | Submit the form without selecting any category. | User is redirected back to the ad creation form. |
| **Upload Image** | Click "Choose File" to select an image for the ad. | Selected file's name displays next to the "Choose File" button. |
| **Incomplete Form** | Failing to fill out all form fields, click the "Submit" button. | User remains on the ad creation page and is prompted to complete the missing fields. |
| **Submit Button** | After filling out all fields accurately, click the "Submit" button. | Button changes color, and upon successful submission, the user is redirected to the page with all ads, seeing their newly created ad with the uploaded image, username, date of publication, categories, text, and either the uploaded image or a default image. The ad also has "Edit" and "Delete" links. |

#### Add Comment

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Authorization** | Try to add a comment without being logged in. | User sees text with links to registration or login pages. |
| **Text Field** | Enter text into the "Text" field and click the "Add Comment" button. | Button changes color. Upon successful comment submission, user is redirected to the ad page and sees their comment. |
| **Delete Comment Link** | A "Delete Comment" link appears next to the user's own comment. | User can delete their own comment. |

### Read

Read submitted ads and comments available to all users.

#### Reading Uploaded Ads

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **General Appearance** | Open the main page, search results, category filter results, or profile page. | All ads have a consistent look: The title is an active link to the ad's page, accompanied by a mini profile image, author's username, time of posting, the ad's text, and ad's image. |
| **For Ad Authors** | If you are logged in and viewing your own ad. | "Edit" and "Delete" links are visible next to your ads. |

#### Reading Uploaded Comments

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Comment Appearance** | Open an individual ad's page. | Comments are visible only on the ad's individual page. |
| **For Comment Authors** | If you are logged in and viewing your own comment. | A "Delete Comment" link is visible next to your comment. |

### Update

Option to edit existing profile and comments is only available to authenticated users.

#### Edit Profile

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Profile Page** | Navigate to your profile page and click "Edit Profile". |  Renders profile edit form with fields pre-populated by existing data.. |
| **Cancel** | Below the edit form, click "Cancel". | User is redirected to the profile page with no action taken. |
| **Cancel** | Below edit form, click "Cancel". | User is redirected to homepage with no action taken. |
| **Update** | Alter form fields according to desired update and click "Update". | User is redirected to the profile page with a message confirming successful profile update. |
| **Incomplete form** | Fail to fill out all form fields and click "Update". | User remains on edit form view and is prompted to complete missing fields. |

#### Edit Ad

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click  submitted by different user. |  Detail view does not show "Edit" button to ensure users can only update their own ads. |
| **Edit Button** | From the ad's detail view, click "Edit" below the ad's body. This button is only visible after logging in. | Renders ad edit form with fields pre-populated by original post. |
| **Cancel** | Below edit form, click "Cancel". | User is redirected to the profile page with no action taken. |
| **Update** | Alter form fields according to desired update and click "Update". | User is redirected to the profile page with a message confirming successful ad update. |
| **Incomplete form** | Fail to fill out all form fields and click "Update". | User remains on edit form view and is prompted to complete missing fields. |

### Delete

Option to delete existing profile, ads and comments is only available to authenticated users.

#### Delete Profile

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Delete Profile Button** | On your profile page, click "Delete Profile". | A confirmation page appears asking if you're sure you want to delete your profile. |
| **Cancel** | Click "Cancel" on the confirmation page. | User is redirected back to the profile page with no action taken. |
| **Confirm Delete** | Click "Yes, Delete" on the confirmation page. | User is redirected to the homepage with a message confirming successful profile deletion. All images related to the profile are removed from the database. |

#### Delete Ad

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Delete Button** | On the ad's detail view, click "Delete". This button is only visible to the ad's author. | A confirmation page appears asking if you're sure you want to delete this ad. |
| **No, Take Me Back** | Click "No, take me back" on the confirmation page. | User is redirected back to the profile page with no action taken. |
| **Confirm Delete** | Click "Yes, Delete" on the confirmation page. | User is redirected to the profile page with a message confirming successful ad deletion. All ads related to the deleted ad are removed from the database. |

#### Delete Comment

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Delete Comment Link** | On the ad's detail view below the comment, click "Delete comment". This link is only visible to the comment's author. | A confirmation page appears asking if you're sure you want to delete this comment. |
| **No, Go Back** | Click "No, go back" on the confirmation page.| User is redirected back to the page displaying all ads with no action taken. |
| **Yes, Delete** | Click "Yes, Delete" on the confirmation page. | User is redirected back to the ad's detail page with a message confirming successful comment deletion. |

## Login

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Username** | Enter an incorrect username or password and click the "Login" button. | User is redirected back to the "Login" page with a message stating "Please enter a correct username and password. Note that both fields may be case-sensitive." |
| **Successful Login** | After entering a correct username and password, click the "Login" button. | User is redirected to the profile page. |
| **Register Link** | Click on the "Register" link. | The link gets underlined and redirects the user to the registration page. |
| **Forgot Password Link** | Click on the "Forgot Password?" link. | The link gets underlined and redirects the user to the "Reset Password" page. |

## Reset Password

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Email Input** | Enter an email into the "Email" field and click the "Send Reset Email" button. | The button gets highlighted and the user is redirected to a Django page with a confirmation text about the email being sent. |

## Logout

Allows user to sign out of existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout Link** | Click the "Logout" link in the navigation menu. | User is logged out and redirected to the homepage. |
| **Navigation Menu** | Check the navigation menu after logging out. | "Logout" link is no longer visible; "Register" and "Login" links appear instead. |

## Email Link in Footer

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Email Link in Footer** | Click on the email link in the footer. | Link is underlined upon hover and clicking it opens the default email client on your Windows system. |