from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/get_todos')
async def get_todos():
    # print("Aaryan")
    conn = sqlite3.connect("todo_db.db")
    cur = conn.execute("select * from todo_table")
    todos = cur.fetchall()
    todos_json = []
    for i in todos:
        single_todo = {}
        single_todo["id"] = i[0]
        single_todo["title"] = i[1]
        single_todo["description"] = i[2]
        single_todo["status"] = i[3]
        todos_json.append(single_todo)

    print(todos_json)
    print(todos)
    return todos_json


@app.post('/create_todo')
async def create_todo(title, description):
    conn = sqlite3.connect("todo_db.db")
    sql = "INSERT INTO todo_table(title, description) VALUES ('%s', '%s')" % (
        title, description)
    conn.execute(sql)
    conn.commit()
    conn.close()


@app.post('/delete_todo')
async def delete_todo(id):
    conn = sqlite3.connect("todo_db.db")
    sql = "DELETE from todo_table WHERE id=%s" % id
    conn.execute(sql)
    conn.commit()
    conn.close()


# @app.post('/update')
# async def update_todo(title, description, id):
#     conn = sqlite3.connect('todo_db.db')
#     sql = 'UPDATE todo_table SET title='%s', description='%s' WHERE id={id}' % (title, description)
#     conn.execute(sql)
#     conn.commit()
#     conn.close()
