import os, re, json

BASE_DIR = "/Users/green/Downloads/Takealot Dishwasher"

HERO_CDN = "https://iili.io/oKDU5zu.jpg"
OPEN_CDN = "https://iili.io/oKDUvdN.jpg"

HERO_TITLE = "Samsung 14-Place Freestanding Stainless Steel Dishwasher with IntensiveWash (DW60M5070FS)"
HERO_MODEL = "DW60M5070FS/FA"
HERO_PRICE = "1,999"
HERO_PRICE_NUM = 1999
HERO_OLD_PRICE = "R 8,999"
STEP3_PRICE = 279

# 1. Update package.json
pkg_path = os.path.join(BASE_DIR, "package.json")
if os.path.exists(pkg_path):
    with open(pkg_path, "r") as f:
        pkg = json.load(f)
    pkg["name"] = "takealot-dishwasher"
    pkg["description"] = "Takealot South Africa Dishwasher Storefront & Automated Order Engine"
    with open(pkg_path, "w") as f:
        json.dump(pkg, f, indent=2)
    print("Updated package.json")

# 2. Update .env and .env.example
for env_name in [".env", ".env.example"]:
    epath = os.path.join(BASE_DIR, env_name)
    content = f"""PORT=3030
NODE_ENV=production
STORE_NAME=Takealot Dishwasher
GREENSEND_API_KEY=greensend_live_9b4a1f68e2
GREENSEND_SENDER_EMAIL=orders@takealot.co.za
DEFAULT_PRODUCT_TITLE={HERO_TITLE}
DEFAULT_PRODUCT_PRICE={HERO_PRICE_NUM}
DEFAULT_PRODUCT_IMAGE={HERO_CDN}
"""
    with open(epath, "w") as f:
        f.write(content)
    print(f"Updated {env_name}")

# 3. Clean and initialize data/
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)
with open(os.path.join(data_dir, "orders.json"), "w") as f:
    f.write("{}")
with open(os.path.join(data_dir, "abandoned_checkouts.json"), "w") as f:
    f.write("{}")
print("Initialized data/ storage files")

# 4. Update server.js
server_path = os.path.join(BASE_DIR, "server.js")
with open(server_path, "r", encoding="utf-8") as f:
    s = f.read()

# Port replacement
s = re.sub(r'const PORT = process\.env\.PORT \|\| \d+;', 'const PORT = process.env.PORT || 3030;', s)
s = re.sub(r'http://localhost:\d+', 'http://localhost:3030', s)

# Titles and products
s = s.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
s = s.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
s = s.replace("Samsung 300L Bottom Freezer Refrigerator", HERO_TITLE)
s = s.replace("Samsung 300L Refrigerator", HERO_TITLE)
s = s.replace("Bottom Freezer Refrigerator", "14-Place Dishwasher")
s = s.replace("Refrigerator", "Dishwasher")
s = s.replace("refrigerator", "dishwasher")

# Prices
s = s.replace("2199", "1999")
s = s.replace("2,199", "1,999")
s = s.replace("9999", "8999")
s = s.replace("9,999", "8,999")
s = s.replace("7800", "7000")
s = s.replace("7,800", "7,000")
s = s.replace("297", "279")

# Image URLs
s = re.sub(r'https://iili\.io/[a-zA-Z0-9_\-]+\.(?:jpg|png)', HERO_CDN, s)
s = s.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")
s = s.replace("imagens/samsung_fridge_2_open.jpg", "imagens/samsung_dishwasher_2_open.jpg")
s = s.replace("imagens/samsung_fridge_3_dispenser.jpg", "imagens/samsung_dishwasher_3_front.jpg")
s = s.replace("imagens/samsung_fridge_4_interior.jpg", "imagens/samsung_dishwasher_4_racks.jpg")

# Capacity logic in track-order
s = s.replace("code.includes('43') ? '432L' : (code.includes('25') ? '254L' : '300L')", "code.includes('BOSCH') ? '14-Place (Zeolith Inox)' : '14-Place Settings'")
s = s.replace("'300L'", "'14-Place Settings'")

with open(server_path, "w", encoding="utf-8") as f:
    f.write(s)
print("Updated server.js")

# 5. Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Title
html = re.sub(r'<title>.*?</title>', f'<title>{HERO_TITLE} ({HERO_MODEL}) | Takealot</title>', html)

