import re

index_path = '/Users/green/Downloads/Takealot Popcorn Maker/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Main Product Title
html = re.sub(r'<title>.*?</title>', '<title>Milex Retro Popcorn Maker - Hot Air Popcorn Machine | Vintage Cinema Style (MRP001) | Takealot</title>', html, flags=re.DOTALL)
html = html.replace('Milex Retro Cinema Popcorn Maker (MRP001) (MRP001)', 'Milex Retro Popcorn Maker - Hot Air Popcorn Machine | Vintage Cinema Style (MRP001)')

# 2. Update Gallery Carousel alt attributes
html = html.replace('Milex 14-Place Freestanding Stainless Steel Popcorn Maker Hero', 'Milex Retro Cinema Popcorn Maker 1950s Style Hero Frontal')
html = html.replace('Milex Retro Popcorn Maker Open Door with Cutlery Tray and Racks', 'Milex Retro Popcorn Maker Popping Hot Golden Popcorn')
html = html.replace('Milex Retro Popcorn Maker Front Digital LED Control Panel', 'Milex Retro Popcorn Maker Detail View Stainless Kettle and Serving Tray')
html = html.replace('Milex Retro Popcorn Maker Interior Spray Arms and Flexible Racks', 'Milex Retro Popcorn Maker Full Packshot with Accessories')

# 3. Update Variation Selector Pills
var_pills_html = '''    <!-- Product Variation / Model Selector -->
    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Model / Bundle: <strong id="selected-size-label">Retro Cinema Style (Milex Hero)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-sliders" style="margin-right: 3px;"></i> Choose variant</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill" data-var-key="compact-1200w" onclick="selectProductVariation('compact-1200w')">
                Compact 1200W Hot Air <span class="pill-badge">R 299</span>
            </button>
            <button class="var-pill active" data-var-key="milex-retro" onclick="selectProductVariation('milex-retro')">
                Milex Retro Cinema (MRP001) <span class="pill-badge" style="background: #007a3d;">Hot R 499</span>
            </button>
            <button class="var-pill" data-var-key="deluxe-kit" onclick="selectProductVariation('deluxe-kit')">
                Deluxe Kit + 1kg Kernels & 4 Flavours <span class="pill-badge">R 599</span>
            </button>
            <button class="var-pill" data-var-key="commercial-8oz" onclick="selectProductVariation('commercial-8oz')">
                Commercial 8oz Vintage Cart <span class="pill-badge">R 999</span>
            </button>
        </div>
    </div>'''

html = re.sub(r'<!-- Product Variation / Size Selector -->.*?<!-- 6\. TakealotMORE Banner', var_pills_html + '\n\n    <!-- 6. TakealotMORE Banner', html, flags=re.DOTALL)

# 4. Update What's Hot Carousel
hot_carousel_html = '''        <!-- 7. What's Hot in Popcorn Makers -->
    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What\'s Hot in Popcorn Makers</div>
        <div class="hot-carousel">
            <!-- Variation 1: Compact 1200W -->
            <div class="hot-card" data-var-key="compact-1200w" onclick="selectProductVariation('compact-1200w', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/popcorn_maker_3_detail.jpg" alt="Compact 1200W Hot Air Popcorn Popper" />
                </div>
                <div class="hot-title">Compact 1200W Electric Hot Air Popcorn Popper (Oil-Free)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 299</span>
                    <span class="hot-old-price">R 1,199</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.7 (790)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 2: Milex Retro Hero -->
            <div class="hot-card active-selection" data-var-key="milex-retro" onclick="selectProductVariation('milex-retro', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/popcorn_maker_1_hero.jpg" alt="Milex Retro Cinema Popcorn Maker" />
                </div>
                <div class="hot-title">Milex Retro Popcorn Maker - Hot Air Cinema Machine (MRP001)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 499</span>
                    <span class="hot-old-price">R 1,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (2,840)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 3: Deluxe Kit -->
            <div class="hot-card" data-var-key="deluxe-kit" onclick="selectProductVariation('deluxe-kit', true)">
                <div class="hot-badges">
                    <div class="badge-black">Gourmet<br>Bundle</div>
                    <div class="badge-blue">76%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/popcorn_maker_2_serving.jpg" alt="Deluxe Kit Popcorn Maker Bundle" />
                </div>
                <div class="hot-title">Milex Retro + 1kg Non-GMO Kernels & 4 Cinema Flavour Shakers Kit</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 599</span>
                    <span class="hot-old-price">R 2,499</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (1,120)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>

            <!-- Variation 4: Commercial 8oz -->
            <div class="hot-card" data-var-key="commercial-8oz" onclick="selectProductVariation('commercial-8oz', true)">
                <div class="hot-badges">
                    <div class="badge-black">Heavy<br>Duty</div>
                    <div class="badge-blue">80%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/popcorn_maker_4_packshot.jpg" alt="Commercial 8oz Vintage Cart Popcorn Machine" />
                </div>
                <div class="hot-title">Commercial 8oz Vintage Cart High-Capacity Popcorn Machine</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 999</span>
                    <span class="hot-old-price">R 4,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (530)</div>
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>
        </div>
    </div>'''

