# IBMHackathon
Recipe Generator Chatbot - Hackathon Submission

## Overview
This project is a simple Recipe Generator Chatbot built using Flask. It helps users with any recipe queries that requires more precise context. The chatbot takes input from users, processes the request, and responds with a suitable response. This app was developed as part of a hackathon submission for the IBM TechXchange Pre-Conference.

## Features
Chat Interface: Users can interact with the chatbot via text input. They can fine tune their queries with filters.

Recipe Suggestions: Input is fed into Watsonx API with an LLM specialised for recipe queries.

User-friendly: The application has a clean and simple interface for easy interaction.

## Prerequisites
Make sure you have the following installed:

Python 3.x
Flask
(Optional) Virtual Environment (recommended for managing dependencies)

### Dependencies

The necessary libraries and dependencies are listed in requirements.txt. These can be installed by running:

```bash
Copy code
pip install -r requirements.txt ```

Project Structure
```php
Copy code
├── app.py               # Main Flask application
├── server.py            # API
├── templates/
│   ├── index.html       # Frontend of the chatbot
├── static/
│   ├── style.css        # Styling for the web interface
└── README.md            # Project documentation
```

## Setup & Installation
Clone the repository:

```bash
git clone https://github.com/username/recipe-generator-chatbot.git
cd recipe-generator-chatbot
```

Install the required dependencies:

```bash
pip install Flask
```

Run the Flask application:

```bash
python app.py
```
Access the app:
Open a web browser and go to http://127.0.0.1:5000 to interact with the chatbot.

## How It Works
User Interaction: The user types their request, such as the ingredients they have or the type of cuisine they want.

Processing: The chatbot processes the input through a tailored IBM Watsonx Prompt Lab LLM and responds accordingly.

Response: The chatbot sends back a recipe suggestion with steps, ingredients, and any additional details or any other recipe/ingredients based response relative to the query.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.