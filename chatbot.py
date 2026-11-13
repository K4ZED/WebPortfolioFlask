import re
import random
from difflib import SequenceMatcher

# ─────────────────────────────────────────────────────────────────────────────
# PROFILE: every fact Byte knows about Kenza lives here.
# Update this dict and every answer follows. Source of truth: the homepage
# (templates/index.html) first, then the CV (static/cv/CV-Kenza-Athallah-Nandana-Wijaya.pdf).
# Byte answers in Kenza's voice (first person). No em dashes, no emoji.
# ─────────────────────────────────────────────────────────────────────────────
PROFILE = {
    "name": "Kenza Athallah Nandana Wijaya",
    "nickname": "Kazed",
    "title": "AI Specialist & Systems Engineer",
    "location": "Surakarta",
    "in_tech_since": 2020,
    "summary": {
        "id": "Aku bikin tools AI dan otomatisasi yang ngambil alih kerjaan manual, dengan latar belakang di data.",
        "en": "I build AI tools and automations that take manual work off people's hands, backed by a background in data.",
    },
    "experience": [
        {
            "key": "dzakiyah",
            "role": "AI Specialist",
            "org": "Dzakiyah Store Group",
            "period": {"id": "2026 sampai sekarang", "en": "2026 to present"},
            "detail": {
                "id": "Aku mengelola dan mengoptimalkan tools AI internal, membangun otomatisasi alur kerja berbasis AI untuk memangkas proses manual, dan menguji tools AI terbaru sesuai kebutuhan bisnis.",
                "en": "I run and tune the internal AI tools, build AI-driven workflow automation that cuts manual processes, and test new AI tools against what the business needs.",
            },
        },
        {
            "key": "freelance",
            "role": "Fullstack Engineer",
            "org": None,  # freelance
            "period": {"id": "2022 sampai sekarang", "en": "2022 to present"},
            "detail": {
                "id": "Aku sudah membangun 8+ aplikasi web untuk klien, dari skema database sampai REST API, pakai Node.js, React.js, PHP dan Laravel.",
                "en": "I've shipped 8+ web apps for clients, from database schema to REST API, using Node.js, React.js, PHP and Laravel.",
            },
        },
        {
            "key": "amigo",
            "role": "Retail Data Analyst Intern",
            "org": "Amigo Group",
            "period": {"id": "Feb 2026 sampai Jul 2026", "en": "Feb 2026 to Jul 2026"},
            "detail": {
                "id": "Aku mengolah data bisnis ritel dan membuat laporan serta dashboard untuk penjualan dan operasional.",
                "en": "I worked with retail business data and built reports and dashboards for sales and operations.",
            },
        },
        {
            "key": "pingfest",
            "role": "Coordinator of Technology",
            "org": "P!NGFEST UNS",
            "period": {"id": "Mar 2024 sampai Okt 2024", "en": "Mar 2024 to Oct 2024"},
            "detail": {
                "id": "Aku memimpin tim di balik pendaftaran online, e-ticket dan info pengunjung real-time, sekaligus menjaga server tetap stabil saat traffic memuncak di masa pendaftaran dan penjualan tiket.",
                "en": "I led the team behind online registration, e-tickets and real-time visitor info, and kept the servers stable through the traffic spikes at peak registration and ticket sales.",
            },
        },
        {
            "key": "telkom",
            "role": "Telecom Data Analyst Intern",
            "org": "Telkom Landmark Surabaya",
            "period": {"id": "Jun 2022 sampai Nov 2022", "en": "Jun 2022 to Nov 2022"},
            "detail": {
                "id": "Aku menganalisis performa BTS se-Jawa Timur dan Madura dan menyediakan laporan real-time untuk tim operasional.",
                "en": "I analyzed BTS performance across East Java and Madura and delivered real-time reports for the operations team.",
            },
        },
    ],
    "projects": [
        {
            "key": "eko", "name": "Eko", "tech": "Python, OpenAI & Gemini API, ChromaDB", "link": "t.me/Eko_BPSbot",
            "summary": {
                "id": "Bot Telegram yang menjawab pertanyaan soal ekonomi Jawa Tengah dengan bahasa sehari-hari, berdasarkan data resmi BPS di 12 topik.",
                "en": "A Telegram bot that answers questions about Central Java's economy in plain language, grounded in official BPS data across 12 topics.",
            },
            "detail": {
                "id": "Eko itu bot Telegram buatanku yang menjawab pertanyaan soal ekonomi Jawa Tengah pakai bahasa sehari-hari, berdasarkan data resmi BPS. Topiknya ada 12, misalnya PDRB, inflasi, ekspor-impor, industri, energi dan nilai tukar petani. Di baliknya ada pipeline RAG: chunking dan embedding ke ChromaDB, pencarian semantik, lalu lapisan LLM yang bisa pindah antara OpenAI dan Gemini.",
                "en": "Eko is a Telegram bot I built that answers questions about Central Java's economy in plain language, grounded in official BPS data. It covers 12 topics, including GRDP, inflation, exports and imports, industry, energy and farmer terms of trade. Under the hood it's a RAG pipeline: chunking and embeddings into ChromaDB, semantic search, and an LLM layer that can switch between OpenAI and Gemini.",
            },
        },
        {
            "key": "podclip", "name": "Podclip", "tech": "Python, LLM, Computer Vision", "link": None,
            "summary": {
                "id": "Mengubah podcast dan live stream YouTube yang panjang jadi klip pendek vertikal, lengkap dengan pemilihan momen otomatis, reframing dan subtitle.",
                "en": "Turns long YouTube podcasts and live streams into vertical short clips, with auto moment picking, smart reframing and subtitles.",
            },
            "detail": {
                "id": "Podclip itu tool pribadiku untuk mengubah podcast dan live stream YouTube yang panjang jadi klip pendek vertikal. LLM memilih momen yang paling menarik, computer vision mengatur framing supaya pembicara tetap di tengah, lalu subtitle ditambahkan otomatis. Dibuat dengan Python.",
                "en": "Podclip is a personal tool that turns long YouTube podcasts and live streams into vertical short clips. An LLM picks the strongest moments, computer vision reframes the shot so the speaker stays centered, and subtitles are added automatically. Built with Python.",
            },
        },
        {
            "key": "agent_hq", "name": "Agent HQ", "tech": "Claude Code, Web UI", "link": None,
            "summary": {
                "id": "Setup di home server tempat AI agent utama mengerjakan tugas coding yang aku kirim dari HP atau iPad di background.",
                "en": "A home-server setup where a head AI agent takes coding tasks I send from my phone or iPad and works on them in the background.",
            },
        },
        {
            "key": "batik", "name": "Batik Manekin Studio", "tech": "Gemini", "link": None,
            "summary": {
                "id": "Tool untuk klien yang membuat foto katalog toko dengan memakaikan batik yang di-upload ke foto manekin, lalu menaruhnya di background hasil generate.",
                "en": "A client tool that generates store catalog photos by dressing mannequin shots in uploaded batik and placing them on generated backgrounds.",
            },
        },
        {
            "key": "geniuz", "name": "Geniuz", "tech": "Next.js, TypeScript, Python, Tailwind CSS", "link": None,
            "summary": {
                "id": "Platform les online. Aku pegang backend-nya: autentikasi admin, manajemen kelas dan pelacakan progres siswa.",
                "en": "An online tutoring platform. I handled the backend: admin auth, class management and student progress tracking.",
            },
            "detail": {
                "id": "Geniuz itu platform les online yang dikerjakan tim berisi 6 orang. Aku pegang backend-nya: autentikasi admin, manajemen kelas, penyajian materi dan pelacakan progres siswa, plus API internal yang dipakai frontend. Stack-nya Next.js, TypeScript, Python dan Tailwind CSS, dengan deployment di Vercel.",
                "en": "Geniuz is an online tutoring platform built by a team of six. I handled the backend: admin auth, class management, serving materials and student progress tracking, plus the internal API the frontend consumes. The stack is Next.js, TypeScript, Python and Tailwind CSS, deployed on Vercel.",
            },
        },
        {
            "key": "gym", "name": "Gym Management PWA", "tech": "Next.js, Supabase", "link": None,
            "summary": {
                "id": "Aplikasi member dan admin dengan check-in QR, booking kelas dan trainer, membership dan pembayaran.",
                "en": "Member and admin apps with QR check-in, class and trainer booking, memberships and payments.",
            },
            "detail": {
                "id": "Gym Management PWA itu aplikasi manajemen gym dengan akses member dan admin yang terpisah. Fiturnya check-in lewat QR, booking kelas dan trainer, serta pengelolaan membership dan pembayaran. Dibangun sebagai PWA pakai Next.js dan Supabase, jadi bisa dipasang di HP seperti aplikasi biasa.",
                "en": "Gym Management PWA is a gym app with separate member and admin access. It handles QR check-in, class and trainer booking, and memberships and payments. It's built as a PWA with Next.js and Supabase, so it installs on a phone like a regular app.",
            },
        },
        {
            "key": "skill_mapping", "name": "AI Skill Mapping", "tech": "IndoBERT, LLM", "link": None, "status": "in_progress",
            "summary": {
                "id": "Skripsiku: memetakan skill AI di lowongan kerja Indonesia dari JobStreet, Glints dan Kalibrr, sambil membandingkan IndoBERT dengan LLM.",
                "en": "My thesis: mapping AI skills in Indonesian job postings scraped from JobStreet, Glints and Kalibrr, comparing IndoBERT with LLMs.",
            },
            "detail": {
                "id": "AI Skill Mapping itu skripsiku, dan sekarang masih berjalan. Aku scraping lowongan kerja dari JobStreet, Glints dan Kalibrr, lalu memetakan skill AI apa saja yang dicari perusahaan di Indonesia. Untuk ekstraksinya aku membandingkan IndoBERT dengan LLM.",
                "en": "AI Skill Mapping is my thesis, and it's still in progress. I scrape job postings from JobStreet, Glints and Kalibrr and map which AI skills Indonesian employers are asking for. For the extraction I compare IndoBERT with LLMs.",
            },
        },
        {
            "key": "dengue", "name": "Dengue Severity Prediction", "tech": "Python, Scikit-learn", "link": None,
            "summary": {
                "id": "Riset untuk memprediksi tingkat keparahan demam berdarah dari data ekspresi RNA darah.",
                "en": "Research on predicting dengue severity from blood RNA expression data.",
            },
        },
        {
            "key": "paddy", "name": "Paddy Field Mapping", "tech": "Google Earth Engine", "link": None,
            "summary": {
                "id": "Klasifikasi tutupan lahan dan analisis spasial sawah di Boyolali, Klaten dan Sukoharjo.",
                "en": "Land-cover classification and spatial analysis of rice fields in Boyolali, Klaten and Sukoharjo.",
            },
        },
        {
            "key": "sentiment", "name": "Social Media Sentiment", "tech": "Python, Scraping, Deep Learning", "link": None,
            "summary": {
                "id": "Scraping komentar dari X, Instagram dan YouTube, lalu membangun model sentimen 3 kelas untuk mengukur opini publik.",
                "en": "Scraped comments from X, Instagram and YouTube and built a 3-class sentiment model to measure public opinion.",
            },
        },
        {
            "key": "route_finder", "name": "Java Route Finder", "tech": "Maps, Routing", "link": None, "status": "in_progress",
            "summary": {
                "id": "Aplikasi peta pribadi dengan mode rute tercepat, teraman, lewat gunung dan tanpa gunung.",
                "en": "A personal maps app with fastest, safest, mountain and non-mountain route modes.",
            },
        },
        {
            "key": "ml_flask", "name": "ML with Flask", "tech": "Scikit-learn, Jinja2", "link": "waows-6-ken-day2.vercel.app",
            "summary": {
                "id": "Model machine learning yang disajikan lewat web app Flask, dan menang Best Project Award.",
                "en": "A machine learning model served through a Flask web app, which won a Best Project Award.",
            },
        },
    ],
    "stack": [
        ({"id": "Bahasa", "en": "Languages"}, "Python, SQL, JavaScript, TypeScript, PHP"),
        ({"id": "AI & LLM", "en": "AI & LLM"}, "OpenAI API, Gemini API, RAG, ChromaDB, embeddings and vector search, AI workflow automation"),
        ({"id": "Data & ML", "en": "Data & ML"}, "Pandas, NumPy, Scikit-learn, EDA, predictive modeling, deep learning"),
        ({"id": "Visualisasi", "en": "Visualization"}, "Matplotlib, Seaborn, Power BI"),
        ({"id": "Web", "en": "Web"}, "React.js, Next.js, Node.js, Laravel, Supabase"),
        ({"id": "Cloud & Tools", "en": "Cloud & Tools"}, "AWS, Azure, GCP, Git, Jupyter Notebook"),
    ],
    "education": [
        {
            "degree": {"id": "S1 Sains Data", "en": "Bachelor's in Data Science"},
            "school": "Universitas Sebelas Maret (UNS), Surakarta",
            "period": {"id": "Agu 2023 sampai 2027", "en": "Aug 2023 to 2027"},
            "note": {
                "id": "Fokusnya AI, machine learning dan sistem data berskala besar.",
                "en": "The focus is AI, machine learning and large-scale data systems.",
            },
        },
        {
            "degree": {"id": "Rekayasa Perangkat Lunak (RPL)", "en": "Software Engineering (RPL)"},
            "school": "SMK Telkom Malang",
            "period": {"id": "Jul 2020 sampai Jun 2023", "en": "Jul 2020 to Jun 2023"},
            "note": {
                "id": "Di sini aku belajar dasar pemrograman, UI/UX dan pengembangan web.",
                "en": "That's where I learned programming fundamentals, UI/UX and web development.",
            },
        },
    ],
    "certifications": {
        "items": ["Python Flask Development", "Flask for Web Applications", "Flask & Machine Learning Fundamentals"],
        "issuer": "CODER Telkom University",
        "year": 2025,
        "awards": 3,  # Best Project Award in all three
        "toefl": 513,
    },
    "clients": [
        {"name": "Wonderland", "sector": {"id": "hiburan & event", "en": "entertainment & events"}},
        {"name": "Luwes Group", "sector": {"id": "ritel & supermarket", "en": "retail & supermarket"}},
        {"name": "Cardinal", "sector": {"id": "fashion & apparel", "en": "fashion & apparel"}},
    ],
    "contact": {
        "email": "kenzaathallah.wijaya@gmail.com",
        "linkedin": "linkedin.com/in/kenzaathallah",
        "github": "github.com/K4ZED",
        "cv": "portfolio-kazed.my.id/static/cv/CV-Kenza-Athallah-Nandana-Wijaya.pdf",
    },
    "open_to": {"id": "AI, otomatisasi dan fullstack", "en": "AI, automation and fullstack"},
}

