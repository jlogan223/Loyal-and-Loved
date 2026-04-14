"""
Character roster and per-article prompt library for Loyal & Loved.

- CHARACTERS: reusable cast of UK pets and owners. Consistent descriptions
  let the same dog/cat/person appear across multiple articles without
  looking like 20 different animals.
- ARTICLE_PROMPTS: one curated scene per article hero, chosen to match
  the article's emotional register (e.g. vet bills → puppy with a
  bandaged paw and recovery cone, not a smiling family at a park).

Rules applied to every prompt:
  - UK setting, natural light, photorealistic, editorial lifestyle feel
  - NO text, NO lettering, NO watermarks anywhere in the frame
  - PG-appropriate: realistic but never gruesome
"""

# Appended to every curated article prompt so the global rules are hard
# to miss, regardless of the scene.
GLOBAL_RULES = (
    " UK setting. Natural light. Warm, authentic, editorial lifestyle feel. "
    "Photorealistic quality with fine detail — not cartoonish unless "
    "specifically requested as an illustration. "
    "ABSOLUTELY NO TEXT, no lettering, no numbers, no words, no captions, "
    "no signs, no labels, no logos, no brand marks, no watermarks, no "
    "writing of any kind anywhere in the image. If any written or printed "
    "element would naturally appear (packaging, paperwork, screens, "
    "collars, signs), render it as blank or abstract with no letters. "
    "Keep the scene PG — realistic but never gruesome or distressing."
)


# Reusable cast. Keep descriptions tight but distinctive so gpt-image-1
# can reliably render the same character twice.
CHARACTERS = {
    # --- Dogs ---
    "luna_golden": "Luna, a three-year-old Golden Retriever with a warm honey-coloured coat and a soft, gentle expression",
    "milo_cockapoo": "Milo, a six-month-old apricot Cockapoo puppy with tight curly fur and big dark eyes",
    "bear_bernese": "Bear, a two-year-old Bernese Mountain Dog with a classic tri-colour coat (black body, white chest blaze, tan markings on face and legs) and a calm, trusting expression",
    "bear_bernese_puppy": "Bear as a ten-month-old Bernese Mountain Dog puppy — tri-colour coat, soft fluffy fur, oversized paws, gentle eyes",
    "willow_collie": "Willow, a five-year-old Border Collie with a glossy black-and-white coat and intense amber eyes",
    "finn_frenchie": "Finn, a four-year-old fawn French Bulldog with alert bat ears and a stocky build",
    "poppy_dachshund": "Poppy, a two-year-old smooth-coated dapple Dachshund with short legs and a long silky body",
    "rufus_lab": "Rufus, an eight-year-old chocolate Labrador with a slightly greying muzzle and soft kind eyes",
    "daisy_springer": "Daisy, a three-year-old English Springer Spaniel with a liver-and-white coat and feathered ears",
    "max_jrt": "Max, a six-year-old Jack Russell Terrier with a compact white body and tan ear patches",
    "rosie_cavalier": "Rosie, a four-year-old Blenheim Cavalier King Charles Spaniel with chestnut and white markings",

    # --- Cats ---
    "oscar_shorthair": "Oscar, a five-year-old British Shorthair cat with a plush silver tabby coat and round copper eyes",
    "bella_tortie": "Bella, a two-year-old Domestic Shorthair with a tortoiseshell coat swirled with cinnamon and chocolate",
    "whiskers_maine": "Whiskers, a seven-year-old Maine Coon with a long brown-tabby coat and tufted ears",
    "luna_ragdoll": "Luna-Rose, a four-year-old Ragdoll cat with cream fur, seal-point face and paws, and sky-blue eyes",
    "tigger_ginger": "Tigger, a three-year-old ginger tabby cat with a white chest and white front mittens",
    "pepper_black": "Pepper, a six-year-old sleek black cat with bright green eyes",

    # --- Other ---
    "kiwi_budgie": "Kiwi, a bright green-and-yellow budgerigar",
    "thumper_rabbit": "Thumper, a grey Holland Lop rabbit with floppy ears",
    "shadow_horse": "Shadow, a ten-year-old dark bay Welsh Cob with a glossy coat",
    "sunny_gpig": "Sunny, a tri-colour guinea pig with smooth short fur",

    # --- People (UK owners) ---
    "sarah_30s": "Sarah, a woman in her early thirties with shoulder-length brown hair and warm brown eyes, wearing a soft oatmeal jumper and jeans",
    "james_40s": "James, a man in his mid-forties with short fair hair and a trimmed beard, wearing a navy quilted gilet over a checked shirt",
    "emma_late20s": "Emma, a woman in her late twenties with auburn wavy hair and small forearm tattoos, wearing urban casual clothing",
    "michael_60s": "Michael, a man in his early sixties with neat silver hair and a kind lined face, wearing a smart-casual olive jumper",
    "priya_30s": "Priya, a British South Asian woman in her mid-thirties with a tidy dark bob and minimal jewellery, wearing smart city-professional clothing",
    "daniel_late20s": "Daniel, a mixed-race man in his late twenties with short curly dark hair and round tortoiseshell glasses, wearing a plain tee and a grey cardigan",
    "lucy_40s": "Lucy, a woman in her early forties with straight blonde hair loosely tied back and a warm motherly smile, wearing a soft cream cardigan",
    "oliver_50s": "Oliver, a tall man in his mid-fifties with salt-and-pepper hair and weathered hands, wearing a checked shirt and green wellies",
    "chloe_early20s": "Chloe, a woman in her early twenties with long ginger hair, light freckles, and a cosy knit jumper",
    "hannah_vet": "Hannah, a woman in her late thirties with dark hair in a low bun and a warm focused face, wearing neat navy veterinary scrubs",
}
C = CHARACTERS


