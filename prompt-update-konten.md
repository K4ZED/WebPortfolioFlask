# Update konten homepage sesuai CV terbaru

Update `templates/index.html` (desain baru yang sudah jadi). **Jangan ubah desain, CSS, animasi, route atau deploy config.** Yang diganti hanya isi teks dan data. Copy di website tetap bahasa Inggris, singkat, natural, dan tanpa em dash (—).

Sebelum mulai, salin `CV-Kenza-Athallah-Nandana-Wijaya.pdf` ke `static/cv/` dan arahkan link "Download CV" ke file itu. CV lama tetap disimpan.

---

## 1. Hero

- Role lines (4 baris): `AI Specialist`, `Systems Engineer`, `Fullstack Dev`, `Data Analyst`
- Description: "AI Specialist and Systems Engineer from Surakarta. I build AI tools and automations that take manual work off people's hands, backed by a background in data."

## 2. Marquee

AI Automation, RAG & LLM, Fullstack Development, Machine Learning, Data Analysis

## 3. About

- Heading: "Building AI that does the boring work."
- Body: "I'm a Data Science student at Universitas Sebelas Maret who works on AI tools, fullstack apps and data. Right now I run internal AI infrastructure at Dzakiyah Store Group, build web apps for clients, and keep shipping side projects around LLMs and automation."
- Daftar bernomor jadi **5 item** (pengalaman), format judul lalu satu baris keterangan:
  1. AI Specialist: Dzakiyah Store Group. 2026 to present. Runs internal AI tools and builds AI-driven workflow automation.
  2. Fullstack Engineer (Freelance): 2022 to present. 8+ web apps for clients, from database schema to REST API.
  3. Retail Data Analyst Intern: Amigo Group. Feb 2026 to Jul 2026. Reports and dashboards for sales and operations.
  4. Coordinator of Technology: P!NGFEST UNS. Mar 2024 to Oct 2024. Led the team behind registration, e-tickets and real-time visitor info.
  5. Telecom Data Analyst Intern: Telkom Landmark Surabaya. Jun 2022 to Nov 2022. BTS performance analysis for East Java and Madura.

## 4. Projects

- Label kanan: `12 / Projects`
- Ganti array project dengan 12 item di bawah (urutan sesuai daftar). Format: name / category / tech / tag / blurb / link.
- Tag `In Progress` tampil dengan warna muted, bukan accent.
- Grid 2 kolom yang ada tetap dipakai. Kalau terlalu panjang, tampilkan 6 dulu dan tambahkan tombol "Show all projects" yang membuka sisanya dengan animasi fade-up yang sama.

1. Eko / AI, RAG / Python, OpenAI & Gemini API, ChromaDB / Live Bot / Telegram bot that answers questions about Central Java's economy in plain language, grounded in official BPS data across 12 topics. / https://t.me/Eko_BPSbot
2. Podclip / AI, Video / Python, LLM, Computer Vision / Personal Tool / Turns long YouTube podcasts and live streams into vertical short clips, with auto moment picking, smart reframing and subtitles. / none
3. Agent HQ / AI Automation / Claude Code, Web UI / Personal Tool / A home-server setup where a head AI agent takes coding tasks I send from my phone or iPad and works on them in the background. / none
4. Batik Manekin Studio / Generative AI / Gemini / Client Tool / Generates store catalog photos by dressing mannequin shots in uploaded batik and placing them on generated backgrounds. / none
5. Geniuz / Fullstack / Next.js, TypeScript, Python / Team of 6 / Online tutoring platform. I handled the backend: admin auth, class management and student progress tracking. / none
6. Gym Management PWA / Fullstack / Next.js, Supabase / PWA / Member and admin apps with QR check-in, class and trainer booking, memberships and payments. / none
7. AI Skill Mapping / NLP Research / IndoBERT, LLM / In Progress / My thesis: mapping AI skills in Indonesian job postings scraped from JobStreet, Glints and Kalibrr, comparing IndoBERT with LLMs. / none
8. Dengue Severity Prediction / Bioinformatics, ML / Python, Scikit-learn / Research / Predicting dengue severity from blood RNA expression data. / none
9. Paddy Field Mapping / Geospatial / Google Earth Engine / Research / Land-cover classification and spatial analysis of rice fields in Boyolali, Klaten and Sukoharjo. / none
10. Social Media Sentiment / NLP, Deep Learning / Python, Scraping / Analysis / Scraped comments from X, Instagram and YouTube and built a 3-class sentiment model to measure public opinion. / none
11. Java Route Finder / Web App / Maps, Routing / In Progress / A personal maps app with fastest, safest, mountain and non-mountain route modes. / none
12. ML with Flask / Machine Learning, Web / Scikit-learn, Jinja2 / Best Project Award / A machine learning model served through a Flask web app. / https://waows-6-ken-day2.vercel.app/

## 5. Impact

Stats: `5+` Years in tech · `8+` Client web apps · `12` Projects built · `3` Best Project Awards

## 6. Clients

Tidak berubah.

## 7. Contact

- Heading: "Got a workflow that should run itself?"
- Body: "I'm open to AI, automation and fullstack work. Send me a message and I'll get back to you."
- Email, GitHub, LinkedIn tetap. "Download CV" mengarah ke CV baru.

---

Setelah selesai: jalankan app secara lokal, cek section Projects (desktop dan 360px), pastikan tidak ada teks yang overflow, lalu tunjukkan ringkasan perubahan. Jangan commit sebelum aku cek.