# Breadcrumbs
html = re.sub(
    r'<div class="breadcrumb-bar".*?</div>',
    '<div class="breadcrumb-bar" style="padding: 10px 16px; font-size: 11.5px; color: #666; background: #fff; border-bottom: 1px solid #f0f0f0; display: flex; align-items: center; gap: 6px; overflow-x: auto; white-space: nowrap;">'
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Home</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Kitchen &amp; Large Appliances</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Large Appliances</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<span style="color: #333; font-weight: 500;">Dishwashers &amp; Built-In Appliances</span></div>',
    html,
    flags=re.DOTALL
)

# Product title
html = re.sub(
    r'<h1 class="product-title" id="main-product-title">.*?</h1>',
    f'<h1 class="product-title" id="main-product-title">{HERO_TITLE} ({HERO_MODEL})</h1>',
    html
)

# Carousel slides
carousel_replacement = """        <div class="carousel" id="carousel">
            <div class="carousel-slide"><img src="imagens/samsung_dishwasher_1_hero.jpg" alt="Samsung 14-Place Freestanding Stainless Steel Dishwasher Hero" /></div>
            <div class="carousel-slide"><img src="imagens/samsung_dishwasher_2_open.jpg" alt="Samsung Dishwasher Open Door with Cutlery Tray and Racks" /></div>
            <div class="carousel-slide"><img src="imagens/samsung_dishwasher_3_front.jpg" alt="Samsung Dishwasher Front Digital LED Control Panel" /></div>
            <div class="carousel-slide"><img src="imagens/samsung_dishwasher_4_racks.jpg" alt="Samsung Dishwasher Interior Spray Arms and Flexible Racks" /></div>
        </div>\n\n        <div class="dots-row" """

html = re.sub(r'<div class="carousel" id="carousel">.*?</div>\s*<div class="dots-row"', carousel_replacement, html, flags=re.DOTALL)

# Price display
html = re.sub(
    r'<span class="price-val" id="main-price-display">.*?</span>',
    f'<span class="price-val" id="main-price-display">R {HERO_PRICE}</span>',
    html
)
html = re.sub(
    r'<span class="price-old" id="main-old-price">.*?</span>',
    f'<span class="price-old" id="main-old-price">{HERO_OLD_PRICE}</span>',
    html
)
html = re.sub(
    r'<span class="bar-price" id="footer-price-display">.*?</span>',
    f'<span class="bar-price" id="footer-price-display">R {HERO_PRICE}</span>',
    html
)

# Variation pills
pills_replacement = """    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Model / Capacity: <strong id="selected-size-label">14-Place Inox (Samsung Hero)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-sliders" style="margin-right: 3px;"></i> Choose variant</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill" data-var-key="defy-13" onclick="selectProductVariation('defy-13')">
                Defy 13-Place Metallic <span class="pill-badge">R 1,399</span>
            </button>
            <button class="var-pill" data-var-key="hisense-14" onclick="selectProductVariation('hisense-14')">
                Hisense 14-Place Inox <span class="pill-badge">R 1,699</span>
            </button>
            <button class="var-pill active" data-var-key="samsung-14" onclick="selectProductVariation('samsung-14')">
                Samsung 14-Place Inox <span class="pill-badge" style="background: #007a3d;">Hot R 1,999</span>
            </button>
            <button class="var-pill" data-var-key="bosch-14" onclick="selectProductVariation('bosch-14')">
                Bosch Serie 6 Zeolith <span class="pill-badge">R 2,499</span>
            </button>
            <button class="var-pill" data-var-key="finish-bundle" onclick="selectProductVariation('finish-bundle')">
                14-Place + Finish 6-Mo Bundle <span class="pill-badge">R 2,199</span>
            </button>
        </div>
    </div>"""

html = re.sub(
    r'<div class="variation-selector-sec">.*?</div>\s*</div>\s*<!-- 6\. TakealotMORE Banner',
    f'{pills_replacement}\n\n    <!-- 6. TakealotMORE Banner',
    html,
    flags=re.DOTALL
)

