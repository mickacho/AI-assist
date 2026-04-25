<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=600&lines=AI+Research+Assistant;Academic+Paper+Generator;Powered+by+GPT-4" />
</h1>

<p align="center">
  <i>Generate structured academic research reports — papers, formulas, and trends — from a single prompt.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-0A0A0A?style=for-the-badge&logo=python&logoColor=yellow" />
  <img src="https://img.shields.io/badge/LangChain-0A0A0A?style=for-the-badge&logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-GPT--4-0A0A0A?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-0A0A0A?style=for-the-badge&logo=pydantic&logoColor=red" />
</p>

---

## What it does

You enter a research topic, a set of key questions, and a time frame. The assistant returns a fully structured report with:

- **6–9 relevant papers** — title, authors, year, venue, URL, and why each is relevant
- **Key mathematical formulas** — with LaTeX code and references
- **Recent trends** — with descriptions and source URLs

All output is structured via Pydantic schemas and printed as clean JSON — ready to pipe into your own pipeline, frontend, or document generator.

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install langchain langchain-openai pydantic python-dotenv
```

### 4. Set your API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-key-here
```

> No API key? The tool runs in **mock mode** automatically — returning sample data so you can explore the output structure without spending credits.

### 5. Run

```bash
python main.py
```

You'll be prompted for:

```
Enter the research topic: transformer attention mechanisms
Key research questions: how does self-attention scale with sequence length
What time frame should the papers be from: 2020-2024
```

---

## Output format

```json
{
  "topic": "transformer attention mechanisms",
  "research_questions": ["how does self-attention scale with sequence length"],
  "time_frame": "2020-2024",
  "papers": [
    {
      "title": "FlashAttention: Fast and Memory-Efficient Exact Attention",
      "authors": ["Dao, T.", "Fu, D.Y.", "Ermon, S."],
      "year": 2022,
      "venue": "NeurIPS",
      "url": "https://arxiv.org/abs/2205.14135",
      "relevance": "Addresses the quadratic complexity bottleneck in self-attention"
    }
  ],
  "formulas": [
    {
      "name": "Scaled Dot-Product Attention",
      "latex": "\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V",
      "description": "Core attention mechanism scaling queries and keys by dimension",
      "reference": "Vaswani et al. (2017)"
    }
  ],
  "trends": [
    {
      "title": "Linear Attention Approximations",
      "description": "Research into reducing attention from O(n²) to O(n) complexity",
      "references": ["https://arxiv.org/abs/2006.16236"]
    }
  ]
}
```

---

## Project structure

```
ai-research-assistant/
├── main.py          # Entry point — schemas, model init, async runner
├── .env             # Your API key (never commit this)
├── .env.example     # Safe template to share
├── .gitignore
└── README.md
```

---

## Configuration

| Variable | Description | Default |
|---|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key | runs in mock mode if unset |

To swap models, change this line in `main.py`:

```python
model = init_chat_model("gpt-4-0613", model_provider="openai")
```

Supported drop-in replacements: `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`

---

## Requirements

- Python 3.10+
- OpenAI API key (optional — mock mode available)

```
langchain
langchain-openai
pydantic
python-dotenv
```

---

## .gitignore reminder

Make sure your `.env` is never committed:

```
.env
.venv/
__pycache__/
*.pyc
```

---

## License

MIT — use it, fork it, build on it.
