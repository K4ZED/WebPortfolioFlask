# Update chatbot (chatbot.py) sesuai konten terbaru

Chatbot di route `/chat` (rule-based, `chatbot.py`) masih pakai data lama. Update supaya jawabannya sama dengan isi homepage baru dan CV terbaru (`static/cv/CV-Kenza-Athallah-Nandana-Wijaya.pdf`). Kalau ada konflik, yang dipakai: homepage (`templates/index.html`) dulu, lalu CV.

## Langkah

1. Baca `chatbot.py` dan jelaskan singkat cara kerjanya: daftar intent, cara matching (keyword/regex/fuzzy), bahasa yang didukung, dan fallback-nya. **Tunggu OK dariku sebelum mengubah apa pun.**
2. Pisahkan semua fakta tentang aku ke satu tempat (misalnya dict `PROFILE` di bagian atas `chatbot.py`, atau `data/profile.json`). Semua jawaban mengambil data dari sana, jadi lain kali cukup update satu tempat.
3. Update dan lengkapi intent berikut. Pertahankan bahasa yang sudah didukung (kalau sebelumnya ID dan EN, tetap dua-duanya):
   - **Profil / siapa kamu**: AI Specialist & Systems Engineer, Data Science UNS (2023 sampai 2027), Surakarta.
   - **Pengalaman**: 5 posisi persis seperti di section About homepage.
   - **Projects**: daftar 12 project (nama + satu kalimat). Tambahkan juga intent per project untuk yang besar, minimal Eko, Podclip, Geniuz, Gym PWA dan AI Skill Mapping (contoh pertanyaan: "Eko itu apa?", "ceritain soal Podclip"). Sertakan link kalau ada (Eko: t.me/Eko_BPSbot).
   - **Skill / tech stack**: sesuai bagian Tech Stack di CV (Bahasa, AI & LLM, Data & ML, Visualisasi, Web, Cloud & Tools).
   - **Pendidikan**: UNS dan SMK Telkom Malang.
   - **Sertifikasi & award**: 3 Best Project Award (CODER Telkom University 2025), TOEFL 513.
   - **Layanan / kerja sama**: terbuka untuk AI, automation dan fullstack work.
   - **Kontak**: email, LinkedIn, GitHub, link download CV baru.
   - **Clients**: Wonderland, Luwes Group, Cardinal.
4. Hapus atau perbarui jawaban yang sudah tidak relevan (misalnya role lama "Graphic Designer" sebagai fokus utama, data pengalaman lama, project lama).
5. Fallback: kalau pertanyaan tidak dikenali, jawab singkat lalu tawarkan 3 sampai 4 topik sebagai saran (Projects, Experience, Skills, Contact). Kalau widget-nya mendukung quick reply, tampilkan sebagai tombol.
6. Gaya jawaban: singkat, natural, orang pertama ("I build...", "Aku lagi..."), tanpa em dash (—) dan tanpa emoji.

## Testing

- Buat `tests/test_chatbot.py` (pytest) dengan minimal 2 pertanyaan per intent, termasuk variasi bahasa Indonesia dan Inggris serta typo ringan. Jalankan sampai semuanya lulus.
- Jalankan app secara lokal dan coba lewat chat widget di homepage: "siapa kamu", "what projects have you built", "Eko itu apa", "kontak", dan satu pertanyaan ngawur untuk cek fallback.
- Pastikan route lain (`/`, `/gh-data`) tidak berubah.

Tunjukkan ringkasan perubahan dan contoh 5 tanya jawab. Jangan commit sebelum aku cek.
