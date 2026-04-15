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


# --- Category heroes (tier 4) ------------------------------------------
# Soft pastel illustrations in the brand palette. Keyed by the category
# slug so build_prompt() picks them up the same way as article heroes.
ARTICLE_PROMPTS.update({

    "pet-insurance": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "A friendly golden retriever and a tabby cat sit peacefully side by side beneath "
        "a large abstract shield motif that arcs over them protectively. Gentle cloud "
        "shapes and a small paw-print decoration float in the background. Pastel palette "
        "of teal (#189181) and soft purple (#8A44F3) on a warm beige background. Clean "
        "simple shapes, cosy hand-drawn feel, reassuring and trustworthy mood."
    ),

    "health-vet-care": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "A friendly cartoon dog and cat sit together on a pastel examination cushion with "
        "an abstract heart-plus-cross medical motif gently floating above. A simple "
        "stethoscope curves around them as a decorative element. Pastel palette of teal "
        "(#189181) and soft purple (#8A44F3), warm beige background, clean simple shapes, "
        "caring and gentle mood."
    ),

    "food-nutrition": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "A cheerful cartoon dog sits happily beside a round bowl of colourful food — "
        "simple abstract shapes suggesting vegetables, a meat piece, and grains. A small "
        "abstract leaf and a water droplet hover nearby. Pastel palette of teal (#189181) "
        "and soft purple (#8A44F3), warm beige background, clean simple shapes, fresh and "
        "wholesome mood."
    ),

    "training-behaviour": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "A friendly cartoon dog sits attentively with one paw raised, looking up at an "
        "abstract hand shape offering a simple bone-shaped treat. A small curved path "
        "loops gently behind them suggesting training progress. Pastel palette of teal "
        "(#189181) and soft purple (#8A44F3), warm beige background, clean simple shapes, "
        "encouraging positive mood."
    ),

    "gear-tech": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "A cartoon dog wearing a simple featureless collar sits beside a small stylised "
        "tracker puck and an abstract water bowl. Subtle connectivity arcs (simple curved "
        "lines) radiate gently outward. Pastel palette of teal (#189181) and soft purple "
        "(#8A44F3), warm beige background, clean simple shapes, modern and friendly mood. "
        "No screens with content, no logos, no text of any kind."
    ),

    "breed-guides": _p(
        "A soft, modern flat illustration (not a photograph) for a UK pet care website. "
        "Four stylised cartoon dogs of different breeds (a Labrador, a Cockapoo, a "
        "Dachshund, and a Bernese Mountain Dog) sit together in a friendly row, each "
        "drawn in a clean simple style. A small cat sits to one side watching. Pastel "
        "palette of teal (#189181) and soft purple (#8A44F3), warm beige background, "
        "clean simple shapes, warm and welcoming mood."
    ),
})


