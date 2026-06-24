# Grammar Assistant Chrome Extension

This is a Chrome extension project I built to help fix grammar and improve writing without needing to open AI every time.

The extension opens in a side panel on the right side of Chrome.  
I can paste text into it, choose a tone like **formal** or **casual**, and it sends the text to my FastAPI backend.  
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

I wanted a faster way to fix grammar while working in apps like Slack and Outlook.  
Instead of going back and forth to AI, typing my promt each time, I wanted a small writing assistant that stays inside the browser.

This is the first version of the project.  
Right now the user still has to copy and paste text into the extension, but later I want to improve it so it can read text directly from the page and maybe even replace it automatically.

---
## What I Learned

- **Chrome Extension Development** - Manifest V3, service workers, side panels, and content scripts
- **Cross-Origin Communication** - messaging between extension and backend API
- **API Integration** - Working with third-party APIs (Gemini) and handling authentication
- **Environment Variables & Secrets Management** - Safely storing API keys
- **FastAPI Backend Design** - Building endpoints to support frontend features
- **CORS & Browser Security** - Understanding browser security policies and proper configuration
- **User Experience (UX)** - Designing intuitive interfaces for productivity tools
- **Asynchronous Programming** - Handling async API calls and loading states
- **State Management** - Managing user input and API responses in the extension
- **Problem-Solving Mindset** - Identifying real workflow problems and building practical solutions


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

## Project Structure

```bash
grammar-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── gemni_services.py
│   │   └── model.py
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