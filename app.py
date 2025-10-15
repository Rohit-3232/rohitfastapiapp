from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
def read_root():
  return{"message": "Welcome to Fastapi"}

@app.get("/greet/{name}")
def greet(name: str):
  return{"message": f"Hello , {name}!"}
