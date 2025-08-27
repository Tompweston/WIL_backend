# Tommy's To-Dos

> A nice first crack at full stack web development, including auth and CI/CD.

## Why
The reason for this project is to learn industry standard devlopment practices/technologies to develop my first modern and secure web app. 

## Features
- Log in/Sign up users 
- Users can add, edit and delete tasks

## Tech Stack
- Frontend: SvelteKit (https://github.com/Tompweston/WIL_frontend)
- Backend: FastAPI
- Database: MongoDB
- Hosting: TBC

## Quick Start
**Prereqs:** , Python 3.13+, MongoDB connection string, 

```bash
# 1) Clone the repository
git clone https://github.com/<you>/<repo>.git
cd <repo>

# 2) Configure environment variables
cp .env.example .env
# Edit .env with your MongoDB connection string and other settings

# 3) Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4) Install dependencies
pip install -e .

# 5) Run the development server
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000
API documentation is available at http://127.0.0.1:8000/docs