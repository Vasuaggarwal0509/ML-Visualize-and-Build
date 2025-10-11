# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Set the working directory
WORKDIR /app

# Copy your project into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose MLflow UI port (5000) and model API port (1234)
EXPOSE 5000 1234

# Run ZenML setup (optional)
RUN zenml init

# Command to run your deployment script
CMD ["python", "run_deployment.py"]