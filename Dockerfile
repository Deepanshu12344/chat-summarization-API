FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install supervisor
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

# Copy your application
COPY . .

# Copy supervisor config
COPY supervisord.conf /etc/supervisord.conf

# Expose both FastAPI and Streamlit ports
EXPOSE 9000 8501

# Run both apps using supervisor
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
