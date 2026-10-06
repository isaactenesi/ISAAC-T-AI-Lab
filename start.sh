#!/bin/bash
cd ~/ai-lab
source venv/bin/activate
ollama serve > /dev/null 2>&1 &
sleep 2
uvicorn app:app --host 0.0.0.0 --port 8080
