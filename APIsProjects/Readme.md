# APIs Projects

Welcome to the folder containing various Python projects, each interacting with a specific API. Below, you'll find a brief description of each project.

# Authors

- [@ORomero227](https://www.github.com/ORomero227)

# **Projects**
- [Habit Tracker](#HabitTracker)
- [Kanye Quote Generator](#KanyeQuoteGenerator)
- [Quizzler](#Quizzler)
- [Workout Tracker](#WorkoutTracker)


# HabitTracker

This Python script demonstrates interactions with the Pixela API, allowing you to create and manage graphical representations of tracked data. The script covers the following functionalities:

- Create an Account:
    Uses the provided USERNAME and MY_TOKEN to create a new user account on Pixela.
- Create a Graph:
    Currently commented out, but includes functionality to create a graph for tracking specific data, such as walking distance.
- Add a Pixel:
    Currently commented out, but includes functionality to add a data point (pixel) to the created graph, specifying the date and quantity.
- Edit a Pixel:
    Currently commented out, but includes functionality to update the quantity of an existing pixel on a specific date.
- Delete a Pixel:
    Currently commented out, but includes functionality to delete a pixel from the graph on a specific date.
  
Feel free to uncomment and utilize the sections of the script that correspond to the Pixela operations you want to perform.

#  KanyeQuoteGenerator

This Python project utilizes the Tkinter library to create a simple GUI application that fetches Kanye West quotes from the "https://api.kanye.rest/" API. 

The application features:
- A background image 
- A Kanye West image button
- A canvas to display the fetched quotes dynamically.

Clicking the Kanye button triggers an API request, and the obtained quote replaces the default text on the canvas.

Key Components

  1. **Tkinter**: Used for creating the graphical user interface.
  2. **Requests library**: Interacts with the Kanye West quote API.
  3. **Canvas**: Displays the quotes.
  4. **Button with Kanye West image**: Triggers quote retrieval.

# Quizzler

Quizzler is a Python quiz application that brings interactive trivia to your fingertips. With a sleek Tkinter-based graphical user interface, this project dynamically fetches questions from the Open Trivia Database, offering a diverse and engaging quiz experience.

  1. Dynamic Question Retrieval: Utilizes the Open Trivia Database API to fetch a set of questions, providing variety in each quiz session.
  2. User-friendly Interface: The Tkinter GUI displays the current score, the question text, and offers immediate feedback on user responses.
  3. Interactive Feedback: Users receive instant feedback with visual cues (green for correct, red for incorrect).
  4. End-of-Quiz Message: Notifies users when they've reached the end of the quiz.


# WorkoutTracker

This Python script empowers users to track their workout activities efficiently, utilizing the Nutritionix and Sheety APIs for exercise recognition and logging. Key components and functionalities of the script include:

1. Nutritionix API Requests:
- User Input: Collects exercise details from the user, which are then sent to the Nutritionix API for exercise recognition.
- Nutritionix Endpoint: Utilizes the Nutritionix API endpoint for natural language exercise recognition.
- Parameters: Sends user details such as gender, weight, height, and age, along with the exercise text, to the Nutritionix API.
- Response Handling: Parses the response to obtain exercise details, including name, duration, and calories burned.

2. Sheety API Requests:
- Sheety Endpoint: Interacts with the Sheety API endpoint for workout tracking.
- Authorization: Utilizes the Sheety authentication token for authorization.
- Logging Workouts: For each recognized exercise, logs a new row in the Sheety worksheet with details such as date, time, exercise name, duration, and calories burned.

#### How to Use:
- Run the script.
- Enter details about the exercises performed when prompted.
- The script will recognize and log the exercises, updating the Sheety worksheet.
