from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, Ashutosh Kumar!"}