# Quick replies shown as buttons in the chat widget (label on the button, message sent on click).
SUGGESTIONS = {
    "id": [
        {"label": "Project", "message": "project kamu apa aja"},
        {"label": "Pengalaman", "message": "pengalaman kamu"},
        {"label": "Skill", "message": "skill kamu apa"},
        {"label": "Kontak", "message": "kontak kamu"},
    ],
    "en": [
        {"label": "Projects", "message": "what projects have you built"},
        {"label": "Experience", "message": "what's your experience"},
        {"label": "Skills", "message": "what are your skills"},
        {"label": "Contact", "message": "how can I contact you"},
    ],
}


# ─────────────────────────────────────────────────────────────────────────────
# Answers, built from PROFILE
# ─────────────────────────────────────────────────────────────────────────────
def _exp(key):
    return next(e for e in PROFILE["experience"] if e["key"] == key)


def _proj(key):
    return next(p for p in PROFILE["projects"] if p["key"] == key)


def _headline(e, lang):
    if e["org"] is None:
        return f"{e['role']} (Freelance)"
    return f"{e['role']} {'di' if lang == 'id' else 'at'} {e['org']}"


def _exp_answer(key, lang):
    e = _exp(key)
    return f"{_headline(e, lang)}, {e['period'][lang]}. {e['detail'][lang]}"


