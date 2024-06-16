# FastAPI Project - Social Media API <img src="https://fastapi.tiangolo.com/img/icon-white.svg" height="25px" width="25px">

This project is a simple social media API built using FastAPI, designed to help interns learn the basics of API development, database interactions, and authentication.


# Features 🚀

User Registration and Authentication: Secure user registration and authentication using JWT.
CRUD Operations for Posts: Create, read, update, and delete posts.
User Management: Manage user data and authenticate users.
Token Verification: Verify JWT tokens to ensure secure access.
# Technologies Used 💻 
<img src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" height="30px"> <img src="https://icon.icepanel.io/Technology/svg/FastAPI.svg" height="30px"> <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Logo" height="30px"> <img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastAPI Logo" height="30px"> <img src="https://icon.icepanel.io/Technology/png-shadow-512/SQLAlchemy.png" height="30px"> <img src="https://avatars.githubusercontent.com/u/110818415?v=4" height="30px"> <img src="https://user-images.githubusercontent.com/5418178/177059352-fe91dcd5-e17b-4103-88ae-70d6d396cf85.png" height="30px">

Fastapi
Python  
SQLite 
SQLAlchemy 
Pydantic 
JWT 
OAuth2

# Setup Instructions ⚙️

Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-socialmedia.git
cd fastapi-socialmedia
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set up the database:
Ensure the database.py and models.py files are correctly set up and create the database tables.
```python
Copy code
models.Base.metadata.create_all(bind=engine)
```

Run the application:

```bash
Copy code
uvicorn main:app --reload
```

# Acknowledgments 🙏
We would like to express our gratitude to the FastAPI, SQLAlchemy, and other open-source communities for their invaluable contributions to this project.
