# Local buzz
This Django project offers an opportunity for the local community to share news in an informal setting. The website combines the features of a bulletin board with casual news sharing between neighbors, like a friendly chat on the street. Topics are not restricted, as long as they fall within the bounds of common sense and decency, which are overseen by the site administrator. Anyone can post news or an advertisement, express their opinions, or simply respond to a post by leaving a comment. However, to take an active part in the life of this online community, one must become a member by registering.

[Link to live site](https://herokuapp.com/)

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
    - [Existing Features](existing-features)
        - [Header](#header)
        - [Footer](#footer)
        - [Home Page](#home-page)
        - [User Account Pages](#user-account-pages)
        - [Browse Ads](#browse-ads)
        - [Ad Detail Page](#ad-detail-page)
        - [Add Ad Form](#add-ad-form)
        - [Update Ad Form](#update-ad-form)
        - [Delete Ad](#delete-ad)
        - [My Posts](#my-posts)
        - [My Bookmarks](#my-bookmarks)
        - [Error Pages](#error-pages)
    - [Security Features and Defensive Design](#security-features-and-defensive-design)
        - [User Authentication](#user-authentication)
        - [Form Validation](#form-validation)
        - [Database Security](#database-security)
        - [Custom error pages](#custom-error-pages)
    - [Future Features](#future-features)
- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [Custom Model](#custom-model)
    - [CRUD](#crud)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Testing](#testing)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment - Heroku](#deployment---heroku)
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

    - User Authentication: Sign up and login functionality.
    - News and Ads Posting: CRUD operations for authenticated users.
    - Search and Sort: Enables users to find posts by keywords, categories, and authors.
    - Profile Page: A user-specific page where one can view all their posts.
For a comprehensive overview of all the features currently implemented, see [Existing Features](#existing-features). Additional functionalities that have not yet been implemented, primarily due to time constraints, are discussed under [Future Features](#possible-future-features).


#### Structure

The site is modeled after a simple blog or bulletin board, offering intuitive navigation. Users can browse posts and perform advanced operations like searching and sorting. However, to post an ad or news, user authentication is required.

#### Skeleton
The initial outline of the project's skeleton can be viewed in Wireframes. The structure is designed to offer intuitive navigation through a familiar layout:

    - The navbar provides quick access to all 
    primary features and varies according to user authentication status.
    - The main content is displayed in a list view, and each post links to its details.
    - Buttons and links are clearly labeled, and instructions are provided where necessary.

#### Surface

The visual design aims to create an atmosphere of informal, neighborly interaction. The layout is clean and straightforward, devoid of any elements that could potentially overwhelm the user. For more details on the visual planning, see [Visual Design Choices](#visual-design-choices).

### Visual Design Choices

### Colour Scheme:
Colour palette from [ASPOSE](https://products.aspose.app)

![Colour Palette](localtalks/localtalks/static/localtalks/images/color.jpg)
The colours chosen are quite neutral and calming. 

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility.

### Images and Icons

The design of the site includes images and icons made in the style of children's drawings. This style was chosen intentionally. The aim of using such images and icons is to create an atmosphere of trust and openness. We want every visitor to our site to feel comfortable and not have the sensation that they are being manipulated or used for commercial purposes. The style of children's drawings contributes to a subconscious feeling of immediacy and sincerity, making the interaction with the site more pleasant and trustworthy.

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

![navbar](localtalks/localtalks/static/localtalks/images/nav1.jpg)

![navbar](localtalks/localtalks/static/localtalks/images/nav2.jpg)

![burger menu](localtalks/localtalks/static/localtalks/images/nav3.jpg)

### Сategory Panel
- Panel with links to ads by category
- The category that the mouse hovers over is    
  highlighted in purple
- Collapsible burger menu with drop-down on small to medium screens

![Categories navbar](localtalks/localtalks/static/localtalks/images/categ-nav1.jpg)

![Categories navbar](localtalks/localtalks/static/localtalks/images/categ-nav2.jpg)

### Home Page

Add Listing Button: Different text is displayed for authenticated and unauthenticated users. Unregistered users are informed that they need to register in order to post an ad.
Only the latest 6 listings are displayed.
The ad title is an active link to the ad's individual page.
In the listing box, you can see the title, a mini-profile picture icon or a default image, information about the author, the publication date, and the category, as well as an image uploaded by the author or a default image. The ad is not limited in character count, but it is restricted in how much text is displayed in the listing field. To view the entire text, a scrolling feature is utilized.
Default images are included to maintain a consistent style.
Unlogged users cannot see the edit or delete ads buttons.
At the bottom of the main page, below the first 6 ads, there is a link to the page with all ads. It is designed in the  the same for all links way — purple in color and underlined when hovered over with the mouse.

![home page](localtalks/localtalks/static/localtalks/images/home1.jpg)

![home page](localtalks/localtalks/static/localtalks/images/home2.jpg)


### Footer

In the footer, you can find contact information: the site admin's email, which is also a link styled in the same way — purple and underlined when hovered over with the mouse.

![footer](localtalks/localtalks/static/localtalks/images/footer.jpg)

### All Ads Page

In addition to the main page, which displays only the first 6 listings, we have created a dedicated 'All Ads' page. It has a design similar to the main page, with a few subtle differences.The purpose of this page is to provide users with access to the entire range of listings without any limitations. This way, users can explore more options and find exactly what they are looking for. Just like on the main page, this page also features an 'Add Listing' button, styled identically for a consistent user experience. The page starts with the heading 'All Ads' and displays 6 listings at a time, similar to the main page. To navigate through multiple listings, pagination is available at the bottom of the page. The current page in the pagination is highlighted in the same color as the category panel, for a unified visual experience.
From a development perspective, having a dedicated 'All Ads' page offers several advantages. First, it helps in optimizing performance; the main page can load faster as it only needs to fetch and display a limited number of listings. This is especially beneficial for users with slower internet connections. Secondly, it provides a more modular approach to development. Features like sorting, filtering, and advanced search can be implemented on the 'All Ads' page without cluttering the main page, making the codebase easier to manage and extend. Lastly, it allows for more targeted analytics. By tracking user interactions on the 'All Ads' page separately, developers can gain insights into user behavior that can be used for future improvements. Overall, the 'All Ads' page not only enhances the user experience but also provides a more manageable and scalable solution for developers.

![All ads page](localtalks/localtalks/static/localtalks/images/all-ads.jpg)

### Profile Page

User's Listings Page (also known as Profile Page)
This page is accessible only to registered and authenticated users. If a user is not authenticated, they will be prompted to log in or register. Authenticated users see a greeting with their name on their page, their rounded profile image links to edit or delete their profile, a link to add a new listing, and all the listings they have published with options to edit or delete each listing. All links are styled in the same way — purple and underlined when hovered over with the mouse — consistent with the overall site design.

![Profile page](localtalks/localtalks/static/localtalks/images/profile.jpg)


## Security Features and Defensive Design
### User Authentication
(x)

### Form Validation
(x)

### Database Security
(x)

### Custom error pages
(x)

## Features

### User Account Pages
(x)

### Browse Ads
(x)

### Ad Detail Page
(x)

### Add Ad Form
(x)

### Update Ad Form
(x)

### Delete Ad
(x)

### My Posts
(x)

### My Bookmarks
(x)

### Error Pages
(x)

### Future Features
(x)

## Deployment - Heroku
(x)

## Forking this repository
(x)

## Cloning this repository
(x)

## Languages
(x)

## Frameworks - Libraries - Programs Used
(x)

## Credits
(x)

## Acknowledgments
(x)