# --- Body images (tier 3) — curated only for HIGH-RISK scenes ---------
# The generic fallback (STYLE_PROMPTS + description + GLOBAL_RULES) is
# fine for most body images. But some descriptions explicitly call for
# brand logos, document close-ups, packaging, charts, or phone screens —
# those are a minefield for garbled text. For those specific scenes we
# override with a text-free alternative that communicates the same idea.
#
# Keyed by "{slug}-pos{position}".
BODY_PROMPTS = {

    # ---- best-pet-insurance-uk ----
    "best-pet-insurance-uk-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). Four identical "
        f"rounded rectangular panels sit side by side, each holding a stylised "
        f"paw-print icon in a different pastel tone (teal, soft purple, warm "
        f"peach, sage green). A small abstract tick mark floats beside two of "
        f"the panels. Warm beige background, clean simple shapes, teal "
        f"(#189181) and soft purple (#8A44F3) accents. Visual metaphor for "
        f"comparing providers, with no brand marks or text of any kind."
    ),

    "best-pet-insurance-uk-pos3": _p(
        f"Warm lifestyle photograph on a light oak kitchen table of a small "
        f"matte-cream calculator next to a neat stack of plain cream papers "
        f"(pages entirely blank — no writing, no letters). A ceramic mug of "
        f"tea and a pen rest beside them. Soft morning daylight, shallow "
        f"depth of field, muted beige and sage palette. No screens, no logos."
    ),

    "best-pet-insurance-uk-pos4": _p(
        f"Close-up lifestyle photograph of a neat, plain cream document on a "
        f"warm oak desk. The document pages are entirely blank — no writing, "
        f"no letters, no printed content anywhere. A silver fountain pen "
        f"rests diagonally across the top page. Soft natural daylight, "
        f"shallow depth of field, muted tones."
    ),

    "best-pet-insurance-uk-pos5": _p(
        f"Warm over-the-shoulder lifestyle photograph of {C['sarah_30s']} "
        f"holding a modern smartphone in a bright UK living room. The phone "
        f"screen is angled away from camera so no on-screen content is "
        f"visible. {C['luna_golden']} rests peacefully on a throw blanket "
        f"beside her. Soft daylight, shallow depth of field, calm unhurried "
        f"atmosphere."
    ),

    # ---- best-dog-gps-tracker-uk ----
    "best-dog-gps-tracker-uk-pos2": _p(
        f"Flat-lay lifestyle photograph on a warm oak surface: three small, "
        f"sleek, matte tracker pucks sit evenly spaced in a row — one black, "
        f"one white, one silver. Each is a plain featureless device with no "
        f"screen content, no branding, no text, no logos of any kind. Soft "
        f"natural daylight, shallow depth of field, muted palette."
    ),

    "best-dog-gps-tracker-uk-pos3": _p(
        f"Action lifestyle photograph of {C['willow_collie']} running "
        f"joyfully along a grassy British park path in soft afternoon light. "
        f"A small, sleek, plain black tracker puck is clearly clipped to her "
        f"tan leather collar (featureless, no logos or text). Ears "
        f"streaming, tongue out, shallow depth of field, lush green bokeh."
    ),

    # ---- best-fresh-dog-food-uk ----
    "best-fresh-dog-food-uk-pos2": _p(
        f"Warm lifestyle photograph of {C['rufus_lab']} sitting proudly on "
        f"a sunlit wooden kitchen floor with a glossy healthy coat, ears "
        f"perked, a freshly-filled matte cream ceramic bowl in front of "
        f"him. The bowl holds colourful gently-cooked food (diced chicken, "
        f"carrots, peas, rice). Soft natural light, muted warm palette, "
        f"shallow depth of field. No packaging, no labels, no text."
    ),

    "best-fresh-dog-food-uk-pos3": _p(
        f"Flat-lay lifestyle photograph on a warm oak kitchen counter: "
        f"three identical plain matte cream food containers sit evenly "
        f"spaced in a row, each holding a different portion of colourful "
        f"freshly-cooked dog food — one chicken and carrot, one beef and "
        f"sweet potato, one fish and greens. Containers are entirely blank, "
        f"no labels, no branding, no text of any kind. Soft daylight, "
        f"shallow depth of field."
    ),

    # ---- pet-insurance-cost-uk ----
    "pet-insurance-cost-uk-pos2": _p(
        f"Wide lifestyle photograph of four different-sized dogs sitting "
        f"together in a row on a soft grey studio backdrop: a small "
        f"Dachshund, a medium Cockapoo, a larger Springer Spaniel, and a "
        f"large Bernese Mountain Dog. Warm, gentle studio lighting. "
        f"Shallow depth of field. Friendly editorial feel, no text."
    ),

    "pet-insurance-cost-uk-pos3": _p(
        f"A soft, modern flat illustration (not a photograph). Four "
        f"abstract pastel bars of varying heights arc gently upward beside "
        f"a small stylised paw-print motif. Simple curved lines suggest "
        f"comparison. Pastel palette of teal (#189181) and soft purple "
        f"(#8A44F3), warm beige background, clean simple shapes, no "
        f"numbers and no text anywhere."
    ),

    "pet-insurance-cost-uk-pos4": _p(
        f"Warm lifestyle photograph of {C['priya_30s']} at a bright UK "
        f"kitchen table with a matte silver calculator and a neat stack of "
        f"plain cream papers (pages blank — no writing). A ceramic cup of "
        f"tea and a pen rest nearby. Soft morning daylight through a "
        f"window, muted palette, thoughtful unhurried atmosphere."
    ),

    # ---- lifetime-vs-annual-pet-insurance body ----
    "lifetime-vs-annual-pet-insurance-pos2": _p(
        f"Warm lifestyle photograph of {C['michael_60s']} sitting "
        f"thoughtfully at a softly-lit UK kitchen table. {C['rufus_lab']} "
        f"rests his head gently on Michael's knee, looking up. A plain "
        f"blank notebook sits open on the table beside a cup of tea. Soft "
        f"window light, muted warm palette, reflective mood. No readable "
        f"text."
    ),

    # ---- flea-tick-worm-protection body ----
    "flea-tick-worm-protection-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). A gentle "
        f"circular calendar ring is made of twelve stylised pastel leaf "
        f"shapes, each a slightly different soft colour to suggest "
        f"seasons. Small abstract tick, flea, and worm motifs float near "
        f"three of the leaves in non-alarming simplified forms. Pastel "
        f"palette of teal (#189181) and soft purple (#8A44F3), warm beige "
        f"background, clean simple shapes, no numbers or letters anywhere."
    ),

    "flea-tick-worm-protection-pos3": _p(
        f"A soft, modern flat illustration (not a photograph). Close-up "
        f"stylised view of a simple pet grooming comb resting on a soft "
        f"pastel surface beside a small cartoon paw. Clean minimal shapes "
        f"only, no realistic insects, no text. Pastel palette of teal "
        f"(#189181) and soft purple (#8A44F3), warm beige background."
    ),

    "flea-tick-worm-protection-pos4": _p(
        f"A soft, modern flat illustration (not a photograph). A simple "
        f"cartoon-style tick-removal tool rests on a pastel surface beside "
        f"an abstract stylised paw. Clean minimal shapes, non-alarming "
        f"and educational feel. Pastel palette of teal (#189181) and soft "
        f"purple (#8A44F3), warm beige background, no text."
    ),

    # ---- pet-dental-care body ----
    "pet-dental-care-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). Two "
        f"side-by-side cartoon dog-tooth shapes sit on a pastel background "
        f"— one clean and bright with a small sparkle motif, the other a "
        f"gentle muted tone suggesting dullness. Kept stylised and "
        f"non-gruesome. Pastel palette of teal (#189181) and soft purple "
        f"(#8A44F3), warm beige background, clean simple shapes, no text."
    ),

    "pet-dental-care-pos3": _p(
        f"A soft, modern flat illustration (not a photograph). A friendly "
        f"cartoon-style golden retriever holds still with a soft content "
        f"expression while an abstract hand holds an oversized pet "
        f"toothbrush. Playful and gentle. Pastel palette of teal (#189181) "
        f"and soft purple (#8A44F3), warm beige background, clean simple "
        f"shapes, no text."
    ),

    # ---- indoor-vs-outdoor-cats body ----
    "indoor-vs-outdoor-cats-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). A ginger "
        f"tabby cat stands in a stylised English garden among simple "
        f"wildflower shapes, with a small abstract car silhouette far in "
        f"the background suggesting mild outdoor risk without any threat. "
        f"Pastel palette of teal (#189181) and soft purple (#8A44F3), "
        f"warm beige background, clean simple shapes, no text."
    ),

    "indoor-vs-outdoor-cats-pos3": _p(
        f"A soft, modern flat illustration (not a photograph). A content "
        f"tabby cat sits inside a simple stylised catio enclosure, "
        f"watching simplified butterflies and flowers in an open garden "
        f"beyond. Clean wooden-frame shapes suggest the catio. Pastel "
        f"palette of teal (#189181) and soft purple (#8A44F3), warm beige "
        f"background, clean simple shapes, no text."
    ),

    # ---- vet-bills-uk body ----
    "vet-bills-uk-pos2": _p(
        f"Warm PG photograph inside a modern UK vet consulting room. "
        f"{C['hannah_vet']} gently examines {C['rosie_cavalier']}'s ear "
        f"with a handheld otoscope. Rosie sits calmly on the padded exam "
        f"table, looking relaxed. Soft daylight through a frosted window, "
        f"out-of-focus equipment behind. Caring and competent mood. "
        f"STRICTLY PG — nothing graphic."
    ),

    "vet-bills-uk-pos3": _p(
        f"Editorial lifestyle photograph of an empty, clean, modern UK "
        f"veterinary operating theatre — soft overhead surgical lights, a "
        f"neat padded operating table, and a tray of plain stainless steel "
        f"instruments. No people, no animals, no blood, no patients. "
        f"Muted sage and cream tones, natural daylight through a frosted "
        f"window. Calm and reassuring."
    ),

    "vet-bills-uk-pos4": _p(
        f"Warm lifestyle photograph of {C['james_40s']} kneeling on a "
        f"soft rug in a bright British living room, smiling as he cuddles "
        f"{C['bear_bernese']} who is fully recovered and happy. A toy sits "
        f"nearby. Soft daylight through the window, muted warm palette, "
        f"genuinely joyful atmosphere."
    ),

    # ---- emergency-vet-costs-uk body ----
    "emergency-vet-costs-uk-pos2": _p(
        f"Warm emotional photograph of {C['chloe_early20s']} standing in a "
        f"softly-lit UK hallway at dusk, holding a smartphone to her ear "
        f"with a focused, concerned expression. {C['poppy_dachshund']} "
        f"rests in her other arm wrapped in a soft blanket. Phone screen "
        f"angled away, no text. Muted warm tones, shallow depth of field."
    ),

    "emergency-vet-costs-uk-pos3": _p(
        f"PG editorial photograph of {C['finn_frenchie']} resting calmly "
        f"on a padded vet recovery mat with a soft white gauze bandage on "
        f"one front leg and a gentle clear IV line attached. He looks "
        f"peaceful. Out-of-focus vet equipment behind. STRICTLY PG — no "
        f"blood, no wounds, no distress."
    ),

    "emergency-vet-costs-uk-pos4": _p(
        f"Warm emotional photograph of {C['emma_late20s']} kneeling on a "
        f"wooden-floored British hallway, hugging {C['finn_frenchie']} "
        f"tightly with a huge relieved smile. Finn wears a small soft "
        f"bandage on one paw and looks happy. Soft daylight, muted warm "
        f"palette, joyful reunion atmosphere."
    ),

    # ---- puppy-first-year-checklist body ----
    "puppy-first-year-checklist-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). Four "
        f"friendly cartoon puppies (a Cockapoo, a Labrador, a Dachshund, "
        f"and a Spaniel) sit in a gentle semicircle on a pastel floor, "
        f"looking up attentively at a simple abstract figure of a trainer "
        f"whose raised hand holds a small bone-shaped treat. Pastel "
        f"palette of teal (#189181) and soft purple (#8A44F3), warm beige "
        f"background, clean simple shapes, no text."
    ),

    # ---- senior-dog-care body ----
    "senior-dog-care-pos2": _p(
        f"A soft, modern flat illustration (not a photograph). An older "
        f"grey-muzzled chocolate Labrador rests peacefully on a large "
        f"round orthopaedic cushion. A small water bowl and a simple toy "
        f"sit nearby. Pastel palette of teal (#189181) and soft purple "
        f"(#8A44F3), warm beige background, clean simple shapes, tender "
        f"and dignified mood, no text."
    ),

    "senior-dog-care-pos3": _p(
        f"A soft, modern flat illustration (not a photograph). An older "
        f"grey-muzzled Labrador sits calmly on an exam cushion while a "
        f"cartoon-style vet gently rests a stylised ultrasound wand "
        f"against his side. Simple abstract equipment shapes. Pastel "
        f"palette of teal (#189181) and soft purple (#8A44F3), warm beige "
        f"background, clean simple shapes, caring mood, no text."
    ),

    # ---- cockapoo-cost-uk body ----
    "cockapoo-cost-uk-pos2": _p(
        f"Warm lifestyle photograph of {C['milo_cockapoo']} sitting "
        f"happily in a patch of soft British garden grass on a sunny "
        f"afternoon. Gentle wildflowers and bokeh behind him, shallow "
        f"depth of field, warm golden sidelight, cheerful curious "
        f"expression."
    ),

    "cockapoo-cost-uk-pos3": _p(
        f"Warm lifestyle photograph of {C['milo_cockapoo']} being gently "
        f"dried with a soft cream towel in a bright, clean British "
        f"grooming salon setting. His curls are damp, eyes bright. A "
        f"grooming brush and a plain ceramic water bowl sit out of focus "
        f"nearby. Soft natural light, muted warm palette, no text on "
        f"bottles or signs."
    ),

    # ---- cost-of-owning-dog-uk body ----
    "cost-of-owning-dog-uk-pos2": _p(
        f"Warm emotional photograph of {C['lucy_40s']} kneeling on a "
        f"pastel rug in a softly-lit UK rescue centre reception, meeting "
        f"{C['max_jrt']} for the first time. Max looks up hopefully with "
        f"bright eyes. Soft daylight, muted warm palette, hopeful gentle "
        f"mood, no signs or lettering in view."
    ),

    "cost-of-owning-dog-uk-pos3": _p(
        f"Warm lifestyle photograph of {C['luna_golden']} being brushed "
        f"gently in a bright clean British grooming salon by a focused "
        f"groomer. Luna stands calmly, glossy coat, relaxed expression. "
        f"Out-of-focus grooming tools in the background, no text, no "
        f"labels, soft daylight."
    ),

    # ---- best-cat-insurance-uk body ----
    "best-cat-insurance-uk-pos2": _p(
        f"Warm PG photograph of {C['whiskers_maine']} sitting calmly on "
        f"a padded grey vet examination table, ears relaxed. "
        f"{C['hannah_vet']} rests one gentle hand softly on his back, "
        f"expression focused and caring. Soft daylight through a frosted "
        f"window, out-of-focus vet equipment behind. No blood, no "
        f"distress."
    ),

    "best-cat-insurance-uk-pos3": _p(
        f"Warm lifestyle photograph split across two soft focal moments: "
        f"{C['luna_ragdoll']} sits peacefully on a cushioned sunlit "
        f"windowsill indoors, while {C['tigger_ginger']} prowls contentedly "
        f"through a blooming cottage-garden flowerbed outside. Natural "
        f"light, shallow depth of field, warm palette. No text."
    ),
}


def get_body_prompt(slug: str, position: int) -> str | None:
    """Return a curated body-image prompt for a given (slug, position),
    or None if we should fall back to the generic style + description."""
    return BODY_PROMPTS.get(f"{slug}-pos{position}")
