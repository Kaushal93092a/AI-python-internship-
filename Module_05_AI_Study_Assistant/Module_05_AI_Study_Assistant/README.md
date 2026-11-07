# 📚 AI Study Buddy

A simple AI-powered web app that helps you learn faster. Paste a topic, notes, or code, choose a mode, and the Google Gemini API does the rest.

Built as the mini project for **Module 05 – AI Tools & Mini Project**.

## ✨ Features

- 🧒 **Explain it simply** – beginner-friendly explanations with analogies
- 📝 **Summarize** – turn long notes into key bullet points
- ❓ **Quiz generator** – 5 multiple-choice questions with answer key
- 💻 **Code helper** – explains and debugs code
- 🗓️ **Study planner** – a 3-day plan for any topic
- 🔒 Your API key stays in your own browser (localStorage); there is no backend

## 🚀 How to run

1. Download or clone this repo.
2. Open `index.html` in any browser (just double-click it).
3. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and paste it into the app.
4. Choose a mode, type your topic, and click **Ask AI**.

## 🛠️ Tech stack

- HTML, CSS, vanilla JavaScript
- Google Gemini API (`generateContent` endpoint)

## 🤖 How AI tools helped me build this

- Used an AI assistant (Claude / ChatGPT / Gemini) to plan features, write the first draft of the code, and improve prompts.
- Learned how prompt wording changes answer quality (see the `PROMPTS` object in `index.html`).

## 📈 Future improvements

- Chat history and follow-up questions
- Save quizzes and notes
- Dark mode
- Streaming responses

## ⚠️ Note on API keys

Never commit your API key to GitHub. This app asks for the key at runtime, so nothing secret is stored in the code.

## 📄 License

MIT
