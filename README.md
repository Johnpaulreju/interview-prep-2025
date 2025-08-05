# 🚀 30-Day ML/AI Interview Mastery Program

*Complete study-plus-build curriculum for mastering Machine Learning and AI concepts with mathematical rigor*

## 0. Orientation (Tonight, 6 Aug)

| What                 | How                                                                                        | Output                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Baseline package** | 30‑item Google Form (math, coding, ML theory); 10‑min live chat to set goals & constraints | *Gap matrix* (I'll tag every topic 0 – 5) + **Personal Road‑Signs** PDF: which remedial pods to activate |
| **Repo skeleton**    | GitHub template with branch‑per‑topic, pre‑wired pytest + nbval                            | Push test commit                                                                                         |

> **Personalisation rule:** if any section in the gap matrix scores < 3, the matching "Remedial Pod" (see legend 🔧) is auto‑inserted on the next available light day.

---

# 🗓️ 30‑Day Map (6 Aug → 5 Sep, interview 6 Sep)

### DAILY RHYTHM  *(≈ 2 h weekday, 4 h weekend)*

| Minute | Slot                  | Method                                                        |
| ------ | --------------------- | ------------------------------------------------------------- |
| 0‑10   | **Spaced Repetition** | Anki deck (auto‑generated from yesterday's notes)             |
| 10‑40  | **Math Deep Read**    | Derivation walk‑through (PDF + whiteboard gif)                |
| 40‑85  | **Code‑From‑Scratch** | Start in NumPy ➜ refactor to scikit‑learn or PyTorch          |
| 85‑100 | **Interview Drill**   | 3 live questions (1 theory, 1 design, 1 "explain like I'm 5") |
| END    | **Commit + PR**       | Notebook tests must pass CI                                   |

*(Weekend blocks concatenate two daily slots; last 30 min is peer/mentor review.)*

---

## Legend of 🔧 Remedial Pods (auto‑inserted if score < 3)

| Pod           | Trigger            | Content                                                                    |
| ------------- | ------------------ | -------------------------------------------------------------------------- |
| **LINALG‑🔧** | Linear algebra < 3 | Basis → eigen, SVD, matrix calculus, 1 extra day                           |
| **MATH‑P**    | Probability < 3    | Bayes, conjugate priors, likelihood vs. posterior                          |
| **DL‑BOOT**   | DL < 2             | Perceptron, back‑prop, ReLU, basic CNN; replaces a Gen‑AI Friday if needed |

---

## Week 1 — Math & Classical ML Foundations

| Date                       | Theme                     | Crystal‑Clear Take‑aways                                                                                      | Hands‑On / Eval                                     |
| -------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **6 Aug**                  | Baseline & Linear Algebra | Why eigenvectors define invariant sub‑spaces; full derivation of SVD; *why* XᵀX appears in normal equation    | Ridge & OLS notebooks + quiz                        |
| **7 Aug**                  | Bayes Core                | Conjugate prior proofs; MAP vs. MLE; Laplace vs. Jeffreys smoothing math                                      | Build Gaussian & Multinomial NB; PR review          |
| **8 Aug**                  | Entropy & Trees           | Info‑Gain vs. Gini math; cost‑complexity pruning proof                                                        | Decision‑Tree + RF notebook; 5‑Q drill              |
| **9 Aug** **(Gen‑AI F#1)** | Tokenization              | BPE merge‑rank proof; WordPiece likelihood maximisation; UnigramLM; OOV math                                  | Write your own BPE; compare tokens across languages |
| **10‑11 Aug (WE)**         | Ensembles + Clustering    | Bias‑variance math for bagging; AdaBoost exponential loss deriv.; EM algorithm; Voronoi intuition for k‑Means | Animate k‑Means & EM; 5‑min lightning talk video    |
| **12 Aug**                 | SVM                       | KKT conditions proof; kernel trick geometry; VC‑dimension intuition                                           | Quad‑prog SVM + RBF; explain mis‑classifications    |

---

## Week 2 — Deep Learning Core

| Date                            | Theme            | Crystal‑Clear Take‑aways                                                                    | Hands‑On / Eval                             |
| ------------------------------- | ---------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **13 Aug**                      | NN & Back‑prop   | Universal Approx. theorem; Jacobian‑style back‑prop; weight‑init statistics                 | MLP on Fashion‑MNIST; grad‑check unit tests |
| **14 Aug** **(Voice Thursday)** | Audio AI         | CTC loss deriv.; Mel filter‑bank math; Tacotron attention alignment                         | Wav2Vec2 ASR + Tacotron TTS Colab           |
| **15 Aug**                      | **REST/Async**   | Light reading + peer code reviews                                                           | —                                           |
| **16‑17 Aug (WE)**              | CNN‑Internals    | Convolution theorem; receptive field calc; batch‑norm var. deriv.; pooling invariance proof | CNN from scratch, filter viz                |
| **18 Aug**                      | RNN ↔ LSTM       | Gate math, vanishing‑grad proof; TBPTT cost                                                 | Bi‑LSTM for NER; compare GRU                |
| **19 Aug** **(Gen‑AI T#2)**     | Image Generative | VAE ELBO, KL tricks; GAN min‑max; diffusion score match                                     | Train tiny VAE; identify mode collapse      |

---

## Week 3 — Transformers & LLMs

| Date                        | Theme                   | Crystal‑Clear Take‑aways                                          | Hands‑On / Eval                           |
| --------------------------- | ----------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| **20 Aug**                  | Attention               | √d\_k scaling proof; Bahdanau vs. Luong math                      | Implement attention in NumPy              |
| **21 Aug**                  | Transformer Skeleton    | Pre‑norm vs. post‑norm gradient math; FFN 4 × size rationale      | Encoder‑decoder full cycle                |
| **22 Aug** **(Gen‑AI F#2)** | LLM Training            | Cross‑entropy; scaling laws curve‑fit; gradient clipping analysis | GPT‑mini (12‑layer) on WikiText‑2         |
| **23‑24 Aug (WE)**          | Fine‑tuning & Alignment | LoRA matrix math; QLoRA quant; PPO, DPO derivations               | Fine‑tune Alpaca‑7B; reward model sandbox |
| **25 Aug**                  | Evaluations             | Perplexity pitfalls; GEMBA; BERTScore math                        | Eval script; create synthetic fail cases  |

---

## Week 4 — Agents, RAG & Prod‑Ops

| Date                           | Theme                  | Crystal‑Clear Take‑aways                                                        | Hands‑On / Eval                                      |
| ------------------------------ | ---------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **26 Aug** **(Agents Monday)** | Reasoning Agents       | ReAct loop maths; tool‑calling protocol spec; chain‑of‑thought entropy          | ReAct agent in LangChain; unit tests for tool errors |
| **27 Aug**                     | LangChain & RAG        | LCEL graph theory; vector vs. hybrid retrieval maths                            | Build Pinecone RAG; measure recall Δ                 |
| **28 Aug**                     | Embeddings & Retrieval | Cosine vs. dot; DPR dual‑encoder loss; ColBERT MaxSim deriv.                    | Train SBERT‐tiny; compare SPLADE                     |
| **29 Aug** **(Gen‑AI F#3)**    | Voice Agents           | Real‑time ASR windowing math; VAD ROC trade‑off; speaker diarization clustering | WebRTC voice bot; latency report                     |
| **30‑31 Aug (WE)**             | MLOps                  | A/B test stats; concept‐drift KS test; Triton batching queue theory             | CI/CD + Prometheus dashboards                        |

---

## Final Stretch

| Date      | Theme                | Output                                                |
| --------- | -------------------- | ----------------------------------------------------- |
| **1 Sep** | Ethics & Safety      | One‑pager cheat‑sheet; scenario Q\&A                  |
| **2 Sep** | Mock Interview #1    | Full scorecard; identify red zones                    |
| **3 Sep** | Buffer / Restitution | Plug gaps flagged in scorecard                        |
| **4 Sep** | Mock Interview #2    | Systems‑design + behavioural                          |
| **5 Sep** | **Power‑Review**     | 250‑card Anki blitz; formula sheet; confidence ritual |
| **6 Sep** | **Interview Day**    | —                                                     |

---

### Built‑in Evaluation & Feedback

| Checkpoint              | Method                               | Threshold          |
| ----------------------- | ------------------------------------ | ------------------ |
| **Mid‑Week Quiz (Wed)** | 5 multi‑part questions (auto‑graded) | ≥ 80 % to proceed  |
| **Weekend Peer Review** | Swap notebooks with mentor (or me)   | All tests green    |
| **Mock Interviews**     | Live 105 min; graded rubric          | ≥ 70 % each domain |

*If a threshold isn't met, the next day becomes "Remedial Focus"; original topic shifts to the buffer day.*

---

## Framework & Tool Commitments

| Area         | Primary Stack                           | Why                                |
| ------------ | --------------------------------------- | ---------------------------------- |
| Classical ML | **scikit‑learn, NumPy**                 | Bread‑&‑butter interview libs      |
| DL + LLM     | **PyTorch + Lightning**                 | Clean Trainer/Callback API         |
| Agents & RAG | **LangChain 0.2+**                      | LCEL graphs & tool calling         |
| Voice        | **Wav2Vec2, WebRTC, Rasa**              | Industrial‑strength ASR & dialogue |
| Deploy       | **FastAPI, Triton, Docker, GH Actions** | Reusable infra patterns            |

---

## Learning Assets You'll Receive

* **Daily Lesson Deck** (PDF) – definition + history + derivation + alternatives
* **Whiteboard GIF** – animated derivation for visual memory
* **Hands‑On Notebook** – NumPy baseline → optimized version (sklearn/PyTorch)
* **Auto‑Gen Anki Cards** – every symbol, formula, hyper‑parameter
* **Flash‑Card Deck** – "Explain X in 60 sec" prompts
* **Mock Interview Rubrics** – detailed feedback per competency
* **Architecture Stencils** – draw\.io templates for whiteboard questions
* **Cheat‑Sheets** – 1‑page quick‑reference per major family (trees, attention, RAG…)

All assets live in the repo; CI enforces notebook‑runs = ✅ and lint = ✅ before merge.

---

## Next Actions (Your Side)

1. **Confirm** that the map & rhythm fit your calendar (esp. weekends).
2. **Tell me** your preferred comms channel for daily drills.
3. Complete tonight's **Baseline package** before midnight IST so we can auto‑insert any 🔧 Remedial Pods by tomorrow morning.

---

## Repository Structure

```
ml-ai-interview-mastery/
├── README.md
├── requirements.txt
├── setup.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── notebooks/
│   ├── week1/
│   ├── week2/
│   ├── week3/
│   └── week4/
├── src/
│   ├── classical_ml/
│   ├── deep_learning/
│   ├── transformers/
│   └── agents/
├── tests/
├── assets/
│   ├── lesson_decks/
│   ├── whiteboard_gifs/
│   ├── anki_cards/
│   └── cheat_sheets/
└── docs/
```

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Complete the baseline assessment
4. Follow the daily curriculum starting with Week 1
5. Submit notebooks via PR for review

## License

This curriculum is designed for personal learning and interview preparation. All implementations are for educational purposes.
