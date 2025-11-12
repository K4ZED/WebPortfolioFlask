const isTouchDevice =
  "ontouchstart" in window || navigator.maxTouchPoints > 0;

document.querySelectorAll('.nav-links a[href^="#"]').forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const targetId = this.getAttribute("href");
    const target = document.querySelector(targetId);
    if (!target) return;

    const header = document.querySelector(".navbar");
    const headerHeight = header ? header.offsetHeight : 0;
    const extraOffset = window.innerWidth <= 768 ? 12 : 4;
    const offset = headerHeight + extraOffset;

    const top =
      target.getBoundingClientRect().top + window.scrollY - offset;

    window.scrollTo({
      top,
      behavior: "smooth",
    });

    document.body.classList.remove("nav-open");
  });
});

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

const heroAvatar = document.querySelector(".hero-avatar");

window.addEventListener("scroll", () => {
  if (!heroAvatar) return;
  const scrollY = window.scrollY || window.pageYOffset;
  const offset = scrollY * 0.04;
  heroAvatar.style.transform = `translateY(${offset}px)`;
});

const avatarFrame = document.querySelector(".avatar-frame");

if (avatarFrame && !isTouchDevice) {
  avatarFrame.addEventListener("mousemove", (e) => {
    const rect = avatarFrame.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;
    const y = (e.clientY - rect.top) / rect.height;
    const rotateX = (y - 0.5) * 10;
    const rotateY = (x - 0.5) * -10;

    avatarFrame.style.transform = `
      perspective(900px)
      rotateX(${rotateX}deg)
      rotateY(${rotateY}deg)
    `;
  });

  avatarFrame.addEventListener("mouseleave", () => {
    avatarFrame.style.transform =
      "perspective(900px) rotateX(0deg) rotateY(0deg)";
  });
}

(function () {
  const bar = document.createElement("div");
  bar.id = "scroll-progress-bar";
  Object.assign(bar.style, {
    position: "fixed",
    top: "0",
    left: "0",
    height: "2px",
    width: "0%",
    background: "linear-gradient(to right, #60a5fa, #93c5fd)",
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

const langToggle = document.getElementById("langToggle");
const langButtons = document.querySelectorAll(".lang-btn");
const bodyEl = document.body;

if (langToggle) {
  langToggle.addEventListener("click", (e) => {
    const btn = e.target.closest(".lang-btn");
    if (!btn) return;
    const lang = btn.getAttribute("data-lang") || "id";

    bodyEl.setAttribute("data-lang", lang);

    langButtons.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
  });
}

const navToggle = document.getElementById("navToggle");
const navLinks = document.querySelector(".nav-links");

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    document.body.classList.toggle("nav-open");
  });
}

const projectCards = document.querySelectorAll(".project-card");

projectCards.forEach((card) => {
  if (isTouchDevice) return;

  card.addEventListener("mouseenter", () => {
    card.classList.add("is-hovered");
  });

  card.addEventListener("mouseleave", () => {
    card.classList.remove("is-hovered");
  });
});

const scrollTopBtn = document.getElementById("scrollTopBtn");

if (scrollTopBtn) {
  const toggleScrollTopBtn = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    if (scrollTop > 260) {
      scrollTopBtn.classList.add("visible");
    } else {
      scrollTopBtn.classList.remove("visible");
    }
  };

  window.addEventListener("scroll", toggleScrollTopBtn);
  window.addEventListener("resize", toggleScrollTopBtn);
  toggleScrollTopBtn();

  scrollTopBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}
