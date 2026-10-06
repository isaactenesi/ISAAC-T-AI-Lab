# ISAAC-T // AI LAB
### Offline Private AI Lab — Built in Harare, Zimbabwe

> Your own ChatGPT that runs 100% offline. No API keys. No cloud.

### Features
- ChatGPT-like UI (Dark, premium, mobile responsive)
- 100% Offline LLM (Ollama + llama3.2:3b)
- Chat with PDFs - Upload reports/books and ask questions
- Private & Secure - No data sent to OpenAI/Google
- Fast - Runs on 8GB RAM laptops

### Quick Start
~/ai-lab/start.sh
Open http://localhost:8080

### Architecture
Browser -> FastAPI (app.py) -> Ollama API (11434) -> llama3.2:3b

### Install From Scratch
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
mkdir ~/ai-lab && cd ~/ai-lab
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn httpx pypdf python-multipart

### Project Structure
app.py - Main app + UI
start.sh - One-click launcher
README.md - Documentation
venv/ - Environment

### Author
Isaac T. - ISAAC-T AI Lab - Harare, Zimbabwe - May 2026
MIT License - Offline Intelligence.