html = re.sub(r'<!-- 7\. What\'s Hot in Popcorn Makers -->.*?<!-- 8\. Sold By Section', hot_carousel_html + '\n\n    <div class="divider"></div>\n\n    <!-- 8. Sold By Section', html, flags=re.DOTALL)

# 5. Update Specifications Table
specs_html = '''        <!-- 14. Product Information -->
    <div class="spec-sec">
        <div class="sec-title">Product Information</div>
        <table class="spec-table">
            <tr>
                <td class="col-label">Categories</td>
                <td class="col-val"><a href="#">Kitchen &amp; Small Appliances</a> / <a href="#">Small Appliances</a> / <a href="#">Popcorn Makers</a></td>
            </tr>
            <tr>
                <td class="col-label">Brand</td>
                <td class="col-val"><a href="#">Milex</a></td>
            </tr>
            <tr>
                <td class="col-label">Warranty</td>
                <td class="col-val">12-Month Official Milex South Africa Warranty</td>
            </tr>
            <tr>
                <td class="col-label">Popping Capacity</td>
                <td class="col-val" id="spec-capacity">Up to 60 Litres Popcorn / Hour (16 Cups per batch)</td>
            </tr>
            <tr>
                <td class="col-label">Model Number</td>
                <td class="col-val" id="spec-model-number">MRP001</td>
            </tr>
            <!-- Extra spec rows that expand on Show More -->
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Heating Technology</td>
                <td class="col-val">Rapid Hot Air Circulation (100% Oil-Free &amp; Healthy)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Popping Time</td>
                <td class="col-val">Under 2.5 minutes per batch</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Popping Efficiency</td>
                <td class="col-val">98.7% Pop Rate (Virtually Zero Unpopped Kernels)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Kettle Material</td>
                <td class="col-val">Food-Grade Stainless Steel with Integrated Motorized Stirrer</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Viewing Windows</td>
                <td class="col-val">360° Panoramic Heat-Resistant Tempered Transparent Glass</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Internal Lighting</td>
                <td class="col-val">Warm Cinema Spotlight &amp; Warming Lamp</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Serving System</td>
                <td class="col-val">Slide-Out Vintage Serving Tray with Ergonomic Chrome Handle</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Accessories Included</td>
                <td class="col-val">Kernel Measuring Spoon, Oil Measuring Spoon, Popcorn Serving Scoop</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Power Rating</td>
                <td class="col-val">300W High Efficiency Energy-Saving Motor</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Voltage &amp; Frequency</td>
                <td class="col-val">220V - 240V ~ 50Hz (Standard SA 3-Pin Plug)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Safety Protection</td>
                <td class="col-val">Thermal Cut-Off, Overheat Protection &amp; Anti-Slip Rubber Feet</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Dimensions (W x D x H)</td>
                <td class="col-val">28.5 cm x 25.0 cm x 45.5 cm</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Net Weight</td>
                <td class="col-val">3.4 kg</td>
            </tr>
        </table>
        <button class="pill-show-more" id="spec-toggle-btn" onclick="toggleSpecs()">Show More</button>
    </div>'''

html = re.sub(r'<!-- 14\. Product Information -->.*?<div class="divider"></div>\s*<!-- 15\. Reviews', specs_html + '\n\n    <div class="divider"></div>\n\n    <!-- 15. Reviews', html, flags=re.DOTALL)

