# Grammar Assistant Chrome Extension

This is a Chrome extension project I built to help fix grammar and improve writing without needing to open AI every time.

The extension opens in a side panel on the right side of Chrome.  
I can paste text into it, choose a tone like **Formal** or **Casual**, and it sends the text to my FastAPI backend.  
The backend then calls the **Gemini API** and returns the improved version of the text.

After that, I can copy the result and paste it back into Slack, Outlook, or wherever I need it.

---

## What this project does

- Opens as a Chrome side panel
- Lets the user paste text into the extension
- Sends the text to a FastAPI backend
- Uses Gemini to fix grammar and improve clarity
- Has tone options:
  - Formal
  - Casual
  - Regenerate by clicking again
- Lets the user copy the generated result

---

## Why I built it

I wanted a faster way to fix grammar while working in apps like Slack and Outlook. Instead of constantly switching tabs and writing prompts, I wanted a lightweight writing assistant that stays inside the browser.

This is the first version of the project. Right now the user still has to copy and paste text into the extension, but later I plan to improve it so it can read selected text directly from the page and possibly replace it automatically.

---

## What I Learned

- **Chrome Extension Development** - Manifest V3, service workers, side panels, and content scripts
- **Cross-Origin Communication** - Messaging between the extension and backend API
- **API Integration** - Working with the Gemini API and handling authentication
- **Environment Variables & Secrets Management** - Safely storing API keys
- **FastAPI Backend Design** - Building REST endpoints to support frontend features
- **CORS & Browser Security** - Understanding browser security policies and proper configuration
- **User Experience (UX)** - Designing intuitive interfaces for productivity tools
- **Asynchronous Programming** - Handling async API calls and loading states
- **State Management** - Managing user input and API responses
- **Problem Solving** - Identifying a real workflow problem and building a practical solution

---

## Tech Stack

### Frontend / Extension

- Chrome Extension
- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn
- Gemini API
- python-dotenv

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.10+
- Google Chrome
- A Gemini API key

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/abenezer-gizaw/GRAMMAR-ASSISTANT.git
cd grammar-assistant
```

### 2. Create and activate a virtual environment

**macOS/Linux**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend/app` directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Backend

From the `backend` directory, start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

---

## Loading the Chrome Extension

1. Open **Google Chrome**.
2. Navigate to:

```
chrome://extensions
```

3. Enable **Developer Mode**.
4. Click **Load unpacked**.
5. Select the `extension` folder.
6. Pin the extension to the Chrome toolbar.
7. Open the side panel and start using the extension.

> **Note:** Make sure the FastAPI backend is running before using the extension.

---

## Project Structure

```text
grammar-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── gemini_services.py
│   │   ├── model.py
│   │   └── .env
│   │
│   ├── requirements.txt
│   └── venv/
│
├── extension/
│   ├── manifest.json
│   ├── service-worker.js
│   ├── sidepanel.html
│   ├── sidepanel.css
│   └── sidepanel.js
│
└── README.md
```

---

## Future Improvements

- Auto-detect selected text from webpages
- Replace selected text directly in supported websites
- Add additional writing tones
- Support multiple AI providers
- Maintain writing history
- Add user-configurable settings

---