# 🐾 Pets API

A robust and simple RESTful API built with **Python**, **FastAPI**, and **SQLAlchemy** to manage a database of pets. This project demonstrates a clean architecture pattern, separating concerns between database models, schemas, and API logic.

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete pets.
- **Automatic Documentation**: Interactive Swagger UI and ReDoc included.
- **SQLite Database**: Lightweight and serverless database integration.
- **Data Validation**: Robust validation using Pydantic schemas.
- **Modular Structure**: Organized codebase for scalability and maintainability.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Server**: Uvicorn
- **Testing**: Pytest

## 📂 Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── main.py           # Application entry point and endpoints
│   ├── database.py       # Database connection and session handling
│   ├── models.py         # SQLAlchemy database models
│   └── schemas.py        # Pydantic schemas for data validation
├── tests/
│   └── test_main.py      # Automated tests
├── run.py                # Script to run the server
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## ⚡ Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pets-api.git
   cd pets-api
   ```

2. **Install dependencies**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database (Optional)**
   The application will automatically create the database tables on the first run. However, if you want to populate it with initial data:
   ```bash
   python src/create_pets_db.py
   ```

## 🏃‍♂️ Running the Application

To start the server, simply run the `run.py` script from the root directory:

```bash
python run.py
```

The server will start at `http://127.0.0.1:8000`.

## 📖 Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Test endpoints directly from the browser.
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - Alternative documentation view.

## 🧪 Testing

To run the automated tests, make sure you have `pytest` installed (included in requirements) and run:

```bash
pytest
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