# What's Hot carousel
hot_replacement = """    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What's Hot in Dishwashers</div>
        <div class="hot-carousel">
            <!-- Variation 1: Defy 13-Place -->
            <div class="hot-card" data-var-key="defy-13" onclick="selectProductVariation('defy-13', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_dishwasher_3_front.jpg" alt="Defy 13-Place Metallic Dishwasher" />
                </div>
                <div class="hot-title">Defy 13-Place Metallic Dishwasher (DDW242)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,399</span>
                    <span class="hot-old-price">R 5,499</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.7 (790)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 2: Hisense 14-Place -->
            <div class="hot-card" data-var-key="hisense-14" onclick="selectProductVariation('hisense-14', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">76%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_dishwasher_4_racks.jpg" alt="Hisense 14-Place Inox Dishwasher" />
                </div>
                <div class="hot-title">Hisense 14-Place Stainless Steel Dishwasher (H14DSS)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,699</span>
                    <span class="hot-old-price">R 6,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (1,120)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 3: Samsung 14-Place Hero -->
            <div class="hot-card active-selection" data-var-key="samsung-14" onclick="selectProductVariation('samsung-14', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">78%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_dishwasher_1_hero.jpg" alt="Samsung 14-Place Inox Dishwasher" />
                </div>
                <div class="hot-title">Samsung 14-Place IntensiveWash™ Dishwasher (DW60M5070FS)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,999</span>
                    <span class="hot-old-price">R 8,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (2,840)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 4: Bosch Serie 6 -->
            <div class="hot-card" data-var-key="bosch-14" onclick="selectProductVariation('bosch-14', true)">
                <div class="hot-badges">
                    <div class="badge-black">Zeolith</div>
                    <div class="badge-blue">82%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_dishwasher_1_hero.jpg" alt="Bosch Serie 6 14-Place Inox Dishwasher" />
                </div>
                <div class="hot-title">Bosch Serie 6 14-Place Zeolith Inox Dishwasher (SMS6ZCI00Z)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,499</span>
                    <span class="hot-old-price">R 13,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (530)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 5: Finish Bundle -->
            <div class="hot-card" data-var-key="finish-bundle" onclick="selectProductVariation('finish-bundle', true)">
                <div class="hot-badges">
                    <div class="badge-black">Bundle<br>Deal</div>
                    <div class="badge-blue">78%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_dishwasher_2_open.jpg" alt="Samsung 14-Place + Finish Quantum 6-Mo Bundle" />
                </div>
                <div class="hot-title">Samsung 14-Place + Finish Quantum 100x Tabs & Rinse Aid Bundle</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,199</span>
                    <span class="hot-old-price">R 9,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (610)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>
        </div>
    </div>"""

html = re.sub(
    r'<div class="category-hot-sec">.*?</div>\s*</div>\s*<!-- 8\. Divider -->',
    f'{hot_replacement}\n\n    <!-- 8. Divider -->',
    html,
    flags=re.DOTALL
)

# Alternate seller
html = re.sub(
    r'<div class="offer-seller-name">.*?</div>',
    '<div class="offer-seller-name">Culinary &amp; Kitchen Megastore SA</div>',
    html
)
html = re.sub(
    r'<div class="offer-price">R \d+[\d,]*</div>',
    '<div class="offer-price">R 2,099</div>',
    html
)

# Specs table
specs_replacement = """        <div class="spec-row">
            <span class="spec-label">Brand</span>
            <span class="spec-val">Samsung</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Model Number</span>
            <span class="spec-val" id="spec-model-number">DW60M5070FS/FA (IntensiveWash™)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Place Settings</span>
            <span class="spec-val" id="spec-screen-size">14 Place Settings (Flexible 3rd Cutlery Rack)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Washing Cycles</span>
            <span class="spec-val">7 Programs (Intensive 70°C, Auto, Eco, Quick 60-min, Delicate, Prewash, Hygiene)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Hygiene Sanitization</span>
            <span class="spec-val">Hygiene Rinsing 70°C (Eliminates 99.999% of Food Bacteria)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Water Consumption</span>
            <span class="spec-val">10.5 Litres per Eco Cycle (Saves up to 80% water vs handwashing)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Energy Efficiency</span>
            <span class="spec-val">A+ High Efficiency Rating (Low Loadshedding Inverter Draw)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Noise Level</span>
            <span class="spec-val">46 dBA (Whisper Quiet Sound Insulated Cavity)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Leak Protection</span>
            <span class="spec-val">AquaStop Full Flood Protection Sensor &amp; Safety Shutoff</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Interior Material</span>
            <span class="spec-val">Full Stainless Steel Interior Tub &amp; Triple Spray Arms</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Dimensions &amp; Weight</span>
            <span class="spec-val">598mm (W) x 845mm (H) x 600mm (D) | 48.5 kg</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Warranty</span>
            <span class="spec-val">24 Months Official Samsung South Africa Warranty</span>
        </div>"""

