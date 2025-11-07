\# Student Manager Flask App



This is a web application for managing a student database, built with Python, Flask, MySQL and Bootstrap.



In the project you will be able to add: 

\*\* Student Name

\*\* Student Age

\*\* Student Grade



This data will automatically be stored in the database, and updated in the web application. 

You will also be able to delete wrong entries. 

Each student will have its unique ID. 





&nbsp; 

---



\## 🚀 How to Run This Project



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/your-username/your-project.git](https://github.com/your-username/your-project.git)

&nbsp;   cd your-project

&nbsp;   ```



2\.  \*\*Create and activate a virtual environment:\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   venv\\Scripts\\activate

&nbsp;   ```



3\.  \*\*Install dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\.  \*\*Set up the database:\*\*

&nbsp;   \* Make sure you have a MySQL server running.

&nbsp;   \* Create a database (e.g., `CREATE DATABASE students;`).

&nbsp;   \* You may need to run a `schema.sql` file to create the tables (if you add one).



5\.  \*\*Create your environment file:\*\*

&nbsp;   \* Copy the `.env.example` file and rename it to `.env`.

&nbsp;   \* Fill in your personal database details in the new `.env` file.

&nbsp;   ```ini

&nbsp;   DB\_HOST=localhost

&nbsp;   DB\_USER=your-mysql-user

&nbsp;   DB\_PASSWORD=your-mysql-password

&nbsp;   DB\_NAME=students

&nbsp;   ```



6\.  \*\*Run the app:\*\*

&nbsp;   ```bash

&nbsp;   flask run

&nbsp;   ```