def _experience_list(lang):
    lines = "\n".join(f"- {_headline(e, lang)} ({e['period'][lang]})" for e in PROFILE["experience"])
    if lang == "id":
        return f"Pengalamanku:\n{lines}\n\nMau aku ceritain salah satunya lebih detail?"
    return f"Here's my experience:\n{lines}\n\nWant more detail on any of these?"


def _project_answer(key, lang):
    p = _proj(key)
    text = p.get("detail", p["summary"])[lang]
    if "detail" not in p:
        text = f"{p['name']}: {text}"
    if p.get("status") == "in_progress" and "detail" not in p:
        text += " Masih dalam pengerjaan." if lang == "id" else " Still in progress."
    if "detail" not in p:
        text += f" Tech: {p['tech']}." if lang == "en" else f" Teknologinya: {p['tech']}."
    if p["link"]:
        text += f"\n\nCoba langsung: {p['link']}" if lang == "id" else f"\n\nTry it: {p['link']}"
    return text


def _projects_list(lang):
    lines = "\n".join(f"- {p['name']}: {p['summary'][lang]}" for p in PROFILE["projects"])
    n = len(PROFILE["projects"])
    if lang == "id":
        return f"Ini {n} project-ku:\n{lines}\n\nTanya aja salah satunya, misalnya \"Eko itu apa?\""
    return f"Here are my {n} projects:\n{lines}\n\nAsk about any of them, for example \"What is Eko?\""