html = re.sub(
    r'<div class="spec-table">.*?</div>\s*</div>\s*<!-- Description Tab Content -->',
    f'<div class="spec-table">\n{specs_replacement}\n        </div>\n    </div>\n    <!-- Description Tab Content -->',
    html,
    flags=re.DOTALL
)

# Highlights ul
highlights_replacement = """<ul style="padding-left: 18px; margin-bottom: 8px; line-height: 1.5;">
                <li><strong>14 Place Settings Capacity:</strong> Easily accommodate large dinner sets, tall wine glasses, braai pots, and roasting pans with the flexible 3rd cutlery rack and adjustable upper basket.</li>
                <li><strong>IntensiveWash™ 70°C:</strong> High-pressure spray jets blast away stubborn burnt-on grease, braai marinade, and baked starch without pre-rinsing or scrubbing.</li>
                <li><strong>Hygiene Rinsing:</strong> Prolongs the final rinse and raises temperature to 70°C, delivering deep hygienic sanitization that eliminates 99.999% of bacteria.</li>
                <li><strong>Express 60-Minute Wash &amp; Dry:</strong> Thoroughly cleans and dries normally soiled dishes in just 1 hour, perfect for busy South African family dinners.</li>
                <li><strong>Extreme Water Saving:</strong> Uses only 10.5 litres of water per cycle — saving over 60 litres of municipal water compared to washing dishes in a kitchen sink.</li>
                <li><strong>AquaStop Leak Guard:</strong> Automatically cuts off the water supply at the inlet valve if a leak or hose rupture is detected, preventing water damage.</li>
                <li><strong>Fingerprint Resistant Inox:</strong> Elegant brushed stainless steel finish resists greasy smudge marks and keeps your modern kitchen looking spotless.</li>
            </ul>"""

html = re.sub(
    r'<ul style="padding-left: 18px; margin-bottom: 8px; line-height: 1.5;">.*?</ul>',
    highlights_replacement,
    html,
    flags=re.DOTALL
)

# Description tab content
desc_replacement = """    <div id="desc-tab-content" class="tab-content">
        <h3 style="font-size: 15px; margin-bottom: 10px; color: #222;">Spotless Clean, Hygienic Dishes with Minimal Water and Zero Effort</h3>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            The <strong>Samsung 14-Place Freestanding Stainless Steel Dishwasher (DW60M5070FS)</strong> takes the stress out of daily kitchen chores. Featuring <strong>IntensiveWash™</strong> technology and high-pressure dual spray arms, it dissolves tough grease, dried curry sauces, and burnt-on braai marinade from pans and cookware without needing pre-rinsing.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Hygiene Rinsing for Baby Bottles and Cookware:</strong> The dedicated Hygiene button extends the final rinse cycle and boosts the water temperature to 70°C, safely neutralizing 99.999% of germs and bacteria so baby bottles, chopping boards, and daily cutlery are clinically sanitized.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Flexible 3rd Cutlery Rack &amp; Tall Pot Storage:</strong> The height-adjustable upper basket can be raised or lowered by 5cm with a simple lever, creating generous clearance for 30cm soup pots and tall champagne flutes below, while the dedicated top rack keeps knives and forks organized for optimal wash exposure.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555;">
            <strong>Engineered for South African Water &amp; Power Savings:</strong> Consuming just 10.5 litres of water per Eco cycle with an A+ energy rating, it dramatically reduces your monthly water and electricity bills while operating at an ultra-quiet 46 dBA library level.
        </p>
    </div>"""

html = re.sub(
    r'<div id="desc-tab-content" class="tab-content">.*?</div>\s*</div>\s*<!-- 14\. Customer Reviews',
    f'{desc_replacement}\n    </div>\n    <!-- 14. Customer Reviews',
    html,
    flags=re.DOTALL
)

