# Quote Generator Web App

A simple web application built using **Python and Flask** that displays a randomly generated programming quote each time the page loads.

This project demonstrates the **basic working of Flask**, including routing, template rendering, and passing data from Python to HTML using the **Jinja2 template engine**.

---

## Project Objective

The purpose of this project is to understand the **core architecture of a Flask web application**, including:

- Flask application setup
- URL routing
- Backend Python logic
- Passing variables from Python to HTML
- Template rendering using Jinja2
- Basic project structure used in Flask applications

This project intentionally **does not use a database** in order to focus only on the fundamental interaction between **Flask, Python, and HTML**.

---

## Technologies Used

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **Jinja2 Template Engine**

---

## Project Structure

```
AI_Quote_Generator_Web_App/
│
├── app.py
├── quotes.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### File Description

**app.py**
Main Flask application. Handles routing and sends data to the HTML template.

**quotes.py**
Contains the list of quotes and the function that randomly selects a quote.

**templates/index.html**
Frontend page where the quote is displayed. Uses Jinja2 syntax (`{{ quote }}`) to receive data from Flask.

**static/style.css**
CSS styling for the webpage.

---

## How the Application Works

1. User opens the web page in a browser.
2. The browser sends a request to the Flask server.
3. Flask matches the request with the defined route (`/`).
4. The `home()` function is executed.
5. `get_random_quote()` from `quotes.py` selects a random quote.
6. Flask sends this quote to the HTML template using `render_template()`.
7. The HTML page displays the quote using the Jinja2 variable `{{ quote }}`.

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/AI_Quote_Generator_Web_App.git
```

### 2. Navigate to the Project Folder

```
cd AI_Quote_Generator_Web_App
```

### 3. Install Flask

```
pip install flask
```

### 4. Run the Application

```
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

Each time the page is refreshed, a **new random quote** will appear.

---

## Learning Outcomes

By completing this project, you will understand:

- The structure of a Flask project
- How Flask handles HTTP requests
- How Python backend logic interacts with HTML templates
- How variables are passed from Python to HTML using Jinja2
- How static files (CSS) are served in Flask

---

## Future Improvements

Possible enhancements include:

- Adding a database to store quotes
- Creating a form to allow users to submit quotes
- Adding JavaScript to generate quotes without refreshing the page
- Converting the project into a REST API
- Deploying the application to a cloud platform

---

## Author

RAHUL KP KURUP
MSc Computer Science Student
Interested in Artificial Intelligence, Machine Learning, and Software Development.
