// Cek device touch biar animasi mouse nggak ganggu di HP
const isTouchDevice =
  "ontouchstart" in window || navigator.maxTouchPoints > 0;

// =======================
// 1. Smooth scroll navbar
// =======================
document.querySelectorAll('.nav-links a[href^="#"]').forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const targetId = this.getAttribute("href");
    const target = document.querySelector(targetId);
    if (!target) return;

    const offset = 70; // tinggi kira2 navbar
    const top = target.getBoundingClientRect().top + window.scrollY - offset;

    window.scrollTo({
      top,
      behavior: "smooth",
    });
  });
});

// ===================================
// 2. Scroll reveal untuk tiap section
// ===================================
const animatedSections = document.querySelectorAll(".section-animate");

const observerOptions = {
  threshold: 0.18,
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

animatedSections.forEach((sec) => observer.observe(sec));

// ====================================
// 3. Parallax halus untuk hero-avatar
// ====================================
const heroAvatar = document.querySelector(".hero-avatar");

window.addEventListener("scroll", () => {
  if (!heroAvatar) return;
  const scrollY = window.scrollY || window.pageYOffset;
  const offset = scrollY * 0.04; // makin besar makin “melayang”
  heroAvatar.style.transform = `translateY(${offset}px)`;
});

// ==========================================
// 4. Tilt 3D lembut buat kartu profile hero
// ==========================================
const avatarFrame = document.querySelector(".avatar-frame");

if (avatarFrame && !isTouchDevice) {
  avatarFrame.addEventListener("mousemove", (e) => {
    const rect = avatarFrame.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width; // 0 - 1
    const y = (e.clientY - rect.top) / rect.height; // 0 - 1

    const rotateX = (y - 0.5) * 10; // derajat
    const rotateY = (x - 0.5) * -10;

    avatarFrame.style.transform = `
      perspective(900px)
      rotateX(${rotateX}deg)
      rotateY(${rotateY}deg)
    `;
  });

  avatarFrame.addEventListener("mouseleave", () => {
    avatarFrame.style.transform = "perspective(900px) rotateX(0deg) rotateY(0deg)";
  });
}

// ==================================================
// 5. Scroll progress bar tipis di paling atas layar
// ==================================================
(function createScrollProgressBar() {
  const bar = document.createElement("div");
  bar.id = "scroll-progress-bar";
  Object.assign(bar.style, {
    position: "fixed",
    top: "0",
    left: "0",
    height: "2px",
    width: "0%",
    background:
      "linear-gradient(to right, #60a5fa, #93c5fd)",
    zIndex: "60",
    pointerEvents: "none",
    transition: "width 0.1s linear",
  });
  document.body.appendChild(bar);

  const updateProgress = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = progress + "%";
  };

  window.addEventListener("scroll", updateProgress);
  window.addEventListener("resize", updateProgress);
  updateProgress();
})();

// ==========================
// 6. Toggle bahasa ID / EN
// ==========================
const langToggle = document.getElementById("langToggle");
const langButtons = document.querySelectorAll(".lang-btn");
const body = document.body;

if (langToggle) {
  langToggle.addEventListener("click", (e) => {
    const btn = e.target.closest(".lang-btn");
    if (!btn) return;
    const lang = btn.getAttribute("data-lang") || "id";

    body.setAttribute("data-lang", lang);

    langButtons.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
  });
}