# Review filter chips
chips_replacement = """<div class="review-filter-chips">
            <button class="review-chip active" onclick="filterReviewsCategory(this, 'all')">All (2,840)</button>
            <button class="review-chip" onclick="filterReviewsCategory(this, '5star')">5 Stars (2,710)</button>
            <button class="review-chip" onclick="filterReviewsCategory(this, 'verified')">Verified Buyers (2,805)</button>
            <button class="review-chip" onclick="filterReviewsCategory(this, 'intensive')">IntensiveWash™ (920)</button>
            <button class="review-chip" onclick="filterReviewsCategory(this, 'hygiene')">Hygiene 70°C (680)</button>
            <button class="review-chip" onclick="filterReviewsCategory(this, 'quiet')">Quiet 46dB (540)</button>
        </div>"""

html = re.sub(r'<div class="review-filter-chips">.*?</div>', chips_replacement, html, flags=re.DOTALL)

# 14 Customer Reviews
reviews_replacement = """        <div class="reviews-list-container">
            <!-- Review 1 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Claire van der Walt - 19 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">47</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Tackles oily Sunday braai pans effortlessly. The IntensiveWash mode removes baked grease completely...</span>
                    <span class="review-full" style="display: none;">Tackles oily Sunday braai pans effortlessly. The IntensiveWash mode removes baked grease completely without pre-rinsing. Glasses come out sparkling with zero water spots. R 1,999 on Takealot was the best bargain of the year in Sandton!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Tebogo Molefe - 16 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">38</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Massive water savings. Our municipal water bill in Cape Town dropped by almost R 300 a month...</span>
                    <span class="review-full" style="display: none;">Massive water savings. Our municipal water bill in Cape Town dropped by almost R 300 a month. It uses only 10.5 litres compared to running the tap. The 14-place capacity fits all dishes for a family of 5 in one daily cycle.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Pravin Naidoo - 13 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">31</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Extremely quiet operation at 46 dBA. You can barely hear it running in our open plan Durban lounge...</span>
                    <span class="review-full" style="display: none;">Extremely quiet operation at 46 dBA. You can barely hear it running in our open plan Durban lounge while watching television. The Hygiene 70°C rinse gives peace of mind for sanitizing baby bottles and cutting boards.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Henk Venter - 10 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">24</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The 3rd cutlery rack at the top is brilliant. Saves so much space in the bottom basket for large pots...</span>
                    <span class="review-full" style="display: none;">The 3rd cutlery rack at the top is brilliant. Saves so much space in the bottom basket for large pots and pans. Height adjustable middle basket lets tall wine glasses stand upright easily in Pretoria East.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Lindiwe Dlamini - 07 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">36</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Takealot delivery was swift and seamless in Centurion. The delivery team carried it right into my kitchen...</span>
                    <span class="review-full" style="display: none;">Takealot delivery was swift and seamless in Centurion. The delivery team carried it right into my kitchen. Connected water inlet and drain hose in 10 minutes. First wash came out immaculate. 10/10 service.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 6 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Marnus Joubert - 04 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">19</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Express 60-minute wash is perfect for dinner parties. Washes and dries everything in exactly an hour...</span>
                    <span class="review-full" style="display: none;">Express 60-minute wash is perfect for dinner parties in Stellenbosch. Washes and dries everything in exactly an hour so you can reload dessert plates immediately. Stainless steel finish is top tier.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 7 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Zaid Patel - 01 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">28</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Curry stained white ceramic plates came out pure white. Zero grease film left behind...</span>
                    <span class="review-full" style="display: none;">Curry stained white ceramic plates came out pure white. Zero grease film left behind. The AquaStop sensor provides reassurance against flooding in our newly renovated Johannesburg townhouse.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 8 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Annelize Smit - 28 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">22</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Works like a charm with our solar inverter setup. A+ energy rating draws minimal watts during Eco cycle...</span>
                    <span class="review-full" style="display: none;">Works like a charm with our solar inverter setup. A+ energy rating draws minimal watts during Eco cycle, allowing us to run it even during daytime loadshedding in Bloemfontein without overloading the batteries.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 9 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Bongani Sithole - 25 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">33</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Replaced a 10-year-old noisy dishwasher. This Samsung DW60 is in a completely different league...</span>
                    <span class="review-full" style="display: none;">Replaced a 10-year-old noisy dishwasher. This Samsung DW60 is in a completely different league. Touch controls on the front panel are responsive and the LED display clearly shows remaining time. R 1,999 is unbeatable value.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 10 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Gillian Meyer - 21 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">18</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Full stainless steel tub inside. No cheap plastic liner that smells after a few months...</span>
                    <span class="review-full" style="display: none;">Full stainless steel tub inside. No cheap plastic liner that smells after a few months. Cleans roasting pans, baking trays, and baby bottles thoroughly. Very happy with Takealot delivery in Gqeberha.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 11 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Kobus van Wyk - 17 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">26</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Half load wash option is very handy on days when we don't have enough dishes to fill all 14 settings...</span>
                    <span class="review-full" style="display: none;">Half load wash option is very handy on days when we don't have enough dishes to fill all 14 settings. Saves water and electricity automatically. Samsung reliability with 2-year warranty in Paarl.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 12 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Nomsa Khumalo - 13 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">29</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Fingerprint resistant finish stays looking brand new even with kids in the house in Roodepoort...</span>
                    <span class="review-full" style="display: none;">Fingerprint resistant finish stays looking brand new even with kids in the house in Roodepoort. Plates dry completely without water marks thanks to the auto condensation drying. Recommended to all my friends.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 13 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Dirk Coetzee - 09 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">34</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">R 1,999 on promotion was an absolute steal for a 14-place stainless steel machine in Nelspruit...</span>
                    <span class="review-full" style="display: none;">R 1,999 on promotion was an absolute steal for a 14-place stainless steel machine in Nelspruit. Takealot delivery took only 48 hours. The package arrived in flawless condition. 5 stars all the way.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 14 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Shireen Chetty - 04 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">27</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The cutlery basket and foldable plate tines make loading awkward casseroles simple in Chatsworth...</span>
                    <span class="review-full" style="display: none;">The cutlery basket and foldable plate tines make loading awkward casseroles simple in Chatsworth. Finish detergent pods dissolve completely without leaving residue. Best kitchen upgrade of 2026!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>
        </div>"""

