This project includes:

1.FastAPI backend (hosted at http://localhost:9000)
2.Streamlit frontend (hosted at http://localhost:8501)
3..env file for secrets like the OpenAI API key
4.requirements.txt for dependency management
5.Docker support for both frontend and backend





Local Development Setup
1. Clone the Repo
git clone https://github.com/Deepanshu12344/chat-summarization-API.git
cd chat-summarization-API

2. Create a .env File
Create a .env file in the root (if not already present):
OPENAI_API_KEY=your_openai_api_key_here

3. Create Virtual Environment and Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

4. Run the FastAPI Backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 9000

5. Run the Streamlit Frontend
Open a new terminal:
streamlit run streamlit_app.py





Dockerized Setup

1. Dockerfile
Here's your updated Dockerfile supporting both FastAPI and Streamlit:
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose both ports
EXPOSE 9000
EXPOSE 8501

CMD ["bash", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 9000 & streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0"]

2. Create .env (if secrets required)
Add .env in .dockerignore to prevent pushing secrets.

3. Build the Docker Image
docker build -t deepanshu091224/chat_api:0.0.1.RELEASE .

4. Run the Docker Container
docker run -p 9000:9000 -p 8501:8501 --env-file .env deepanshu091224/chat_api:0.0.1.RELEASE

5. Push to Docker Hub
Make sure you're logged in:
docker login
docker push deepanshu091224/chat_api:0.0.1.RELEASE



Testing APIs
Use Postman or curl to test:

POST /chats

POST /chats/summarize

POST /chats/analyze

GET /chats/{conversation_id}



Directory Structure
chat-summarization-API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── llm_utils.py
├── streamlit_app.py
├── requirements.txt
├── .env
├── Dockerfile
└── README.md