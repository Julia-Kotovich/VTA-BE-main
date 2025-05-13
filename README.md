# Virtual Teaching Assistant (VTA) Backend

A Django-based backend service for a Virtual Teaching Assistant that provides intelligent responses to questions about the Capstone project course. The system uses BERT-based question answering to provide accurate and contextually relevant responses.

## Author
**Julia Kotovich**

## Project Overview
This project implements a question-answering system that:
- Processes natural language questions about the Capstone project
- Provides relevant answers using a fine-tuned BERT model
- Collects user feedback and ratings for responses
- Maintains a history of interactions

## Technical Stack
- Python 3.10+
- Django 5.0.4
- Hugging Face Transformers (BERT)
- Poetry for dependency management
- SQLite database

## Prerequisites
- Python 3.10 or higher
- Poetry (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone git@github.com:Julia-Kotovich/VTA-BE-main.git
cd VTA-BE-main
```
2. need to add model from the local machine + 2 files (gc-api-keys.json and .env)
```bash 
scp -r /Users/juliakotovich/Projects/VTA-BE-main/VTA-tools/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf julia@5.1.100.213:~/VTA-BE-main/VTA-tools/models/
scp -r /Users/juliakotovich/Projects/VTA-BE-main/gc-api-keys.json julia@5.1.100.213:~/VTA-BE-main
scp -r /Users/juliakotovich/Projects/VTA-BE-main/.env julia@5.1.100.213:~/VTA-BE-main
```

3. Install Poetry and dependencies:
```bash
sudo apt install python3-poetry
poetry install
```

3. Download the pre-trained model

4. Set up the database:
```bash
poetry run python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
poetry run python manage.py createsuperuser
```

## Running the Application

1. Activate the Poetry environment:
```bash
poetry shell
```

2. Start the Django server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000) (locally) or [http://5.1.100.213:8000](http://5.1.100.213:8000) (on the server).

## API Endpoints

### Question Answering
```http
POST /api/vta-answer/
Content-Type: application/json

{
    "query": "What is a design tool used for?"
}
```

### Response Feedback
```http
POST /api/vta/feedback/
Content-Type: application/json

{
    "userFeedback": "I like the model",
    "userId": "user-uuid"
}
```

### Like/Dislike Response
```http
GET /api/vta/like/
GET /api/vta/dislike/

Parameters:
- VTAText: The response text
- userId: User identifier
- likeStatus: Boolean indicating like/dislike
```

## Project Structure
```
VTA-BE-main/
├── api/                 # Main application code
├── QA_VTA/              # Question answering implementation
├── VTA_Backend/         # Django project settings
├── vta_qa_model/        # Model and training data
│   ├── model/           # BERT model files
│   └── training/        # Training datasets
├── VTA-tools/           # Utility scripts
├── manage.py            # Django management script
├── poetry.lock          # Poetry lock file
├── pyproject.toml       # Poetry project configuration
└── requirements.txt     # Python dependencies (for reference)
```

## Development
- The project uses Poetry for dependency management
- Code formatting follows PEP 8 guidelines
- Database migrations are handled through Django's migration system

## Notes
- The repository does not include the fine-tuned model due to its size
- Make sure to keep your API keys and tokens secure
- The system requires the BERT model to be properly placed in the `vta_qa_model/model/` directory

## License
[Your License Here]

All [Endpoints](http://127.0.0.1:8000/api/routes/)