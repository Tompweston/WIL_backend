#  ⚡️FastAPI Backend For To-Do App

A modern, fast (for python) back-end built with **FastAPI**. To see the frontend to the this full stack web app see my other repo here: 
https://github.com/Tompweston/WIL_backend

---

## 📖 About the Project

This the backend where the following are processed:
- Preform CRUD operations
- Preform authentication checks on all aspects of the app from users to routes 

---

## 🛠 Tech Stack

| Layer     | Technology |
|-----------|-----------|
| Frontend  | SvelteKit (TypeScript) |
| Runtime   | Bun |
| Backend   | FastAPI + UV |   
| Database  | MongoDB |
| Auth      | Better Auth |
| Styling   | CSS |

---

## ⚙️ Prerequisites

Before you begin, make sure you have uv installed:

### You can download it here 
https://docs.astral.sh/uv/getting-started/installation/

## 📦 Installation
1. Clone this repository using
   ```
   git clone https://github.com/Tompweston/WIL_backend.git
   cd WIL_backend 
   ```
2. Install dependencies using:
   ```
   uv venv      # Create a virtual environment
   uv sync --frozen && uv cache prune --ci # install dependencies 

   ```
4. Run the project in dev mode using:
   ```
   uv run fastapi dev
   ```
   or use the following to build a preview of a production version:
   ```
   uv run fastapi run
   ```
5. Make sure you have an instance of the frontend running to access the UI :)
   You can find that here:
   https://github.com/Tompweston/WIL_frontend.git