def _about(lang):
    P = PROFILE
    uns = P["education"][0]
    if lang == "id":
        return (f"Aku {P['name']}, biasa dipanggil {P['nickname']}. Aku {P['title']} dari {P['location']}, "
                f"sekarang kuliah Sains Data di Universitas Sebelas Maret ({uns['period']['id']}). {P['summary']['id']}")
    return (f"I'm {P['name']}, most people call me {P['nickname']}. I'm an {P['title']} from {P['location']}, "
            f"studying Data Science at Universitas Sebelas Maret ({uns['period']['en']}). {P['summary']['en']}")


def _skills(lang):
    lines = "\n".join(f"- {label[lang]}: {items}" for label, items in PROFILE["stack"])
    if lang == "id":
        return f"Tech stack-ku:\n{lines}"
    return f"My tech stack:\n{lines}"


def _education(lang):
    lines = "\n".join(
        f"- {ed['degree'][lang]}, {ed['school']} ({ed['period'][lang]}). {ed['note'][lang]}"
        for ed in PROFILE["education"])
    return ("Pendidikanku:\n" if lang == "id" else "My education:\n") + lines


def _certifications(lang):
    c = PROFILE["certifications"]
    items = ", ".join(c["items"][:-1]) + (" dan " if lang == "id" else " and ") + c["items"][-1]
    if lang == "id":
        return (f"Aku dapat {c['awards']} sertifikasi dari {c['issuer']} di {c['year']}: {items}. "
                f"Di ketiganya aku menang Best Project Award. Untuk bahasa, skor TOEFL-ku {c['toefl']}.")
    return (f"I earned {c['awards']} certifications at {c['issuer']} in {c['year']}: {items}. "
            f"I won the Best Project Award in all three. My English score is TOEFL {c['toefl']}.")


def _clients(lang):
    cl = PROFILE["clients"]
    lines = "\n".join(f"- {c['name']} ({c['sector'][lang]})" for c in cl)
    if lang == "id":
        return f"Di sisi desain, aku pernah bikin materi visual dan branding untuk:\n{lines}"
    return f"On the design side, I've made visual and branding work for:\n{lines}"


