# 🦋 Project Butterfly AI

Project Butterfly AI is a personal growth assistant designed to help individuals transition toward their dream goals — starting with my own journey from Site Reliability Engineer (SRE) to AI Engineer in 5 months.

Every day, the bot sends a motivational question via Telegram to encourage reflection, focus, and deliberate action, building momentum one day at a time.

---

## ✨ What This Project Is About

- **Build consistent habits** through daily AI-powered coaching prompts
- **Practice critical AI Engineer skills** including Python automation, CI/CD pipelines, and cloud-native thinking
- **Grow this MVP into a fully-fledged AI agent** for personal and professional development

---

## 🛠️ Tech Stack and AI Engineering Skills Practiced

| Area | Tech Used |
|:---|:---|
| Programming Language | Python 3.11 |
| API Integration | Telegram Bot API |
| Automation | GitHub Actions (cron jobs + push-triggered builds) |
| Secrets Management | GitHub Actions Secrets |
| Software Design | Modular architecture (separating logic and data) |
| Containerization | Docker + GitHub Container Registry (GHCR) |
| Deployment Strategy | Serverless, event-driven scheduling |
| Versioning | Semantic Versioning: `v1.1.3` + test builds as `test-v1.1.3.1` |
| Future Expansion | FastAPI backend, PostgreSQL database, OpenAI/Hugging Face APIs |

---

## 🔁 Iterations and Thought Process

This project was intentionally built through **progressive iterations**, simulating real-world AI engineering workflows:

1. **Phase 0 - Idea and MVP**
   - Start with a minimal Telegram bot using pure Python
   - Manually send a daily question using a hardcoded string

2. **Phase 1 - CI/CD Automation**
   - Migrate to GitHub Actions with scheduled cron jobs
   - Automatically run the bot daily without human intervention

3. **Phase 2 - Data Decoupling**
   - Move daily questions into a separate `questions.txt` file
   - Prepare the system for scalability and easier updates

4. **Phase 3 - Smart Progression**
   - Switch from random questions to **rotating structured questions**
   - Build a daily learning and habit stack aligned with career growth

5. **Phase 4 - Containerized & Versioned CI/CD**
   - Auto-publish production builds to GHCR as `vX.Y.Z`
   - Auto-publish dev/test builds as `test-vX.Y.Z.N` for traceability
   - Enable manual and push-based triggers for full control

6. **Planned Phase 5 and Beyond**
   - Record user answers and analyze growth patterns
   - Introduce lightweight database storage (PostgreSQL or Supabase)
   - Add NLP features for dynamic, personalized coaching
   - Deploy a backend API (FastAPI) for future expansion

---

## 📦 Docker Image Versions on GHCR

| Type | Tag Pattern | Example Pull |
|------|-------------|---------------|
| 🚀 Production | `vX.Y.Z` | `docker pull ghcr.io/pl2134/project-butterfly-ai:v1.1.3` |
| 🧪 Dev Test | `test-vX.Y.Z.N` | `docker pull ghcr.io/pl2134/project-butterfly-ai:test-v1.1.3.2` |

Pull the latest images:

```bash
# Latest release version
docker pull ghcr.io/pl2134/project-butterfly-ai:latest

# Latest test version (after v1.1.3)
docker pull ghcr.io/pl2134/project-butterfly-ai:test-v1.1.3.2
```

Badges:

[![GHCR Release](https://img.shields.io/badge/GHCR-v1.x.x-blue?logo=docker)](https://github.com/users/PL2134/packages/container/project-butterfly-ai)
[![GHCR Dev](https://img.shields.io/badge/GHCR-test--v1.x.x.x-yellow?logo=docker)](https://github.com/users/PL2134/packages/container/project-butterfly-ai)

---

## 📈 Why This Matters for My Career Transition

Project Butterfly AI is more than just a side project — it is **a live demonstration of applied AI Engineer skills**, including:

- Automating workflows and tasks
- Thinking modularly for scalable system design
- Integrating APIs effectively
- Using cloud-native CI/CD tools
- Building iterative, real-world AI-powered products

---

## 🚀 How To Run It Yourself

1. Create your own Telegram Bot through [BotFather](https://t.me/botfather)
2. Set two GitHub Secrets in your repository:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
3. Push your Python script and GitHub Action workflow
4. Enable GitHub Packages permissions for GHCR pushes
5. Watch as your daily coaching begins — automatically!

---

## 🦋 Final Note

_"Big transformations happen one small action at a time."_  
Project Butterfly AI is my commitment to continuous, daily, deliberate growth — and my first public step toward becoming a full-fledged AI Engineer.

---
