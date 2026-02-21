# 1. Use the specific Python version you have been using
FROM python:3.11

# 2. Hugging Face requires a special non-root user for security
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 3. Set the working folder inside the container
WORKDIR /app

# 4. Copy your requirements and install them
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 5. Copy the rest of your Django project files
COPY --chown=user . /app

# 6. Expose the specific port Hugging Face listens to
EXPOSE 7860

# 7. The command to start your Django server!
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:7860"]