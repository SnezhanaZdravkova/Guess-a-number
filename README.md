![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# GUESS-A-NUMBER

----

> Guess-A-Number is a Python based application fully run within the terminal.

> This app runs three levels of difficulty, where the player has the options to chooce:
>
>> 1. First level: The Player has to guess a randomly generated number between 1 and 10.
>> 2. Second level: The Player has to guess a randomly generated number between 1 and 100.
>> 3. Thirth level: The Player has to guess a randomly generated number between 1 and 1000.

> This application explores the posibilites of automation with Python, handling user inputs and random outcomes through the use of classes and functions.

> Guess-A-Number is deployed on Heroku.

> Live Link to the app on Heroku here: [Guess-A-Number](https://guess-a-numbe.herokuapp.com/ "Guess-A-Number")

----

## Application across difference platforms

 ![devices](/images/devices.jpg)

- https://techsini.com/multi-mockup/
The multi device website mockup generator online tool above have been used to render preview images on a selection of Apple devices.

---
## Program flow charts:

> ![flowchart-manual](/images/flowchart-manual.jpg)

> ![flowchart-Lucidchart](/images/flowchart-lu.jpg)

> - I used the charts as templates for me visualise how I was going to go about building this application.

## UX Description
>
### How to play the game:

> Guess-A-Number is an input based application, where depending on assigned input options, the player can make selections on what game level they'd like to play.
> - In the first level, the player must try to guess a number between 1-10, which the computer has "thought off". The player can enter a number one at a time, and they will get feedback from the terminal on whether their guess was higher or lower than the computer's number. When they guess correctly, they will be told along with the number of attempts it took to guess it, number of games they plaied. The player can have only 5 tries.
> - A prompt then encourages the player to either play again, or exit the game.

> - In the second level, the player must try to guess a number between 1-100, which the computer has "thought off". The player can enter a number one at a time, and as on the first level, they will get feedback from the terminal on whether their guess was higher or lower than the computer's number. When they guess correctly, they will be told along with the number of attempts it took to guess it, number of games they plaied. The player can have only 8 tries.
> - A prompt ask the player to play again, if "yes" the game starts again, if "no" it says "Bye".

> - In the thirth level, the player has 10 tries and must try to guess a number between 1-1000, which the computer has "thought off" as a random number. The player can enter a number one at a time. The player is told to go lower or higher depend of the input. Once the player guess correctly is congratulate.
> - A prompt then encourages the player to either play again, or exit the game.

## User Stories

### The user can expect the following:

- A completely intuitive game with easy to comprehend instructions/rules
- A completely command-line-interface based game
- Can be played as many time as the player wish. This game is to be enjoyed at the user's own pace.
- Playable across all devices.
- Enjoy a random-number-based game
- Be able to exit the application at the end of a game.

## Technologies and Libraries Used

- Python:Functions, this has been the main tool used in my project.
- Github: The cloud based service for hosting repositories for over 73 million developers.
- Gitpod: An open-source developer platform for remote development.
- Git: Used to add, commit and push my changes to the server.
- Lucidchart.com: Used to plan and create my wireframes for my projects.
- Heroku: Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- Built-in Libraries as random - used for dealing with random numbers.
- PEP8 Validator for checking that my Python code meets PEP8 standards.

## Application Features

This application comprises of 3 level games:

- A guessing game level one - from 1 to 10
- A guessing game level two - from 1 to 100
- A guessing game level three - from 1 to 1000

At the beginning of the application, there is a welcome message/main menu that also re-prints at the end of a game round should the player wish to go back to the main menu:

## Testing and Validation
I ran my code through a PEP8 Validator and it passed with no issues/warnings:

![pep8-validator](/images/pep8.jpg)

To test my application, I did my preliminary checks as I went along in the terminal in Gitpod using print() statements in various sections of code. I did further testing in the browser on Window a deployed link through Heroku to make sure all output was working as expected. This did indeed lead me to make adjustments particularly in print and in input statement spacing or too long lines.
I checked to make sure the game ran in correct order by making first running small sections of the game followed by the whole game when it was near completion.

To test the game:
- checked correct prompts appeared when expected
- checked spacing, colour and spelling were all as desired
- checked correct inputs appeared when expected and handled information with no errors.

## Bugs and Issues
No caught problem if the player use by mistake enter letter instead a number, I wanted to use Try statement with the exception of ValueError, coudent figure out how.

![problem](/images/problem.jpg)

## Deployment
Follow the steps below to see how to deploy a repository through Heroku:
- 1. Open the Heroku site, login and access your dashboard and select "create new app".
- 2. You will be brought to a new page where you can enter the name of your app and the region you are based in. Once you do this, click on the "create app" button.
- 3. Once you do this, you will be brought to the app-specific dashboard.
- 4. Make sure you connect/link your github account for ease of deployment and then head to the settings tab to configure vars and install required buildpacks.
- 5. You will want your config vars to have the key and value --> PORT and 8000
- 6. Buildpacks required will be Python and Node.JS in that order.
- 7. Once this is done, you are ready to begin deploying your application!

You can also enable auto or manual deployments if you link your github account and repository to your Heroku account. This enables much faster linked deployments without using the CLI.

## Credits
- Code institute lessonss
- Many thanks to my college @Tara Helberg
- Many thanks to my mentor Ronan
- thanks to @robrovno for help for my README
- Youtube tutorial by Tech with Tim
- LucidCart.com


