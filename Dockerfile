# Use the official Python image from the Docker Hub
FROM python:3.11
RUN apt-get update -y && apt-get upgrade -y
# Set the working directory in the container
WORKDIR /app
COPY ./pyproject.toml /app/pyproject.toml
ADD src /app/src
COPY ./main.py /app/main.py
ENV PYTHONPATH=./src
# Copy the requirements file into the container
RUN pip install --no-cache-dir --upgrade poetry
#RUN poetry config virtualenvs.create true
#RUN poetry install --no-dev --no-interaction --no-ansi --extras all
RUN pip install python-dotenv
RUN poetry install

# Install the required dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container


# Expose the port that the FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
