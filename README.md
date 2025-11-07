# Student Manager Flask App

This is a simple web application for managing a student database, built with Python, Flask, and MySQL.

In the project you will be able to add: 

* Student Name

* Student Age

* Student Grade

This data will automatically be stored in the database, and updated in the web application. 

You will also be able to delete wrong entries. 

Each student will have its unique ID. 

![example](https://github.com/user-attachments/assets/0bc4ae63-62ab-4c59-b9d5-04b6dda64073)


---

## 🚀 How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-project.git](https://github.com/your-username/your-project.git)
    cd your-project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    * Make sure you have a MySQL server running.
    * Create a database (e.g., `CREATE DATABASE students;`).
    * You may need to run a `schema.sql` file to create the tables (if you add one).

5.  **Create your environment file:**
    * Copy the `.env.example` file and rename it to `.env`.
    * Fill in your personal database details in the new `.env` file.
    ```ini
    DB_HOST=localhost
    DB_USER=your-mysql-user
    DB_PASSWORD=your-mysql-password
    DB_NAME=students
    ```

6.  **Run the app:**
    ```bash
    flask run
    ```
