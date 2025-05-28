FROM python:3.13.3-slim

# Create app user and group
RUN groupadd --gid 1000 app && \
    useradd --create-home --gid 1000 --uid 1000 app


# Set working directory
WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change the ownership to the app user
RUN chown -R app:app /app

# Switch to the non-root app user
USER app

# Copy the application code
COPY . .

# Expose port used by the application
EXPOSE 5000

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
