
***Rocket.Chat API Integration***

***Overview***
This README provides instructions for setting up and integrating with the Rocket.Chat API using Docker and Python. It covers configuration, Docker Compose setup, API integration for user login and message sending, and how to run the application.

***Prerequisites***
Docker: Ensure Docker and Docker Compose is installed machine.
Python: Python 3.7 or higher.
HTTPX:  Python library for making HTTP requests. Install it using pip install httpx.
FastAPI:For building web applications. Install it using pip install fastapi.

***Configuration***
Before starting, you'll need to configure several environment variables. These include database connection strings, API URLs, and port settings. Modify the following variables in your environment or docker-compose.yml:

***Docker Compose Setup***
A docker-compose.yml file is provided for easy deployment of Rocket.Chat and its MongoDB database. This setup handles service definitions, environment variables, and volume management.
Create a docker-compose.yml file with the provided configuration.
Use docker-compose up -d to start the services.

***API-Integration***

***Login User***
This functionality allows users to authenticate with their Rocket.Chat credentials. Upon successful login, an authentication token and user ID are returned for subsequent API calls.

***Send Message***
Once authenticated, users can send messages to specific channels using the API. This functionality requires the channel name and message text as input.

***Running the Application***
Start Docker Containers: Run "docker-compose up -d" to launch Rocket.Chat and MongoDB.
Authenticate: Use the login function to authenticate a user.
Send Messages: Call the send message function with the desired parameters.

