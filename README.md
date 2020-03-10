# Project 4

project status: <strong>work in progress</strong>
- [ ] <strong>complete</strong>
- [x] <strong>work in progress</strong>

[![Build Status](https://travis-ci.org/Danhayes3008/project-4.svg?branch=master)](https://travis-ci.org/Danhayes3008/project-4)

Due to a major error i couldn't fix on my first attempt to build this project, i have been left with no choice but to start it again.
Luckily at least half the work done can be salvaged and it is my hope that on this second attempt i will not run into the same problems
that i had in the last one. As i transferred a-lot of the files over from my first attempt at the project i have decided to add a link to that
said repository called <a href="https://github.com/Danhayes3008/milestone4">milestone4</a> so that people can see how the project has improved since i started again.

### Table of Contents
to help navigate the readme i have added this list of links to the relevant sections.

 - [Site's Purpose](#Site's-Purpose)
 - [Wire-frames](#Wire-frames)
 - [future updates](#future-updates)
 - [Try it You're Self](#Try-it-You're-Self)
 - [Technologies](#Technologies)
 - [contributions](#contributions)

<strong><h2>Site's Purpose:</h2></strong>
-

This site is designed to be like a real charity's website. The idea was that it would give people information on what the charity is and what there goals are whilst also providing 
details on how to get in-touch with them or visit the office. I wanted every user to have the ability to view how much they have donated to the cause and also provide them with a certificate or a plague if they donated a-lot of money. I kept the site as basic as i could so that once it was finish i could add new features and improve on other stuff before submitting it for review but it looks like I may not have the time for that so i have done my best to give it a decent look and flow hoping the site will still be passable even with all the content I wanted to add not being included. 

<strong><h2>Deployed site:</h2></strong><a href="https://charity-project-4.herokuapp.com/" target="_blank"> Help The Homeless</a>
-

<strong><h2>Wire-frames:</h2></strong>
-

I have tried to keep the site as close to the wire-frames as I could, but the site has changed a-lot since they were made if there is time once the project is finished. This is the main priority for after the site is finished to make more wire-frames for the pages that dont have one.

<strong><h2>future updates:</h2></strong>
-

- improved layout
- total donated to the charity feature so that the public can see how much the charity has managed to raise
- top donations section so everyone can see who has contributed the most to the charity
- stories from people that have had there lives changed by the charity
- history of what the charity has done to help the homeless.
- better donation system
- fake adverts

<strong><h2>try it you're self:</h2></strong>
-

This project was made using vs code so i recommend if you wish to try out my site download the repository from my github page. To do so follow the instructions bellow:

- Head over to <a href="https://github.com/Danhayes3008/project-4">my github page</a> to download the folder
- Click on clone and download then click on download zip
- extract the file after downloading anywhere you want
- open the folder with vs code

I recommend creating a virtual environment at this point to better manage the project. To do so follow these instructions:

- python -m venv .env(the environment name)

After this all that is left is to create the env.py to hold the hidden key information, get a access key for stripe, set the project up on Heroku and create the aws bucket

<strong><h2>Technologies:</h2></strong>
-

<strong><h3>HTML:</h3></strong>
As with all other websites html, there much that can be done using the html tags from making simple paragraphs to writing scripts, styles and even php coding. All that is needed is a imaginative mind toy find a way to use these features to make the site both look and run smoothly.

<strong><h3>CSS/SCSS:</h3></strong>
the css is used to make the site have a more professional and interesting look to it but it don’t stop there. CSS files can be generated using SCSS coding which is more neater and structured than making a single css style file. With the SCSS you can have all the styles separated into multiple files so that when you need to go back and change something all you have to do is search that one file of lets say 20 lines of code instead of searching over 100 lines of code. This then can be integrated into a main file by simply importing the scss files into another scss file to generate the css file that will hold all the styling for the site. In my opinion this is the best method to control the styling and helps prevent long hours of searching for that one line that needs tweaking.

<strong><h3>JS:</h3></strong>
the use of Java Script is to give the site functionality. whilst this project has not used much Java Script it is used to display information in the charts i have used and to manage to stripe payments. The charts are simple ones that use the information in the file to fill a chart imported from the any-chart website, with the strip one no modifications must be done as it will prevent payments going through.

<strong><h3>Django:</h3></strong>
Django makes up the backbone of this project. with its well organized structure sites can be quickly built and deployed. It is one of many python extensions by
by far it is the best one in my current opinion for web site development. Django also works well with sqlite3 to create complex databases to meet any need either its a simple library or a complex shop database or a social media site.

<strong><h3>Stripe:</h3></strong>
Stripe is a payment managing system that acts like a middle man. It is easy to set up in your project and has a built in testing feature. The testing feature comes with test card details so that you don’t have to test your site using a real card. In the stripe website you can view all the information pushed through stripe through multiple charts and lists.

<strong><h3>AWS:</h3></strong>
we used aws buckets to store the static content and media files for this project.

<strong><h2>Testing:</h2></strong>
In this project i have done both manual testing of the site and some written testing. All written tests run though the Travis sight for simple testing every-time a file is published. 
A link to the test plus a indicator displaying if the build is passing or failing has also been placed at the top of this readme file. It is my hope to provide evidence that i have a basic understanding of testing however i wont be testing everything in the project with written tests.

[Back To The Top](#Project_4)

<strong><h2>contributions:</h2></strong>
-

- I managed to get some of the donation history section of the profile page working by following the code another student posted on the slack channels. If it wasn't for slack user  r_andy79 i wouldn't have gotten this working so soon. This method that i was using was only working in a limited capacity but after my coding was fixed with the help of Chris Zielinski i was able to get it working correctly.

- Anna_ci on slack channels helped me get my site working on Heroku. With her help i was able to get Heroku to work in the terminal on visual studio code were i am doing my project.

- After struggling for days trying to get my background image sorted i came across a video on YouTube that helped me get it working. The video i followed to get this to work was
<a href="https://www.youtube.com/watch?v=jW1IFBv35kE">Full Screen Background Html/Css</a> by youtuber-<a href="https://www.youtube.com/channel/UCnw4nJg3VWgXz6itvH8NkgQ">WClarkson</a>

- whilst searching for how to allow my users to change there passwords whilst logged into the site i came across multiple methods to do so. After trying a few these methods i found one that worked from <a href="https://simpleisbetterthancomplex.com/snippets/change-password-view/" target="_blank">simpleisbetterthancomplex.com</a>. This method was simple to implement and to understand.

- whilst searching online on how to allow a user to delete there account in django i cam across a reddit post from <a href="https://www.reddit.com/r/webdev/comments/cjfmg8/django_deleting_user_accounts/"> u/Science-Compliance </a> explaining how to do so. have have followed the instructions in the readme on how this is done and give full credit to that feature to the owner of the reddit post.

<strong><h3>project restructuring:</h3></strong>
-

Whilst trying to fix my donation history section of the profile page i was made to overhaul a-lot of the coding to make it all work. This was due to naming conflicts, after a few hours of working on it with a fellow student who helped me i was able to get the site working how i wanted it. The credit for this all goes to Chris Zielinski (ckz7880 on slack channels) from code institute slack chat-rooms as he walked me though fixing my site step by step after i made a right mess of it. Luckily not much was needed to be fixed but a rewrite of the carts context file, some models, the forms dealing with the donation and the views that was needed to fix all this. After fixing the problems with my code i was better able to understand how we were able to filter the donations made by the user logged in. I also received help from Faidon Minas Dermesonoglou from code institute slack chat-rooms. Faidon (Feddie_lead on slack channels) tried to explain the problem to me but because my code was a mess i was not able to correctly implement his advice on how to filter donations by user logged in.