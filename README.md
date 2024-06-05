![Amazon Q Developer header](images/q-vscode-header.png)

## Next Generation Developer Tools

*A hands on guide to working with Amazon Q Developer. Made by DevRel with 💖.*

In this hands on lab, we are going to run through how to use the next generation of developer tooling to help make our jobs as developers more enjoyable and productive.

We will create a new application from scratch, and then build upon this and perform many of the tasks you would typically do as a developer. 

One thing to bear in mind before we start. Unlike other workshops, because of the non deterministic nature of these tools, there is no guarantee that the output will be the same as what your peers will see. What that means is that if you are working in groups, you can all expect different outputs. We have provided a [sample repo](https://github.com/094459/ada-python-demo-app) that you can use as a baseline, but we encourage you to explore and work with your own experiments - this is the most effective way of learning how these tools work.
 
The workshop is split into a number of different labs, with some lectures as well. This is what we will cover

* Introduction to next generation developer tools
* Setting up, and getting starting with Amazon Q Developer
* Building our URL Shortener application
* Fixing and improving our application
* Adding new features
* Running Security scans
* Adding Tests
* Documenting our application

There is an additional lab that looks at how to deploy your completed application onto AWS.

---

**What you will need**

You will need VScode IDE (or as an alternative, IntelliJ) with the following VSCode plugins installed

* Amazon Q Developer plugin - https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode
* * [Download v1.3](https://github.com/aws/aws-toolkit-vscode/releases/download/amazonq/v1.3.0/amazon-q-vscode-1.3.0.vsix) - do not use (1.4) 
* Python plugin for VScode - https://marketplace.visualstudio.com/items?itemName=ms-python.python
* PostgreSQL cli tools - "brew install postgresql" (Mac) , use the windows installer to just install the cli tools (windows), or "sudo apt get install libpq-dev" (Ubuntu),"sudo dnf install libpq-devel" (Fedora)
* Python 3.10 or newer
* git

You will access to a Postgres database. At the end of this lab, there are instructions on how you can run a local Postgres database using Docker or Finch.

The final lab will require you to have an AWS account, as we will be deploying the application we develop into AWS. You can still complete the previous labs without an AWS account, so if you do not have access to one, then miss this lab out.

**Getting your environment ready**

Once you have read the pre-req's, it is time to start up VSCode.

We will be using files in the following GitHub repo, [ada-python-demo-app](https://github.com/094459/ada-python-demo-app). The repo has a number of different branches which have been used to checkpoint the code at different stages. This will make it easy for you to follow along. For those unfamiliar with git, we will use the following syntax

```
git checkout <branch name>
```

This will change the files open in your VSCode, so do not be alarmed if they change - it will most likely be the branch you are in. You can explore the branches via the GitHub gui, or via the cli by typing "git branch -a".

On your laptop, find a working directoy you want to use for this lab. From VScode, open up a new Terminal window, and from command prompt run the following to start our database.

Mac/Linux
```
cd <your working directory>
python -m venv .venv
source .venv/bin/activate
git clone https://github.com/094459/ada-python-demo-app.git
cd ada-python-demo-app
```
Windows
```
cd <your working directory>
git clone https://github.com/094459/ada-python-demo-app.git
cd ada-python-demo-app
```

Use the Python VScode plugin to create a new Virtual environment (venv) using a version of Python that is equal or greater than 3.10. This should create a .venv directory. You can then activate it from the terminal.

```
 .\.venv\Scripts\activate
```

VSCode Server

If you are using the VSCode server running on EC2, your home directory will be /workshop. We need to create our virtual Python environment this way:

```
python -m venv ~/.venv
source ~/.venv/bin/activate
git clone https://github.com/094459/ada-python-demo-app.git
cd ada-python-demo-app
```

If you are using VSCode running on EC2, I recommend using the inline browser that you can access from the link in the Ports tab. Whilst you can open a normal browser window, I found that it would often cache items. Feel free to experiment, and if you are seeing stale pages or updates not loading that you expect, try the inline browser and see if that changes. To access that, use the link as in the following screen shot.

![how to launch the inline browser in VSCode server running on EC2](images/vscode-browser.png)

> **Tip!** I have provided a CloudFormation tempalte that allows you to spin up VSCode running on EC2 in the [resources folder](resources/vscode-server.yaml)


**How do follow along**

Given the non deterministic nature of generative AI tools, the output you will get from running these prompts will be different to the output I got when creating this. You might be asking yourself, how will I know what is right or wrong, and how will I cope if things go horribly wrong? This is kind of intentional. Working with generative AI tools like Amazon Q Developer open you up to a new flow, a new way of working. If your expectation was that these tools will generate working code every time, then it is time to reset that expectation. The output that these tools provide will be your starting point, and get you 80% of the way there. You can then use Amazon Q Developer to help iterate and complete the remaining. If that does not work, at each different section of this lab, the git repo has a number of checkpoints. These have been implemented as branches, so you can start off without worrying if the previous lab failed.

Everyone running through this lab will have a different experience, but I hope the takeaway from this is a better understanding of the flow you will start to develop in using these tools to write software.

If you are working through this in a group setting, then the person running the lab will lead from the front and you can take your guidance from them.

#  Introduction to next generation developer tools (45 min)

To kick things off you will look at a quick overview of what we mean by generative AI developer tools. This will take a look at the typical use cases where developers can apply them, take a look at developer journeys in more detail, before finishing up with some tips as to how to use them effectively.

![First slide of lecture](images/ppt-cover.png)

This will set you up nicely for the practical hands on element, where we will actually do some of those use cases.

# Setting up, and getting starting with Amazon Q Developer (20 min)

We are now ready for the first hands on part of this lab, setting up the generative AI developer tooling we are going to be using. We are going to be using Amazon Q Developer, a next generation developer tool that provides you with in-line code suggestions and a chat interface to help your developer flow. This is installed into your IDE (VSCode and IntelliJ are supported) via a plugin. Once the plugin is installed, we need to login using something that is called a Builder ID account. This allows you to access the Free Tier of Amazon Q Developer, without the need for an AWS account. So we first need to set that up, and then install the Amazon Q Developer plugin.

**Creating your Builder ID**

Creating a Builder ID is the first step in being able to use the Amazon Q Developer plugin. All you need is a valid email address to create a Builder ID. Head over to the [Builder ID page](https://profile.aws.amazon.com/) and then complete the creation by registering a valid email address. You can follow these screenshows to see the flow. After accessing the Builder ID page, you will need to provide an email address (1) and then create an alias (Your Name) (2). You will be sent an email verification which you will need to enter (3), and the email should only take a few moments to arrive (but check your SPAM folder just in case)(4)

![creation of a builder id flow](images/q-vscode-builderid-1.png)

Once you have received that code, enter it to validate your account (5), which should provide confirmation (6). You will be returned back to the initial screen, where you can now enter your email address (7) and password (8) and you should then see the Builder Profile page (9), where you can view your profile.

![completion of the builder id](images/q-vscode-builderid-2.png)

When you hear the term Builder ID when working with AWS services, this is the account they are referring to. It is separate from the AWS account, but is used by a number of services to provide access to those who want to try and AWS without the need for a full AWS account.


> **Logging out of your Builder ID** Sometimes you might need to log out of your Builder ID, and in order to do this you should head over to your [Builder ID Profile page](https://profile.aws.amazon.com/#/profile/details) and use the **Sign Out** button on the top left. Clicking on this will return you to the sign on page.


**Installing Amazon Q Developer**

Now that we have our Builder ID profile, lets install the Amazon Q Developer plugin. From the Extensions side bar, click on the icon to view the extensions marketplace. Typically we would search for "Amazon Q Developer" and we would find and the use the Install link to install the plugin.(1) As of writing, v1.4 has a small issue which means we are going to install it a different way. [Download the v1.3](https://github.com/aws/aws-toolkit-vscode/releases/download/amazonq/v1.3.0/amazon-q-vscode-1.3.0.vsix) locally on your machine. From the Extension menu (2), click on the .. to open up the menu, and then select "Install from VSIX". This will bring up a file browser, and you will now select the file you downloaded (v1.3 of the plugin)

![Installing the Amazon Q Developer plugin](images/q-vscode-install-1.png)

If the installation has been completed successfully, we will see a couple of things. First we will see a new Q icon on the left hand side bar (1), and you should also the the Amazon Q status bar at the bottom, with a X (2)

![Successfull installation of Amazon Q Developer](images/q-vscode-install-2.png)

If you click on that, you should see a menu pop up that shows that you are currently not signed in. We will do that next.

**Signing into Amazon Q Developer**

Now that we have our Builder ID created, and installed the Amazon Q Developer plugin, we can take the last step which is to login using that Builder ID. From the previous screenshot, if we click on the Q icon it will bring up the Amazon Q menu (3). When we click on that, we will see the login options for Amazon Q Developer (4) - there are two, we will ignore the "Use wit Pro Licence" and click on the "Use for Free" box and then click on Continue. This will bring up a pop up box (5). Take a note of the reference code, and then click on Proceed to Browser, which will bring up (6). Review that the code is the same as for the previous step, and then click on "Confirm and Continue", which will then bring up (7) to let you review the permissions that the Amazon Q Developer will need to work. If you are happy, click on "Allow Access" and if successfull, you will see the final screen (8) which you can close.

> **Note!** You might notice in the bottom left corner of VSCode the information panel that says that the Amazon Q plugin has opened up your web page. This will close automatically once the login has completed

![Signing into Amazon Q Developer using your Builder ID](images/q-vscode-signin-1.png)

Once you have logged in you will notice a few things. First the Q panel on the left hand side will be replaced with a chat window. You will also notice that at the bottom, the Amazon Q status bar will have changed form "X Amazon Q" to "|> Amazon Q". When you click on that, you will also see that you are now logged into Amazon Q using your AWS Builder ID.

![Sign in complete](images/q-vscode-signin-2.png)

We have now set up everything and are ready to go.

> **Logging out** If you want to log out, all you need to do is click on the Amazon Q status bar link to bring up the menu, and then select the Sign Out option. You can then repeat the process above to sign back in as you need

**Amazon Q Developer Settings**

Before we dive into the labs, it is worth going through how you can configure Amazon Q Developer and tailor it to your requirements. From the Extensions icon on the left icon bar, we can click on the cog wheel next to the Amazon Q Developer plugin, which will bring up the settings you can configure. This is handy to know incase you want to make changes later on. For the time being, we can leave this as is.

![Amazon Q Developer Settings](images/q-vscode-settings-1.png)

**Exploring Amazon Q Developer**

Like all developer tools, it is worth spending some time to explore and see how they work to really maximise the benefit to your productivity. In this section we will cover at a high level what Amazon Q Developer provides you with, but I would encourage you to explore.

*Amazon Q Developer menu options*

When we click on the Amazon Q status bar link at the bottom of VSCode, we will see the following pop up. This provides you will access to Amazon Q Developer options, most of which you will not need whilst you are using it, but you will come back to do certain things. Let's go through what each of these options provides.

![amazon q developer menu options](images/amazon-q-developer-plugin-menu.png)

* Pause Auto-Suggestions (Currently Running) - Amazon Q Developer provides you with suggested code blocks and snippets whilst working directly in your code. You can turn off this behaviour by clicking on this link (you will notice that it will then change to Resume Auto-Suggestions, Currently Paused, and the Amazon Q icon in the bottom status bar will also change). Every developer is different, and some prefer to have this option disabled, others enabled, so you will need to see what feels best for you. When paused, you can still invoke Amazon Q Developer to provide in-line code suggestions, by using the VSCode shortcuts (OPTION + C). Speaking of keyboard short cuts, lets check those out
* Open Code Reference Log - the underlying models that are used to power Amazon Q Developer use some open source code repositories, using Apache 2.0 and MIT licenced source files. Should code suggestions include portions from those projects, Amazon Q Developer will let you know by outputting this to the "Code Reference Log" which you can open by clicking on this menu option. When you click on this, you may see "Don't want suggestions that include code with references? Uncheck this option in Amazon Q: Settings". When using Builder ID you are not able to change this configuration, and the default option is to always include suggestions with code references. As you use Amazon Q Developer, check in here from time to time to see whether you are using code from those open source repositoires.
* Try inline suggestions Examples - this provides a quick tutorial to walk you through the basics of how to use Amazon Q Developer inline suggestions
* Run Project Scan - this kicks off a security scan of the code in the current project, using Amazon Q Developer and other AWS services to help you identify security issues before you ship the code. We will be exploring this later in the labs
* Open Chat Panel - this will open up the Amazon Q Developer chat panel if you close it
* Send Feedback / Connect with us on GitHub / View Documentation - these options provide you with additional ways you can provide feedback if Amazon Q Developer is not working the way you think it should
* Open Settings - will open the Amazon Q Developer plugin settings options (as covered above)
* Sign Out (Connected as AWS Builder ID) - allows you to log out of your current session, with the identity displayed. During this lab, it will always be AWS Builder ID. 

*Keyboard shortcuts*

You can control how you invoke Amazon Q Developer via the various key shortcuts, including customising these to how you work.

![keyboard shortcuts for Amazon Q Developer](images/amazon-q-vscode-shortcuts.png)

One of the key short cuts to know when you are working in the inline editor, is the < and > arrows. These allow you to cycle through suggestions when you are prompted by Amazon Q Developer.

*Chat Interface*

You can open the Chat Panel by clicking on the Amazon Q status bar link at the bottom, which by default, will make it appear on the left hand side with the other application artifacts (like files open, git files, etc). You can drag the Chat Panel to the right hand side, as in the screenshot below, which I find helpful as it allows me to see my files in the project, the files I am editing, and then also provide me with my chat interface.

![Amazon Q Developer Chat interface](images/q-vscode-screen-layout.png)

You can click on the + to open several chat sessions. When using Amazon Q Developer, the plugin will remember the conversations and use that in subsequent responses. This is very helpful when using Amazon Q to work through and troubleshoot issues. We will see this throughout this lab. You can open up to ten of these different tabs or conversations.

Amazon Q Developer also has some power features which are invoked using the /

* /dev invokes the Amazon Q Developer Agent for software development, and with this, it can create files, add new features, add tests, create documentation, and more. It first of all generates a plan, asks you to review, and then it will generate the code for you. With the Builder ID you are limited to how many times you can use this, so we will not be using this during the main lab, but we will come back and explore this if there is time at the end.
* /transform invokes the Amazon Q Developer Agent for transformation that helps you migrate Java 8 projects to Java 17, taking the effort out of modernising your applications. We will not be using that during this lab, but it is worth knowing about if you are working with old Java applications.

**Note!** When using /dev and /transform with Builder IDs, you have limited quota. You can find out more on the official [Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing/), if you scroll half way down you will see a table which outlines the limits you have open to you.


*Menu bar integration*

When you are working on our code within the editor, Amazon Q Developer provides a handy way to quickly invoke it to perform a number of functions. When working on a file, you can select a portion of code, or even if you want the whole thing, and then when you RIGHT CLICK, you will see an "Send to Amazon Q" menu option, which when you select you will see a number of options:

![Amazon Q Developer editor menus](images/q-vscode-editor-menu.png)

* Explain - this will send whatever you have highlighted to the Amazon Q Chat panel, and ask Amazon Q to help explain what this code does
* Refactor - this will review the snippet and suggest ways you can improve code readability or efficiency, among other improvements
* Fix - this is handy if you are seeing linting errors in your code, or are trying to resolve other issues with your code
* Optimise - this will look to see if it can optimise the performance of the code you have selected
* Send to Prompt - this will copy the portion you have selected and then move it to the Amazon Q Developer Chat Panel. You can then provide your own prompt to ask Amazon Q Developer what you want it to do. This is an easier way than copy/pasting the code snippet yourself.

*Context*

During the lecture you will have heard about large language model context sizes. In effect, this is the amount of information that can be provided to tools like Amazon Q Developer, for them to then reason and make suggestions. When working with Amazon Q Developer, there are two modalities you need to be aware about.

* When using the Amazon Q Developer inline code - when you are in the editor, latency and performance are critical, and so this affects the context size that Amazon Q Developer is able to use. It will take the prompt provided, as well as additional information within the file its working on 
* When using the Amazon Q Developer chat interface - when you use the Amazon Q Developer chat, you will notice there is a small number just below the submit icon (4000/4000). This is the size of the context window. From a latency perspective, there is less need to be very responsive, and so this allows Amazon Q Developer to provide a bigger context size.
* Amazon Q Developer chat inteface tabs - you can open up several chat interface tabs by clicking on the + next to the Chat. Each of these will be new conversations with new context. You can open up to ten of these chat conversations.

Amazon Q Developer also uses things such as open tabs in VSCode, as well as key files depending on programming language (for example, the pom.xml in Java) to add additional information to help it make better suggestions.

If you want to get low level and see this working, you can check the logging of the Amazon Q Developer plugin and see this in action.


*Amazon Q Developer logs*

You can access the various Amazon Q Developer plugin logs from the OUTPUT menu option that appears when you have the terminal section in VSCode. When you select the pull down menu, you will see Amazon Q and Amazon Q Logs. The latter provides detailed information about how the plugin is working and interacting with the backend generative AI services powered by Amazon Bedrock.

*Additional learning resources*

I have just covered the basics here, but we are always plublishing new content that shows how other developers are doing cool things with Amazon Q Developer. If you want to know more, head over to [community.aws](https://community.aws/amazon-q)

**Understanding how to ask Amazon Q Developer questions**

As you explore the world of generative AI developer tools, one thing you will need to think about is that in order to get useful output and results, you need to ensure that you provide tools like Amazon Q Developer, the right input. What do I mean?

The "Prompt" or "Chat Interface" is how tools like Amazon Q Developer know what they need to do, in the same way that when you are using a search engine, you enter terms you want to search for. It is tempting to treat these chat interfacts like search, but that will lead to poor results. Here are some things to think about that will improve the output from tools like Amazon Q Developer.

* Provide as much information as possible - rather than say "Add a README" as a prompt, a better one would be "Create a README.md file for this project that will explain what this project does, what the key files are, and how to run it."
* If the output is not what you expect, you can use follow up prompts to help steer and improve the output. Using terms like "Can you provide a more detailed response" or "Can you give a code example" are good ways you can maintain the context and memory of what has been asked before, and refine the output
* If the ouput is good, use the thumbs up and down to provide feedback - this will ensure that the responses improve over time
* If the output is bad, use the thumbs down and use the additional link to provide feedback - this will help ensure that you do not get the same poor results back
* Rephrase the question - sometimes, the  output you get will not be great. This is part of the nature of how these tools work. Sometimes, it is better to reword or re-think your prompt and try again
* Remember these tools are non deterministic - it is easy to forget that every time you run the same prompt, you are likely to get different results and output. That is the nature of these tools - it is a feature not a bug
* Debug errors by copying important parts of error messages - one of the powerful ways these tools can help you improve your productivity is by reducing context switching and allowing you to stay within your code editor whilst troubleshooting and fixing errors. Just grab the most peritent part of the error, and then send it to the Amazon Q Developer Chat panel and ask questions like "How do I resolve this error", or "What does this mean". 



Ok, you are now up to speed with the Amazon Q Developer plugin, and it is time to see what you can achieve with it.

## Building and Exploring a new application (25 min)

In this lab we are going to use a very simple use case - we want to create a application in Python that will allow us to save and the use urls. We have chosen Python as it makes it easy to follow along and understand how these next generation developer tools work. So our URL shortner application will initially have some basic functionality, an MLP - Minimum Lovable Product.The github repo shared at the beginning of this document provides the all the code we will need. We will be using Amazon Q Developer to help us add more code and improve the basic functionality.

We are going to start with the basic application that has been generated using Amazon Q Developer (see the note next to see how this was created). For the purpose of time we are not going to re-create this, but you can have a go once the labs have been completed, to see how you get on.

> **Using Amazon Q Developer /dev**
> I created a sample project using Amazon Q Developer, with the /dev Agent for software development. I used the following prompt:
>
>"Create a simple Flask application that provides URL shortening functionality. Create a number of different routes to /add a new url to be shortened, and /view to view an existing url that has been shortened."
>
> This is the basis for the sample code project. It takes around 10-15 mins to complete this, so for the purpose of the lab I have skipped this. Feel free to experiment and see what you can create using this.


**Lab 01-1 Getting our application up and running**

From VSCode, we should still have our Postgres database running in the Terminal window within VSCode. Click on the + to open up another Terminal. The first thing we need to do is make sure that we are running in the Python virtual environment we created

Mac
```
cd <your working directory>
source .venv/bin/activate
cd ada-python-demo-app
```
Windows
```
cd <your working directory>
.\venv\Scripts\activate
cd ada-python-demo-app
```

VSCode Server

If you are using the VSCode server running on EC2, your home directory will be /workshop. We need to create our virtual Python environment this way:

```
python -m venv ~/.venv
source ~/.venv/bin/activate
cd ada-python-demo-app
```



If you check out your files and directories, you should see the following:

```
/
├── ada-python-demo-app
    ├── app.py
    ├── finch
    └── postgres.yml
    └── templates
        ├── add.html
        └── view.html
```


Now that we have our Python environment setup, we can ask Amazon Q how to run this application. From the Amazon Q Chat Panel, type in the following

```
How do I run this application?
```


Read the output, and then use the output to help you run the application. What happens when you run this application? You should get an error when you try and run the application. Use Amazon Q Developer Chat to see how it can help you solve that error.


Follow the output and resolve the problem. Try restarting the application and see if it works this time. If you have no errors, then you should see something like this:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

The application is now up and running, but how do we know what it does? We can use Amazon Q Developer to help us. We can ask it something like:

```
How do i use this application from the browser?
```

Review the output and also experiment and try a few other prompts that you might use. Are they helpful? What works and what does not work?

You should now be able to use the information from Amazon Q and interact with this application via a browser to complete to tasks - one to create a new url shortcut, and then two, to review a url shortcut.

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to resolve the issue and you can now run the application, you can proceed to the next lab.

---

**Lab 01-2 Fixing the app**

In this next lab we are going to use Amazon Q Developer to show how easy it is to fix bugs whilst you are working and in the flow. We need to first switch to a branch of the code that we have deliberately broken. From the VScode terminal run the following command

```
git checkout broken
```

Try running the application again. Does it run? Ok, now try using the application to add a new URL. You should now encounter an error which you will see both on the browser, but also in the terminal window where you ran the application.

Use Amazon Q Developer chat to help you fix this error. Copy the error to the Amazon Q Developer Chat panel, and ask it "How do I fix this error -> " and then paste the error message.

Review the output. You should be able to see that the information provided will help you resolve the problem. Fix the code, save it and then re-run the application. Try adding a new URL, and this time it should work perfectly.

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to resolve the issue and you can now run the application, you can proceed to the next lab.

---

**Lab 01-3 In code suggestions**

In this next lab, we are going to use Amazon Q Developer to help us speed up how to write our code within the editor itself. We will not be using the Amazon Q Developer chat panel, we will be activating the suggestions using Python's comment symbol # (if you are trying this for other languages, you will use the commenting symbols that language uses)

Place your cursor a line 8 in the app.py and hit return a couple of times.

```
from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

url_mapping = {}
<-- here
```

From the beginning of the line, type the following:

```
# Create a function that returns a random quote that features Yoda
```

When you hit return, you should see "Amazon Q is generatring...." and after a few seconds, it should suggest some code. 

![Amazon Q Developer suggestion](images/yoda-q-choice-1.png)

You will notice this is greyed out. We can use the Amazon Q Developer keyboard shortcuts of < and > to switch been different suggestions. Hit the > and you will see a different code.

![Amazon Q Developer alternative code suggestion](images/yoda-q-choice-2.png)

I like this one better. To accept the code we hit TAB.

You will notice that this code is not actually complete. It leaves this open for me to add any other quotes that I might to return. In this instance I am happy with the selection, so I just hit backspace to remove the comma, and then close the array by typing the ]

![Closing the function](images/yoda-close-braket.png)

When I hit return, you will notice that Amazon Q Developer is not done suggesting stuff. You will notice more greyed out code that it wants you to add. In this case, we need to this to complete our function, so we hit TAB again. Once that code has been accepted, we hit return.

Amazon Q Developer still isn't done. It would like me to add a new route to this application (/) so that it can display a quote. We can hit TAB to accept that, we now have a new route.

![New route added](images/yoda-add-route.png)

> **When to stop!!** Sometimes when using tools like Amazon Q Developer, the suggestions might keep on going. You are in control, so you need to be intentional as to when you want to stop the suggestions happening. In this instance, now that we have our function, we can just hit return rather than TAB and that will stop further suggestions from coming.

As it stands, if we run this code it will not work as there is no index.html within this application. We need to create this. From the templates folder, add a new file called "index.html".

At this point it is worth noting that the inline suggestions do not work for html, so we cannot ask Amazon Q Developer like we just did to add the code. We can however, ask the Amazon Q Developer Chat panel. So lets do that.

```
Provide the html code for the index.html page that will display the yoda_quote
```

You can see the output it generates here. 

![Asking Amazon Q Developer for the index.html code](images/yoda-html.png)

I add this code to the index.html, and save the file. When I now run this application, you will see the following when you open a browser window.

![Adding inspirational messages](images/yoda-motd.png)


> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the persist branch. Access this by using the following command:
> 
> ```
> git checkout inline
> ```
> You will notice that files update in your local repo.
>

*Checking Amazon Q Developer logs*

Before we complete this lab, from the VSCode tab OUTPUT select AMAZON Q LOGS from the pulldown. Take a few minutes to explore the output. You can see in more details how Amazon Q Developer is interacting with the backend model that is being served by Amazon Bedrock.

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to created a new function and can now run the application, you can proceed to the next lab.

---

**Lab 01-4 Security Scan**

When we were exploring some of the capabilities that Amazon Q Developer provides, performing Security Scans was one of these. Using the Amazon Q menu options, kick off a Security Scan.

Whilst that is running, from the OUTPUT tab, look at the Amazon Q Logs and Amazon Q Security Scan Log. This is where the output from running these scans is generated.

Once the scan is complete, you should see one finding. Check out the PROBLEMS tab and you will find errors here. If you click on the file, it will take you to the problem area in the file. VSCode highlights this with a lightbulb icon.

If you hover over this, it should bring up a panel. This can be a bit fiddly as it disappears when you least expect it! From the panel that comes up, it provides more details about this security issue. You should see a link on that panel called "Explain". We can use the Explain which will then send this information over to the Amazon Q Developer Chat panel.

Review the output and then apply the suggest fix.

Re-run the Security Scan. If everything has worked ok, you should now have no security findings.

**Complete:** When you have managed to resolve the security issue, you can proceed to the next lab.

---

## Improving our Application (90 min) 

In this next section, we will start working to improve our application by adding new features, adding tests, and then creating documentation so that other developers and users know how to use this application.

**Lab 02-1 Persisting URLs to a file**

The current application does not persist the shortcuts generated, so lets fix that and get Amazon Q Developer to help us. If you have not already done so, close all tabs and open up the app.py. Select all the code, and then RIGHT CLICK and use the "Send to Amazon Q" meny option. Select the "Send to Prompt" option, which will add it to the Amazon Q Chat Panel. From there (the Chat Panel), add the following prompt. 

```
Add a mechanism to persist added url's to a local file
```

Review the output and start incorporating the code changes. If you run into errors, then use Amazon Q to help you fix those errors. Once you have completed the code updates, run the application and try and add a view URLs. 

Does the application still work? What has happened to those URLs that you created? Check to see if the code is the same or different to the person next to you. Add a new URL and remember the shotcut code. The the code to make sure it works,

Stop the application (CTRL + C) and then restart it. Try the shortcut code again. It should work, as we have now perisisted this to a local file. Once you have tested this, shut down the application again using CTRL + C


> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the persist branch. Access this by using the following command:
> 
> ```
> git checkout persist
> ```
> You will notice that files update in your local repo.
> 

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When the app is successfully persisting shortend urls to a file, and you can stop/start the application and those short urls still work, you can proceed to the next lab.

---


**Lab 02-2 Display current short cuts**

The application does not currently provide a way to list all shortcuts, so lets fix that. Lets see how we can use Amazon Q Developer to help us create the necessary changes.

This time we are just going to use the Amazon Q Developer Chat panel to ask for help. From the chat, lets type in the following:

```
Create code that adds a new route to this Flask application that displays all the current short cuts
```

Review the findings and implement the suggestions. If there are any errors, use Amazon Q Developer to help you fix those. Once you have completed that, run the application and test the new functionality. It should display the shortend URLs you have already saved in the previous labs.

> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the summary branch. Access this by using the following command:
> 
> ```
> git checkout summary
> ```
> You will notice that files update in your local repo.
> 

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When the app now has a page that displays all the shortcuts, you can proceed to the next lab.

---

**Lab 02-3 Optimise the code**

The code you currently have might not be optimised. We can use Amazon Q Developer to help us optimise our code, and so we are going to now use it to improve our code by checking to make sure that we only provide valid URL's as well as not allowing us to submit duplicate URLs.

```
Update the code so that it checks for valid url's before saving

```

Again review the suggestions and implement the code. Now start the application and check to see if you can add URLs. Try and add incorrect ones to see what happens.

Once you have got that working, we will now try another optimisation. This time we will update the code so that it checks for duplicates before saving the URL. We enter the following in the Amazon Q Developer Chat panel:

```
Update the code so that it checks for duplicate url's before saving
```

Again, review the code, implement it and then try adding duplicate URLs. What happens? It should not allow you to now save duplicate or incorrect URLs.

The final update is to make sure that when we submit one of the shortcut codes, the application successfull redirects rather than just displaying a url. We will use the Amazon Q Developer Chat panel again, submitting the following:

```
Update the code so that the short_id route automatically redirects to the saved URL
```

Again, review the code, implement it and then try accessing the url using one of the shortcut codes. What happens? It should now automatically redirect you to that application.

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to add these improvements on how the application works, you can proceed to the next lab.

---

**Lab 02-4 Storing our data in a database**

Up until now we have been using a local file to store our short cuts. This is great for our local solution, but as we scale, we need to store this on something that can be accessed by many machines. A database is a good choice for this, so let us update our code to store all our shortcuts on a Postgres database.

We have a local Postgres database up and running - if you have not done that yet, use the instructions provided to spin up a local Postgres database using Docker or Finch. This will create a local Postgre database with a user (postgres) and password (change-me).

*Creating a database*

The first thing we will do is create a database we can use, we will call it urldb. Lets see how Amazon Q Developer can guide us.

```
I have a local Postgres database running in a docker container. I want to create a new database called urldb. Provide a step by step guide on how to do this.
```

Review the output. It will most likely ask you to use a tool called "psql" but we do not have this installed on our environment. You know what I am going to say right? Lets ask Amazon Q Developer to help us simplify how to install this.

```
How do I install psql for my local database running Postgres 15.6. I am using Ubuntu.
```

You should see a difference in the level of detail and relevance to our setup. 

> **Hint!** This is what Amazon Q Developer suggested for me which worked great
> 
> ```
> sudo apt install wget ca-certificates
> wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
> sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
> sudo apt update
> sudo apt install postgresql-client-15
> ```



We should complete the steps outlined to install psql. Check to make sure you have it working by running the following:

```
psql --version
```

And you should get something like

```
psql (PostgreSQL) 15.7 (Ubuntu 15.7-1.pgdg22.04+1)
```

Now complete the previous steps that Amazon Q Developer (scroll up to the previous output in the Chat interface) to create your database.

> **Hint!** When I ran this, this was the command I ran to create this new database
>
> ```
> psql -U postgres -h 127.0.0.1
> ```
> Enter password
>
> postgres =#
> postgres=# CREATE DATABASE urldb;
> CREATE DATABASE
> \l
>  urldb     | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
> \q
> ```

We now have our new database.

*Updating our application*

Using Amazon Q Developer Chat, we ask it

```
Can you update the app so that when a new url is added, it stores it in a postgres database called urldb. when creating the table we want to create columns for the url, the shortcut and a time stamp when this was created
```

Review the code as before and update and make changes. You will need to do some additional things depending on the code suggestions made.

* You will need to review the way that your code connects to the Postgres database - this might be via environment variables, or directly in the code
* You will need to install some additional Python libraries - when running the application with updated code, use Amazon Q Developer to help you troubleshoot these errors, for example:

> How do I fix ModuleNotFoundError: No module named 'psycopg2'
> When I try and install I get this error - Error: pg_config executable not found.

* There is a hand VSCode plugin that allows you to connect to Postgres databases and easily view/modify the data - https://marketplace.visualstudio.com/items?itemName=cweijan.dbclient-jdbc


One of the really helpful ways that developers are using tools like Amazon Q Developer is when working with SQL. Whilst the SQL code in our application is very simple, you can imagine how useful getting help on more complex queries will be. In our code, lets update the code so that we list all short cuts by date order. We can use a prompt like this:

```
Update the sql query to order results by date
```

Again review the code and implement and test it.

> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the summary db. Access this by using the following command:
> 
> ```
> git checkout db
> ```
> You will notice that files update in your local repo.
> 

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to configure this application to persist short cuts to the database, you can proceed to the next lab.

---

**Lab 02-4 Adding Tests**

Now that we have our application where we want it, we can now use Amazon Q Developer to help us write some unit tests. If you are new or not so familiar with writing tests, we can use tools like Amazon Q Developer to provide a higher level overview and additional information. For example

```
What are the most popular Python testing frameworks that might be suitable for this project
```

For this project we are going to use Pytest, so lets use Amazon Q Developer to help us write those. Select all the code in the project and then use the "Send to Amazon Q" menu option, selecting "Send to Prompt". From the Chat Panel add the followin:

```
Create tests using pytest that let me validate adding shortcuts, using short cuts, and displaying all shortcuts
```

Review the output, and compare this with the folk near you. Implement the code and then follow the instructions to run the tests. You will probably get some initial errors around addition Python libraries that need to be installed via pip.

Use the Amazon Q Developer Chat panel to help you fix issues with failing tests. You may notice a few issues such as missing imports or perhaps a test assertion that needs to be updated.


> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the tests branch. Access this by using the following command:
> 
> ```
> git checkout tests
> ```
> You will notice that files update in your local repo.
> 

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have managed to write working tests, you can proceed to the next lab.

---

**Lab 02-5 Adding Documentation**

One of the most effective applications of tools like Amazon Q Developer has been to help automate the task of documenting our projects. Now that we have a complete project, we want to make sure we do not skip the most important part - documenting how it works for the next developer who comes along and wants to use this.

Lets ask via the Chat panel the following

```
Create a README that shows how this app works and how to test and run it
```

Review the output. What do you think, is it detailed enough? You can explore and experiment with this. If the documentation does not have enough detail, then ask a follow up prompt to provide more details.

We can also document the code itself, providing docstrings to document each function within our application. Lets use the Chat panel:

```
Create docstrings that explain how each function in this application works
```
Review the output and make changes. We now have a working application that has documentation and tests. Not bad for such a short time.

> **If you cannot get this to work**
> If you struggle to get the code to work, you can use the code in the repo in the docs branch. Access this by using the following command:
> 
> ```
> git checkout docs
> ```
> You will notice that files update in your local repo.
> 

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have created documentation for this project, you can proceed to the next lab.

---

**Lab 02-6 Open Sourcing our project**

The final lab will show how we can use tools like Amazon Q Developer to simplify tasks such as open sourcing our project. Using the Amazon Q Developer Chat panel, we can ask it the following prompts:

```
> I want to open source this project, what do i need to do
> can you provide me with a sample MIT licence file
> can you update it for my company, beachgeek.co.uk
> how do i add an SPDX header to this project?
```

Review the output for each of these prompts and then make changes. As these files and updates will not make any impact to the functionality, there is no need to test the application.

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** Congratulations, you have completed this hands on lab. If you have time, there are some additional ideas for activities for you to do. Otherwise, go and congratulate yourself with a well earned beverage of your choice!

---

**Additional Things to do**

If you want to experiment more, then here are some additional activities you can try. Use Amazon Q Developer to guide you to doing these, using all the skills you have picked up so far.

1. Add or change a home page, that displays a message and then provides links add and display shortcuts

> **Hint!** You can try using Amazon Q Developer inline to do this

2. Select the code and look for optimistion opportunities within the code.

> **Hint!** There are a number of ways you can optimise the code, so first use Amazon Q Developer Optimise, and take it from there

3. Try and recreate this application in a different programming language

> **Hint!** Choose a programming language you are familiar with and where you have everything already available on your developer machine. Reproducing this in Node or Java works well, but you should be able to use other programming languages too

4. Explore how you can use Amazon Q Developer to help you understand how to deploy this application on AWS

> **Hint!** Select blocks of code and see whether you think the explaination makes sense.


## Deploying our application (90 min) 

For this lab, you will need to have access to an AWS account, and have enough privileges to create, deploy, and then delete resources. In this lab we are going to use Amazon Q Developer to help us understand how we can deploy this application on AWS, and then ask it to help guide us through each of the steps. By the end of this, we should have our simple application up and running in the Cloud.

**Lab 03-1 Deployment options**

We want to deploy this application on AWS, and we want to do that via containers. Amazon Q Developer can help us narrow down and select the right AWS service to help you. Let's ask it some questions about our application, and the container deployment options it thinks are well suited.

```
I want to deploy this application on a container solution. What are these best container deployment options on AWS, for this application?
```

Review the output. Is this helpful? Did you try some follow up questions/prompts?

```
Which of these is the simplest to get started with?
How do I get started with this?
```

The output of this is likely to suggest (remember, non determinsitic tools will always vary in their output) that AWS Fargate and Amazon ECS as the likely best deployment option. This does seem like a good selection, so we will proceed on the basis of wanting to deploy our application on Amazon ECS.

The next step is to ask Amazon Q Developer how our application might need to change when deploying to Amazon ECS. I try the following prompt

```
Update this application so that it will run on Amazon ECS
```

Review your output. When I ran this, it provided some general changes that would be needed whether I was deploying this to Amazon ECS or another compute environment.

> **Hint!** The output I got asked to change two things. 1/ Remove the "if __name__ == '__main__':" code block as this is using the Flask development server and not ideal for running on a server, and 2/ create an entrypoint script and use something like Gunicorn WSGI server to start the application. This is what my script looked like
>
> ```
> #!/bin/sh
> # Start the WSGI server
> gunicorn --bind 0.0.0.0:5000 app:app
> ```
>
> I now start my application using ./entrypoint.sh (change to .bat if you are using Windows)

Make the necessary changes to make your application ready for its server life.

**Complete:** You can proceed to the next lab.

---

**Lab 03-2 Migrating our database**

We have been running our Postgres database locally, which was fine as we developed our application. We now need to think about how to move the database portion. Lets see how we can get Amazon Q Developer to help us.

```
What are the best options for deploying this Postgres 15.6 database on AWS?
```

Explore the output. You will likely be offered a number of options. Ask follow up questions to help you get clearer answers.

```
Which is the best options for this application?
```

You can also ask specific questions based on your non functional requirements. For example, if performance, or scale, or cost is your biggest concern, refine your prompts to help you get more specific information. Use the interactive chat approach to ask follow up questions to provide more specific informtion. Try some of the following to see what you get.

```
If cost is my most important consideration, what is the best option?
I only want to spin up a test postgres database, which option should I go with?
```

We are going to proceed on the basis of using Amazon RDS Postgres for our database. Now that we now what we want, we need to get some help from Amazon Q Developer to guide us through this. Using the output of the first stage (the decision to deploy our application on Amazon ECS) we might craft a prompt that looks like the followiing

```
This is a completely new setup, assume I do not have any existing resources set up. Provide a step by step guide on how I can setup a single Amazon RDS PostgreSQL database server.
```

Review the output - you should find that Amazon Q Developer has provided a nice checklist of things you need to do to get this application up and running.

> **Tip!** You can ask follow up questions, perhaps you liked the checklist but you want more specific details about one of the points, or maybe you are not sure how to do another. This is the great thing about the interactive chat interaction with Amazon Q Developer - as it remembers the previous responses, it proivdes more contextualised answers based on the sum of the questions and answers that have come before.

One follow up question I typically ask is the following:

```
Can you show me a cloudformation template that provisions this in the eu-west-2 region for me.
```

> **Tip!** It is helpful to provide as much information as possible when asking Amazon Q Developer to provide code suggestions. In this instance, it might not know that I want to deploy this in the London region, so I need to provide that additional context for it.

Review the output. If it is anything like mine, you should get a detailed Cloudformation teplate, which we can paste into a new file.

From your IDE, create a new file called "rds-deployment.yaml" and paste the contents of the code into this file.

Before we use it, open it up in your IDE and make sure that the VPC details match the AWS Region you are going to deploy it into. The file in the GitHub repo is current set to eu-west-2 (London) but you might be running this from a different region.

From the AWS CloudFormation console, now create a new stack (making sure you check your AWS region) using this cloudformation template (using the "Upload a template file" option).

You might encounter errors when deploying this template. If you do, use Amazon Q to help you troubleshoot. When I did this the first time, I was able to use Amazon Q Developer to help me remove a line that was deprecated and no longer needed.


Once this has completed, how can we test this out. One of the simplest ways we can connect to our RDS Postgres database is use AWS Cloudshell. This will open up a terminal that already has psql installed and ready to go.

```
I am using AWS Cloudshell. Tell me how do I connect to my RDS Postgres database.
```


When you do this, you are likely to get an error. This makes sense - we provisioned our Amazon RDS Postgres database, but we did not configure inbound access at the network level. We need to allow inbound access to our Cloudshell terminal. We can ask Amazon Q Developer to help with this task.

```
How do I enable inbound access to my RDS postgres database
```

As you review the output and go through the steps, you will need to provide our external IP address. If you do not know this, (or even if you do) ask Amazon Q Developer to show you how to do this.

```
How do i find my external IP via the command line
```

> **Good to know!** You will get a number of options. The one I liked the best (and was new to me, so hurrah I learned something new) was to run:
> 
> ```
> wget -qO- ipinfo.io/ip
> ```
> Which provided my external IP.
>


Amend the database security group to add the new inbound rule that will allow your Cloudshell to access your database. Try and access your database again, this time should be prompted to enter your password.

> **Hint** This is the command I used (change the hostname for your RDS postgres hostname)
>
> ```
> psql --host={hostname} --port=5432 --username=postgres --dbname=urldb
>```
>


(Optional Task - Exporting and Importing existing data)

You will already have some data in your local Postgres database, and perhaps you might want to move this data to the new Amazon RDS Postgres database you have setup. There are many options available, so lets see if Amazon Q Developer can help us with this task.

```
What is the simplest way of migrating data from my local Postgres database running in a local docker container, to my Amazon RDS instance running ?
```

You should get some useful information. It looks like we need to use a tool called pg_dump, to export the local data and then use the same tool to import into Amazon RDS Postgres. This tool is not installed on our environment, so we can ask Amazon Q on how to do that

```
How do I install pg_dump on my local machine
```

Review the output, but do **not** run the commands yet. When using tools like Amazon Q Developer, it is really important to put as much detail and context into the request. If you do not, you might likely get output that is correct, but perhaps for not your specific setup. I am redo this prompt to improve the liklihood of good outputs.

```
How do I install pg_dump for my local database running Postgres 15.6. I am using Ubuntu.
```

You should see a difference in the level of detail and relevance to our setup. We should complete the steps outlined to install pg_dump.


Check to make sure you have it working by running the following:

```
pg_dump --version
```

And you should get something like

```
pg_dump (PostgreSQL) 15.7 (Ubuntu 15.7-1.pgdg22.04+1)
```

> **Hint!** You should be guided by Amazon Q Developer to run a command that will export your database. This is the command that it provided me.
>
> ```
> pg_dump -U postgres -d urldb -h 127.0.0.1 -p 5432 -F c > backup.sql
> ```
> 
> Which generated an export file in my local directory,

You should now have a pg_dump export on your local VSCode development machine. We now need to import this into our Amazon RDS Postgres database.

We have already configured the access to our RDS Postgres database via Cloudshell, so we will use that environment to do the import.

Open up a Cloudshell environment, and make sure you are in the same AWS region as your database. From the ACTION menu (top right) you can select UPLOAD FILE and then select your Postgres backup  file (in my example, this was backup.sql). It is a small file and so will not take any time at all.

Now from the Cloudshell environemnt, we can now import our data. As this is a new Postgres environment, we first have to create our database. We can use the same approach as we did when we created it locally, just changing the {hostname}

```
psql -U postgres -h {hostname}
```

> **Hint!** The {hostname} is the fully qualified DNS name of your Amazon RDS Postgres database, not IP. In my example, it was "qlabrdsdb-rdsdatabase-07oxzbaciljh.ceinbxvexcbx.eu-west-1.rds.amazonaws.com"


After entering the password, create your "urldb" database and exit.

Depending on what Amazon Q Developer has guided you, we now need to restore from our backup. Lets ask Amazon Q Developer how to do this.

```
How do I restore a pg_dump backup. I am running Postgres 15.6 on Ubuntu.
```

Review the output, and try running the command. You should now have your old data in the new database.

> **Hint!** This is the command I ran. Notice here how I put the hostname in " " - I needed to do this as pg_restore generated an error when I left them out.
>
> ```
> pg_restore -U postgres -h "{hostname}" -d urldb backup.sql
> 
> ```

We can now check and see if our data is all good by connecting in Cloudshell via psql and running the follwoing query

```
> psql -U postgres -h {hostname} -d urldb

urldb=> select * from shortcuts;
 id | shortcut |           url            |         created_at         
----+----------+--------------------------+----------------------------
  1 | 0hBXEm   | http://www.bbc.co.uk     | 2024-06-04 11:01:22.852552
  2 | NqAo9I   | https://www.amazon.co.uk | 2024-06-04 11:01:25.286275
(2 rows)
```

Looks good, you have now finished this optional lab.

-

Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have setup the RDS Postgres database for this project, you can proceed to the next lab.

----

**Lab 03-3 Containerising our application**

We have our database migrated, now lets do the same thing for our application. In the first lab we explored the guide of guidance and advice that tools like Amazon Q Developer can provide us. We used the Amazon Q Developer Chat interface, and we decided that we were going to deploy this on Amazon ECS. The first step in doing that is building our container locally, and then pushing that to a container registery, which in our case will be Amazon ECR.

> **Amazon Q Developer in the AWS Console** Did you know you can also use Amazon Q within the AWS console? I sometimes find it useful to run the same prompt across both to compare the output. It uses a model that is trained on over 17 years of AWS data. Whilst the model is hosted on Amazon Bedrock, it is different to the one used for the Amazon Q Developer in the IDE. You do need to have an AWS account and for your user to be enabled.

Lets start by asking how to build a container image for our application.

```
What are the steps I need to follow to building a container image of this application
```

Review the output - if yours is anything like mine, it should provide a good starting point for what we need to do. 1. Create a requirements.txt file for our Python dependencies, 2. Create a Dockerfile, 3. Build and package our container image, and finally 4. Configure environment variables. We will ask Amazon Q Developer to help us with each of these. 

The first one is easy, how to create a requirements.txt file. As Amazon Q Developer, and it should provide a response that includes "pip freeze > requirements.txt". After it has been created, review the file. 

The next step is to create our Docker file. So lets ask Amazon Q Developer to help us.

```
Create a docker file for this application
```

Review the output. It should look pretty good. If we try and build this as is, it will fail. Why? I can hear you all say. One of the Python libraries we are installing (psycopg2) has a dependency on the underlying Postgres client libraries, so we need to install that as part of the Docker file. No worries, lets ask Amazon Q Developer to help us. 

```
Create a docker file for this application. Include dependencies required by the psycopg2 library, and make sure it runs in a Python virtual environment
```

When you look at the new recomendations from Amazon Q Developer, you will see that it installs libpq-dev which is what we need. We can now build our container image.

```
sudo docker build -t ada-q-lab .
[+] Building 19.4s (14/14) FINISHED                                                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 851B                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                               0.5s
 => [internal] load .dockerignore                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                  0.0s
 => CACHED [build 1/5] FROM docker.io/library/python:3.9-slim@sha256:088d9217202188598aac37f8db0929345e124a82134ac66b8bb50ee9750b045b            0.0s
 => [internal] load build context                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                 0.0s
 => [build 2/5] RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     libpq-dev     && rm -rf /var/lib/apt/  10.6s
 => [stage-1 2/5] RUN useradd --create-home appuser                                                                                              0.3s
 => [stage-1 3/5] WORKDIR /app                                                                                                                   0.0s
 => [build 3/5] WORKDIR /app                                                                                                                     0.0s 
 => [build 4/5] COPY requirements.txt .                                                                                                          0.0s 
 => [build 5/5] RUN pip install --no-cache-dir -r requirements.txt                                                                               7.7s 
 => [stage-1 4/5] COPY --from=build /app /app                                                                                                    0.0s 
 => [stage-1 5/5] RUN chown -R appuser:appuser /app                                                                                              0.2s 
 => exporting to image                                                                                                                           0.1s 
 => => exporting layers                                                                                                                          0.1s 
 => => writing image sha256:cf81852e621ab3e451ac1dc4248091962fe67877b754a608350518c9306ac966                                                     0.0s 
 => => naming to docker.io/library/ada-q-lab    
```

> **Hint!** You can find the Dockerfile created [here](resources/Dockerfile)


Now that we have our application containerised, lets make sure it works. As we are going to be running our application in a Docker container, we need to change the local host to the IP of your machine. This will vary based on where you are running this workshop. If you are running this on your local machine, you will need to use the reserved hostname "host.docker.internal". If you are running this from VSCode on EC2, you will need to find the private IP address of the instance. The easiest way to do this is to find the EC2 instance via the CloudFormation template, and then from the EC2 console, find the private IP address from the instance details.

```
docker run -p 5000:5000 -e DB_HOST=127.0.0.1 | host.docker.internal -e DB_NAME=urldb -e DB_USER=postgres -e DB_PASSWORD=change-me -e SECRET_KEY=your_secret_key ada-q-lab

```

> **Note!** We are only testing to make sure the app comes up, so you should see the home page when you open the browser. 

When we were using the Flask dev server, we could exit the application by hitting CTRL + C. You can try this, and it might work depending on where you are running this. The other way is to send a QUIT signal to the gunicorn process. We do that by running the following command.

```
ps -ef | grep gunicorn | awk '{print $2}' | xargs sudo kill -QUIT 
```

Which should shut it down.


Now that we have a container image of our application, we need to store it into a container registery, so lets ask Amazon Q Developer to remind us how that goes again.

```
I want to push this container image to a container registry. Provide a step by step guide, including creating the registry.
```

Review the steps, these should be pretty straight forward to complete. Call your Amazon ECR repository "url-app". You can find the AWS Account Number and AWS Region from environment variables (echo $AWS_ACCOUNTID && echo $AWS_REGION)

> **Hint!** These are the command I ran - yours will be different as they will have different AWS Account IDs and possibly different AWS regions.
>
> ```
> aws ecr get-login-password --region eu-west-1 | sudo docker login --username AWS --password-stdin xxxxx.dkr.ecr.eu-west-1.amazonaws.com
> sudo docker tag ada-q-lab xxxxxx.dkr.ecr.eu-west-1.amazonaws.com/url-app:1.0.0
> sudo docker push xxxxx.dkr.ecr.eu-west-1.amazonaws.com/url-app:1.0.0
> ```
>

If you go back to the Amazon ECR console, you should now see you have your application's container image there, with a tag set to 1.0.0. Open up the image, you will notice that the container image has a URI. We will need to use this later on, so make sure you find it before proceeding.

That is this part complete. Before proceeding to the next lab, shut down the application by using CTRL + C and returning to the command prompt.

**Complete:** When you have containerised our application, you can proceed to the next lab.

----

**Lab 03-4 Configuring and Deploying our application to Amazon ECS**

Now that we have a container image we can use, the next step is to create the execution environment for our container. We are going to be using Amazon ECS to do this. We need to connect this to our Amazon RDS Postgres database, so lets ask Amazon Q Developer what we need to do.

```
I want a step by step guide on how to run this container application on Amazon ECR in Amazon ECS. I need to connect to my Amazon RDS Postgres database, which I configure by exposing environment variables (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, and SECRET_KEY)
```

Take a look at the output and follow through the instructions. Is it helpful and does it make sense?

As a good developer, we are always looking to automate our tasks. Lets see if we can ask a follow on question, and ask Amazon Q Developer to help create a CloudFormation template for us.

```
Create a CloudFormation template that does this for me. Make sure that it creates 1. a way for this application to be accsedd from the internet. 2. configures access so that the ECS cluster can access the RDS Postgres database.
```

If you are not very confident or familiar with CloudFormation templates, you might need to proceed carefully. You can use Amazon Q Developer to help explain or add/change things you feel are not quite right, or missing.

I also followed up with additional improvements as I noticed some of the things I asked were not created.

```
Can you update this template so that it asks for the RDS Security Group.
Update the template to include ingress from the ECS cluster to the RDS database
Can you update it so that it creates logs in Cloudwatch
Change the health check from / to /add
```

Review your output. [Here](resources/ecs-deployment.yaml) is the one that it created for me. Compare how they are different or similar. Use this one to do your deployment

You are going to need to grab a lot of information from previous steps in order to deploy the application to Amazon ECS. You are going to need:

* AppImageURI is the link to your container image. This is the URI that you looked at in Amazon ECR.
* The hostname of your Amazon RDS Postgres database (in my example, this was qlabrdsdb-rdsdatabase-07oxzbaciljh.ceinb9vexcbc.eu-west-1.rds.amazonaws.com)
* The name of your user - this will be "postgres"
* The name of your database - this will be "urldb"
* The password - this will be "change-me"
* The Secret Key - you can enter any string, I used "secret"
* The VPC ID - select the VPC that your Amazon RDS database is using. You can get this from the Amazon RDS console
* The Subnet IDs - select the two public subnets from the same VPC. You can get this from the Amazon RDS console
* RDSSecurityGroup - select the security group which will be modified to allow ingress traffic from this ECS cluster

The deployment will take several minutes, so perfect time for a break.

After about 10 minutes, the deployment should complete. Check the "Output" tab for the CloudFormation stack, where you will find the external DNS for your url shorterning application. You can try and access it, and try it out. It should work exactly as on your local setup.

Explore what has been created. Check out the Amazon ECS console, and look at the service and tasks that are running. You can view the Logs and it should look familiar.

> **Hint!** If you are struggling, the completed code that Amazon Q Developer generated for me can be found at the ecs branch of the repo, which you can access by
>
> ```
> git checkout ecs
> ```

You can make changes to your application. Once you have made changes, you will need to:

* re-build your local container image, with a different tag
* push the updated container image to the Amazon ECR container repo
* update the CloudFormation tempalte to use a new URI for the container image


**Complete:** Congratulations, you have completed all the labs. Remember to remove, delete, and clean up all the resources you created if you are running this in your own AWS environment. If you are doing this within a Workshop Studio environment, you are good to go.


**Additional activities**

If you want to explore this lab more, here are some ideas that you can look to partner with Amazon Q Developer to work through.

1. Instead of using environment variables to manage connection details to your Amazon RDS Postgres database, use AWS Secrets Manager
2. Implement a simple CI/CD system that allows you to automate the process of making changes to your code
3. Add a new feature to your application that exports all the url's it has saved
4. Add OpenTelemetry support for this application, and then explore some of the traces and spans from within the AWS console.


## Finish and Clean up

Once you have completed this lab, make sure you have removed any resources you do not want to keep by following these instructions

**Shutdown the Postgres database**

If you created a local Postgres database, you need to shut this down. Open the terminal session where you started Postgres and CTRL+C, and then run the following command when the command prompt returns

```
docker compose -p local-postgres -f postgres.yml down
```

You can additional delete any container images that were downloaded 


**Clean up the lab directories**

Delete the working directory we created at the beginning of this lab, which contains all the files we worked on.

**Remove your Cloud based VSCode**

If you spun up a VSCode instance on Amazon EC2, then follow the instructions (below, in the "Creating supporting resources to run this lab" section) to delete the instance.

**Remove AWS resources**

If you did optional lab of deploying the application to AWS, then you will need to remove the resources created. As we used AWS CDK to deploy our application to AWS, then we can use this to clean up all the resources using the "cdk destroy {stack}" command.

You will also need to delete the container images and the image repository created in Amazon ECR.



## Creating supporting resources to run this lab

To get the most from this lab, you will need to be running VSCode, and be able to install and run a few other components (Docker, VSCode Amazon Q Developer plugins, etc). If you are not able to do this, then what are your options? I have successfully run this lab using [GitPods](https://gitpod.io/workspaces) although I had to run a Postgres database separately (I used an Amazon RDS instance to do this). Alternatively you can spin up a VSCode environment on an EC2 instance.

**Setting up VSCode on EC2**

If you have access to an AWS account, then you can use [the following Cloudformation template](https://aws-oss.beachgeek.co.uk/3xa) to deploy VSCode server on an EC2 instance. After downloading this gist locally, log into the AWS account you want to use. From the AWS CloudFormation console, go to CREATE NEW STACK, and then use the UPLOAD A TEMPLATE FILE option, selecting the downloaded template. You can accept the defaults (you will need to give it a name), and deployment will only take 5-10 minutes. Once deployed, from the OUTPUTs tab, you will see two things you need to access your new VSCode cloud desktop - a URL link to it, and a password. Click on the link, and then enter the password and you should then be presented with VSCode.

![Running VSCode in EC2](/images/ada-q-ec2-vscode.png)

This has all the developer tools you will need to run this lab, as well as experiment with other programming languages such as Java, Rust, .NET, and Node.

I have been running this for a week, and the daily cost is around $1.50.

*Cleaning up and removing your VSCode on EC2*

After you have finished, make sure you clean up and delete all the resources. From the AWS CloudFormation console, select the stack and then use the DELETE STACK option to remove your VSCode on EC2 environment.

**Setting up a local Postgres database**

If you want to run one locally, you can use the following which uses Docker Compose (or Finch if you are using that) to spin up a local Postgres database.


*Start a local Postgres database*

This lab will need a running Postgres database. We will be using Docker to get one locally up and running. If you do not have or are allowed to have Docker installed, please speak with the instructor - they will provide a suitable workaround that will allow you to connect to a Postgres database.

Follow these instructions if you DO have Docker running locally. 

In this directory we have our docker compose file, which we can see provides a very simple setup for running a local PostgreSQL database.

```
version: '3'
volumes:
  psql:
services:
  psql:
    image: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: change-me
    volumes:
      - psql:/var/lib/postgresql/data 
    ports:
      - 5432:5432% 
```
Take note of the username (postgres) and password (change-me) that will get configured for this local Postgres database. It will use the standard port of 5432.

To start our Postgres database (make sure you are in the finch directory)

```
cd finch
docker compose -p local-postgres -f postgres.yml up
```
You should see output that looks similar to the following:

```
INFO[0000] Creating network local-postgres_default      
INFO[0000] Ensuring image postgres                      
INFO[0000] Creating container local-postgres-psql-1     
INFO[0000] Attaching to logs                            
psql-1 |
psql-1 |PostgreSQL Database directory appears to contain a database; Skipping initialization
psql-1 |
psql-1 |2024-05-15 16:18:45.413 UTC [1] LOG:  starting PostgreSQL 15.6 (Debian 15.6-1.pgdg120+2) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
psql-1 |2024-05-15 16:18:45.414 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
psql-1 |2024-05-15 16:18:45.414 UTC [1] LOG:  listening on IPv6 address "::", port 5432
psql-1 |2024-05-15 16:18:45.416 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
psql-1 |2024-05-15 16:18:45.420 UTC [29] LOG:  database system was interrupted; last known up at 2024-05-14 13:34:27 UTC
psql-1 |2024-05-15 16:18:45.514 UTC [29] LOG:  database system was not properly shut down; automatic recovery in progress
psql-1 |2024-05-15 16:18:45.518 UTC [29] LOG:  redo starts at 0/1E4F2B8
psql-1 |2024-05-15 16:18:45.518 UTC [29] LOG:  invalid record length at 0/1E4F3A0: expected at least 24, got 0
psql-1 |2024-05-15 16:18:45.518 UTC [29] LOG:  redo done at 0/1E4F368 system usage: CPU: user: 0.00 s, system: 0.00 s, elapsed: 0.00 s
psql-1 |2024-05-15 16:18:45.521 UTC [27] LOG:  checkpoint starting: end-of-recovery immediate wait
psql-1 |2024-05-15 16:18:45.528 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.003 s, sync=0.002 s, total=0.009 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB; lsn=0/1E4F3A0, redo lsn=0/1E4F3A0
psql-1 |2024-05-15 16:18:45.531 UTC [1] LOG:  database system is ready to accept connections
```

Leave this up and running in a command window as we will need to connect to this as we build our application.

> **Stopping the local Postgres database**
>
>To stop the Postgres database, use CTRL + C
>
>```
>^CINFO[0119] Stopping containers (forcibly)               
>INFO[0119] Stopping container local-postgres-psql-1  
>```
>
> and then type the following
>
>```
>docker compose -p local-postgres -f postgres.yml down
>```
>Which will return you back to the command line.
>

*Additional tools for VSCode*

In addition, you may find the following VSCode plugin useful for connecting to local databases. With the trial/free version, it allows you to connect to three databases.

* Database Client JDBC - https://marketplace.visualstudio.com/items?itemName=cweijan.dbclient-jdbc