FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py /app/
COPY test_hello_world.py /app/

# Install Python dependencies
RUN pip install flask selenium webdriver-manager

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH=$CHROME_BIN:$PATH

# Run Flask app in background and test
CMD flask run --host=0.0.0.0 --port=5000 & \
    sleep 5 && \
    python test_hello_world.py
