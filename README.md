# BeautyPal


![BeautyPal] (static/readme_files-userview/.png) 



[View the live project here](https://lukyhet.github.io/Project_Four/)


## Introduction

Our full stack project  is called 'BeautyPal'. It was made to provide a specialized social network for those interested in beauty including sobjects like haircare, makeup, skincare, face yoga. The target audience is those who love beauty and want to want to share and learn about techniques, products, routines and more.

<details>

![Image of the BeautyPal](static/readme_files-userview/.png)

</details>

Movie Trivia was created for social purposes. It has groups created to discuss different topics related to beauty, like haircare, skincare, best products, etc.  The topic browse and activity feed are designed to facilitate the easy access to the information shared inside the groups. The users can create a username and password wich allows them to write messages, edit them, delete them and engage in interaction with other participants.

Beautypal was made as the fourth milestone project to achieve the Diploma in Software Development at the Code Institute. 

The purpose of this project is the Presentation of our first full stack project, and the main goal is to build an interactive site including both front-end and back-end that responds to the users actions, allowing them to actively engage with our website´s data from any electronic dispositive with internet access.


## UX
###  User Demographic
The user for this website is: 

- Young and adult people, the majority of them women, who are interested in beauty and the beauty indsutry. 
- Those who enjoy sharing experiences and knowledge online creating a sense of community through interaction with others with similar interests.
- Beauty lovers who are engaged with skincre, haircare, makeup and other related topics in a healthy and productive way as a contribution to their own well-being and the community's well-being.


#### User Goals

- To participate and share user’s knowledge about beauty related topics with an extended community of peers who have similar interests.
- Have a pleasent user experience when seeing an attractive website with contrasting colours as well as a clear design.
- Have a clear display of all the features available in the website in different electronic dispositives through the websites responsiveness.


## Features 

This is a one page website with a small and specialized social network that displays a name 'BeautyPal', a logo which is a free.png icon of a mirror made by (https://icons8.com/) downloaded from (https://icons8.com/icons/set/mirror). 

The website's home displays content divides in three columns bing the one in the center the widest one because it contains the feed, the columns to the left and right sides of the feed display the topic browse and the recent activity. On top of the site there's a navigation bar that has a search bar, a user's settings/login-logout dropdown menu and the logo and name of the website to the left.

Under the navigation bar there's important information about the content of the columns on the left and right sides of the site, like "Browse Topic" or "Recent Activity". The center displays a button that allows the user to create a new room to discuss a specific topic and shows the number of rooms already created and available.

All the buttons, the questions and table are easily identifiable by the contrast of the background, lines, and text.



#### Responsiveness

The site counts with responsive design. ![Am I responsive](assets/readme_files/responsiveness.png)



</details>    

To be able to materialize our idea for this project and get some needed direction as new developer I used several tutorials and discussed it my mentor from Code Institute Antonio Rodriguez. Even though my idea was to make a booking website at the beginning I found interesting resources and guidance online to built a little social network, which was one of the options for the fourth project to aspire to the Diploma in Software Development at the Code Institute and a more interesting challenge. At the end the decission was to build a basic social network website to discuss beauty, a topic that has a lot of followers and great market possibilities. I looked up to several examples online to be able to build this website, specially Traversy Media youtube channel django course wich includes guidance on how to build this kind of full stack site. 

The mentioned example of inspirational and educational site is [Traversy Media - Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI). 


### Design

#### Colour Scheme

Django allows to import themes, great features that were used in this project and adapted though, specially the color palette. The colors were chosen by the developer based on the hues of the 'mirror icon' used as the logo of "BeautyPal", the background is dark purple giving deepness and contrast to the other elements in the site. The rest of the colors in the palette are: A lighter shade of purple for the containers, blue for the accents and the search bar, and coral pink for the button and other accents, the text lighter shades of grey came from the theme. We must say that the colors hues and codes came from  palettes by palette ideas shared by  [canvas.com](https://www.canva.com/colors/color-palettes/everest-springs/). This combination creates harmonious colour scheme with good contrast, and femenine notes. 


#### Typography

The typography displayed in the website is given by the theme installed according to django's posibilities, the theme and all it's components are visible in (/static/styles/style.css). Somo of theme were adapted by the developer to match the UX, our inspiration and targeted population of the BeautyPal.



## Debugging

Several bugs were detected by developer tools. The bigest one happened when trying to alter the models and settings given by django to create the user and superuser, to try and fix the error we went to stack [StackOverflow](https://stackoverflow.com/questions/2450954/ but it could not be fixed, wich led to the duplication of the repository by cloning it causing other problems due to the need to reinstall django, environment and other tools. Code Institute's tutor, Christine Greaney-Kelley helped was fundamental to create a new workspace form the original repository and install some of the tools needed, without loosing our code.

Other types pf bugs detected were related to typos and indentation problems, the code was fixed by correcting it.


### Features to Implement in the future

- **Notifications**
     - Picture uploading would allow the users to personalize their profiles even more and would make it more "real" social network looking.
     - Notification service for interactions.
     

## Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wikipedia")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wikipedia")
- [JS](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wikipedia")
- [PY](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to PY Wikipedia")
- [DJANGO](https://en.wikipedia.org/wiki/Django_(web_framework) "Link to django Wikipedia"")



### Frameworks, Libraries & Programs Used


- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was as workspace for writing code,
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub is being used to store this repository.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to check the responsiveness of the design.
- [W3C](https://validator.w3.org/ "Markup Validation Service")
     - W3C Was used to validate the HTML code.
- [W3C](https://validator.w3.org/ "Markup Validation Service")
     - W3C Was used to validate the CSS code.
- [JShint](https://jshint.com/ "JShint")
     - JShint Was used to validate the JS code.
- [Icons8](https://icons8.com/ "Link to Icons8 homepage")
     - Icons8 was used to get icons for the Logo,
- [Canva.com](https://www.canva.com/ "Link to canva homepage")
     - Canva was used to get inspiration and codes for the colors in this website.
- [stackoverflow.com](https://stackoverflow.com/ "Link to stackoverflow homepage")
     - stackoverflow was used to research, find and fix bugs in this project.



## Testing


The W3C Markup Validator, W3C CSS Validator and JSHint Services were used to validate all the code of this repository and every warning was corrected until the code came up clean in every validator mentioned.

-W3C Markup Validator ![HTML](/assets/readme-files/htmlvalidated.png)

-W3C CSS Validator ![CSS](/assets/readme-files/cssValidated.png)

-JSHint javaSrcipt Validator ![JS](/assets/readme-files/JSValidated.png)


## Deployment

This project was deployed in GitHub [View the live project here](https://lukyhet.github.io/Project_Four/).

    
## Credits 

### Content and Code

- The most important inspiration and guidance came from the Python Django 7 Hour Course by 
Traversy Media available in YouTube in which the knowledgeable tutor goes through the basics of django while building a full stack social network for developers website. All the features mentioned in that course are not implemented in Beautypal.

- [Traversy Media course in YouTube](https://www.youtube.com/watch?v=PtQiiknWUcI     "Link to video course in Youtube").


Several other sources were consulted and their guides followed, for example:


- To fix bugs and find alternatives:

- [StackOverflow](https://stackoverflow.com/questions/65918550/how-to-solve-user-updating-problem-in-django "Link to StackOverflow").
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page").


- To remeber and refresh some python concepts and fix indentation problems:
- [Progamming with Mush/Youtube](https://www.youtube.com/watch?v=kqtD5dpn9C8 "Link to Youtube Python course").


### Media

- The icon used for the logo was downloaded for free from [Flaticon](https://icons8.com/ "Link to icons8.com") 
- The images used in this README.md file were taken by the developer as printscreens or pictures.


## Acknowledgements

- I want to thank and recognize the job of my mentor Antonio Rodriguez who has helped me understand and fix issues that came during the project's process.
- I also want to mention and thank Christine Greaney-Kelley, Scott Kipp and Oisin Tohak from student tutors at Code Institute for taking the time and explaining how to work through the errors found while building this website.


[Back to top](#BeautyPal!)

***










