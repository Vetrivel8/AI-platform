# AI Platform - Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (optional)

## Installation & Running

### Option 1: Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

Backend runs on: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

Frontend runs on: `http://localhost:3000`

### Option 2: Docker Compose

```bash
docker-compose up
```

This will start:
- Backend on `http://localhost:8000`
- Frontend on `http://localhost:3000`

## Available Endpoints

### Health Check
- `GET /health` - Check if API is running

### Models
- `GET /models` - List available models
- `POST /predict` - Make predictions
- `POST /upload-model` - Upload a new model

### Request Example
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"input_text": "Hello", "model_name": "default"}'
```

## Project Structure
```
AI-platform/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── config.py         # Configuration
│   ├── requirements.txt   # Python dependencies
│   └── .env.example      # Environment variables template
├── frontend/
│   ├── App.jsx           # React main component
│   ├── App.css           # Styling
│   ├── package.json      # Node dependencies
│   └── Dockerfile        # Frontend container
├── models/               # Model storage
├── Dockerfile            # Backend container
├── docker-compose.yml    # Docker composition
└── README.md            # Documentation
```

## Environment Variables
Copy `.env.example` to `.env` and update as needed:
```
DEBUG=True
HOST=0.0.0.0
PORT=8000
WORKERS=4
DATABASE_URL=sqlite:///./test.db
MODEL_PATH=./models
```

## Next Steps
1. Add your AI models to the `/models` directory
2. Customize the prediction logic in `backend/main.py`
3. Extend the React frontend components
4. Add authentication/authorization as needed
5. Set up database models for persistence

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### Module Not Found
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

### CORS Issues
CORS is already configured in `main.py`. Adjust allowed origins as needed.