# 6. Update Reviews Container with 14 Authentic South African Popcorn Reviews
reviews_html = '''        <div id="reviews-list-container">
            <!-- Review 1 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Kagiso Sithole - 26 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">48</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Absolute game-changer for family movie nights! The vintage cinema look is stunning and it pops popcorn in under 2 minutes...</span>
                    <span class="review-full" style="display: none;">Absolute game-changer for family movie nights! The vintage cinema look is stunning and it pops popcorn in under 2 minutes. The whole house smells like Ster-Kinekor! The kids were mesmerized watching the golden popcorn tumble out of the stainless steel kettle. 100% oil-free and crunchy!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Liam van der Merwe - 18 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">39</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Virtually zero unpopped kernels. The motorized stirring arm ensures every single kernel pops perfectly fluffy...</span>
                    <span class="review-full" style="display: none;">Virtually zero unpopped kernels. The motorized stirring arm ensures every single kernel pops perfectly fluffy without burning. The warming light keeps it nice and hot while watching rugby with friends. Solid build quality from Milex.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Nompumelelo Dlamini - 04 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">31</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">So healthy! No oily mess or greasy fingers. The slide-out tray makes serving into popcorn bags effortless...</span>
                    <span class="review-full" style="display: none;">So healthy! No oily mess or greasy fingers. The slide-out tray makes serving into popcorn bags effortless. We dusted it with salt and vinegar seasoning and it tasted incredible. Cleanup takes less than 30 seconds with a damp cloth.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Jacques Du Plessis - 29 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">24</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Got this on Takealot Daily Deal for R499. Incredible value considering retail is usually R2,000...</span>
                    <span class="review-full" style="display: none;">Got this on Takealot Daily Deal for R499. Incredible value considering retail is usually R2,000. It looks like a high-end showpiece in our entertainment area. Ordered on Tuesday afternoon and it arrived at our door in Centurion by Wednesday morning!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Amina Patel - 12 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">28</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">My daughters birthday party was an instant hit thanks to this popcorn cart machine. Made batch after batch...</span>
                    <span class="review-full" style="display: none;">My daughters birthday party was an instant hit thanks to this popcorn cart machine. Made batch after batch without any overheating. Popcorn came out light, crispy and huge. Everyone commented on how authentic the cinema taste was!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 6 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Brendan Fourie - 08 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">19</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Much better than microwave popcorn which is packed with palm oil and artificial chemicals...</span>
                    <span class="review-full" style="display: none;">Much better than microwave popcorn which is packed with palm oil and artificial chemicals. With this Milex machine, you control the ingredients completely. Just pure organic popping corn and whatever spices you love. A must-have for healthy snacking.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 7 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Thabo Mokoena - 22 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">15</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The built-in warming light is fantastic. It keeps the popcorn warm and crunchy even 40 minutes into a film...</span>
                    <span class="review-full" style="display: none;">The built-in warming light is fantastic. It keeps the popcorn warm and crunchy even 40 minutes into a film. The magnetic door opens smoothly and the measuring scoops included make portioning foolproof. 5 stars all the way!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 8 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Chloe Botha - 15 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">22</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Compact enough to fit nicely on the kitchen counter but looks like an authentic 1950s cinema popper...</span>
                    <span class="review-full" style="display: none;">Compact enough to fit nicely on the kitchen counter but looks like an authentic 1950s cinema popper. The candy red gloss and chrome details are gorgeous. Very fast delivery to Ballito. Takealot packaging was well padded and safe.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 9 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Sipho Khumalo - 01 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">17</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Very low power consumption. Runs perfectly even on my home inverter setup during stage 2 loadshedding...</span>
                    <span class="review-full" style="display: none;">Very low power consumption. Runs perfectly even on my home inverter setup during stage 2 loadshedding. At 300W it pulls very little battery power while giving us piping hot snacks. Highly recommended!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 10 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Megan Oosthuizen - 20 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">26</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Sweet caramel popcorn turned out incredible! The stainless steel kettle is non-stick and wipes down easily...</span>
                    <span class="review-full" style="display: none;">Sweet caramel popcorn turned out incredible! The stainless steel kettle is non-stick and wipes down easily. We tried butter salt first and then glazed caramel, both were perfection. My family is obsessed with this machine!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 11 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Gareth Naidoo - 28 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">13</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Top tier gift idea! Bought one for my brother and ended up ordering a second one for my own home...</span>
                    <span class="review-full" style="display: none;">Top tier gift idea! Bought one for my brother and ended up ordering a second one for my own home. Delivery was next day via Takealot driver. Setup took 2 minutes out of the box. Super easy to operate with the two front toggle switches.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 12 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Zanele Ndlovu - 10 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">33</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Healthy school lunchbox snack sorted! Makes enough popcorn in 3 minutes to fill all 3 kids snack containers...</span>
                    <span class="review-full" style="display: none;">Healthy school lunchbox snack sorted! Makes enough popcorn in 3 minutes to fill all 3 kids snack containers. Stays crispy all day long. Much healthier than processed chips or sweets. A fantastic household investment.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 13 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Dirk Coetzee - 17 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">21</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Robust construction, quiet motor, and popping speed is lightning fast. Excellent South African customer support...</span>
                    <span class="review-full" style="display: none;">Robust construction, quiet motor, and popping speed is lightning fast. Excellent South African customer support from Milex. The 12-month warranty provides great peace of mind. Everything works as advertised.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 14 -->
            <div class="review-single-card extra-review" style="display: none;">
                <div class="review-card-top">
                    <div>
                        <strong>Farhana Cassim - 05 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">35</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Brings authentic cinema nostalgia right into your home. The kids look forward to Friday night movies all week...</span>
                    <span class="review-full" style="display: none;">Brings authentic cinema nostalgia right into your home. The kids look forward to Friday night movies all week because of this machine. Easy to use, safe, and makes delicious warm popcorn. Best purchase on Takealot this year!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>
        </div>'''