def _p(text: str) -> str:
    """Append global rules to a scene prompt."""
    return text.strip() + GLOBAL_RULES


# One curated scene per article hero. When an article's slug appears here,
# this prompt is used verbatim instead of a generic style + description.
ARTICLE_PROMPTS = {

    "best-pet-insurance-uk": _p(
        f"Wide, warm lifestyle photograph inside a bright British living room at golden hour. "
        f"On a cosy pale-grey linen sofa, {C['luna_golden']} is curled peacefully beside "
        f"{C['oscar_shorthair']}. Both pets look relaxed and content, the cat nestled against "
        f"the dog's shoulder. Soft side-lighting from a large sash window, gentle bokeh of a "
        f"houseplant and a warm throw. Muted cream and sage palette, shallow depth of field. "
        f"The mood is safety and peace of mind — nothing clinical, no paperwork in frame."
    ),

    "best-cat-insurance-uk": _p(
        f"Warm close-up photograph of {C['oscar_shorthair']} sitting upright on a cream wool "
        f"blanket by a sunlit sash window in a British home. Soft rim light picks out the "
        f"silver-tabby fur, eyes slightly closed in contentment. Gentle bokeh of a terracotta "
        f"pot and fern in the background. Intimate, reassuring, well-cared-for atmosphere."
    ),

    "best-dog-gps-tracker-uk": _p(
        f"Action lifestyle photograph of {C['bear_bernese']} mid-stride across a green British "
        f"countryside meadow in late-afternoon light. A small, sleek, matte-black modern GPS "
        f"tracker unit is clearly visible clipped to his tan leather collar (render the tracker "
        f"as a plain featureless puck — no text, no logos, no screen). Wind lifts his fur, ears "
        f"slightly back, joyful expression. Rolling soft hills and warm golden sunlight in the "
        f"background, shallow depth of field."
    ),

    "best-fresh-dog-food-uk": _p(
        f"Top-down lifestyle photograph of {C['luna_golden']} eating from a matte cream ceramic "
        f"bowl containing colourful freshly-cooked dog food — visible chunks of gently-cooked "
        f"chicken, diced carrots, green beans, peas, and rice, glossy and appetising. On warm "
        f"oak kitchen floorboards. Natural daylight from one side. Shallow depth of field. No "
        f"packaging, no branding, no text of any kind visible in the frame."
    ),

    "cockapoo-cost-uk": _p(
        f"Portrait photograph of {C['milo_cockapoo']} sitting on a soft blush-pink wool blanket "
        f"in a bright, airy British home. Head tilted slightly to one side, big curious dark "
        f"eyes, one front paw raised inquisitively. Natural window light, warm cream and sage "
        f"background with a gentle bokeh, shallow depth of field. Playful but well-groomed."
    ),

    "cost-of-owning-dog-uk": _p(
        f"Wide lifestyle photograph of {C['lucy_40s']} sitting at a sunny British kitchen table "
        f"with {C['daisy_springer']} resting her head affectionately on Lucy's knee. A warm "
        f"speckled mug of tea and a small open notebook sit on the table — the notebook pages "
        f"are blank (no readable writing). Morning light through the window, ceramics and a "
        f"small jug of dried lavender on a shelf behind. Warm, reassuring, everyday UK home "
        f"atmosphere — the feeling is careful thoughtful planning, not stress."
    ),

    "emergency-vet-costs-uk": _p(
        f"Emotionally warm photograph inside a clean, modern UK vet consulting room. "
        f"{C['daisy_springer']} is lying calmly on a padded grey exam table, a soft white gauze "
        f"bandage neatly wrapped around her front right leg. {C['hannah_vet']} leans in with "
        f"one hand gently resting on Daisy's shoulder, a reassuring, focused expression on her "
        f"face. Soft clinical daylight through a frosted window. Out-of-focus vet equipment in "
        f"the background. STRICTLY PG — no blood, no wounds visible, just a neatly bandaged "
        f"paw and a recovering pet. The emotional register is 'this happened, she is going to "
        f"be OK'."
    ),

    "flea-tick-worm-protection": _p(
        f"A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        f"{C['luna_golden']} and {C['pepper_black']} sit side by side in a sunlit English "
        f"country garden with soft grass and small wildflowers. Around them float subtle "
        f"abstract shield motifs, a clean leaf, and a single water droplet — visual metaphors "
        f"for protection. Cosy hand-drawn feel, pastel palette featuring teal (#189181) and "
        f"soft purple (#8A44F3), warm beige background, clean simple shapes."
    ),

    "indoor-vs-outdoor-cats": _p(
        f"A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        f"Split composition: on the left, a ginger tabby cat sits peacefully on a cushioned "
        f"windowsill inside a warm home, looking calmly out; on the right, the same ginger "
        f"tabby prowls through a wildflower garden under sunshine. A gentle vertical divider "
        f"suggests a pane of glass between the two scenes. Pastel palette of teal (#189181) "
        f"and soft purple (#8A44F3), warm beige background, clean simple shapes."
    ),

    "lifetime-vs-annual-pet-insurance": _p(
        f"Warm lifestyle photograph on a sunlit British garden lawn in early summer. "
        f"{C['rufus_lab']} lies peacefully on the grass while {C['milo_cockapoo']} sits beside "
        f"him, looking up at the older dog — a visual metaphor of a life-long timeline from "
        f"puppy to senior. Soft golden side-light, shallow depth of field, gentle bokeh of "
        f"green grass and wildflowers. The mood is warm and reflective. No documents, no text."
    ),

    "pet-dental-care": _p(
        f"A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        f"A friendly cartoon-style dog with a bright, clean-toothed smile sits next to an "
        f"oversized soft pet toothbrush. Nearby, a tabby cat watches curiously. Gentle "
        f"pastel palette featuring teal (#189181) and soft purple (#8A44F3), warm beige "
        f"background, clean simple shapes, playful friendly mood."
    ),

    "pet-insurance-cost-uk": _p(
        f"Warm lifestyle photograph of {C['sarah_30s']} at a bright UK kitchen table with "
        f"{C['luna_golden']} resting her chin affectionately on the edge of the table beside "
        f"Sarah's hand. A laptop sits open but the screen is angled away from camera so no "
        f"content is readable. A small ceramic plant pot and a cup of tea nearby. Soft morning "
        f"light through a window, muted warm palette, relaxed and unhurried atmosphere — "
        f"careful research, not stress."
    ),

    "puppy-first-year-checklist": _p(
        f"A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        f"A small golden retriever puppy sits happily at the centre, with gentle curved lines "
        f"radiating outward to simple iconic shapes representing puppy milestones — a food "
        f"bowl, a soft toy, a rolled leash, a tiny leaf, a cosy round bed. Pastel palette "
        f"featuring teal (#189181) and soft purple (#8A44F3), warm beige background, clean "
        f"simple shapes, cheerful optimistic mood."
    ),

    "senior-dog-care": _p(
        f"A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        f"An older grey-muzzled chocolate Labrador rests peacefully curled up on a round "
        f"cushioned bed. A small potted plant and a water bowl sit nearby. Pastel palette "
        f"featuring teal (#189181) and soft purple (#8A44F3), warm beige background, clean "
        f"simple shapes, tender and dignified mood."
    ),

    "vet-bills-uk": _p(
        f"Emotionally warm photograph inside a bright, clean, modern UK vet consulting room. "
        f"{C['bear_bernese_puppy']} is lying calmly on a padded grey exam table. A soft white "
        f"gauze bandage is neatly wrapped around his front right paw. He wears a soft grey "
        f"recovery cone around his head and looks up gently at the camera. {C['hannah_vet']} "
        f"stands beside him, one hand resting softly on his back, her expression reassuring. "
        f"Warm natural daylight through a window, out-of-focus vet equipment in the "
        f"background. STRICTLY PG — no blood, no wounds, no distress — just a bandaged paw "
        f"and a puppy recovering well. The emotional register is 'this could happen to any "
        f"pet — he's going to be OK, and good insurance means the bill won't be devastating'."
    ),
}


def get_article_prompt(slug: str) -> str | None:
    """Return a curated prompt for an article slug, or None if no custom
    prompt exists. The caller should fall back to a generic style-based
    prompt built from the placeholder description."""
    return ARTICLE_PROMPTS.get(slug)
