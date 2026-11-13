# DBMS-A3

### Video link https://youtu.be/hMWlqu-kAsU?si=m0MJmMrSc5fo7X7V

## Compile and run

From the project root, create and activate a virtual environment, then install
the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and set `DATABASE_URL` to your
PostgreSQL connection URL:

```text
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/database_name
```

Python does not require a separate build step. To check that the source files
compile, run:


```powershell
python -m compileall app main.py
```

Create the database tables with:

```powershell
python -m app.create_tables
```
then run 
python -m app.seed
python main.py

The project currently provides database setup and student operations, but no
interactive command-line application. For example, after configuring the
database, list students from the project root with:

```powershell
python -c "from app.students import getAllStudents; getAllStudents()"
```
