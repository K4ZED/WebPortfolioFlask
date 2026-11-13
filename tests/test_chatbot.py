"""Tests for the rule-based chatbot (Byte) and the /chat route.

Run from the project root:  python -m pytest -q
"""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import chatbot  # noqa: E402
from chatbot import PROFILE, INTENTS, SUGGESTIONS, classify, get_reply  # noqa: E402


# (question, expected tag, expected language or None to skip the language check)
CASES = [
    # profile
    ("siapa kamu", "about", "id"),
    ("who are you", "about", "en"),
    ("tell me about yourself", "about", "en"),
    ("kenza itu siapa?", "about", "id"),
    ("perkenalkn diri dong", "about", "id"),  # typo
    # experience (all 5 roles)
    ("pengalaman kamu apa aja", "experience", "id"),
    ("what's your work experience", "experience", "en"),
    ("pengalamn kerja", "experience", "id"),  # typo
    ("kerja di mana sekarang?", "exp_dzakiyah", "id"),
    ("where do you work now", "exp_dzakiyah", "en"),
    ("ceritain soal dzakiyah store group", "exp_dzakiyah", "id"),
    ("are you a freelancer?", "exp_freelance", "en"),
    ("freelance fullstack kamu gimana", "exp_freelance", "id"),
    ("magang di amigo ngapain aja", "exp_amigo", "id"),
    ("what did you do at Amigo Group", "exp_amigo", "en"),
    ("pingfest itu apa", "exp_pingfest", "id"),
    ("tell me about P!NGFEST", "exp_pingfest", "en"),
    ("magang di telkom", "exp_telkom", "id"),
    ("what did you do at telkom landmark", "exp_telkom", "en"),
    # projects (list + one intent per project)
    ("what projects have you built", "projects", "en"),
    ("project kamu apa aja", "projects", "id"),
    ("projek kamu apa", "projects", "id"),  # typo
    ("Eko itu apa?", "project_eko", "id"),
    ("tell me about the eko telegram bot", "project_eko", "en"),
    ("ceritain soal Podclip", "project_podclip", "id"),
    ("what is podclp", "project_podclip", "en"),  # typo
    ("agent hq itu apa", "project_agent_hq", "id"),
    ("how does your AI agent home server work", "project_agent_hq", "en"),
    ("batik manekin studio itu apa", "project_batik", "id"),
    ("tell me about the mannequin catalog photo tool", "project_batik", "en"),
    ("geniuz itu apa", "project_geniuz", "id"),
    ("tell me about genius the tutoring platform", "project_geniuz", "en"),  # typo
    ("aplikasi gym kamu", "project_gym", "id"),
    ("what is the gym pwa", "project_gym", "en"),
    ("skripsi kamu tentang apa", "project_skill_mapping", "id"),
    ("tell me about your thesis", "project_skill_mapping", "en"),
    ("ai skill maping", "project_skill_mapping", None),  # typo
    ("prediksi demam berdarah", "project_dengue", "id"),
    ("dengue project", "project_dengue", None),
    ("pemetaan sawah", "project_paddy", None),
    ("paddy field mapping", "project_paddy", None),
    ("analisis sentimen kamu", "project_sentiment", "id"),
    ("social media sentiment project", "project_sentiment", None),
    ("java route finder itu apa", "project_route_finder", "id"),
    ("what is your route finder app", "project_route_finder", "en"),
    ("ml with flask", "project_ml_flask", None),
    ("is there a live demo", "project_ml_flask", "en"),
    # skills
    ("skill kamu apa", "skills", "id"),
    ("what are your skills", "skills", "en"),
    ("tech stak", "skills", None),  # typo
    ("bahasa pemrograman apa aja", "skills", "id"),
    # education
    ("pendidikan kamu", "education", "id"),
    ("where do you study", "education", "en"),
    ("kuliah di mana", "education", "id"),
    ("dulu smk di mana", "education", "id"),
    # certifications & awards
    ("sertifikat apa aja", "certifications", "id"),
    ("do you have any awards", "certifications", "en"),
    ("skor toefl kamu berapa", "certifications", "id"),
    ("sertifkasi", "certifications", None),  # typo
    # services
    ("bisa di hire?", "services", "id"),
    ("are you open to work", "services", "en"),
    ("mau kerja sama bikin chatbot", "services", "id"),
    # contact
    ("kontak", "contact", "id"),
    ("how can I contact you", "contact", "en"),
    ("emailnya apa", "contact", "id"),
    ("download cv", "contact", None),
    ("kontk", "contact", None),  # typo
    # clients
    ("klien kamu siapa aja", "clients", "id"),
    ("who are your clients", "clients", "en"),
    ("wonderland", "clients", None),
    # years
    ("sudah berapa lama di tech", "years_experience", "id"),
    ("how many years of experience do you have", "years_experience", "en"),
    # conversation
    ("halo", "greeting", "id"),
    ("hello there", "greeting", "en"),
    ("kamu bot?", "identity", "id"),
    ("what is byte", "identity", "en"),
    ("bisa bantu apa", "help", "id"),
    ("what can i ask", "help", "en"),
    ("apa kabar", "smalltalk", "id"),
    ("how are you", "smalltalk", "en"),
    ("makasih ya", "farewell", "id"),
    ("thank you", "farewell", "en"),
]


