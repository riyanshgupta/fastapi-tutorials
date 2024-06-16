# FastAPI Project - Social Media API <img src="https://fastapi.tiangolo.com/img/icon-white.svg" height="25px" width="25px">

This project is a simple social media API built using FastAPI, designed to help interns learn the basics of API development, database interactions, and authentication.


# Features 🚀

User Registration and Authentication: Secure user registration and authentication using JWT.
CRUD Operations for Posts: Create, read, update, and delete posts.
User Management: Manage user data and authenticate users.
Token Verification: Verify JWT tokens to ensure secure access.
# Technologies Used 💻 <img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastAPI Logo" height="30px"> <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" alt="Python Logo" height="25px" width="25px"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/97/Sqlite-square-icon.svg" alt="SQLite Logo" width="25px" height="25px">

FastAPI  <img src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" height="30px">

Python  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" height="30px">

SQLite <img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastAPI Logo" height="30px">

SQLAlchemy <img src="https://icon.icepanel.io/Technology/png-shadow-512/SQLAlchemy.png" height="30px">

Pydantic <img src="https://avatars.githubusercontent.com/u/110818415?v=4" height="30px">

JWT <img src="https://user-images.githubusercontent.com/5418178/177059352-fe91dcd5-e17b-4103-88ae-70d6d396cf85.png" height="30px">

OAuth2

# Setup Instructions ⚙️

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/fastapi-socialmedia.git
cd fastapi-socialmedia
Install dependencies:

bash
Copy code

'''
pip install -r requirements.txt
'''

Set up the database:
Ensure the database.py and models.py files are correctly set up and create the database tables.

python
Copy code

'''
models.Base.metadata.create_all(bind=engine)
'''

Run the application:

bash
Copy code

'''
uvicorn main:app --reload
'''

# Acknowledgments 🙏
We would like to express our gratitude to the FastAPI, SQLAlchemy, and other open-source communities for their invaluable contributions to this project.