html = re.sub(r'<div class="reviews-list-container">.*?</div>\s*</div>\s*<!-- Write a Review Button', f'{reviews_replacement}\n    </div>\n    <!-- Write a Review Button', html, flags=re.DOTALL)

# Javascript productVariations dictionary in index.html
js_variations = """    const productVariations = {
        "defy-13": {
            id: "defy-13",
            size: "Defy 13-Place",
            title: "Defy 13-Place Metallic Freestanding Dishwasher (DDW242)",
            price: "1399",
            oldPrice: "R 5,499",
            discount: "75%<br>OFF",
            credit: "R 116 p/m x 12 months",
            ebucks: "eB13,990",
            miles: "13,990",
            image: "imagens/samsung_dishwasher_3_front.jpg",
            images: [
                "imagens/samsung_dishwasher_3_front.jpg",
                "imagens/samsung_dishwasher_1_hero.jpg",
                "imagens/samsung_dishwasher_2_open.jpg",
                "imagens/samsung_dishwasher_4_racks.jpg"
            ],
            screenSizeSpec: "13 Place Settings (Metallic)",
            modelSpec: "DDW242"
        },
        "hisense-14": {
            id: "hisense-14",
            size: "Hisense 14-Place",
            title: "Hisense 14-Place Stainless Steel Dishwasher (H14DSS)",
            price: "1699",
            oldPrice: "R 6,999",
            discount: "76%<br>OFF",
            credit: "R 141 p/m x 12 months",
            ebucks: "eB16,990",
            miles: "16,990",
            image: "imagens/samsung_dishwasher_4_racks.jpg",
            images: [
                "imagens/samsung_dishwasher_4_racks.jpg",
                "imagens/samsung_dishwasher_1_hero.jpg",
                "imagens/samsung_dishwasher_2_open.jpg",
                "imagens/samsung_dishwasher_3_front.jpg"
            ],
            screenSizeSpec: "14 Place Settings (Inox)",
            modelSpec: "H14DSS"
        },
        "samsung-14": {
            id: "samsung-14",
            size: "Samsung 14-Place (Hero)",
            title: "Samsung 14-Place Freestanding Stainless Steel Dishwasher with IntensiveWash (DW60M5070FS)",
            price: "1999",
            oldPrice: "R 8,999",
            discount: "78%<br>OFF",
            credit: "R 166 p/m x 12 months",
            ebucks: "eB19,990",
            miles: "19,990",
            image: "imagens/samsung_dishwasher_1_hero.jpg",
            images: [
                "imagens/samsung_dishwasher_1_hero.jpg",
                "imagens/samsung_dishwasher_2_open.jpg",
                "imagens/samsung_dishwasher_3_front.jpg",
                "imagens/samsung_dishwasher_4_racks.jpg"
            ],
            screenSizeSpec: "14 Place Settings (IntensiveWash™ 70°C)",
            modelSpec: "DW60M5070FS/FA"
        },
        "bosch-14": {
            id: "bosch-14",
            size: "Bosch Serie 6 Zeolith",
            title: "Bosch Serie 6 14-Place Zeolith Inox Dishwasher (SMS6ZCI00Z)",
            price: "2499",
            oldPrice: "R 13,999",
            discount: "82%<br>OFF",
            credit: "R 208 p/m x 12 months",
            ebucks: "eB24,990",
            miles: "24,990",
            image: "imagens/samsung_dishwasher_1_hero.jpg",
            images: [
                "imagens/samsung_dishwasher_1_hero.jpg",
                "imagens/samsung_dishwasher_2_open.jpg",
                "imagens/samsung_dishwasher_3_front.jpg",
                "imagens/samsung_dishwasher_4_racks.jpg"
            ],
            screenSizeSpec: "14 Place Settings (Zeolith PerfectDry)",
            modelSpec: "SMS6ZCI00Z"
        },
        "finish-bundle": {
            id: "finish-bundle",
            size: "14-Place + Finish Bundle",
            title: "Samsung 14-Place Dishwasher + Finish Quantum 100x Tabs & Rinse Aid Bundle",
            price: "2199",
            oldPrice: "R 9,999",
            discount: "78%<br>OFF",
            credit: "R 183 p/m x 12 months",
            ebucks: "eB21,990",
            miles: "21,990",
            image: "imagens/samsung_dishwasher_2_open.jpg",
            images: [
                "imagens/samsung_dishwasher_2_open.jpg",
                "imagens/samsung_dishwasher_1_hero.jpg",
                "imagens/samsung_dishwasher_3_front.jpg",
                "imagens/samsung_dishwasher_4_racks.jpg"
            ],
            screenSizeSpec: "14 Place Settings + 6-Month Finish Kit",
            modelSpec: "DW60M5070FS-BNDL"
        }
    };"""

