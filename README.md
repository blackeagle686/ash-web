# Ashborn Web

Ashborn Web is a modern, high-performance landing page and backend for the Ashborn AI Agent. Built with FastAPI and a modular architecture, it provides a seamless experience for users to learn about, download, and interact with the Ashborn ecosystem.

## Features

- **Dynamic Landing Page**: Responsive UI with a premium aesthetic and glassmorphism design.
- **Modular Backend**: Clean separation of concerns using FastAPI APIRouter.
- **Authentication**: Integrated mock login and registration system.
- **Automated Downloads**: Secure endpoint for downloading the latest Ashborn IDE bundles.
- **Real-time Stats**: API endpoints providing live project metrics.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Templating**: Jinja2
- **Frontend**: Vanilla CSS, HTML5, JavaScript
- **Server**: Uvicorn

## Project Structure

The project follows a modular backend architecture to ensure scalability and maintainability:

```text
ash-web/
├── app.py              # Main entry point
├── backend/            # Modular backend logic
│   ├── api/            # API endpoints (Auth, System, Stats)
│   └── pages.py        # Route handlers for HTML pages
├── static/             # Static assets (CSS, JS, Images)
├── templates/          # Jinja2 templates
└── requirements.txt    # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/blackeagle686/ash-web.git
   cd ash-web
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server with auto-reload enabled:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:3000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Mohammed Alaa**
- [GitHub](https://github.com/blackeagle686)
- [LinkedIn](https://www.linkedin.com/in/mohammed-alaa-670867254/)
- [Phoenix AI Framework](https://darklord6861.pythonanywhere.com/en/)
