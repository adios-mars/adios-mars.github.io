# Ruth Yeneneh — Software Engineering Portfolio

This project is a modern, high-performance portfolio for **Ruth Yeneneh** ([@adios-mars](https://github.com/adios-mars)), a Software Engineering student pursuing her Bachelor's degree in Addis Ababa, Ethiopia.

Built with a clean dark theme, golden amber accents (`#FFDB70`), smooth tab transitions, and dynamic project filtering.

## 🚀 Key Features

1. **Sidebar Profile (`data-sidebar`)**:
   - Official avatar from GitHub (`https://avatars.githubusercontent.com/u/250560417?v=4`).
   - Title: **Software Engineering Student**.
   - Contact links: Email (`adiosruthe@gmail.com`), GitHub (`@adios-mars`), LinkedIn (`@ruth-yeneneh`), Location (`Addis Ababa, Ethiopia`).
   - Collapsible contact menu for mobile screens.

2. **About Me (`data-page="about"`)**:
   - Bio detailing Ruth's journey as a Software Engineering student building practical systems, voice AI agents, mobile tools, and full-stack web applications.
   - Core specialization pillars: Systems & Networking, Web & Microservices, Mobile Engineering, and Voice AI & Automation.
   - Core technology pills.

3. **Resume (`data-page="resume"`)**:
   - Education: B.Sc. in Software Engineering (Currently Pursuing Bachelor's Degree) + Self-Directed Technical Labs.
   - Projects & Experience: Open-Source Student Developer, AI Voice Assistant & Systems Engineering, Backend & Bot Development Labs.
   - Technical Skill Progress Bars: React 19 / Next.js, Flutter & Dart, Systems C / POSIX, Tailwind CSS v4, Python / Asyncio, Cloud Databases.

4. **Projects (`data-page="projects"`)**:
   - Filter categories: **All**, **Mobile**, **Web Development**, **Systems**.
   - Real GitHub repositories:
     - **Taxi Ale (ታክሲ አለ)** — Real-Time Minibus Transit Tracking (Flutter & OSM).
     - **Addis Market Tracker** — Staple food commodity price comparison platform & Telegram Mini App (FastAPI, SQLite, Jinja2).
     - **Veda — AI Voice Assistant** — Low-latency voice assistant with WebRTC VAD, Deepgram STT, and LLM failover.
     - **Katch** — Collaborative Reading Tracker & Social Bookshelf (React 19, Supabase).
     - **Multi-User Chat System** — Concurrent Client-Server in C with POSIX threads & raw Berkeley TCP sockets.
     - **Campus Attendance Bot** — Telegram Attendance Tracking System (Python, Aiogram 3, SQLite).

5. **Blog / Technical Notes (`data-page="blog"`)**:
   - Technical write-ups covering Taxi Ale's zero-cost OSM routing, C multi-threaded socket servers, Addis Market commodity pricing, and Veda voice AI architecture.

6. **Contact (`data-page="contact"`)**:
   - Google Maps iframe centered on Addis Ababa, Ethiopia with custom dark theme filter.
   - Active form submission endpoint using FormSubmit (`https://formsubmit.co/adiosruthe@gmail.com`).

---

## 💻 How to Run Locally in VS Code Terminal

Open your VS Code terminal (`Ctrl + ~`) in the project folder and run:

```bash
# Using Python
python3 -m http.server 3000

# Or using Node.js / npx
npx serve .
```

Then open your browser at [http://localhost:3000](http://localhost:3000).