def _contact(lang):
    c = PROFILE["contact"]
    body = f"- Email: {c['email']}\n- LinkedIn: {c['linkedin']}\n- GitHub: {c['github']}\n- CV: {c['cv']}"
    if lang == "id":
        return f"Kamu bisa hubungi aku lewat:\n{body}\n\nLewat email biasanya paling cepat aku balas."
    return f"You can reach me here:\n{body}\n\nEmail is usually the fastest way to get a reply."


def _services(lang):
    c = PROFILE["contact"]
    if lang == "id":
        return (f"Aku terbuka untuk kerjaan {PROFILE['open_to']['id']}: tools AI internal, chatbot RAG, "
                f"otomatisasi alur kerja, sampai aplikasi web dari database sampai API. "
                f"Kirim pesan ke {c['email']} atau LinkedIn, nanti aku balas.")
    return (f"I'm open to {PROFILE['open_to']['en']} work: internal AI tools, RAG chatbots, workflow automation, "
            f"and web apps from database to API. Send me a message at {c['email']} or on LinkedIn and I'll get back to you.")


def _years(lang):
    since = PROFILE["in_tech_since"]
    if lang == "id":
        return (f"Aku sudah 5+ tahun di dunia tech, mulai {since} waktu masuk jurusan RPL di SMK Telkom Malang. "
                f"Sekarang fokusku di AI, otomatisasi dan fullstack.")
    return (f"I've been in tech for 5+ years, since {since} when I started software engineering at SMK Telkom Malang. "
            f"These days my focus is AI, automation and fullstack.")


