# stuff-squared
## 52 apps 52 weeks. 

it is quite simple - every week i will develop/launch a new app (of all sorts: mobile, web, SMS, etc.) and launch a subsquent blog post documenting the process. 


im relatively new to the world of programming (~ 2 years), so this will be an effective way for me to get my hands dirty, and fortify my skillset, while further understanding the process by which i can try to effect real change (however big or small) in the world. it is unlikely that any of these projects themselves will solve any meaningful problems, but they will nonetheless help me build a requisite understanding of how to get there. 


-------------------------------------------------------------------------------------------------------------------

## app 1, week 1: "albert, the genius text messaging companion"


![small-abl](https://user-images.githubusercontent.com/63463942/203387083-5c431f22-317c-4537-b1d8-5cc6a5430705.png)


description: albert is simple - you text him stuff (+1 831 - 618 - 2709), and he will hopefully respond in an interesting/humorous/informative way. 

technical details: he was pieced together using python, more specifically i used GPT3 for the vast majority the response engine (some hardcoding, and i also hope to implement my own training set sometime), Twilio SMS API, Flask, and ngrok for processing all the sending/recieving of messages. also, i deployed albert using the google cloud compute engine. 

**text albert +1 831 - 618 - 2709**


blog post: https://medium.com/@avstuff/52-apps-52-weeks-af7d3ad765dc


-------------------------------------------------------------------------------------------------------------------


examples of albert at work: 

**basic conversation**: 



![2medium-albrert](https://user-images.githubusercontent.com/63463942/203387830-a0a59769-520d-447d-ba3a-ca8d3dfdadc1.png)





-------------------------------------------------------------------------------------------------------------------

**subjective prompt-response**: 



![subjective](https://user-images.githubusercontent.com/63463942/203389947-e318e001-12e7-48bc-8735-50ee6fd43f8d.png)






-------------------------------------------------------------------------------------------------------------------

**technical prompt-response**: 



![gravi-alb](https://user-images.githubusercontent.com/63463942/203387993-fb771307-fd46-443f-b00d-c5566f532bc0.png)







-------------------------------------------------------------------------------------------------------------------


## app 2, week 2: Healthviz 


https://healthviz.app/ -- only works on desktop web browsers. will render blank screen on mobile browser. 


![ui pic](https://user-images.githubusercontent.com/63463942/203390358-ae5fc67f-6df2-44f4-b9d5-4b1b58fef8a4.png)



description: the goal of healthviz is to provide users with a simple, but powerful tool for tracking their health and fitness data. users can log daily workouts, meals, and mental health updates and on the backend, healthviz will store these user logs and visualize this data via a dashboard. healthviz is a web-based application (currently only works for desktop browsing)

motivations: 

- i often find that data visualization/data analysis tools within the realm of fitness tracking tend to be somewhat underwhelming. given my background in data analysis, i figured this would be an interesting thing to try and improve upon. 

- i started an extensive weight loss journey in 2021 (having since lost 80 lbs) and attribute much of my initial fitness momentum to a fitness dashboard that i created for myself, with which i would log all calorie intake/expenditure/deficit, workout logs, meals, mental health status, etc.. This type of tool helped me further cement my motivation for the weight loss journey and thus, i figured i would put my own spin on a health tracking app. 



-------------------------------------------------------------------------------------------------------------------


## app 3, week 3: 'the portal'

https://the-portal.app/   - if browsing on mobile, it only works with the latest iOS version. 


![portal](https://raw.githubusercontent.com/avwtr/stuff-squared/main/portal/portalimg.png)

description: the portal is a simple website in which you can input a text prompt, and recieve a unique, AI generated image based on your prompt. the portal uses the DALLE-2 model developed by OpenAI and is interfaced via streamlit. the portal will serve as a foundational app, that i will continue to add/contribute to over time (similar to most of the apps i develop for this project). in particular, i would like to migrate towards using Stable Diffusion instead of DALLE, implement a more custom built-model, and perhaps even build in an image to image capability. 

motivations: 
- DALLE and Stable Diffusion are some of the most exciting new technologies developed within the AI/ML space, and in general. 
- AI/ML are my core interest, and i will learn a lot about prompt-engineering, model-training, interfacing ML technology into consumer facing applications, etc.
- there is lots of room for growth/addition - i can continue to add on top of this initial version. 


-------------------------------------------------------------------------------------------------------------------

## app 4, week 4: taskTrail

https://tasktrail.app/


![taskTrail](https://github.com/avwtr/stuff-squared/blob/main/taskTrail/smaller.png?raw=true)


description: taskTrail is a web app that helps you log tasks/events as you complete them (entering in some details regarding the completed task/event). taskTrail then consolidates all of your logs, allows you to query them retroactively, and offers some simple data visualizations regarding your activity. 

motivations: 
- i often find most task management tools to be inept. 
- taskTrail is something simple, and easy - it is something that i would use. 
- in a time crunch, taskTrail was somewhat straighforward to develop when compared to alternatives. 

-------------------------------------------------------------------------------------------------------------------


## app 5, week 5: Triviaverse

![trivia](https://github.com/avwtr/stuff-squared/blob/main/triviaverse/gr.png?raw=true)


description: triviaverse is a simple, science trivia mobile app, built for iOS. the app generates 10 unique science trivia questions (pulling from the open trivia API) - once you complete a quiz, the app will display your score, and you can retry with a new of questions. 

motivations: 
- i am new to the world of mobile app development, so this would be a good way for me to learn Swift/iOS dev
- i wanted to refresh my understanding of app store deployment/Xcode/testflight/etc. 
