# Cookie Clicker Automation

Hey there, if you have ever played [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game developed by DashNet and ever wondered how addictive it is. I have been playing past few days now and figured that there are multiple strategies to be used but, the primary method of getting a cookie is by clicking on the cookie chip which is pretty tiring and your mouse might crash :wink:or stop working. Thereby, I used [Selenium](https://www.selenium.dev/) automation tool to do the job. 

## Prerequisites

- [Selenium Driver](https://www.selenium.dev/)
- [Chrome Driver](https://chromedriver.chromium.org/downloads)

### Steps

1. Download the code and open in your local IDE.
2. If you have a game that's already running then head over to options > export save and copy the whole content and paste it in [import.txt](CookieClicker/import.txt) file.
3. Click on run.
4. After 5000 clicks it plays a notification sound to notify you to buy something from the store since, the user interaction is not appreciated by the automation tool.  You can modify these settings in the code and you will get 10 seconds to perform your action.

![Cookie Clicker](images/CCA.gif)

:information_source:Customize it your way, don't make the webdriver to click 10,000 times as it throws an error.



**Date: 5/6/2021**