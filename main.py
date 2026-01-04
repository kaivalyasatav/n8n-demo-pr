from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="FastAPI Starter Project",
    description="A basic FastAPI application",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI!",
        "status": "Running successfully 🚀"
    }

# Sample GET endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "greeting": f"Hello, {name}!"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }
