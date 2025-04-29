FROM python:3.13.3-slim

# Create app user and group
RUN groupadd --gid 1000 app && \
    useradd --create-home --gid 1000 --uid 1000 app

# Create project directory in the container 
RUN mkdir -p /home/app/src

# Set working directory
WORKDIR /home/app/src

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Change the ownership to the app user
RUN chown -R app:app /home/app/src

# Switch to the non-root app user
USER app

# Expose port used by the application
EXPOSE 5000

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