# ─────────────────────────────────────────────────────────────────────────────
# Intents. Order matters only for exact ties: specific intents come first.
# "answer" is a function (lang) -> str, or a dict of variant lists per language.
# ─────────────────────────────────────────────────────────────────────────────
INTENTS = [
    # ── Projects, one intent each
    {"tag": "project_eko", "patterns": [
        "eko", "eko bot", "bot eko", "eko bps", "eko bpsbot", "bot telegram", "telegram bot", "bps bot",
        "bot ekonomi", "ekonomi jawa tengah", "central java economy", "data bps"],
     "answer": lambda l: _project_answer("eko", l)},
    {"tag": "project_podclip", "patterns": [
        "podclip", "pod clip", "short clip", "short clips", "klip pendek", "potong podcast", "clip podcast",
        "podcast clip", "podcast clips", "auto clip"],
     "answer": lambda l: _project_answer("podclip", l)},
    {"tag": "project_agent_hq", "patterns": [
        "agent hq", "agenthq", "ai agent", "home server", "claude code", "coding agent"],
     "answer": lambda l: _project_answer("agent_hq", l)},
    {"tag": "project_batik", "patterns": [
        "batik", "manekin", "mannequin", "batik manekin", "batik manekin studio", "foto katalog", "catalog photo"],
     "answer": lambda l: _project_answer("batik", l)},
    {"tag": "project_geniuz", "patterns": [
        "geniuz", "genius", "les online", "online tutoring", "tutoring platform", "platform les", "bimbel online"],
     "answer": lambda l: _project_answer("geniuz", l)},
    {"tag": "project_gym", "patterns": [
        "gym", "gim", "gym pwa", "gym management", "aplikasi gym", "gym app", "pwa", "fitness", "check in qr"],
     "answer": lambda l: _project_answer("gym", l)},
    {"tag": "project_skill_mapping", "patterns": [
        "ai skill mapping", "skill mapping", "skripsi", "thesis", "tugas akhir", "indobert", "jobstreet",
        "lowongan kerja", "job postings"],
     "answer": lambda l: _project_answer("skill_mapping", l)},
    {"tag": "project_dengue", "patterns": [
        "dengue", "demam berdarah", "dbd", "rna", "dengue severity", "bioinformatics", "bioinformatika"],
     "answer": lambda l: _project_answer("dengue", l)},
    {"tag": "project_paddy", "patterns": [
        "paddy", "paddy field", "sawah", "padi", "earth engine", "google earth engine", "geospatial", "geospasial"],
     "answer": lambda l: _project_answer("paddy", l)},
    {"tag": "project_sentiment", "patterns": [
        "sentiment", "sentimen", "analisis sentimen", "sentiment analysis", "opini publik", "public opinion",
        "social media sentiment"],
     "answer": lambda l: _project_answer("sentiment", l)},
    {"tag": "project_route_finder", "patterns": [
        "route finder", "java route finder", "rute", "route", "maps app", "aplikasi peta", "aplikasi maps"],
     "answer": lambda l: _project_answer("route_finder", l)},
    {"tag": "project_ml_flask", "patterns": [
        "ml with flask", "flask", "machine learning flask", "flask app", "live demo"],
     "answer": lambda l: _project_answer("ml_flask", l)},

    # ── Experience, one intent per role
    {"tag": "exp_dzakiyah", "patterns": [
        "dzakiyah", "dzakiyah store", "dzakiyah store group", "ai specialist", "kerja sekarang",
        "kerja di mana sekarang", "kerja dimana sekarang", "current job", "where do you work", "currently working",
        "lagi kerja di mana"],
     "answer": lambda l: _exp_answer("dzakiyah", l)},
    {"tag": "exp_freelance", "patterns": [
        "freelance", "freelancer", "fullstack engineer", "freelance fullstack", "client web apps",
        "web apps for clients", "aplikasi web klien"],
     "answer": lambda l: _exp_answer("freelance", l)},
    {"tag": "exp_amigo", "patterns": [
        "amigo", "amigo group", "retail data analyst", "magang di amigo", "internship amigo", "data ritel"],
     "answer": lambda l: _exp_answer("amigo", l)},
    {"tag": "exp_pingfest", "patterns": [
        "pingfest", "p ngfest", "ping fest", "coordinator of technology", "koordinator teknologi",
        "pekan teknologi", "event uns"],
     "answer": lambda l: _exp_answer("pingfest", l)},
    {"tag": "exp_telkom", "patterns": [
        "telkom", "telkom landmark", "telkom surabaya", "bts", "telecom", "telekomunikasi", "magang di telkom",
        "internship telkom"],
     "answer": lambda l: _exp_answer("telkom", l)},

    # ── Profile topics
    {"tag": "certifications", "patterns": [
        "sertifikat", "sertifikasi", "certification", "certifications", "certificate", "award", "awards",
        "penghargaan", "prestasi", "achievement", "achievements", "best project", "best project award", "juara",
        "toefl", "english", "bahasa inggris", "telkom university", "coder"],
     "answer": _certifications},
    {"tag": "education", "patterns": [
        "pendidikan", "kuliah", "kampus", "sekolah", "smk", "smk telkom", "smk telkom malang", "uns",
        "universitas", "sebelas maret", "jurusan", "major", "education", "study", "studi", "kuliah di mana",
        "kuliah dimana", "degree", "sains data", "semester", "lulus kapan", "graduate", "rpl",
        "rekayasa perangkat lunak", "where do you study"],
     "answer": _education},
    {"tag": "clients", "patterns": [
        "klien", "client", "clients", "klien kamu", "klien siapa", "your clients", "worked with", "wonderland", "luwes", "luwes group", "cardinal", "desain", "design",
        "graphic design", "desain grafis", "designed for", "branding", "poster"],
     "answer": _clients},
    {"tag": "services", "patterns": [
        "open to work", "hire", "hire you", "hiring", "rekrut", "bisa di hire", "kerja sama", "kerjasama",
        "collaborate", "collaboration", "kolaborasi", "layanan", "jasa", "services", "available", "tersedia",
        "lagi open", "terima project", "terima freelance", "open for freelance", "bikin website", "bikin aplikasi",
        "buat chatbot", "can you build", "work with you", "work together"],
     "answer": _services},
    {"tag": "contact", "patterns": [
        "kontak", "hubungi", "contact", "email", "gmail", "linkedin", "github", "reach you", "reach out",
        "get in touch", "cv", "resume", "download cv", "sosial media", "social media", "whatsapp"],
     "answer": _contact},
    {"tag": "years_experience", "patterns": [
        "berapa tahun", "sudah berapa lama", "how many years", "how long", "years of experience", "lama di tech",
        "sejak kapan", "since when", "mulai coding", "started coding"],
     "answer": _years},
    {"tag": "skills", "patterns": [
        "skill", "skills", "keahlian", "kemampuan", "tech stack", "stack", "teknologi apa", "tools apa",
        "bahasa pemrograman", "programming language", "programming languages", "what can you do", "bisa apa",
        "jago apa", "skillset", "what technologies", "tools", "framework", "machine learning", "data science",
        "llm", "rag", "openai", "python", "react", "next js", "laravel", "backend", "frontend", "fullstack",
        "cloud", "aws", "power bi", "visualisasi", "visualization", "deep learning", "ai"],
     "answer": _skills},
    {"tag": "projects", "patterns": [
        "project", "projects", "proyek", "portofolio", "portfolio", "karya", "what have you built",
        "what did you build", "pernah bikin apa", "bikin apa aja", "daftar project", "list project",
        "show me projects", "what projects", "hasil kerja"],
     "answer": _projects_list},
    {"tag": "experience", "patterns": [
        "pengalaman", "pengalaman kerja", "pernah kerja", "magang", "internship", "internships", "kerja di mana",
        "kerja dimana", "riwayat kerja", "work experience", "experience", "career", "karir", "where have you worked",
        "pekerjaan", "data analyst"],
     "answer": _experience_list},
    {"tag": "about", "patterns": [
        "siapa kamu", "kamu siapa", "siapa kenza", "siapa kazed", "kenza itu siapa", "who are you", "who is kenza",
        "tell me about yourself", "about you", "about kenza", "tentang kamu", "tentang kenza", "perkenalkan diri",
        "profil", "profile", "bio", "kenalan", "introduce yourself", "where are you from", "where are you based",
        "asal dari mana", "tinggal di mana", "domisili", "ceritain tentang kamu"],
     "answer": _about},

    # ── Conversation
    {"tag": "identity", "suggest": True, "patterns": [
        "kamu bot", "apakah kamu bot", "siapa byte", "byte itu apa", "byte siapa", "what is byte", "who is byte",
        "are you a bot", "are you ai", "are you real", "kamu robot", "kamu ai", "is this a bot"],
     "answer": {
         "id": ["Aku Byte, bot kecil berbasis aturan yang dibuat Kenza untuk website ini. Aku jawab dari sudut pandang Kenza, pakai info yang sama dengan homepage dan CV."],
         "en": ["I'm Byte, a small rule-based bot Kenza built for this site. I answer in Kenza's voice, using the same info as the homepage and CV."],
     }},
    {"tag": "help", "suggest": True, "patterns": [
        "help", "bantuan", "bisa bantu apa", "kamu bisa bantu apa", "what can i ask", "menu", "topik", "topics",
        "pilihan", "aku harus tanya apa", "options"],
     "answer": {
         "id": ["Kamu bisa tanya soal project, pengalaman, skill, pendidikan, sertifikasi, klien, atau cara menghubungiku. Atau pilih salah satu di bawah."],
         "en": ["You can ask about my projects, experience, skills, education, certifications, clients, or how to reach me. Or pick one below."],
     }},
    {"tag": "smalltalk", "patterns": [
        "apa kabar", "how are you", "gimana kabarmu", "lagi apa", "sedang apa", "how s it going", "whats up",
        "what s up", "lagi ngapain"],
     "answer": {
         "id": ["Baik, makasih udah nanya! Lagi sibuk ngurus tools AI dan beberapa side project. Mau tahu soal yang mana?"],
         "en": ["Doing well, thanks for asking! Busy with AI tools and a few side projects. What would you like to know?"],
     }},
    {"tag": "greeting", "suggest": True, "patterns": [
        "halo", "hai", "hello", "hi", "hey", "hei", "haloo", "hellow", "selamat pagi", "selamat siang",
        "selamat malam", "halo kak", "hi there", "good morning", "good afternoon", "good evening",
        "assalamualaikum", "pagi", "permisi"],
     "answer": {
         "id": [
             "Halo! Ini Byte, asisten di portofolio Kenza. Aku jawab dari sudut pandang Kenza, jadi tanya aja soal project, pengalaman, skill, atau cara menghubungiku.",
             "Hai, makasih udah mampir! Mau tahu soal project, pengalaman, atau skill-ku?",
         ],
         "en": [
             "Hi! This is Byte, the assistant on Kenza's portfolio. I answer as Kenza, so ask me about my projects, experience, skills or how to reach me.",
             "Hey, thanks for stopping by! Want to hear about my projects, experience or skills?",
         ],
     }},
    {"tag": "farewell", "patterns": [
        "bye", "dadah", "selamat tinggal", "sampai jumpa", "terima kasih", "makasih", "thanks", "thank you",
        "oke thanks", "ok bye", "ok makasih", "sudah cukup", "itu saja", "cukup", "ok terima kasih",
        "terimakasih", "thx", "see you", "good bye", "goodbye"],
     "answer": {
         "id": ["Sama-sama! Kalau ada yang mau ditanya lagi, aku di sini.", "Makasih udah ngobrol, mampir lagi kapan aja ya."],
         "en": ["You're welcome! If you have more questions, I'm right here.", "Thanks for the chat, drop by anytime."],
     }},
]

