import os

os.chdir(r"C:\Users\ishan\Documents\Projects\Awesome-Small-Language-Models")

os.makedirs("assets", exist_ok=True)

svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2a2a72" />
      <stop offset="100%" stop-color="#009ffd" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)" rx="15" ry="15" />
  
  <text x="50%" y="40%" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#ffffff" text-anchor="middle" filter="url(#glow)">
    Awesome Small Language Models
  </text>
  
  <text x="50%" y="70%" font-family="Arial, sans-serif" font-size="24" fill="#e0e0e0" text-anchor="middle">
    <tspan>History, Progression, Variants &amp; Applications</tspan>
  </text>
  
  <circle cx="100" cy="100" r="10" fill="#ffeb3b">
    <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="cy" values="100;90;100" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="100" r="10" fill="#00e5ff">
    <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="cy" values="100;110;100" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>"""

with open(os.path.join("assets", "banner.svg"), "w") as f:
    f.write(svg_content)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

replacements = {
    "# Awesome-Small-Language-Models": '<p align="center"><img src="./assets/banner.svg" alt="Banner"></p>\n\n# 🌟 Awesome-Small-Language-Models 🚀',
    "## Small Language Models (SLMs): History, Progression, Variants, & Applications": "## 🧠 Small Language Models (SLMs): History, Progression, Variants, & Applications",
    "## 1. The Macro Chronological Evolution": "## 📅 1. The Macro Chronological Evolution",
    "## 2. Core Functional & Compression Variants": "## ⚙️ 2. Core Functional & Compression Variants",
    "## 3. The Edge Inference & Quantization Matrix": "## 📉 3. The Edge Inference & Quantization Matrix",
    "## 4. Production Engineering Challenges & Mitigations": "## 🛡️ 4. Production Engineering Challenges & Mitigations",
    "## 5. Frontier Real-World Industrial Applications": "## 🌍 5. Frontier Real-World Industrial Applications",
    "## References": "## 📚 References"
}

for old, new in replacements.items():
    readme = readme.replace(old, new)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
