<a name="readme-top"></a>

<div align="center">
  <h1><b>SEPSIS PREDICTION</b></h1>
</div>

# Table of Contents

- [Table of Contents](#-table-of-contents)
- [Sepsis Prediction](#sepsis-prediction)
  - [Features](#features)
  - [🛠 Built With](#-built-with)
- [Objectives](#objectives)
- [Streamlit Page Configuration](#streamlit-page-configuration)
- [Dockerfile for API](#dockerfile-for-api)
- [📝 License](#-license)
- [👥 Authors](#-authors)
- [⭐️ Show your support](#️-show-your-support)

# Sepsis Prediction<a name="about-project"></a>

**Sepsis Prediction** This project aims to develop a machine learning-based solution to predict whether a patient will develop sepsis. Sepsis is a life-threatening condition caused by the body's response to an infection, which can lead to tissue damage, organ failure, and death. Early detection and treatment are crucial for improving patient outcomes.
The project involves training several machine learning models to predict the likelihood of a patient developing sepsis based on various input features. These models are then deployed via an API, and a user-friendly interface is created using Streamlit to allow healthcare professionals to input patient data and receive predictions.


## Features

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

## 🛠 Built With <a name="built-with"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
  <ul>
    <li><a href="">Docker</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## **Objectives**<a name="objectives"></a>
1. Sepsis Prediction: Build a reliable and accurate ML model to predict sepsis, contributing to early detection and intervention.
2. Model Confidentiality: Ensure the ML model architecture remains confidential while providing prediction services through an API.
3. Accessibility: Enable users to interact with the sepsis prediction model via an easy-to-use API, making it accessible to those who already use APIs in their workflows.
4. Scalability: Develop an API that can handle multiple requests efficiently, ensuring it can scale as the number of users increases.

**Project Goals**
To build a reliable and accurate ML model to predict sepsis.
To create an easy-to-use API using FastAPI to embed the model and provide accessibility to users.

**Hypothesis**
Ho: High body mass index (BMI) has no effect on the development of sepsis in patients.
H1: High body mass index is associated with the development of sepsis in patients.

**Analytical Questions**
1. How does the level of plasma glucose affect the outcome of the sepsis test?
2. Do bloodwork results have an effect on whether sepsis is negative or positive?
3. What is the relationship between blood pressure and whether a patient will develop sepsis?
4. What is the relationship between body mass index and whether a patient will develop sepsis?
5. What is the relationship between age and development of sepsis?
6. What is the relationship between having insurance and development of sepsis?

**Timeline**
Week 1: Data understanding, preparation
Week 2: Modelling, evaluation
Week 3: Building API, deployment
Week 4: Containerization, API performance evaluation

## **Streamlit Page Configuration**<a name="streamlit-page-configuration"></a>
The Streamlit page is configured with a title, icon, and wide layout for better user experience. The configuration is set using st.set_page_config().

![Page screenshot of the app](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/app.PNG)

- A title and introduction are provided to explain the purpose of the application. The markdown section gives users an overview of sepsis, the importance of early detection, and instructions on how to use the application.

- **Input Form**
The show_form function creates a form for users to input patient data. The form is divided into three columns to organize the input fields neatly.

![App inputs](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/uoo.PNG)

The form is submitted using a button, which triggers the prediction process.

- **Making Predictions**
Upon form submission, the input data is sent to the backend API for prediction. The application handles the response, displaying the prediction result or an error message if the request fails.

![Prediction request](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/predict.PNG)
![Successful response](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/successful%20response.PNG)

## **Dockerfile for API**<a name="dockerfile-for-api"></a>
Overview
The Dockerfile is used to create a Docker image for the Sepsis Prediction API. This image encapsulates all dependencies and configurations needed to run the API, ensuring a consistent environment across different deployments.

- **Base Image**
The base image used is python:3.12.2. This image includes Python 3.12.2 and provides a clean environment to set up the application.

![Dockerfile code for the API](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/api%20doc.PNG)

- **Copying Requirements File**
The requirements file, which lists all the dependencies for the project, is copied into the /tmp directory in the Docker image.

- **Setting the Working Directory**
 The working directory is set to /app, where the application code has been copied. This ensures that all subsequent commands are run in the context of this directory.

- **Exposing the API Port**
 The Docker container exposes port 8000, which is the port on which the API will be accessible. This allows external access to the API when the container is running.

- **Running the Application**
 The command to start the API is specified. uvicorn is used as the ASGI server to run the FastAPI application. The API will be accessible at host 0.0.0.0 on port 8000.

 ![Running API on uvicorn](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/fastapi.PNG)

## **Dockerfile for Streamlit Application**
Overview
The Dockerfile is used to create a Docker image for the Sepsis Prediction Streamlit application. This image encapsulates all dependencies and configurations needed to run the Streamlit app, ensuring a consistent environment across different deployments.**

- **Base Image**
The base image used is python:3.12.2 This image includes Python 3.12.2 and provides a clean environment to set up the application.

![Dockerfile for the frontend Streamlit app](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/docker%20streamli.PNG)

- **Copying Requirements File**
The requirements file, which lists all the dependencies for the project, is copied into the /tmp directory in the Docker image.

- **Installing Dependencies**
The dependencies specified in the requirement.txt file are installed using pip.

- **Running the Application**
The command to start the Streamlit application is specified. The main.py file is the entry point for the Streamlit app, and the app will be accessible at port 8501.

### **Docker Compose Configuration**
Overview
The docker-compose.yml file is used to define and manage multi-container Docker applications. In this project, Docker Compose is used to set up two services: the API and the Streamlit client. This setup ensures that both services can communicate with each other seamlessly within a shared network.

![Code for Docker Compose File](https://github.com/ZawadiLMG/ML-API-Using-FastAPI/blob/main/Utils/doc%20compose.PNG)

**Version**
The version of Docker Compose being used is specified as 3.

**Building and Deploying the Docker Containers**
1. **Building the Docker Containers**
I built the Docker images for both the API and the Streamlit client.

2. **Starting the Services with Docker Compose**
After successfully building the Docker images, I started both the API and the Streamlit client services using Docker Compose

3. **Accessing the Streamlit Application**
Access the Streamlit application via the link: http://localhost:8501


<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Loyce Zawadi Mumbua**

- GitHub: [GitHub Profile](https://github.com/ZawadiLMG)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/loyce-mumbua/)
- Medium: [Medium Profile](https://medium.com/@mumbualoyce)
- Email: mumbualoyce@gmail.com
- deployed app :[Streamlit app](http://localhost:8501)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>