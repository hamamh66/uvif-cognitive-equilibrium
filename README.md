# Variational Equilibrium as an Organizing Principle of Natural and Artificial Cognitive Systems

LaTeX source and companion simulation for the single-author manuscript

> **Variational Equilibrium as an Organizing Principle of Natural and Artificial
> Cognitive Systems: From Objective Maximization to Balanced Persistence**
> H. Hamam — Faculty of Engineering, Université de Moncton

**Status:** manuscript in preparation for submission to *Cognitive Systems Research*
(Elsevier). This repository is private while the manuscript is under review.

---

## Contents

| Path | What it is |
|---|---|
| `main.tex` | Manuscript root (`elsarticle`, `review` mode, `elsarticle-num`) |
| `Sections/` | Body sections, one file per section |
| `Sections/References.bib` | Bibliography — 58 entries |
| `Figures/` | Conceptual figures |
| `notebook/` | Companion simulation of the Section 6.6 predictions |
| `notebook/outputs/` | Figures, tables and run log produced by that notebook |

## Building

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Compiles clean: 59 pages, no undefined citations or cross-references, no uncited
bibliography entries.

## The companion notebook

`notebook/UVIF_Cognitive_Equilibrium_H1_H4.ipynb` implements the five forces as explicit
functions and tests the four predictions H1–H4 stated in Section 6.6. It ships executed,
with outputs and figures embedded.

Three rules govern it, and they are worth stating because they are the reason to trust
the numbers:

1. **Nothing is tuned on what it is scored on.** Environments are split once into disjoint
   calibration and evaluation sets; every comparator's free parameters are fitted on
   calibration and every reported number comes from evaluation.
2. **No hand-set weight vector decides a headline result.** State dependence lives inside
   the force functions. Comparator weights are searched densely, and the search range is
   widened until the fit stops improving, so the comparator is never understated.
3. **Seed-fixed and deterministic.** Policy search is an exhaustive grid argmax.

### Results

| Prediction | Verdict | Evidence |
|---|---|---|
| **H1** state-dependent force weighting | supported in-model | best fixed-weight agent's held-out error is 1.52× the mean-policy baseline — worse than predicting the mean; UVIF plays 33 distinct policies across 90 held-out environments, the comparator 1 |
| **H2** sustainability beyond the episode | supported in-model | sustained-regime policy is locally suboptimal by 0.374 per episode yet stays viable; the single-episode policy exhausts its resource immediately |
| **H3** irreversibility ≠ large negative utility | supported only in the narrow form | best monotone penalty leaves ~10–15% unexplained, but its coefficient runs to whatever ceiling the search allows |
| **H4** per-force failure signatures | supported in-model | four ablations give four distinguishable deployment curves |

All conclusions survive ±40% perturbation of every model constant (Section 8 of the
notebook).

### What the notebook does not establish

It is a simulation of the framework's own dynamics, not evidence about real cognitive
systems. The functional forms were chosen by the author. A confirmed prediction here means
the framework is internally coherent and the predicted signature is well defined and
measurable — not that it is true of human or animal cognition. Section 10 of the manuscript
states that the paper reports no experiments, and that statement stands.

H3 failed on first implementation — protection was modelled as an additive penalty, which
*is* a large negative utility, so the test was vacuous and returned a perfect fit. The
failure and its diagnosis are retained in Section 5 of the notebook rather than removed,
and they are why the manuscript now states H3 in its restricted finite-coefficient form.

## Related work

A companion empirical study, *Thresholds as Institutional Commitments: Limits of
Confidence-Based Human Review*, is under review at *Social Sciences & Humanities Open*.
The two papers are independent: neither depends on the other for its claims.

## License

All rights reserved pending publication.
