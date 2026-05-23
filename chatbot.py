import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

INTENTS = [
    {
        "tag": "greeting",
        "patterns": [
            "halo", "hai", "hello", "hi", "hey", "selamat pagi", "selamat siang", "selamat malam",
            "apa kabar", "halo kak", "hi there", "good morning", "good afternoon", "good evening",
            "hei", "haloo", "hellow"
        ],
        "response": "Halo! Saya Byte, asisten virtual Kenza. Ada yang ingin kamu tanyakan tentang portofolionya?"
    },
    {
        "tag": "farewell",
        "patterns": [
            "bye", "dadah", "selamat tinggal", "sampai jumpa", "terima kasih", "makasih", "thanks",
            "thank you", "oke thanks", "ok bye", "ok makasih", "sudah cukup", "itu saja", "cukup",
            "ok terima kasih", "terimakasih"
        ],
        "response": "Terima kasih sudah berkunjung! Semoga informasinya bermanfaat."
    },
    {
        "tag": "about",
        "patterns": [
            "siapa kamu", "siapa kenza", "siapa kazed", "ceritain tentang kamu", "perkenalkan diri",
            "who are you", "who is kenza", "tell me about yourself", "about kenza", "tentang kenza",
            "kamu siapa", "dia siapa", "profil kenza", "profil kazed", "bio kenza", "kenza itu siapa"
        ],
        "response": (
            "Kenza Athallah Nandana Wijaya (alias Kazed) adalah profesional teknologi dengan pengalaman "
            "lebih dari 5 tahun sejak 2020. Spesialisasinya mencakup:\n"
            "- Data Analytics & Data Science\n"
            "- Backend Development\n"
            "- Graphic Design\n\n"
            "Ia pernah magang sebagai Data Analyst di Telkom dan Amigo Group, keduanya secara hybrid."
        )
    },
    {
        "tag": "skills",
        "patterns": [
            "skill apa", "bisa apa", "keahlian apa", "kemampuan apa", "teknologi apa", "tools apa",
            "what skills", "what can you do", "tech stack", "what technology", "keahlian kenza",
            "dia bisa apa", "kamu bisa apa", "skill kenza", "kemampuan kenza", "list skill"
        ],
        "response": (
            "Kenza memiliki keahlian di 5 bidang utama:\n"
            "- Data Analyst: Python, SQL, Power BI, Excel\n"
            "- Data Science: TensorFlow, Scikit-learn, Pandas, NumPy\n"
            "- Data Engineering: ETL, PostgreSQL, pipeline data\n"
            "- Backend Dev: Go, FastAPI, Node.js, Flask\n"
            "- Graphic Design: Canva, Figma, Adobe Illustrator"
        )
    },
    {
        "tag": "data_analyst",
        "patterns": [
            "data analyst", "analisis data", "data analysis", "power bi", "visualisasi data",
            "data visualization", "skill data analyst", "pengalaman data", "excel data",
            "laporan data", "dashboard data", "reporting"
        ],
        "response": (
            "Sebagai Data Analyst, Kenza menggunakan Python, SQL, dan Power BI untuk mengelola data "
            "dari pengumpulan hingga visualisasi. Ia berpengalaman membangun dashboard dan laporan "
            "analitik dari pengalamannya di Telkom dan Amigo Group."
        )
    },
    {
        "tag": "data_science",
        "patterns": [
            "data science", "machine learning", "ml", "artificial intelligence", "deep learning",
            "tensorflow", "scikit-learn", "scikit learn", "neural network", "model ml",
            "ai kenza", "model prediksi", "klasifikasi", "regresi", "clustering"
        ],
        "response": (
            "Di bidang Data Science, Kenza menggunakan Python dengan library:\n"
            "TensorFlow, Scikit-learn, Pandas, NumPy, dan Jupyter Notebook\n"
            "untuk membangun model machine learning seperti klasifikasi, regresi, dan clustering."
        )
    },
    {
        "tag": "backend",
        "patterns": [
            "backend", "backend dev", "backend developer", "golang", "go lang", "fastapi",
            "nodejs", "node js", "flask backend", "rest api", "api development", "server side",
            "web backend", "backend development", "database", "postgresql", "microservice"
        ],
        "response": (
            "Untuk Backend Development, Kenza menggunakan:\n"
            "Go (Golang), FastAPI, Node.js, Flask\n"
            "Terbiasa membangun REST API dan bekerja dengan database PostgreSQL."
        )
    },
    {
        "tag": "graphic_design",
        "patterns": [
            "desain", "design", "grafis", "graphic design", "canva", "figma", "adobe", "illustrator",
            "poster", "banner", "visual design", "logo", "branding", "desain grafis", "ui design",
            "desain event"
        ],
        "response": (
            "Untuk Graphic Design, Kenza menggunakan Canva sebagai tool utama, "
            "dengan kemampuan dasar di Figma dan Adobe Illustrator "
            "untuk kebutuhan event dan branding."
        )
    },
    {
        "tag": "projects",
        "patterns": [
            "project apa", "portofolio", "karya", "hasil kerja", "apa saja projectnya", "contoh project",
            "what projects", "portfolio", "show me projects", "daftar project", "project kenza",
            "project yang sudah dibuat", "proyek"
        ],
        "response": (
            "Beberapa project Kenza:\n"
            "- BTS Performance Analysis: analisis performa jaringan dengan Python & Power BI\n"
            "- Web Dashboard: dashboard interaktif visualisasi data\n"
            "- P!NGFEST: website event dengan Next.js & Tailwind CSS\n"
            "- Pemoela Lab: company profile digital solution\n\n"
            "Cek bagian Projects di website untuk detail lebih lanjut."
        )
    },
    {
        "tag": "pingfest",
        "patterns": [
            "pingfest", "p!ngfest", "ping fest", "event website", "website event pingfest"
        ],
        "response": (
            "P!NGFEST adalah website event yang dibangun menggunakan Next.js dan Tailwind CSS. "
            "Dirancang dengan tampilan modern dan responsif untuk keperluan event."
        )
    },
    {
        "tag": "pemoela_lab",
        "patterns": [
            "pemoela", "pemoela lab", "digital solution", "company profile pemoela",
            "startup kenza", "perusahaan kenza"
        ],
        "response": (
            "Pemoela Lab adalah digital solution milik Kenza sendiri. "
            "Website company profile-nya dibangun dengan Next.js dan Tailwind CSS, "
            "menampilkan layanan dan profil perusahaan secara profesional."
        )
    },
    {
        "tag": "experience",
        "patterns": [
            "pengalaman", "pernah kerja", "magang", "internship", "kerja di mana", "riwayat kerja",
            "work experience", "where worked", "career", "karir", "riwayat pekerjaan",
            "pernah magang di mana", "pengalaman kerja"
        ],
        "response": (
            "Kenza memiliki pengalaman magang di:\n"
            "- Telkom Indonesia: Data Analyst (hybrid)\n"
            "- Amigo Group: Data Analyst (hybrid)\n\n"
            "Keduanya fokus pada pengelolaan dan visualisasi data menggunakan Python, SQL, dan Power BI."
        )
    },
    {
        "tag": "telkom",
        "patterns": [
            "telkom", "magang di telkom", "internship telkom", "kerja di telkom", "telkom indonesia"
        ],
        "response": (
            "Kenza pernah magang di Telkom Indonesia sebagai Data Analyst. "
            "Tugasnya meliputi pengelolaan, analisis, dan visualisasi data "
            "menggunakan Python, SQL, dan Power BI secara hybrid."
        )
    },
    {
        "tag": "amigo",
        "patterns": [
            "amigo", "amigo group", "magang di amigo", "internship amigo", "kerja di amigo"
        ],
        "response": (
            "Kenza juga pernah magang di Amigo Group sebagai Data Analyst. "
            "Pekerjaan dilakukan secara hybrid, mengelola dan memvisualisasikan data "
            "menggunakan Python, SQL, dan Power BI."
        )
    },
    {
        "tag": "education",
        "patterns": [
            "pendidikan", "sekolah", "smk", "pendidikan terakhir", "latar belakang pendidikan",
            "education", "background", "latar belakang", "riwayat pendidikan", "almamater",
            "sekolah di mana", "lulusan mana", "rekayasa perangkat lunak", "rpl"
        ],
        "response": (
            "Kenza memiliki latar belakang pendidikan dari SMK Telkom Malang, "
            "jurusan Rekayasa Perangkat Lunak (RPL). "
            "Fondasi teknis di bidang software engineering terbentuk dari sini."
        )
    },
    {
        "tag": "contact",
        "patterns": [
            "kontak", "hubungi", "email", "cara menghubungi", "mau kontak", "bisa dihubungi",
            "contact", "reach out", "get in touch", "gmail", "linkedin", "github",
            "nomor telepon", "sosial media", "social media"
        ],
        "response": (
            "Kamu bisa menghubungi Kenza melalui:\n"
            "- Email: kenzaathallah.wijaya@gmail.com\n"
            "- LinkedIn: linkedin.com/in/kenzaathallah\n"
            "- GitHub: github.com/K4ZED\n\n"
            "Atau scroll ke bagian Kontak di website ini."
        )
    },
    {
        "tag": "availability",
        "patterns": [
            "tersedia", "open to work", "bisa direkrut", "available", "sedang cari kerja",
            "apakah tersedia", "lagi cari kerja", "hire kenza", "rekrut", "apakah open",
            "apakah menerima tawaran", "freelance"
        ],
        "response": (
            "Ya, Kenza saat ini terbuka untuk peluang kerja dan magang, "
            "baik full-time maupun part-time, di bidang:\n"
            "Data Analytics, Data Science, Backend Development, maupun Graphic Design.\n\n"
            "Hubungi langsung via email atau LinkedIn."
        )
    },
    {
        "tag": "years_experience",
        "patterns": [
            "berapa tahun pengalaman", "sudah berapa lama", "pengalaman berapa tahun",
            "how many years", "how long experience", "lama pengalaman"
        ],
        "response": (
            "Kenza memiliki pengalaman lebih dari 5 tahun di dunia teknologi sejak 2020, "
            "mencakup Data Analytics, Data Science, Backend Development, dan Graphic Design."
        )
    },
]

FALLBACK = (
    "Maaf, saya kurang memahami pertanyaanmu.\n"
    "Coba tanyakan seputar: skill, project, pengalaman kerja, pendidikan, atau kontak Kenza."
)

_model = None
_encoded = None
_responses = None


def _ensure_loaded():
    global _model, _encoded, _responses
    if _model is not None:
        return
    _model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    patterns, responses = [], []
    for intent in INTENTS:
        for p in intent["patterns"]:
            patterns.append(p.lower())
            responses.append(intent["response"])
    _encoded = _model.encode(patterns, convert_to_numpy=True)
    _responses = responses


def get_response(message: str, threshold: float = 0.42) -> str:
    _ensure_loaded()
    vec = _model.encode([message.lower()], convert_to_numpy=True)
    sims = cosine_similarity(vec, _encoded)[0]
    best = int(np.argmax(sims))
    return _responses[best] if sims[best] >= threshold else FALLBACK
