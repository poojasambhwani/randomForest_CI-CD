# Start with a base image that includes Python
FROM python:3.8

# Set a working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY src/ .

# Run the app
CMD ["python", "app.py"]
