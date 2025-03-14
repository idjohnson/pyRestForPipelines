# my-flask-api/README.md

# My Flask API

This project is a simple Flask application that serves a REST API with an "approved" endpoint.

## Project Structure

```
my-flask-api
├── src
│   ├── app.py          # Main application file
│   └── test_app.py     # Unit tests for the application
├── requirements.txt     # Dependencies for the application
├── Dockerfile           # Dockerfile to build the application
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage

- **GET /approved**: Returns the current status.
- **POST /approved**: Updates the status based on the payload.

### Example Requests

- To get the current status:
  ```
  curl -X GET http://localhost:5000/approved
  ```

- To update the status to "approved":
  ```
  curl -X POST http://localhost:5000/approved -H "Content-Type: application/json" -d '{"status": "approved"}'
  ```

- To update the status back to "pending":
  ```
  curl -X POST http://localhost:5000/approved -H "Content-Type: application/json" -d '{"status": "pending"}'
  ```

## Docker

To build and run the application using Docker, use the following commands:

1. Build the Docker image:
   ```
   docker build -t my-flask-api .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 my-flask-api
   ```

## License

This project is licensed under the MIT License.