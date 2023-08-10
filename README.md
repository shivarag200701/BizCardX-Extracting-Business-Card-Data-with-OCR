# BizCardX-Extracting-Business-Card-Data-with-OCR
Bizcard Extraction is a Python application built with Streamlit, EasyOCR, OpenCV, regex function, and MySQL database. It allows users to extract information from business cards and store it in a MySQL database. The main purpose of Bizcard is to automate the process of extracting key details from business card images, such as the name, designation, company, contact information, and other relevant data. By leveraging the power of OCR (Optical Character Recognition) provided by EasyOCR, Bizcard is able to extract text from the images.

![bizcard](https://github.com/beingbvh/BizcardX/assets/135937352/5f667473-1895-4c8e-af35-ec72ec78100f)

## What is EasyOCR?
EasyOCR, as the name suggests, is a Python package that allows computer vision developers to effortlessly perform Optical Character Recognition. It is a Python library for Optical Character Recognition (OCR) that will enable you to easily extract text from images and scanned documents. In my project, I have used easyOCR to extract text from business cards.

When it comes to OCR, EasyOCR is the most sort after Python package:

- The EasyOCR package can be installed with a single pip command.
- The dependencies on the EasyOCR package are minimal, making it easy to configure your OCR development environment.
- Once EasyOCR is installed, only one import statement is required to import the package into your project.
- From there, all you need is two lines of code to perform OCR — one to initialize the Reader class and then another to OCR the image via the readtext function.

## Project Overview
BizCardX is a user-friendly tool for extracting information from business cards. The tool uses OCR technology to recognize text on business cards and extracts the data into a SQL database after classification using regular expressions. Users can access the extracted information using a GUI  using Streamlit. The BizCardX application is a simple and intuitive user interface that guides users through the process of uploading the business card image and extracting its information. The extracted information would be displayed in a clean and organized manner, and users would be able to easily add it to the database with the click of a button. Further, the data stored in the database can be easily Read.

## Libraries/Modules used for the project!
 - Pandas - (To Create a DataFrame with the scraped data)
 - MySQL.connector - (To store and retrieve the data)
 - Streamlit - (To Create a Graphical user Interface)
 - EasyOCR - (To extract text from images)
## Features
- Extracts text information from business card images using EasyOCR.
- Utilizes OpenCV for image preprocessing, such as resizing, cropping, and enhancing.
- Uses regular expressions (RegEx) to parse and extract specific fields like name, designation, company, contact details, etc.
- Stores the extracted information in a MySQL database for easy retrieval.
- Provides a user-friendly interface built with Streamlit to upload images, extract information, and view the database.
## Workflow
To get started with BizCardX Data Extraction, follow the steps below:


- Install the required libraries using the pip install command. Streamlit, mysql.connector, pandas, easyocr or you can refer to the requirements text file.

- Once the user uploads a business card, the text present in the card is extracted by **easyocr** library.

- The extracted text is sent to  the function.py file which classifies the respective text as company name, cardholder name, designation, mobile number, email address, website URL, area, city, state, and pin code using loops and some regular expressions.

- On Clicking the **upload to MySql server** button the data gets stored in the MySQL Database. (Note: Provide respective host, user, password, and database name in sql.py file for establishing a connection.)


