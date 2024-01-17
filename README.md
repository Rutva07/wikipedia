# Wikipedia

## Overview

This is a basic Wikipedia application that utilizes Python, HTML, CSS, Bootstrap and the Django framework. It facilitates a collaborative environment where users can seamlessly contribute, edit, and explore content anonymously, fostering increased engagement and collaboration.

## Components and Interactions

### Django (manage.py) 
Serves as the command-line interface for managing key functionalities of the Django project. Streamlines project management, providing a convenient way to perform routine tasks and configurations during both development and deployment phases.

### HTML Template (encyclopedia/templates/encyclopedia/..)
These are the template files that defines the structure and style of the web pages. It includes input forms for posting/editing information, button to submit messages, and links.

### CSS Styles (within all .html files)
This includes simple styles to enhance the visual appearance of the message blocks and form elements.

### Markdown files (entries/..)
This includes existing markdown files. Whenever user creates,edits or deletes content on the website, particular action will simultaneously occur on corresponding markdown file.

## How to Start the Application

1. Clone the repository: git clone https://github.com/Rutva07/wikipedia.git
2. Navigate to the project directory: cd wikipedia
3. Run the Flask application in terminal: python manage.py runserver
4. Navigate to given address.