FALLBACK = {
    "id": [
        "Hmm, yang itu aku belum bisa jawab. Coba tanya soal project, pengalaman, skill, atau kontakku.",
        "Maaf, aku belum paham maksudnya. Aku bisa cerita soal project, pengalaman, skill, atau kontakku.",
    ],
    "en": [
        "Hmm, I don't have an answer for that yet. Try asking about my projects, experience, skills or contact.",
        "Sorry, I didn't catch that. I can tell you about my projects, experience, skills or contact.",
    ],
}

# Word hints used for a lightweight ID/EN language guess.
_EN_HINTS = {
    "what", "who", "how", "why", "when", "where", "are", "is", "am", "do", "does", "you", "your",
    "yourself", "me", "my", "the", "can", "could", "tell", "about", "skills", "skill", "experience",
    "project", "projects", "contact", "hire", "available", "work", "worked", "education", "background",
    "hello", "hi", "hey", "thanks", "thank", "please", "show", "reach", "give", "list", "have", "has",
    "good", "morning", "afternoon", "evening", "bye", "goodbye", "of", "for", "built", "build", "did",
    "certifications", "clients", "it", "this", "that", "a", "an", "and",
}
_ID_HINTS = {
    "apa", "siapa", "kamu", "kah", "apakah", "bisa", "dia", "yang", "kerja", "gimana", "gmn", "tolong",
    "dong", "kak", "saya", "aku", "punya", "mau", "ingin", "keahlian", "kemampuan", "pengalaman",
    "pendidikan", "kontak", "hubungi", "halo", "hai", "makasih", "terima", "proyek", "ceritain",
    "ceritakan", "nya", "aja", "sih", "buat", "soal", "tentang", "itu", "ini", "dan", "di", "mana",
    "dimana", "berapa", "kuliah", "pernah", "bikin", "lagi", "sekarang",
}


