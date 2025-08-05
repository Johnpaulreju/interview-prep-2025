# Baseline Quiz – ML/AI Interview Mastery  
*Date: 6 Aug 2025*  
*Instructions: answer without external references to give an honest snapshot of your current recall. Show workings where asked.*

---

## Math & Stats

1. **Linear Algebra**  
   Show that if \(A\) is full-rank and square, \((A^{\top}A)^{-1}A^{\top}\) is the left inverse of \(A\).

2. **Linear Algebra**  
   State and (briefly) prove the spectral theorem for real symmetric matrices.

3. **Calculus**  
   Derive \(\dfrac{\partial}{\partial x}(x^{\top}Ax)\) for symmetric \(A\).

4. **Probability**  
   Give a real-world example where the Beta prior is conjugate to the Binomial likelihood and compute the posterior parameters.

5. **Information Theory**  
   Compute the entropy of  
   *a)* a fair 4-sided die, and  
   *b)* an unfair die with \(P = (0.7,\,0.1,\,0.1,\,0.1)\).

---

## Classical Machine Learning

6. **Bias / Variance**  
   Decompose \(E[(\hat f(x)-f(x))^{2}]\) into bias² + variance + noise.

7. **k-Nearest Neighbours**  
   Why does test error approach Bayes error as \(k\!\to\!\infty\) and \(n\!\to\!\infty\) with \(k/n\!\to\!0\)?

8. **Naïve Bayes**  
   Derive the Gaussian NB decision boundary for two classes assuming equal variance.

9. **Decision Trees**  
   Define *cost-complexity pruning* and show how the parameter \(\alpha\) trades off tree size vs. fit.

10. **Support Vector Machines**  
    Write the dual for the soft-margin SVM and explain each constraint term.

---

## Deep Learning

11. **Activations**  
    Prove that ReLU is piece-wise linear and discuss its effect on gradient flow.

12. **Back-propagation**  
    For a single hidden-layer MLP, derive the gradient of MSE with respect to the weights.

13. **Convolutional NNs**  
    Calculate the receptive field of a 3-layer ConvNet with kernel sizes (3, 3, 3) and stride 1 throughout.

14. **Recurrent NNs**  
    Explain the vanishing-gradient problem mathematically for a vanilla RNN.

15. **Optimizers**  
    Write Adam’s parameter update in a single equation and explain each bias-correction term.

---

## Transformers & LLMs

16. **Attention**  
    Why is the \(\sqrt{d_k}\) scaling necessary in dot-product attention?

17. **Positional Encoding**  
    Show that sinusoidal positional encodings allow any fixed offset to be expressed as a linear function of two basis frequencies.

18. **Training Dynamics**  
    Sketch the reasoning behind Kaplan et al.’s scaling law \(L(N) \propto N^{-\alpha}\).

19. **Fine-Tuning (LoRA)**  
    Explain the LoRA decomposition \(W = W_0 + BA\) and how rank \(r\) affects FLOPs and memory use.

20. **Alignment (RLHF)**  
    Write the PPO *clipped* objective used in RLHF and interpret each term.

---

## Gen-AI · Agents · RAG

21. **Tokenization**  
    Perform one merge step of BPE for the corpus **“low lower lowest”** starting from a character vocabulary.

22. **Embeddings**  
    What is the numerical range of cosine similarity, and why is it often preferred over Euclidean distance for dense text vectors?

23. **Retrieval-Augmented Generation**  
    List two scenarios where hybrid BM25 + dense retrieval outperforms pure dense retrieval.

24. **LangChain**  
    Name three LCEL building blocks and describe their role in a ReAct agent chain.

25. **Voice AI**  
    Define CTC loss formally and state the key independence assumption it relies on.

---

## MLOps · Production

26. **Docker**  
    Explain the difference between `CMD` and `ENTRYPOINT`.

27. **Monitoring**  
    Provide a formula for detecting **concept drift** using the Kolmogorov-Smirnov statistic.

28. **A/B Testing**  
    Compute the z-score for a lift from 10 % to 12 % on 5 000 samples per arm.

29. **Ethics & Privacy**  
    In plain English, what does differential privacy’s \((\epsilon, \delta)\) guarantee mean?

30. **Model Security**  
    How does model watermarking help detect extraction attacks?

---

### Submission

- Save this file as `baseline_quiz.md` in the project root.  
- Commit & push before **23:59 IST, 6 Aug 2025**.

Good luck — and remember: clarity over quantity!
