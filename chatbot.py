import re
import random
from difflib import SequenceMatcher

# Each intent carries keyword patterns (ID + EN) and several response variants per
# language, so Byte answers in the visitor's language and never sounds robotic.
INTENTS = [
    {
        "tag": "greeting",
        "patterns": [
            "halo", "hai", "hello", "hi", "hey", "selamat pagi", "selamat siang", "selamat malam",
            "halo kak", "hi there", "good morning", "good afternoon", "good evening",
            "hei", "haloo", "hellow", "assalamualaikum", "pagi", "permisi",
        ],
        "id": [
            "Halo! Aku Byte, asisten virtual Kenza. Mau tahu soal apa, nih? Bisa skill, project, pengalaman, atau cara menghubunginya.",
            "Hai! Aku Byte, senang kamu mampir. Ada yang ingin kamu tahu tentang Kenza?",
            "Halo, aku Byte! Tanya aja apa pun soal Kenza, dari skill sampai project-nya.",
        ],
        "en": [
            "Hi! I'm Byte, Kenza's virtual assistant. What would you like to know? Skills, projects, experience, or how to reach out?",
            "Hey there! I'm Byte, glad you stopped by. Anything you'd like to know about Kenza?",
            "Hello! I'm Byte. Feel free to ask me anything about Kenza, from skills to projects.",
        ],
    },
    {
        "tag": "smalltalk",
        "patterns": [
            "apa kabar", "how are you", "gimana kabarmu", "lagi apa", "sedang apa", "kabar baik",
            "how's it going", "whats up", "what's up", "kamu sehat", "lagi ngapain",
        ],
        "id": [
            "Aku baik, makasih udah nanya! Lagi siap bantu kamu kenalan sama portofolio Kenza. Mau mulai dari mana?",
            "Selalu siap, hehe. Ngomong-ngomong, mau aku ceritain soal skill atau project Kenza?",
        ],
        "en": [
            "I'm doing great, thanks for asking! Ready to walk you through Kenza's portfolio. Where shall we start?",
            "Always up and running! By the way, want me to tell you about Kenza's skills or projects?",
        ],
    },
    {
        "tag": "identity",
        "patterns": [
            "kamu bot", "apakah kamu bot", "kamu siapa sih", "kamu ai", "apakah kamu ai", "siapa byte",
            "are you a bot", "are you ai", "are you real", "what are you", "kamu robot", "byte itu apa",
        ],
        "id": [
            "Betul, aku Byte, asisten virtual di portofolio Kenza. Tugasku bantu jawab pertanyaan soal dia. Mau mulai dari mana?",
            "Aku Byte, bot kecil buatan Kenza buat nemenin kamu eksplor portofolionya. Tanya aja, ya!",
        ],
        "en": [
            "Yep, I'm Byte, the virtual assistant on Kenza's portfolio. I'm here to answer questions about him. Where should we start?",
            "I'm Byte, a little bot Kenza built to help you explore the portfolio. Go ahead and ask!",
        ],
    },
    {
        "tag": "help",
        "patterns": [
            "bisa bantu apa", "kamu bisa bantu apa", "help", "bantuan", "aku harus tanya apa",
            "what can i ask", "what can you help", "menu", "pilihan", "topik apa saja",
        ],
        "id": [
            "Aku bisa bantu jelasin soal: skill, project, pengalaman kerja & magang, pendidikan, klien, sampai cara menghubungi Kenza. Mau yang mana dulu?",
        ],
        "en": [
            "I can help with: skills, projects, work & internship experience, education, clients, and how to contact Kenza. Which one first?",
        ],
    },
    {
        "tag": "about",
        "patterns": [
            "siapa kamu", "siapa kenza", "siapa kazed", "ceritain tentang kamu", "ceritakan tentang kenza",
            "perkenalkan diri", "who are you", "who is kenza", "tell me about yourself", "about kenza",
            "tentang kenza", "dia siapa", "profil kenza", "profil kazed", "bio kenza", "kenza itu siapa",
        ],
        "id": [
            "Kenza Athallah Nandana Wijaya (alias Kazed) itu praktisi teknologi dengan pengalaman 5+ tahun sejak 2020. Fokusnya di Data Analytics, Data Science, Backend Development, dan Graphic Design. Dia pernah jadi Data Analyst di Telkom dan Amigo Group.",
            "Singkatnya: Kenza (atau Kazed) sudah 5 tahun lebih di dunia tech. Dia main di data, backend, sekaligus desain grafis. Pengalaman magangnya sebagai Data Analyst di Telkom dan Amigo Group, dua-duanya hybrid.",
        ],
        "en": [
            "Kenza Athallah Nandana Wijaya (aka Kazed) is a tech practitioner with 5+ years of experience since 2020. He focuses on Data Analytics, Data Science, Backend Development, and Graphic Design, and has worked as a Data Analyst at Telkom and Amigo Group.",
            "In short: Kenza (or Kazed) has spent 5+ years in tech, working across data, backend, and graphic design, with Data Analyst internships at Telkom and Amigo Group, both hybrid.",
        ],
    },
    {
        "tag": "skills",
        "patterns": [
            "skill", "skills", "skill apa", "skill nya apa", "bisa apa", "bisa ngapain", "jago apa",
            "keahlian", "keahlian apa", "kemampuan", "kemampuan apa", "teknologi apa", "tools apa",
            "what skills", "what can you do", "tech stack", "what technology", "keahlian kenza",
            "kamu bisa apa", "skill kenza", "kemampuan kenza", "list skill", "skillset",
        ],
        "id": [
            "Kenza punya keahlian di 5 bidang:\n- Data Analyst: Python, SQL, Power BI, Excel\n- Data Science: Scikit-learn, Deep Learning, NLP, Jupyter\n- Data Engineering: Python, SQL, ETL, AWS/Azure/GCP\n- Backend: Python, Flask, FastAPI, REST API\n- Desain Grafis: Canva, Figma, Adobe Illustrator\n\nMau aku bahas salah satunya lebih dalam?",
        ],
        "en": [
            "Kenza's skills span 5 areas:\n- Data Analyst: Python, SQL, Power BI, Excel\n- Data Science: Scikit-learn, Deep Learning, NLP, Jupyter\n- Data Engineering: Python, SQL, ETL, AWS/Azure/GCP\n- Backend: Python, Flask, FastAPI, REST API\n- Graphic Design: Canva, Figma, Adobe Illustrator\n\nWant me to go deeper on any of these?",
        ],
    },
    {
        "tag": "data_analyst",
        "patterns": [
            "data analyst", "analisis data", "data analysis", "power bi", "visualisasi data",
            "data visualization", "skill data analyst", "pengalaman data", "excel data",
            "laporan data", "dashboard data", "reporting",
        ],
        "id": [
            "Sebagai Data Analyst, Kenza pakai Python, SQL, dan Power BI buat ngolah data dari pengumpulan sampai visualisasi. Dia berpengalaman bikin dashboard dan laporan analitik selama magang di Telkom dan Amigo Group.",
        ],
        "en": [
            "As a Data Analyst, Kenza uses Python, SQL, and Power BI to handle data from collection to visualization. He's built dashboards and analytics reports during his internships at Telkom and Amigo Group.",
        ],
    },
    {
        "tag": "data_science",
        "patterns": [
            "data science", "machine learning", "ml", "artificial intelligence", "deep learning",
            "scikit-learn", "scikit learn", "neural network", "model ml", "ai kenza",
            "model prediksi", "klasifikasi", "regresi", "clustering", "nlp", "sentiment analysis",
        ],
        "id": [
            "Di Data Science, Kenza membangun model machine learning dan analisis sentimen pakai Scikit-learn serta pendekatan deep learning, lengkap dengan evaluasi model. Tools-nya: Python, Jupyter, plus NLP buat data teks.",
        ],
        "en": [
            "In Data Science, Kenza builds machine learning models and sentiment analysis using Scikit-learn and deep learning approaches, complete with model evaluation. Toolset: Python, Jupyter, plus NLP for text data.",
        ],
    },
    {
        "tag": "backend",
        "patterns": [
            "backend", "backend dev", "backend developer", "fastapi", "flask backend", "rest api",
            "api development", "server side", "web backend", "backend development", "bikin api",
        ],
        "id": [
            "Untuk Backend, Kenza pakai Python dengan Flask dan FastAPI buat bikin REST API yang nyajiin data dan hasil analitik, lalu di-deploy ke cloud. Version control-nya pakai Git.",
        ],
        "en": [
            "For Backend, Kenza uses Python with Flask and FastAPI to build REST APIs that serve data and analytics results, then deploys them to the cloud. Version control with Git.",
        ],
    },
    {
        "tag": "graphic_design",
        "patterns": [
            "desain", "design", "grafis", "graphic design", "canva", "figma", "adobe", "illustrator",
            "poster", "banner", "visual design", "logo", "branding", "desain grafis", "ui design",
            "desain event",
        ],
        "id": [
            "Buat Desain Grafis, Canva jadi tool utama Kenza, ditambah kemampuan dasar di Figma dan Adobe Illustrator. Dia sering bikin materi visual buat event dan branding. Beberapa kliennya: Wonderland, Luwes Group, dan Cardinal.",
        ],
        "en": [
            "For Graphic Design, Canva is Kenza's main tool, plus foundational skills in Figma and Adobe Illustrator. He often creates visual materials for events and branding. A few of his clients: Wonderland, Luwes Group, and Cardinal.",
        ],
    },
    {
        "tag": "projects",
        "patterns": [
            "project", "projects", "project apa", "punya project apa", "portofolio", "karya", "hasil kerja",
            "apa saja projectnya", "contoh project", "what projects", "portfolio", "show me projects",
            "daftar project", "project kenza", "project yang sudah dibuat", "proyek", "pernah bikin apa",
        ],
        "id": [
            "Beberapa project Kenza:\n- BTS Performance Analysis: analisis performa jaringan (Python & Power BI)\n- Web Dashboard: visualisasi data interaktif\n- P!NGFEST: website event (PHP, Laravel, Blade)\n- Pemoela Lab: company profile digital solution\n\nScroll ke bagian Projects buat lihat semuanya, termasuk demo website-nya.",
        ],
        "en": [
            "Some of Kenza's projects:\n- BTS Performance Analysis: network performance analysis (Python & Power BI)\n- Web Dashboard: interactive data visualization\n- P!NGFEST: event website (PHP, Laravel, Blade)\n- Pemoela Lab: digital solution company profile\n\nScroll to the Projects section to see them all, including live demos.",
        ],
    },
    {
        "tag": "pingfest",
        "patterns": [
            "pingfest", "p!ngfest", "ping fest", "event website", "website event pingfest", "pekan teknologi",
        ],
        "id": [
            "P!NGFEST itu website resmi acara Pekan Teknologi UNS, dibangun dengan PHP, Laravel, dan Blade. Isinya profil acara, pendaftaran lomba & seminar, plus sistem ticketing peserta.",
        ],
        "en": [
            "P!NGFEST is the official website for UNS Tech Week, built with PHP, Laravel, and Blade. It covers the event intro, competition & seminar registration, and a participant ticketing system.",
        ],
    },
    {
        "tag": "pemoela_lab",
        "patterns": [
            "pemoela", "pemoela lab", "digital solution", "company profile pemoela",
            "startup kenza", "perusahaan kenza", "agency kenza",
        ],
        "id": [
            "Pemoela Lab adalah digital solution agency milik Kenza sendiri. Website company profile-nya dibangun pakai PHP, Laravel, dan Blade, menampilkan layanan dan profil perusahaan. Ada demo-nya di bagian Projects.",
        ],
        "en": [
            "Pemoela Lab is Kenza's own digital solution agency. Its company profile site is built with PHP, Laravel, and Blade, showcasing services and the company profile. There's a demo in the Projects section.",
        ],
    },
    {
        "tag": "experience",
        "patterns": [
            "pengalaman", "pernah kerja", "magang", "internship", "kerja di mana", "kerja dimana aja",
            "riwayat kerja", "work experience", "where worked", "career", "karir", "riwayat pekerjaan",
            "pernah magang di mana", "pengalaman kerja", "pernah magang",
        ],
        "id": [
            "Pengalaman Kenza:\n- Data Analyst Intern di Amigo Group (lewat MBKM)\n- Telecom Data Analyst di Telkom Landmark Surabaya\n- Freelance Graphic Designer di CV. Dharma Syafa Kreasi\n- Campus Ambassador MySkill\n\nMagang data-nya dijalani secara hybrid.",
        ],
        "en": [
            "Kenza's experience:\n- Data Analyst Intern at Amigo Group (via MBKM)\n- Telecom Data Analyst at Telkom Landmark Surabaya\n- Freelance Graphic Designer at CV. Dharma Syafa Kreasi\n- MySkill Campus Ambassador\n\nThe data internships were done in a hybrid setup.",
        ],
    },
    {
        "tag": "telkom",
        "patterns": [
            "telkom", "magang di telkom", "internship telkom", "kerja di telkom", "telkom indonesia",
            "telkom landmark", "bts",
        ],
        "id": [
            "Di Telkom (Telkom Landmark Surabaya), Kenza jadi Telecom Data Analyst. Dia ngumpulin dan nganalisis data performa BTS di Jawa Timur dan Madura buat dukung keputusan operasional, pakai Python, SQL, dan Power BI.",
        ],
        "en": [
            "At Telkom (Telkom Landmark Surabaya), Kenza worked as a Telecom Data Analyst. He collected and analyzed BTS performance data across East Java and Madura to support operational decisions, using Python, SQL, and Power BI.",
        ],
    },
    {
        "tag": "amigo",
        "patterns": [
            "amigo", "amigo group", "magang di amigo", "internship amigo", "kerja di amigo",
        ],
        "id": [
            "Di Amigo Group, Kenza magang sebagai Data Analyst lewat program MBKM. Dia ngelola dan nganalisis data bisnis di lingkungan ritel buat mendukung pengambilan keputusan, dikerjakan secara hybrid.",
        ],
        "en": [
            "At Amigo Group, Kenza interned as a Data Analyst through the MBKM program. He managed and analyzed business data in a retail setting to support decision-making, done in a hybrid setup.",
        ],
    },
    {
        "tag": "clients",
        "patterns": [
            "klien", "client", "clients", "klien kenza", "wonderland", "luwes", "luwes group",
            "cardinal", "klien yang ditangani",
        ],
        "id": [
            "Sebagai freelance graphic designer, Kenza pernah menangani klien seperti Wonderland (hiburan & event), Luwes Group (ritel), dan Cardinal (fashion). Pekerjaannya bikin poster, banner, backdrop, dan konten promosi.",
        ],
        "en": [
            "As a freelance graphic designer, Kenza has worked with clients like Wonderland (entertainment & events), Luwes Group (retail), and Cardinal (fashion). The work included posters, banners, backdrops, and promotional content.",
        ],
    },
    {
        "tag": "education",
        "patterns": [
            "pendidikan", "sekolah", "smk", "kuliah", "kampus", "pendidikan terakhir",
            "latar belakang pendidikan", "education", "background", "latar belakang", "riwayat pendidikan",
            "almamater", "sekolah di mana", "lulusan mana", "rekayasa perangkat lunak", "rpl", "uns", "studi",
        ],
        "id": [
            "Kenza sekarang menempuh S1 Sains Data di Universitas Sebelas Maret (sejak 2023). Sebelumnya, dia lulusan Rekayasa Perangkat Lunak (RPL) dari SMK Telkom Malang. Dari sanalah fondasi teknisnya terbentuk.",
        ],
        "en": [
            "Kenza is currently pursuing a Bachelor's in Data Science at Universitas Sebelas Maret (since 2023). Before that, he graduated in Software Engineering (RPL) from SMK Telkom Malang, where his technical foundation was formed.",
        ],
    },
    {
        "tag": "contact",
        "patterns": [
            "kontak", "hubungi", "email", "cara menghubungi", "mau kontak", "bisa dihubungi",
            "contact", "reach out", "get in touch", "gmail", "linkedin", "github",
            "nomor telepon", "sosial media", "social media", "kontaknya apa",
        ],
        "id": [
            "Kamu bisa menghubungi Kenza lewat:\n- Email: kenzaathallah.wijaya@gmail.com\n- LinkedIn: linkedin.com/in/kenzaathallah\n- GitHub: github.com/K4ZED\n\nAtau langsung scroll ke bagian Kontak di bawah.",
        ],
        "en": [
            "You can reach Kenza via:\n- Email: kenzaathallah.wijaya@gmail.com\n- LinkedIn: linkedin.com/in/kenzaathallah\n- GitHub: github.com/K4ZED\n\nOr just scroll down to the Contact section.",
        ],
    },
    {
        "tag": "availability",
        "patterns": [
            "tersedia", "open to work", "bisa direkrut", "available", "sedang cari kerja",
            "apakah tersedia", "lagi cari kerja", "hire kenza", "hire", "rekrut", "apakah open",
            "apakah menerima tawaran", "freelance", "terbuka untuk kerja", "lagi open", "bisa di hire",
        ],
        "id": [
            "Iya, Kenza lagi terbuka buat peluang kerja dan magang, full-time maupun part-time, di Data Analytics, Data Science, Backend, atau Graphic Design. Kalau tertarik, langsung hubungi via email atau LinkedIn ya!",
        ],
        "en": [
            "Yes, Kenza is open to job and internship opportunities, full-time or part-time, in Data Analytics, Data Science, Backend, or Graphic Design. If you're interested, reach out via email or LinkedIn!",
        ],
    },
    {
        "tag": "years_experience",
        "patterns": [
            "berapa tahun pengalaman", "sudah berapa lama", "pengalaman berapa tahun",
            "how many years", "how long experience", "lama pengalaman", "berapa lama di tech",
        ],
        "id": [
            "Kenza sudah 5+ tahun di dunia teknologi, sejak 2020. Rentangnya luas: dari Data Analytics, Data Science, Backend Development, sampai Graphic Design.",
        ],
        "en": [
            "Kenza has 5+ years in tech, since 2020. The range is broad: from Data Analytics and Data Science to Backend Development and Graphic Design.",
        ],
    },
    {
        "tag": "farewell",
        "patterns": [
            "bye", "dadah", "selamat tinggal", "sampai jumpa", "terima kasih", "makasih", "thanks",
            "thank you", "oke thanks", "ok bye", "ok makasih", "sudah cukup", "itu saja", "cukup",
            "ok terima kasih", "terimakasih", "thx", "see you", "good bye",
        ],
        "id": [
            "Sama-sama! Semoga harimu menyenangkan, mampir lagi kapan aja ya.",
            "Terima kasih sudah ngobrol! Kalau ada yang mau ditanya lagi, aku di sini.",
        ],
        "en": [
            "You're welcome! Have a great day, and drop by anytime.",
            "Thanks for chatting! If you have more questions, I'm right here.",
        ],
    },
]