html = re.sub(r'<div id="reviews-list-container">.*?</div>\s*<button class="load-more-reviews-btn"', reviews_html + '\n\n        <button class="load-more-reviews-btn"', html, flags=re.DOTALL)

# 7. Update JavaScript Variations Object
js_variations_code = '''    // Product Variations Data Dictionary (Popcorn Makers)
    const productVariations = {
        'compact-1200w': {
            title: 'Compact 1200W Electric Hot Air Popcorn Popper (Oil-Free)',
            label: 'Compact 1200W (Red Mini)',
            price: 299,
            oldPrice: 1199,
            discount: '75%',
            image: 'imagens/popcorn_maker_3_detail.jpg',
            capacity: '1200W High Speed Vortex / 12 Cups in 2 Mins',
            modelNumber: 'HP-1200-MINI',
            rating: '4.7 (790)',
            reviewsCount: '790'
        },
        'milex-retro': {
            title: 'Milex Retro Popcorn Maker - Hot Air Cinema Machine (MRP001)',
            label: 'Retro Cinema Style (Milex Hero)',
            price: 499,
            oldPrice: 1999,
            discount: '75%',
            image: 'imagens/popcorn_maker_1_hero.jpg',
            capacity: 'Up to 60 Litres Popcorn / Hour (16 Cups per batch)',
            modelNumber: 'MRP001',
            rating: '4.9 (2,840)',
            reviewsCount: '2,840'
        },
        'deluxe-kit': {
            title: 'Milex Retro + 1kg Non-GMO Kernels & 4 Cinema Flavour Shakers Kit',
            label: 'Deluxe Kit + Kernels & 4 Flavours',
            price: 599,
            oldPrice: 2499,
            discount: '76%',
            image: 'imagens/popcorn_maker_2_serving.jpg',
            capacity: 'Full Cinema Kit + 1kg Gourmet Corn + 4 Shakers',
            modelNumber: 'MRP001-BNDL',
            rating: '4.9 (1,120)',
            reviewsCount: '1,120'
        },
        'commercial-8oz': {
            title: 'Commercial 8oz Vintage Cart High-Capacity Popcorn Machine',
            label: 'Commercial 8oz Heavy Duty',
            price: 999,
            oldPrice: 4999,
            discount: '80%',
            image: 'imagens/popcorn_maker_4_packshot.jpg',
            capacity: 'Commercial 8oz Kettle / 120 Litres per hour',
            modelNumber: 'CPM-800-CART',
            rating: '4.9 (530)',
            reviewsCount: '530'
        }
    };'''

html = re.sub(r'// Product Variations Data Dictionary.*?const productVariations = \{.*?\};', js_variations_code, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Popcorn Maker index.html full update complete!')
