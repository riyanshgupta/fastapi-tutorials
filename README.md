# FastAPI - Tutorial 

This project is a simple social media API (type) built using FastAPI, designed to help interns learn the basics of API development, database interactions, and authentication.


# Features 🚀

User Registration and Authentication: Secure user registration and authentication using JWT.
CRUD Operations for Posts: Create, read, update, and delete posts.
User Management: Manage user data and authenticate users.
Token Verification: Verify JWT tokens to ensure secure access.

# Technologies Used 💻 
<img src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" height="50px"> &nbsp;&nbsp;&nbsp; <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" height="50px">  &nbsp;&nbsp;&nbsp;  <img src="https://icon.icepanel.io/Technology/png-shadow-512/SQLAlchemy.png" height="50px">  &nbsp;&nbsp;&nbsp;  <img src="https://avatars.githubusercontent.com/u/110818415?v=4" height="50px">  &nbsp;&nbsp;&nbsp;  <img src="https://user-images.githubusercontent.com/5418178/177059352-fe91dcd5-e17b-4103-88ae-70d6d396cf85.png" height="50px">

Python <br> 
Fastapi <br> 
SQLite <br>
SQLAlchemy </br>
Pydantic <br>
JWT </br>
OAuth2 <br>

# Setup Instructions ⚙️

Clone the repository:
```bash
git clone https://github.com/riyanshgupta/fastapi-tutorials.git
cd fastapi-tutorials
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set up the database:
Ensure the database.py and models.py files are correctly set up and create the database tables.
```python
models.Base.metadata.create_all(bind=engine)
```

Run the application:

```bash
uvicorn main:app --reload
```

# Acknowledgments 🙏
We would like to express our gratitude to the FastAPI, SQLAlchemy, and other open-source communities for their invaluable contributions to this project.