FALLBACK = {
    "id": [
        "Hmm, aku belum nangkep maksudnya. Coba tanya soal skill, project, pengalaman, pendidikan, atau kontak Kenza ya.",
        "Maaf, itu agak di luar yang aku tahu. Tapi aku bisa cerita soal skill, project, atau pengalaman Kenza. Mau yang mana?",
    ],
    "en": [
        "Hmm, I didn't quite catch that. Try asking about Kenza's skills, projects, experience, education, or contact.",
        "Sorry, that's a bit outside what I know. But I can tell you about Kenza's skills, projects, or experience. Which one?",
    ],
}

# Word hints used for a lightweight ID/EN language guess.
_EN_HINTS = {
    "what", "who", "how", "why", "when", "where", "are", "is", "am", "do", "does", "you", "your",
    "yourself", "me", "my", "the", "can", "could", "tell", "about", "skills", "skill", "experience",
    "project", "projects", "contact", "hire", "available", "work", "worked", "education", "background",
    "hello", "hi", "hey", "thanks", "thank", "please", "show", "reach", "give", "list", "have", "has",
    "good", "morning", "afternoon", "evening", "bye", "goodbye", "of", "for",
}
_ID_HINTS = {
    "apa", "siapa", "kamu", "kah", "apakah", "bisa", "dia", "yang", "kerja", "gimana", "gmn", "tolong",
    "dong", "kak", "saya", "aku", "punya", "mau", "ingin", "keahlian", "kemampuan", "pengalaman",
    "pendidikan", "kontak", "hubungi", "halo", "hai", "makasih", "terima", "proyek", "ceritain",
    "ceritakan", "nya", "aja", "sih", "buat", "soal", "tentang",
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
    # every pattern token present (scattered order, typo-tolerant)
    matched = sum(1 for t in pw if _tok_match(t, msg_tokens))
    if matched == n:
        return 0.9, n
    if matched:
        # partial coverage stays below the answer threshold on its own
        return 0.6 * (matched / n), matched
    return 0.0, 0


def _best_intent(msg_words, msg_tokens: set):
    """Return (intent, confidence) for the best-scoring intent, tie-broken by specificity."""
    best = (0.0, 0)
    best_intent = None
    for intent in INTENTS:
        for pattern in intent["patterns"]:
            sc = _score(msg_words, msg_tokens, pattern)
            if sc > best:
                best = sc
                best_intent = intent
    return best_intent, best[0]


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


def get_response(message: str, threshold: float = 0.6) -> str:
    """Return a natural, language-matched response for the best intent.

    Lightweight keyword + fuzzy matcher: no ML model and no heavy dependencies, so it
    starts instantly and deploys anywhere. Responses vary per call to avoid sounding canned.
    """
    msg = _norm(message)
    if not msg:
        return random.choice(FALLBACK["id"])
    msg_words = msg.split()
    msg_tokens = set(msg_words)
    lang = _detect_lang(msg_tokens)

    best_intent, conf = _best_intent(msg_words, msg_tokens)
    if best_intent is None or conf < threshold:
        return random.choice(FALLBACK[lang])

    # fall back to the other language if an intent lacks variants in the detected one
    variants = best_intent.get(lang) or best_intent.get("id") or best_intent.get("en")
    return random.choice(variants)
