from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx
app = FastAPI()

HTML = """
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Isaac-T Lab</title>
<style>
*{box-sizing:border-box} body{margin:0;font-family:Inter,system-ui;background:radial-gradient(1200px 600px at 10% -10%,#1e3a8a22,transparent),#0a0c10;color:#e7e7ea;display:flex;flex-direction:column;height:100vh}
header{padding:18px 22px;border-bottom:1px solid #1e222e;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:800;letter-spacing:.5px} .dot{width:8px;height:8px;background:#22c55e;border-radius:50%;display:inline-block;margin-right:6px;box-shadow:0 0 12px #22c55e}
#chat{flex:1;overflow-y:auto;padding:24px;max-width:800px;width:100%;margin:0 auto}
.msg{padding:14px 18px;border-radius:18px;margin:12px 0;line-height:1.5;max-width:85%;animation:pop .2s ease}
.user{background:linear-gradient(135deg,#2a5bd7,#4f7eff);margin-left:auto;border-bottom-right-radius:6px}
.bot{background:#171a23;border:1px solid #242938;border-bottom-left-radius:6px}
.bar{padding:16px;max-width:800px;width:100%;margin:0 auto;display:flex;gap:10px}
input{flex:1;padding:14px 18px;border-radius:24px;border:1px solid #242938;background:#12141b;color:white;outline:none;font-size:15px}
input:focus{border-color:#2a5bd7} button{padding:14px 22px;border-radius:24px;border:0;background:#2a5bd7;color:white;font-weight:600;cursor:pointer}
@keyframes pop{from{transform:translateY(6px);opacity:0}to{transform:translateY(0);opacity:1}}
small{color:#6b7280}
</style></head><body>
<header><div class=logo><span class=dot></span>ISAAC-T // AI LAB</div><small>llama3.2:3b - offline</small></header>
<div id=chat></div>
<div class=bar><input id=q placeholder="Ask anything..."><button onclick=send()>Send</button></div>
<script>
const chat=document.getElementById('chat');const q=document.getElementById('q');
q.addEventListener('keydown',e=>{if(e.key==='Enter')send()});
async function send(){
 if(!q.value.trim()) return;
 let p=q.value; q.value='';
 chat.innerHTML+=`<div class="msg user">${p}</div>`;
 let tmpId='tmp'+Date.now(); chat.innerHTML+=`<div class="msg bot" id="${tmpId}">... thinking</div>`; chat.scrollTop=chat.scrollHeight;
 let r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:p})});
 let d=await r.json();
 document.getElementById(tmpId).innerHTML=d.response.replace(/\\n/g,'<br>');
 chat.scrollTop=chat.scrollHeight;
}
</script></body></html>
"""

@app.get("/")
def home(): return HTMLResponse(HTML)

@app.post("/api/chat")
async def chat(body: dict):
    system = "You are Isaac-T AI Lab assistant. Built by Isaac T in Harare, Zimbabwe. Offline, private, helpful. Help with coding, AI, study, business. Never say you are MIT. If asked who you are, say: I am Isaac-T AI Lab - Offline AI built by Isaac T."
    user_prompt = body.get("prompt","")
    full_prompt = system + "\n\nUser: " + user_prompt + "\nAssistant:"
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post("http://127.0.0.1:11434/api/generate", json={"model":"llama3.2:3b","prompt":full_prompt,"stream":False})
        return {"response": r.json().get("response","")}
