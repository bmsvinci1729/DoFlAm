# Use an official Python base image
FROM public.ecr.aws/lambda/python:3.12

# Set a working directory inside the container
WORKDIR /app

# Copy everything from current directory into /app
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Expose the port your Flask app runs on
EXPOSE 5000

# Run the Flask app
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

COPY . ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
