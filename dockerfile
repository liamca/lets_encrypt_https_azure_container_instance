# Use an official Python runtime as a parent image  
FROM python:3.7-slim  
  
# Set the working directory in the container to /app  
WORKDIR /app  
  
# Install any needed packages specified in requirements.txt  
RUN pip install --trusted-host pypi.python.org flask  
  
# Add the current directory contents into the container at /app  
ADD app.py /app  
  
# Make port available to the world outside this container  
EXPOSE 80  
  
# Run app.py when the container launches  
CMD ["python", "app.py"]  
