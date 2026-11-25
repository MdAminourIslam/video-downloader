<div align="center">

# 📥 Video Downloader

### Download YouTube & Facebook videos — beautifully simple.

**MP4** (1080p · 720p · 480p · 360p) &nbsp;·&nbsp; **MP3** (320 · 128 kbps)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange)](https://github.com/yt-dlp/yt-dlp)
[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-For%20personal%20use-lightgrey)](#-license--fair-use)

Paste a link → see the preview → pick a quality → download. That's it.

**🌐 Live demo:** `https://video-downloader.onrender.com`
*see [video-downloader](https://video-downloader-36ym.onrender.com/))*

</div>

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎬 **YouTube + Facebook** | Paste a link — the platform is detected automatically |
| 🖼️ **Live preview** | Thumbnail + title before you download (incl. Facebook Reels) |
| 🎥 **MP4 video** | 1080p / 720p / 480p / 360p |
| 🎵 **MP3 audio** | 320 / 128 kbps |
| 📊 **Download progress** | Big % number, progress bar, MB downloaded / total |
| 🌙 **Dark mode** | Follows your system, or toggle it yourself |
| 🌐 **English / বাংলা** | Switch the whole interface with one tap |
| 📱 **Mobile friendly** | Responsive design + hamburger menu on phones |
| 🎨 **Classical design** | Ivory & gold, serif typography, shield logo |

> ⚠️ **Fair use:** only download videos you own or have permission to download.

---

## 🗂️ What's inside

```
video-downloader/
├── index.html         # The website (open it in a browser)
├── server.py          # The server — FastAPI + yt-dlp (does the real downloading)
├── requirements.txt   # Python packages
├── run.bat            # Windows: double-click to run
├── run.sh             # Mac / Linux: bash run.sh
├── Dockerfile         # Docker image (ffmpeg included) — for Render
├── render.yaml        # One-click free deploy on Render
└── .gitignore         # Keeps downloads, caches & secrets out of git
```

---

## 🚀 Quick start — run on your computer

### 1. Extract the zip
Right-click `video-downloader.zip` → **Extract All**.

### 2. Install Python (3.10+)
Check first:
```bash
python --version
```
Don't have it? Download from [python.org](https://www.python.org/downloads/) — during install, tick **"Add python.exe to PATH"**.

### 3. Install ffmpeg (needed for MP3 & for joining video + audio)
```bash
winget install ffmpeg
```
Then check it:
```bash
ffmpeg -version
```
`winget` not working? Get it from [ffmpeg.org](https://ffmpeg.org/download.html) or run `choco install ffmpeg`.

### 4. Install the packages
```bash
cd video-downloader
pip install -r requirements.txt
```

### 5. Start the server
```bash
python server.py
```
Or simply double-click **`run.bat`** (Windows) / run **`bash run.sh`** (Mac/Linux).

### 6. Open the app
```
http://localhost:8000
```

### 7. Download a video
1. Paste a YouTube or Facebook video link.
2. Click **Check** — you'll see *"Server is running — ready to download"* in green.
3. Pick MP4 quality or MP3, then hit **Download**. The file lands in your Downloads folder.

**Use it from your phone (same Wi-Fi):** keep the server running on your computer, find your computer's IP with `ipconfig` (look for *IPv4 Address*, e.g. `192.168.1.5`), then open `http://192.168.1.5:8000` in your phone's browser. For use from anywhere, deploy it — see below.

---

## 🐙 Push to GitHub

Everything is already prepared (`.gitignore`, `render.yaml`, `Dockerfile`) — just push.

### Step 1 — Create an empty repo
1. Open [github.com/new](https://github.com/new).
2. **Repository name:** `video-downloader`
3. **Description:**
   ```
   Download YouTube & Facebook videos as MP4 (1080p/720p/480p/360p) or MP3 (320/128 kbps) — beautiful Bangla web app with dark mode, English/Bangla language, and classical design.
   ```
4. Choose **Public** (easiest for free deploy).
5. **Do NOT tick** "Add a README file", ".gitignore" or "license" — the repo must stay empty, this project already has its own README.
6. Click **Create repository**.

### Step 2 — Push from this folder
Replace `YOUR-USERNAME` with your real GitHub username:
```bash
cd video-downloader
git init
git add .
git commit -m "Video Downloader - YouTube + Facebook, MP4 + MP3"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/video-downloader.git
git push -u origin main
```
> First push may ask for a **Personal Access Token** instead of a password — create one at GitHub → Settings → Developer settings → Personal access tokens.

### Step 3 — Push updates later
```bash
git add .
git commit -m "Describe your change"
git push
```
If it's deployed on Render, every push auto-deploys the new version.

---

## ☁️ Deploy for free — Render

### Step 1 — Create a Render account
Open [render.com](https://render.com) and sign up **with GitHub**, then authorize it.

### Step 2 — Create the Web Service
1. Dashboard → **New + → Web Service**.
2. Choose **Build and deploy from a Git repository** → select `video-downloader` → **Connect**.
3. **Name:** `video-downloader` → your link becomes `https://video-downloader.onrender.com`
4. **Region:** Singapore *(closest to Bangladesh, so it's faster)*
5. **Branch:** `main`
6. **Runtime:** Docker — picked up automatically from `render.yaml`, nothing to change.
7. **Instance Type:** **Free**
8. Click **Create Web Service**. The first deploy takes 3–5 minutes (it builds the Docker image).

### Step 3 — Done 🎉
Open your link from anywhere — phone included. No computer needs to stay on.

> 💤 **Free-plan note:** after ~15 minutes with no visitors the server sleeps; the next visit can take 30–50 seconds to wake up. That's Render's free-plan rule, not a bug. Download one video at a time for best results.

---

## 🛠️ Tech stack

- **Frontend:** single `index.html` — HTML, CSS, vanilla JS (no build step)
- **Backend:** Python + [FastAPI](https://fastapi.tiangolo.com/) + [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Media:** [ffmpeg](https://ffmpeg.org/) for MP4 merging & MP3 conversion
- **Deploy:** [Docker](https://www.docker.com/) + [Render](https://render.com) (free plan)

### API
| Endpoint | What it does |
|---|---|
| `GET /` | Serves the website |
| `GET /health` | Returns `{"ok": true}` |
| `GET /api/info?url=` | Video title, thumbnail, duration, uploader |
| `GET /api/download?url=&type=mp4\|mp3&quality=` | Downloads the file |

The server reads the `PORT` environment variable when hosted (Render sets it) and falls back to `8000` locally.

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| *"Server is not running"* | The `python server.py` window must stay open. Run it again if it closed. |
| *`python` is not recognized* | Python wasn't added to PATH — reinstall it with the PATH tick, or try `py server.py`. |
| *`ffmpeg` not found* | Repeat step 3 above. Without ffmpeg, MP3 won't work and MP4 video+audio won't merge. |
| *Download fails* | Check the link, and try a public video first — private / login-only videos can't be downloaded. |
| *Stop the server* | Press `Ctrl + C` in the terminal. |

---

## 📜 Changelog

- **v7 — Dark mode, language, classical design, logo, hamburger menu:** dark-mode toggle, full English/বাংলা switch, ivory-red-gold classical design with serif brand, shield logo left of the title, 3-line menu on phones.
- **v6 — Facebook Reel preview fixed:** `/reel/` links are converted to `watch?v=` for the official plugin, so public Reels show their real cover; fallback card no longer clips its text.
- **v5 — Facebook cover/thumbnail fixed:** preview iframe loads immediately; thumbnails show uncropped (`object-fit: contain`) with a blurred background.
- **v4 — Facebook preview fixed:** preview box always visible; official Facebook video plugin loads the real preview without a server.
- **v3 — Clean download page + % progress:** setup section moved out of the site, separate "How to download" page, big % + progress bar + MB downloaded/total.
- **v2 — Redesign:** responsive, mobile-friendly, one-page guide, ready for GitHub.
- **v1 — First release:** YouTube + Facebook, MP4 + MP3, local Python server.

---

## 📄 License & fair use

Built for personal use — download only your own videos or videos you have permission to download. YouTube and Facebook are trademarks of their respective owners.

<div align="center">

Made with ❤️ — paste a link, pick a quality, download.

</div>
