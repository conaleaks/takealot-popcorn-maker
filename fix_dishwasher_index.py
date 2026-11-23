import os, re

index_path = "/Users/green/Downloads/Takealot Dishwasher/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace category-hot-sec
idx1 = text.find('<div class="category-hot-sec">')
idx2 = text.find('<div class="divider"></div>\n\n    <!-- 8. Sold By Section', idx1)

new_hot_section = """<div class="category-hot-sec">
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
    </div>\n\n    """

if idx1 != -1 and idx2 != -1:
    text = text[:idx1] + new_hot_section + text[idx2:]
    print("Replaced category-hot-sec in Dishwasher!")

# 2. Global replacements
text = text.replace('imagens/samsung_fridge_1_hero.jpg', 'imagens/samsung_dishwasher_1_hero.jpg')
text = text.replace('imagens/samsung_fridge_2_open.jpg', 'imagens/samsung_dishwasher_2_open.jpg')
text = text.replace('imagens/samsung_fridge_3_dispenser.jpg', 'imagens/samsung_dishwasher_3_front.jpg')
text = text.replace('imagens/samsung_fridge_4_interior.jpg', 'imagens/samsung_dishwasher_4_racks.jpg')

text = text.replace('300L Inox (RB30)', '14-Place Inox (DW60)')
text = text.replace('300 Litres (Fridge: 202L, Freezer: 98L)', '14 Place Settings (Flexible 3rd Cutlery Rack)')
text = text.replace('300L', '14-Place')
text = text.replace('selectedPrice = "2199"', 'selectedPrice = "1999"')
text = text.replace('let selectedVariationKey = "300l";', 'let selectedVariationKey = "samsung-14";')
text = re.sub(r'let selectedTitle = ".*?";', 'let selectedTitle = "Samsung 14-Place Freestanding Stainless Steel Dishwasher with IntensiveWash (DW60M5070FS)";', text)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated Dishwasher index.html cleanly!")
