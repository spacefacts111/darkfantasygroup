# All prompts are dark‑fantasy core with fresh twists\ nPROMPTS = [
    "An ominous dark fantasy castle perched atop a shattered obsidian spire, bathed in psychedelic auroras",
    "A shadowy dragon with glowing, otherworldly runes soaring through a neon-tinged cosmic storm",
    "A haunted forest of twisted black trees with luminescent mushrooms under a swirling galaxy",
    "Dark knights in ethereal armor wandering a floating labyrinth of swirling fractal portals",
    "A colossal ancient rune circle dripping with starlight in a ghostly, psychedelic wasteland"
]

PROVIDER        = "DalleImageProvider"
PROVIDER_ARGS   = {"prompts": PROMPTS}

CAPTIONER       = "TrendAwareCaptioner"
CAPTIONER_ARGS  = {"gpt_model": "gpt-4o-mini", "trending_kw_count": 3}

POSTER          = "720231214218582"
POSTER_ARGS     = {}  # uses FB_GROUP_ID & FB_PAGE_TOKEN env vars
