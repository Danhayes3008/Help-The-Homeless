## Help The Homeless
---

project status: <strong>work in progress</strong>
- [x] <strong>complete</strong>
- [ ] <strong>work in progress</strong>

[![Build Status](https://travis-ci.org/Danhayes3008/project-4.svg?branch=master)](https://travis-ci.org/Danhayes3008/project-4)

Due to a major error i couldn't fix on my first attempt to build this project, i have been left with no choice but to start it again.
Luckily at least half the work done can be salvaged and it is my hope that on this second attempt i will not run into the same problems
that i had in the last one. As i transferred a-lot of the files over from my first attempt at the project i have decided to add a link to that
said repository called [milestone4](https://github.com/Danhayes3008/milestone4) so that people can see how the project has improved since i started again.

*Table of Contents*

to help navigate the README i have added this list of links to the relevant sections.

- [Site's Purpose](#Site's-Purpose)
- [Wire-frames](#Wire-frames)
- [future updates](#future-updates)
- [Try it You're Self](#Try-it-You're-Self)
- [Technologies](#Technologies)
- [contributions](#contributions)

## Site's Purpose:
---

This site is designed to be like a real charity's website. The idea was that it would give people information on what the charity is and what there goals are whilst also providing 
details on how to get in-touch with them or visit the office.I wanted every user to have the ability to view how much they have donated to the cause and also provide them with a certificate or a plague if they donated a-lot of money.I kept the site as basic as i could so that once it was finish i could add new features and improve on other stuff before submitting it for review but it looks like I may not have the time for that so i have done my best to give it a decent look and flow hoping the site will still be passable even with all the content I wanted to add not being included. 

## UX:
---

The site is designed so that people can see what the charity aims to do with the money donated and provides a simple method to donate to the charity. With using a cart system for doing the donating I have provided the users a chance to alter there donated amount before submitting the payment in-case they want to donate more or less than originally entered. The payment page has been set up so that the user has to enter there details every time so that no card details are stored on the site. This was done to prevent there card details from being collected if the database was hacked as the database would not hold this information.

The address part requires the users to enter there details every-time, This is because i have not got around to updating the profile model to include there address details so that they don't have to enter it every time. This update will be part of the better donation system that i wish to do if there was time ( or once the project has been assessed ). The reason for the address details is so that the charity can post certificates to the user or a plaque.

As an account is needed for them to donate i have made a profile page so that the users can see there donations made, and change there profile details as-well as delete there accounts too.

## Deployed site:

You can find the deployed site with the link below.

[Help The Homeless](https://charity-project-4.herokuapp.com/) 

## Wire-frames:
---

I have tried to keep the site as close to the wire-frames as I could, but the site has changed a-lot since they were made. If there is time once the project is finished I will made more for the pages that don't have a wireframe, but I don't think there will be time to do so. 

You can find the wire-frames [here](https://github.com/Danhayes3008/project-4/tree/master/wireframes). The main priority for after the site is finished to make more wire-frames for the pages that dont have one.

## future updates:
---

- improved layout
- total donated to the charity feature so that the public can see how much the charity has managed to raise 
- top donations section so everyone can see who has contributed the most to the charity
- ~~stories from people that have had there lives changed by the charity~~ (This has been added now)
- history of what the charity has done to help the homeless.
- better donation system
- fake adverts

[Back To The Top](#Help-The-Homeless)

## Bugs:
---

 - Profile images sometimes get squashed or stretched depending on the size of the image. This will be fixed at some point by trying to resize the images on upload
 but right now this is not something i know how to do.
 - Styling is focused for just Google chrome browser. When there is time i will fix this by trying to add styling for the other browsers.
 - Minor styling issues for all the screen sizes, This will be fixed by refining the scss and css coding.
 - The donation history currently keeps displaying all the donations for that user in one page, a pagination needs adding to fix this so that it only displays so many at one time
 - The admin styling needs more work. I have only recently learned this could be done and still working on it.

 [Back To The Top](#Help-The-Homeless) 

## try it you're self:
---

This project was made using vs code so i recommend if you wish to try out my site download the repository from my Git-Hub page. To do so follow the instructions bellow:

- Head over to [my github page](https://github.com/Danhayes3008/project-4) to download the folder
- Click on clone and download then click on download zip
- extract the file after downloading anywhere you want
- open the folder with vs code

I recommend creating a virtual environment at this point to better manage the project. To do so follow these instructions:

- python -m venv .env(the environment name)

After this all that is left is to create the env.py to hold the hidden key information, get a access key for stripe, set the project up on Heroku and create the aws bucket

[Back To The Top](#Help-The-Homeless)

## Technologies:
---

- HTML:
    - As with all other websites html, there much that can be done using the html tags from making simple paragraphs to writing scripts, styles and even php coding. All that is needed is a imaginative mind toy find a way to use these features to make the site both look and run smoothly.

- CSS/SCSS:
    - the css is used to make the site have a more professional and interesting look to it but it don’t stop there. CSS files can be generated using SCSS coding which is more neater and structured than making a single css style file. With the SCSS you can have all the styles separated into multiple files so that when you need to go back and change something all you have to do is search that one file of lets say 20 lines of code instead of searching over 100 lines of code. This then can be integrated into a main file by simply importing the scss files into another scss file to generate the css file that will hold all the styling for the site. In my opinion this is the best method to control the styling and helps prevent long hours of searching for that one line that needs tweaking.

- JavaScript:
    - the use of Java Script is to give the site functionality. whilst this project has not used much Java Script it is used to display information in the charts i have used and to manage to stripe payments. The charts are simple ones that use the information in the file to fill a chart imported from the any-chart website, with the strip one no modifications must be done as it will prevent payments going through.

- Django:
    - Django makes up the backbone of this project. with its well organized structure sites can be quickly built and deployed. It is one of many python extensions by
by far it is the best one in my current opinion for web site development. Django also works well with sqlite3 to create complex databases to meet any need either its a simple library or a complex shop database or a social media site.

- Stripe:
    - Stripe is a payment managing system that acts like a middle man. It is easy to set up in your project and has a built in testing feature. The testing feature comes with test card details so that you don’t have to test your site using a real card. In the stripe website you can view all the information pushed through stripe through multiple charts and lists.

- AWS:
    - we used aws buckets to store the static content and media files for this project.

## Testing:
---

In this project i have done both manual testing of the site and some written testing. All written tests run though the Travis sight for simple testing every-time a file is published. 
A link to the test plus a indicator displaying if the build is passing or failing has also been placed at the top of this README file. It is my hope to provide evidence that i have a basic understanding of testing however i wont be testing everything in the project with written tests.
Due to the time restraint and not having the time to write tests for all the site's features most of the testing was done manually whilst simple written tests were done to show I understand how to do them

[Back To The Top](#Help-The-Homeless)

## Credit:
---

all code, images, information sourced from other sites and people are used for learning purposes and are not being used for commercial use. If at any time the owner of any content wishes for me to remove stuff sourced from them I will do so.

## contributions:
---

- I managed to get some of the donation history section of the profile page working by following the code another student posted on the slack channels. If it wasn't for slack user  r_andy79 i wouldn't have gotten this working so soon. This method that i was using was only working in a limited capacity but after my coding was fixed with the help of Chris Zielinski i was able to get it working correctly.

- Anna_ci on slack channels helped me get my site working on Heroku. With her help i was able to get Heroku to work in the terminal on visual studio code were i am doing my project.

- After struggling for days trying to get my background image sorted i came across a video on YouTube that helped me get it working. The video i followed to get this to work was
[Full Screen Background Html/Css](https://www.youtube.com/watch?v=jW1IFBv35kE)</a> by YouTuber - [WClarkson](https://www.youtube.com/channel/UCnw4nJg3VWgXz6itvH8NkgQ)

- whilst searching for how to allow my users to change there passwords whilst logged into the site i came across multiple methods to do so. After trying a few these methods i found one that worked from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/snippets/change-password-view/). This method was simple to implement and to understand.

- whilst searching online on how to allow a user to delete there account in Django i cam across a Reddit post from [u/Science-Compliance](https://www.reddit.com/r/webdev/comments/cjfmg8/django_deleting_user_accounts/) </a> explaining how to do so. have have followed the instructions in the README on how this is done and give full credit to that feature to the owner of the Reddit post.

- During the manual testing of my site on my mobile i discovered that the update profile form sets the date backwards and the bootstrap form does not tell you of this. So i looked online and discovered at [learningaboutelectronics.com](http://www.learningaboutelectronics.com/Articles/How-to-add-a-placeholder-to-a-Django-form-field.php) that i could add placeholders to my forms using the code provided on that page.

[Back To The Top](#Help-The-Homeless)

## project restructuring:
---

Whilst trying to fix my donation history section of the profile page i was made to overhaul a-lot of the coding to make it all work. This was due to naming conflicts, after a few hours of working on it with a fellow student who helped me i was able to get the site working how i wanted it. The credit for this all goes to Chris Zielinski (ckz7880 on slack channels) from code institute slack chat-rooms as he walked me though fixing my site step by step after i made a right mess of it. Luckily not much was needed to be fixed but a rewrite of the carts context file, some models, the forms dealing with the donation and the views that was needed to fix all this. After fixing the problems with my code i was better able to understand how we were able to filter the donations made by the user logged in. I also received help from Faidon Minas Dermesonoglou from code institute slack chat-rooms. Faidon (Feddie_lead on slack channels) tried to explain the problem to me but because my code was a mess i was not able to correctly implement his advice on how to filter donations by user logged in.

[Back To The Top](#Help-The-Homeless)

## Media
---

For the images i used both Google images with the search settings set to display only images that are free to use to find images i can use in my site. I also used a site that allows you to download and use images without where the owners have given permission for others to use them and not to give credit or acknowledgments for there ownership of the images. The site used was [Pixabay](https://www.pixabay.com)
