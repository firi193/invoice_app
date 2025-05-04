FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set PYTHONPATH for internal imports like `from reports import reports`
ENV PYTHONPATH=/app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the container
COPY ./app /app

# Add debug to check files in the container
RUN ls -R /app

# Expose the port
EXPOSE 8000

# Start the FastAPI app with the correct path
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
