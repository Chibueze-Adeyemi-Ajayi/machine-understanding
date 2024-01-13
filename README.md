# Brain: Machine Understanding

This app is a simple Flask application that demonstrates how computer understands texts using Large Language Models like transformers and the basic structure of a Flask project and includes a Dockerfile for containerization.

## Prerequisites

- [Python](https://www.python.org/) (>=3.6)
- [Docker](https://www.docker.com/)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Chibueze-Adeyemi-Ajayi/machine-understanding
    cd machine-understanding
    ```

2. Build the Docker image:

    ```bash
    docker build -t nlp/machine_understanding .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 3000:3000 machine_understanding
    ```

    The Flask app will be accessible at [http://localhost:3000](http://localhost:3000).

## Project Structure

MyFlaskApp/
│
├── /
├── ml.py
├── Dockerfile
├── requirements.txt
├── api.py
├── .dockerignore
├── .gitignore
└── README.md

markdown
Copy code

- `/`: Contains the main Flask application.
- `Dockerfile`: Configuration file for building the Docker image.
- `requirements.txt`: Python dependencies.
- `api.py`: Script to run the Flask app.

## Contributing

Feel free to contribute to this project. Submit issues for bug reports or feature requests, and feel free to submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.