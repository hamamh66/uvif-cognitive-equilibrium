# Variational Equilibrium as an Organizing Principle of Natural and Artificial Cognitive Systems

LaTeX source and companion simulation code for the manuscript:

> **Variational Equilibrium as an Organizing Principle of Natural and Artificial Cognitive
> Systems: From Objective Maximization to Balanced Persistence**
> Habib Hamam, Faculty of Engineering, Université de Moncton, Moncton, NB, Canada.

*Status: under review.*

---

## The paper in brief

Cognitive systems, biological and artificial, are commonly modelled as optimizers: agents
that maximize a scalar objective such as reward, utility, accuracy, or negative prediction
error. The paper argues that maximization is the wrong idealization for a cognitive system
that must stay functional over long horizons, and develops an alternative.

The **Unified Variational Intelligence Framework (UVIF)** characterizes cognition as the
continuous, constrained balancing of five competing forces:

| Force | Role |
|---|---|
| Epistemic pull | acquisition of information that reduces uncertainty |
| Protective shield | preservation of states whose loss is unrecoverable |
| Computational drag | the resource cost of inference itself |
| Efficiency imperative | action within the window in which it remains useful |
| Sustainability field | feasibility of the operating policy over long horizons |

The organizing principle is **Variational Equilibrium**: an operating manifold along which
no force can be further satisfied without violating the admissibility constraints imposed
by the others. The paper positions this against the free-energy principle and active
inference, resource-rational analysis, allostatic regulation, and integrated cognitive
architectures, and states four predictions (H1–H4) by which the framework can be
distinguished from them.

## Repository contents

| Path | Description |
|---|---|
| `main.tex` | Manuscript root |
| `Sections/` | Body sections, one file each |
| `Sections/References.bib` | Bibliography |
| `Figures/` | Conceptual figures |
| `notebook/UVIF_Cognitive_Equilibrium_H1_H4.ipynb` | Simulation of predictions H1–H4 |
| `notebook/outputs/` | Figures, tables and run log produced by the notebook |

## Building the manuscript

Requires a TeX distribution with `elsarticle`. The class and bibliography style files are
included.

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Produces a 59-page document in Elsevier review format, with no undefined citations or
cross-references.

## Running the simulation

```bash
pip install numpy pandas matplotlib jupyter
jupyter notebook notebook/UVIF_Cognitive_Equilibrium_H1_H4.ipynb
```

The notebook runs top to bottom in under a minute on a laptop, with no GPU and no external
data. It is committed with its outputs already executed, so the results can be read without
running anything. Outputs are written to `Outputs/UVIF_CognitiveEquilibrium_Article2/`
relative to the working directory, or to Google Drive if run in Colab.

## What the simulation tests

The five forces are implemented as explicit functions of a policy and an environment state.
Each of the paper's four predictions is then tested against a comparator drawn from the
accounts the paper contrasts itself with.

| Prediction | Result |
|---|---|
| **H1** — the balance between epistemic and pragmatic drives is a state variable, not a fixed model parameter | Supported. The best fixed-weight comparator, fitted on held-out environments, has 1.52× the error of predicting the mean policy. The framework produces 33 distinct policies across 90 environments; the comparator produces 1. |
| **H2** — long-horizon viability is a force in its own right, not a long-horizon utility term | Supported. Under an identical payoff structure, the sustained-regime policy is locally suboptimal by 0.374 per episode yet remains viable indefinitely, while the single-episode policy exhausts its resource budget. |
| **H3** — exposure to unrecoverable outcomes is an admissibility constraint, not a large negative utility | Supported in restricted form only. The best monotone utility penalty leaves 10–15% of held-out policy variation unexplained, but its fitted coefficient grows without bound as the search range widens. A sufficiently steep penalty therefore approximates the constraint in the limit, and only the finite-coefficient claim is defensible. |
| **H4** — suppressing a single force produces a characteristic failure mode | Supported. Four single-force ablations yield four distinguishable deployment trajectories, two of which end in viability failure by different routes. |

Every qualitative conclusion survives ±40% perturbation of each of the six model constants.

### Methodology

* Environments are split once into disjoint calibration and evaluation sets. Comparator
  parameters are fitted on calibration; all reported figures come from evaluation.
* Comparator search ranges are widened until the fit stops improving, so no result depends
  on having understated the alternative.
* Policy search is an exhaustive grid argmax under a fixed seed, so runs are deterministic.

### Scope

The notebook is a simulation of the framework's own dynamics using functional forms chosen
by the author. It establishes that each prediction is well posed and that the framework
produces the predicted signature where a natural comparator does not. It is **not** evidence
about human or animal cognition, and does not test the framework empirically. The
experimental designs that would do so are set out in the manuscript, which reports no
experiments and presents UVIF as a research programme rather than a validated account.

## Citation

```bibtex
@unpublished{hamam2026variational,
  author = {Hamam, Habib},
  title  = {Variational Equilibrium as an Organizing Principle of Natural and
            Artificial Cognitive Systems: From Objective Maximization to
            Balanced Persistence},
  year   = {2026},
  note   = {Manuscript under review}
}
```

## Contact

Habib Hamam — Habib.Hamam@umoncton.ca

## License

All rights reserved pending publication.