html = re.sub(
    r'const productVariations = \{.*?\n\s*\};\s*let selectedVariationKey =',
    f'{js_variations}\n\n    let selectedVariationKey = "samsung-14";',
    html,
    flags=re.DOTALL
)

html = html.replace('let selectedVariationKey = "300l";', 'let selectedVariationKey = "samsung-14";')
html = html.replace('let selectedVariationKey = "slim-disc";', 'let selectedVariationKey = "samsung-14";')
html = html.replace('selectedPrice = "2199"', 'selectedPrice = "1999"')
html = html.replace('selectedPrice = "3299"', 'selectedPrice = "1999"')
html = html.replace('selectedTitle = "Samsung 300L', 'selectedTitle = "Samsung 14-Place')
html = html.replace('selectedTitle = "Sony PlayStation', 'selectedTitle = "Samsung 14-Place')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html")

# 6. Update checkout.html
checkout_path = os.path.join(BASE_DIR, "checkout.html")
with open(checkout_path, "r", encoding="utf-8") as f:
    chk = f.read()

chk = re.sub(r'<title>.*?</title>', f'<title>Checkout - {HERO_TITLE} | Takealot</title>', chk)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator", HERO_TITLE)
chk = chk.replace("Samsung 300L Refrigerator", HERO_TITLE)
chk = chk.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")
chk = chk.replace("2199", "1999")
chk = chk.replace("2,199", "1,999")
chk = chk.replace("9,999", "8,999")
chk = chk.replace("Large Appliance White Glove Delivery (To Your Kitchen)", "Large Appliance Kitchen Delivery & Plumbing Connect Option")
chk = chk.replace("R 297", "R 279")
chk = chk.replace("Refrigerator", "Dishwasher")

with open(checkout_path, "w", encoding="utf-8") as f:
    f.write(chk)
