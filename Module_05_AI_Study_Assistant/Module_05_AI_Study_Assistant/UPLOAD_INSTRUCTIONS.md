# How to Upload This Project (GitHub + LinkedIn)

## Part 1 – Upload to GitHub (no command line needed)

1. Go to https://github.com and sign in (create a free account if needed).
2. Click the **+** icon (top right) → **New repository**.
3. Repository name: `ai-study-buddy`
   - Description: `AI-powered study assistant built with the Gemini API`
   - Choose **Public**
   - Tick **Add a README file**? **No** (we already have one).
   - Click **Create repository**.
4. On the new empty repo page, click **uploading an existing file**.
5. Drag and drop these files from the `ai-study-buddy` folder:
   - `index.html`
   - `README.md`
   - `LICENSE` (if present)
6. Scroll down, write a commit message like `Initial commit: AI Study Buddy`, and click **Commit changes**.

## Part 1b – (Optional) Upload using Git commands

```bash
cd ai-study-buddy
git init
git add .
git commit -m "Initial commit: AI Study Buddy"
git branch -M main
git remote add origin https://github.com/<your-username>/ai-study-buddy.git
git push -u origin main
```

## Part 2 – Make it live with GitHub Pages (bonus, free)

1. In your repo, go to **Settings → Pages**.
2. Under **Build and deployment**, set Source = **Deploy from a branch**.
3. Branch = **main**, folder = **/ (root)**, click **Save**.
4. After 1–2 minutes your app is live at:
   `https://<your-username>.github.io/ai-study-buddy/`
5. Add this link to your README and your LinkedIn post.

## Part 3 – Post on LinkedIn

1. Open `LINKEDIN_POST.md` and copy the post text.
2. Replace `<your-github-repo-link>` and `<your-live-demo-link>` with your real links.
3. On LinkedIn click **Start a post**, paste the text.
4. Add a screenshot or a short screen recording of the app (it makes the post perform much better).
5. Click **Post**.
6. Copy the post URL and submit it with your GitHub repo link as your deliverables.

## Checklist before submitting

- [ ] Repo is **Public**
- [ ] README is visible on the repo page
- [ ] No API key is inside any file
- [ ] LinkedIn post is published with the repo link
