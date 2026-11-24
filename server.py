"""
Video Downloader Server — YouTube + Facebook
MP4 video (1080p/720p/480p/360p) + MP3 audio
Run:  pip install fastapi uvicorn yt-dlp   then   python server.py
Needs: Python 3.10+ and ffmpeg
Open: http://localhost:8000
"""
import os, tempfile, uuid
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import yt_dlp

app = FastAPI(title="Video Downloader")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

TMP = tempfile.mkdtemp(prefix="vdl_")
BASE = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def home():
    idx = os.path.join(BASE, "index.html")
    if os.path.exists(idx):
        return FileResponse(idx, media_type="text/html")
    return {"ok": True, "msg": "Put index.html next to server.py"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/api/info")
def info(url: str = Query(...)):
    try:
        with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
            d = ydl.extract_info(url, download=False)
    except Exception as e:
        raise HTTPException(400, str(e))
    return {"title": d.get("title"), "thumbnail": d.get("thumbnail"),
            "duration": d.get("duration"), "uploader": d.get("uploader")}

@app.get("/api/download")
def download(url: str = Query(...), type: str = Query("mp4"),
             quality: str = Query("720")):
    job = os.path.join(TMP, uuid.uuid4().hex)
    os.makedirs(job, exist_ok=True)
    if type == "mp3":
        opts = {"format": "bestaudio/best", "outtmpl": job + "/audio.%(ext)s",
                "postprocessors": [{"key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": quality}]}
        ext = "mp3"
    else:
        h = quality
        opts = {"format": (f"bv*[height<={h}][ext=mp4]+ba[ext=m4a]/"
                           f"b[height<={h}][ext=mp4]/b[height<={h}]/b"),
                "merge_output_format": "mp4",
                "outtmpl": job + "/video.%(ext)s"}
        ext = "mp4"
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            d = ydl.extract_info(url, download=True)
            title = (d.get("title") or "video").strip()
    except Exception as e:
        raise HTTPException(400, str(e))
    files = [f for f in os.listdir(job) if f.endswith("." + ext)]
    if not files:
        raise HTTPException(500, "File তৈরি হয়নি")
    safe = "".join(c for c in title if c.isalnum() or c in " -_")[:80] or "video"
    return FileResponse(os.path.join(job, files[0]),
                        filename=f"{safe}.{ext}",
                        media_type="audio/mpeg" if ext == "mp3" else "video/mp4")

if __name__ == "__main__":
    import uvicorn
    # Hosting platforms (e.g. Render) provide the port via the PORT
    # environment variable; fall back to 8000 for local use.
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