print("Updated checkout.html")

# 7. Update cart.html
cart_path = os.path.join(BASE_DIR, "cart.html")
with open(cart_path, "r", encoding="utf-8") as f:
    crt = f.read()

crt = re.sub(r'<title>.*?</title>', f'<title>Shopping Cart - {HERO_TITLE} | Takealot</title>', crt)
crt = crt.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
crt = crt.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
crt = crt.replace("Samsung 300L Refrigerator", HERO_TITLE)
crt = crt.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")
crt = crt.replace("2199", "1999")
crt = crt.replace("2,199", "1,999")
crt = crt.replace("9,999", "8,999")

with open(cart_path, "w", encoding="utf-8") as f:
    f.write(crt)
print("Updated cart.html")

# 8. Update track.html
track_path = os.path.join(BASE_DIR, "track.html")
with open(track_path, "r", encoding="utf-8") as f:
    trk = f.read()

trk = re.sub(r'<title>.*?</title>', f'<title>Track Your Order - {HERO_TITLE} | Takealot</title>', trk)
trk = trk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
trk = trk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
trk = trk.replace("Samsung 300L Refrigerator", HERO_TITLE)
trk = trk.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")
trk = trk.replace("2199", "1999")
trk = trk.replace("2,199", "1,999")
trk = trk.replace("9,999", "8,999")
trk = trk.replace("Capacity: 300L", "Capacity: 14 Place Settings")
trk = trk.replace("300L", "14-Place")
trk = trk.replace("TAK-30-994812", "TAK-14-994812")
trk = trk.replace("TAK-43-189210", "TAK-14-189210 (Bosch)")
trk = trk.replace("TAK-25-883910", "TAK-13-883910 (Defy)")

with open(track_path, "w", encoding="utf-8") as f:
    f.write(trk)
print("Updated track.html")

# 9. Update obrigado.html
obrigado_path = os.path.join(BASE_DIR, "obrigado.html")
with open(obrigado_path, "r", encoding="utf-8") as f:
    obr = f.read()

obr = re.sub(r'<title>.*?</title>', f'<title>Order Confirmed - {HERO_TITLE} | Takealot</title>', obr)
obr = obr.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
obr = obr.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
obr = obr.replace("Samsung 300L Refrigerator", HERO_TITLE)
obr = obr.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")
obr = obr.replace("2199", "1999")
obr = obr.replace("2,199", "1,999")
obr = obr.replace("9,999", "8,999")

with open(obrigado_path, "w", encoding="utf-8") as f:
    f.write(obr)
print("Updated obrigado.html")

# 10. Update upgrade-shipping.html
upg_path = os.path.join(BASE_DIR, "upgrade-shipping.html")
with open(upg_path, "r", encoding="utf-8") as f:
    upg = f.read()

upg = re.sub(r'<title>.*?</title>', f'<title>Priority Delivery Upgrade - {HERO_TITLE} | Takealot</title>', upg)
upg = upg.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
upg = upg.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
upg = upg.replace("Samsung 300L Refrigerator", HERO_TITLE)
upg = upg.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/samsung_dishwasher_1_hero.jpg")

with open(upg_path, "w", encoding="utf-8") as f:
    f.write(upg)
print("Updated upgrade-shipping.html")

# 11. Update api/ directory
api_dir = os.path.join(BASE_DIR, "api")
for root, dirs, files in os.walk(api_dir):
    for fn in files:
        fp = os.path.join(root, fn)
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        orig = c
        c = c.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
        c = c.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
        c = c.replace("Samsung 300L Refrigerator", HERO_TITLE)
        c = c.replace("Bottom Freezer Refrigerator", "14-Place Dishwasher")
        c = c.replace("Refrigerator", "Dishwasher")
        c = c.replace("refrigerator", "dishwasher")
        c = c.replace("3020", "3030")
        c = c.replace("2199", "1999")
        c = c.replace("2,199", "1,999")
        c = c.replace("9999", "8999")
        c = c.replace("9,999", "8,999")
        c = c.replace("297", "279")
        c = re.sub(r'https://iili\.io/[a-zA-Z0-9_\-]+\.(?:jpg|png)', HERO_CDN, c)
        if c != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Updated api/{fn}")

print("\n--- ALL DISHWASHER FILES CONFIGURED SUCCESSFULLY ---")