@pytest.mark.parametrize("question,tag,lang", CASES)
def test_classify(question, tag, lang):
    got_tag, conf, got_lang = classify(question)
    assert got_tag == tag, f"{question!r}: expected {tag}, got {got_tag} ({conf:.2f})"
    if lang:
        assert got_lang == lang, f"{question!r}: expected lang {lang}, got {got_lang}"


def test_every_intent_has_at_least_two_cases():
    counts = {}
    for _, tag, _ in CASES:
        counts[tag] = counts.get(tag, 0) + 1
    missing = [i["tag"] for i in INTENTS if counts.get(i["tag"], 0) < 2]
    assert not missing, f"intents with fewer than 2 test questions: {missing}"


@pytest.mark.parametrize("question", ["asdfgh qwerty", "berapa harga cabai hari ini", "what is the capital of France"])
def test_fallback_offers_quick_replies(question):
    reply = get_reply(question)
    assert reply["suggestions"], "fallback should come with quick replies"
    labels = {s["label"] for s in reply["suggestions"]}
    assert labels in ({"Projects", "Experience", "Skills", "Contact"}, {"Project", "Pengalaman", "Skill", "Kontak"})


@pytest.mark.parametrize("lang", ["id", "en"])
def test_suggestion_messages_route_to_the_right_intent(lang):
    expected = ["projects", "experience", "skills", "contact"]
    for sug, tag in zip(SUGGESTIONS[lang], expected):
        got_tag, _, got_lang = classify(sug["message"])
        assert got_tag == tag, sug
        assert got_lang == lang, sug


# ── content: answers follow PROFILE and the homepage ──────────────────────────
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿]")


def _all_answers():
    for intent in INTENTS:
        for lang in ("id", "en"):
            ans = intent["answer"]
            if callable(ans):
                yield intent["tag"], ans(lang)
            else:
                for v in ans[lang]:
                    yield intent["tag"], v
    for lang in ("id", "en"):
        for v in chatbot.FALLBACK[lang]:
            yield "fallback", v


def test_no_em_dash_or_emoji_anywhere():
    for tag, text in _all_answers():
        assert "—" not in text, f"em dash in {tag}"
        assert not EMOJI.search(text), f"emoji in {tag}"


def test_no_outdated_content():
    stale = ["Pemoela", "MySkill", "Campus Ambassador", "Dharma Syafa", "Web Dashboard", "BTS Performance Analysis"]
    for tag, text in _all_answers():
        for word in stale:
            assert word not in text, f"outdated '{word}' in {tag}"


def test_profile_matches_homepage():
    assert [e["role"] for e in PROFILE["experience"]] == [
        "AI Specialist", "Fullstack Engineer", "Retail Data Analyst Intern",
        "Coordinator of Technology", "Telecom Data Analyst Intern",
    ]
    assert len(PROFILE["projects"]) == 12
    assert PROFILE["projects"][0]["name"] == "Eko" and PROFILE["projects"][-1]["name"] == "ML with Flask"
    assert [c["name"] for c in PROFILE["clients"]] == ["Wonderland", "Luwes Group", "Cardinal"]


def test_experience_answer_lists_all_five_roles():
    for lang in ("id", "en"):
        text = get_reply("pengalaman kamu" if lang == "id" else "what's your work experience")["response"]
        for e in PROFILE["experience"]:
            assert e["role"] in text


def test_projects_answer_lists_all_twelve():
    text = get_reply("what projects have you built")["response"]
    for p in PROFILE["projects"]:
        assert p["name"] in text


def test_eko_answer_has_link():
    for q in ("Eko itu apa", "what is eko"):
        assert "t.me/Eko_BPSbot" in get_reply(q)["response"]


def test_contact_answer_has_all_channels_and_new_cv():
    text = get_reply("kontak")["response"]
    for v in ("kenzaathallah.wijaya@gmail.com", "linkedin.com/in/kenzaathallah", "github.com/K4ZED",
              "CV-Kenza-Athallah-Nandana-Wijaya.pdf"):
        assert v in text


def test_skills_answer_covers_cv_tech_stack():
    text = get_reply("what are your skills")["response"]
    for label in ("Languages", "AI & LLM", "Data & ML", "Visualization", "Web", "Cloud & Tools"):
        assert label in text


def test_certifications_answer():
    text = get_reply("do you have any awards")["response"]
    assert "CODER Telkom University" in text and "Best Project Award" in text and "513" in text


def test_answers_are_first_person():
    assert get_reply("who are you")["response"].startswith("I'm ")
    assert get_reply("siapa kamu")["response"].startswith("Aku ")


# ── routes ────────────────────────────────────────────────────────────────────
@pytest.fixture()
def client():
    import app as app_module
    app_module._gh_cache["data"] = '{"total":{},"contributions":[]}'
    app_module._gh_cache["ts"] = 10 ** 12  # fresh cache, so /gh-data makes no network call
    return app_module.app.test_client()


def test_chat_route_returns_response_and_suggestions(client):
    res = client.post("/chat", json={"message": "halo"})
    data = res.get_json()
    assert res.status_code == 200
    assert data["response"] and isinstance(data["suggestions"], list) and data["suggestions"]


def test_chat_route_rejects_empty_and_long_messages(client):
    assert client.post("/chat", json={"message": ""}).get_json()["response"] == "Pesan tidak valid."
    assert client.post("/chat", json={"message": "a" * 301}).get_json()["response"] == "Pesan tidak valid."


def test_other_routes_still_work(client):
    assert client.get("/").status_code == 200
    res = client.get("/gh-data")
    assert res.status_code == 200 and res.mimetype == "application/json"
