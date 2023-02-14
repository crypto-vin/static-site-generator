# Flask-based Static Site Generator

## Introduction

A static site generator is a tool that generates a website consisting of static HTML, CSS, and JavaScript files. It takes input files, such as Markdown or HTML, and uses templates to generate a complete website that can be served directly by a web server without the need for a dynamic web application or database. Examples of popular static site generators include Jekyll, Hugo, and Gatsby. This, however, is a DIY static generator sample that I worked on and developed myself. It takes markdown input files and converts it to an output file that contains HTML file content, which is then loaded into a Flask Webapp for easy manouvering and hosting.

# Contents

- About
- Requirements
- How To Implement The Static Site Generator
- Credit

# About

Flask is a micro web framework that can be used to build dynamic web applications, but it can also be used as the foundation for a static site generator. Flask provides a simple and flexible way to generate static sites by allowing you to programmatically generate HTML files based on templates and data.

With Flask, you can define routes that map to specific pages on your website, and then use templates to generate the HTML for each page. You can also use Flask extensions and plugins to add additional functionality, such as support for Markdown or other markup languages.

One common approach to using Flask as a static site generator is to define a set of routes that map to different pages on your site, and then use Flask's built-in Jinja templating engine to generate the HTML for each page. You can also use Flask's static file handling capabilities to serve CSS, JavaScript, and other static assets.

Overall, Flask provides a lightweight and flexible foundation for generating static sites, and is a popular choice for developers who want to create custom static site generators that can be tailored to their specific needs.

# Requirements

You will need to first install Python in your local PC
If already installed, install the following modules:
- click==8.1.3
- colorama==0.4.6
- Flask==2.2.2
- importlib-metadata==6.0.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- markdown2==2.4.7
- MarkupSafe==2.1.2
- Werkzeug==2.2.2
- zipp==3.13.0

Most of the modules above come with flask, hence you won't necessarily need to install them one bu one

# How to Implement the Static Site Generator
