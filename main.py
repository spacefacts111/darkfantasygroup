import os
import importlib
from plugin import ContentItem
from dotenv import load_dotenv

# Load local .env (for dev)
_dotenv = os.path.join(os.path.dirname(__file__), ".env")
if os.path.isfile(_dotenv):
    load_dotenv(_dotenv)

# Read config
from config import (
    PROVIDER, PROVIDER_ARGS,
    CAPTIONER, CAPTIONER_ARGS,
    POSTER, POSTER_ARGS
)

# Dynamically build components

def build_component(fqcn: str, args: dict):
    module = importlib.import_module('plugin')
    cls = getattr(module, fqcn)
    return cls(**args)


def main():
    # Instantiate
    provider  = build_component(PROVIDER, PROVIDER_ARGS)
    captioner = build_component(CAPTIONER, CAPTIONER_ARGS)
    poster    = build_component(POSTER, POSTER_ARGS)

    # 1) Get content
    item: ContentItem = provider.get_next_item()

    # 2) Generate caption & hashtags
    caption, hashtags = captioner.make_caption(item)
    message = f"{caption}\n\n{hashtags}"

    # 3) Publish to Group
    post_id = poster.publish(item, message)
    print(f"✅ Group post ID: {post_id}")

if __name__ == "__main__":
    main()
