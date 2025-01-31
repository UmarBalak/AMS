# Job Application Management System (JAMS) API

📌 **Project Overview**  
The Job Application Management System (JAMS) API is a FastAPI-based backend service designed to manage job postings, candidate applications, and the application process. It offers CRUD operations for managing jobs, candidates, and applications while using SQLAlchemy ORM to interact with a SQL database (PostgreSQL).

🚀 **Deployment**  
- **Hosted API**: [https://amsapi.onrender.com](https://amsapi.onrender.com)  
- **Live API Docs**: [https://amsapi.onrender.com/docs](https://amsapi.onrender.com/docs)

🚀 **Features**
- **Job Management**: Add, update, retrieve, and delete job postings.
- **Candidate Management**: Register, update, and delete candidate profiles.
- **Application Management**: Apply for jobs, view applications, and update their statuses.
- **SQL Integration**: Data is stored and managed in a PostgreSQL database via SQLAlchemy ORM.
- **RESTful API**: Well-structured API with auto-generated OpenAPI documentation.

🏗️ **Tech Stack**
- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: OAuth2 + JWT (Planned)
- **Deployment**: Render
- **Documentation**: Auto-generated Swagger UI

🌐 **API Endpoints**

| Method | Endpoint                  | Description                                      |
|--------|---------------------------|--------------------------------------------------|
| `POST`   | /jobs/                    | Create a new job posting                        |
| `GET`    | /jobs/                    | Get all job postings                            |
| `GET`    | /jobs/{id}                | Get job posting by ID                           |
| `PUT`    | /jobs/{id}                | Update job posting details                      |
| `DELETE` | /jobs/{id}                | Delete a job posting                            |
| `POST`   | /candidates/              | Register a new candidate                        |
| `GET`    | /candidates/              | Get all candidates                              |
| `GET`    | /candidates/{id}          | Get candidate profile by ID                     |
| `PUT`    | /candidates/{id}          | Update candidate profile                        |
| `DELETE` | /candidates/{id}          | Delete a candidate profile                      |
| `POST`   | /applications/            | Apply for a job                                 |
| `GET`    | /applications/{id}        | Get applications by candidate or job ID         |
| `PUT`    | /applications/{id}        | Update application status                       |
| `DELETE` | /applications/{id}        | Delete an application                           |


## 📜 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/UmarBalak/AMS.git
cd AMS
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file with:

```
DATABASE_URL=postgresql://username:password@localhost/dbname
```

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

### 5️⃣ Access API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🤝 Contributing

Want to contribute? Feel free to fork this repo, create a new branch, and submit a pull request!

## 📜 License

This project is licensed under the MIT License.



