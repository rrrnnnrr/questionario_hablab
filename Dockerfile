# Use the official Python base image
FROM python:3.11.3-slim-buster

# Set the working directory in the container
WORKDIR /questionario_hablab

# Copy everything to the working directory
COPY . /questionario_hablab

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose a port that your Flask application will be listening on
EXPOSE 5000

# Run the Flask application
# CMD python ./run.py
CMD ["/bin/bash", "gunicorn_start.sh"]