def _norm(text: str) -> str:
    """Lowercase and strip everything but letters/digits/spaces."""
    text = text.lower()
    text = re.sub(r"[^0-9a-z]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _detect_lang(tokens) -> str:
    """Guess the message language from word hints. Defaults to Indonesian."""
    en = sum(1 for t in tokens if t in _EN_HINTS)
    idn = sum(1 for t in tokens if t in _ID_HINTS)
    return "en" if en > idn else "id"


def _fuzzy(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def _tok_match(pt: str, msg_tokens: set) -> bool:
    """A pattern token matches a message token: exact, prefix (Indonesian suffixes like
    "emailnya"/"projectnya"), or fuzzy for words >= 4 chars (typos)."""
    if pt in msg_tokens:
        return True
    if len(pt) >= 4:
        for mt in msg_tokens:
            if len(mt) >= 4 and (mt.startswith(pt) or _fuzzy(pt, mt) >= 0.82):
                return True
    return False


def _contains_seq(words, seq) -> bool:
    """True if `seq` appears as a contiguous run of whole words inside `words`."""
    n = len(seq)
    for i in range(len(words) - n + 1):
        if words[i:i + n] == seq:
            return True
    return False


def _score(msg_words, msg_tokens: set, pattern: str):
    """Return (confidence 0..1, specificity) of one pattern against the message.

    Specificity (matched word count) breaks ties so a precise phrase like
    "magang di telkom" outranks a broad keyword like "magang".
    """
    pw = _norm(pattern).split()
    n = len(pw)
    if n == 0:
        return 0.0, 0
    # contiguous whole-word phrase match: strongest, most specific
    if _contains_seq(msg_words, pw):
        return 1.0, n
    # same phrase, in order, with typos ("ai skill maping")
    for i in range(len(msg_words) - n + 1):
        if all(_tok_match(t, {msg_words[i + j]}) for j, t in enumerate(pw)):
            return 0.95, n
    # every pattern token present (scattered order, typo-tolerant)
    matched = sum(1 for t in pw if _tok_match(t, msg_tokens))
    if matched == n:
        return 0.9, n
    if matched:
        # partial coverage stays below the answer threshold on its own
        return 0.6 * (matched / n), matched
    return 0.0, 0


_MATCH_FLOOR = 0.6  # a pattern counts as a real match from here up


def _best_intent(msg_words, msg_tokens: set):
    """Return (intent, confidence) for the best-scoring intent.

    In-order phrase matches (exact or with typos) outrank scattered-word matches.
    Within a tier the most specific pattern wins, so "ai skill maping" (3 words, in
    order, one typo) beats the single word "skill", while "skripsi kamu tentang apa"
    still goes to "skripsi" rather than the scattered "tentang kamu".
    """
    best = (False, False, 0, 0.0)
    best_intent = None
    for intent in INTENTS:
        for pattern in intent["patterns"]:
            conf, spec = _score(msg_words, msg_tokens, pattern)
            key = (conf >= _MATCH_FLOOR, conf >= 0.95, spec, conf)
            if key > best:
                best = key
                best_intent = intent
    return best_intent, best[3]


def classify(message: str, threshold: float = 0.6):
    """Inspect matching: returns (tag, confidence, lang). `tag` is None below threshold."""
    msg = _norm(message)
    if not msg:
        return None, 0.0, "id"
    msg_words = msg.split()
    msg_tokens = set(msg_words)
    lang = _detect_lang(msg_tokens)
    intent, conf = _best_intent(msg_words, msg_tokens)
    tag = intent["tag"] if (intent and conf >= threshold) else None
    return tag, conf, lang


def _render(intent, lang: str) -> str:
    answer = intent["answer"]
    if callable(answer):
        return answer(lang)
    variants = answer.get(lang) or answer.get("id") or answer.get("en")
    return random.choice(variants)


def get_reply(message: str, threshold: float = 0.6) -> dict:
    """Return {"response": str, "suggestions": [{"label", "message"}, ...]}.

    Lightweight keyword + fuzzy matcher: no ML model and no heavy dependencies, so it
    starts instantly and deploys anywhere. Suggestions are quick-reply buttons for the
    widget; they come with greetings, help, the bot-identity answer and the fallback.
    """
    tag, _conf, lang = classify(message, threshold)
    if tag is None:
        return {"response": random.choice(FALLBACK[lang]), "suggestions": SUGGESTIONS[lang]}
    intent = next(i for i in INTENTS if i["tag"] == tag)
    return {
        "response": _render(intent, lang),
        "suggestions": SUGGESTIONS[lang] if intent.get("suggest") else [],
    }


def get_response(message: str, threshold: float = 0.6) -> str:
    """Plain-text answer (kept for backwards compatibility)."""
    return get_reply(message, threshold)["response"]
