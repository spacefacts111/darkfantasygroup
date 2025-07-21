# Railway‑Deployed Facebook GROUP Bot (Dark Fantasy Vibes)

This standalone repo runs a bot that:
1. Generates dark‑fantasy images via DALL·E
2. Crafts captions & hashtags using Google Trends + GPT
3. Posts to your Facebook **Group** on a schedule

## Setup

1. **Env Vars** (Railway Settings → Variables):
   - `OPENAI_API_KEY`
   - `FB_GROUP_ID`          # your target Facebook Group ID
   - `FB_PAGE_TOKEN`       # long‑lived token for your account

2. **Deploy**
   - Connect this repo to Railway
   - In **Plugins → Scheduled Jobs**, add:
     ```
     Command: python main.py
     Schedule: 0 9 * * *   # runs at 10:00 BST
     ```

3. **Enjoy**! Your Group will receive fresh, dark‑fantasy posts daily.
