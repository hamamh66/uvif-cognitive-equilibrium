# Variational Equilibrium in Cognitive Systems

LaTeX source and companion code for the manuscript

> **Variational Equilibrium in Cognitive Systems: A Conceptual Framework for Adaptive
> Viability**
> Habib Hamam, Faculty of Engineering, Université de Moncton, Moncton, NB, Canada.

*Status: manuscript in preparation. Not peer reviewed.*

---

## Correction notice

An earlier revision of this repository reported two results that are **false**. Both are
refuted by code in this repository, and the refutations are reproduced in the companion
notebook rather than deleted.

**Claimed: the framework's implementation departs from scalar optimization.** It does not.
The implemented score is a unit-weighted sum of five state-dependent component functions,
and the policy is a grid argmax of that sum. A unit-weight scalarization over the same
components selects the identical policy in 180 of 180 declared environments. The earlier
comparison appeared to show otherwise only because its comparator evaluated every component
at a fixed reference state, so it could not respond to the environment at all. That
measured state responsiveness, not fixed versus adaptive weighting.

**Claimed: choices under an admissibility ceiling on unrecoverable loss cannot be
reproduced by a monotone utility penalty with a finite coefficient.** They can. The hinge
penalty `22 · max(0, loss − 0.15)` reproduces the constrained policy in 180 of 180
environments. The earlier search ranged only over power penalties `b · loss^g`, a family
that cannot express a threshold; widening `b` therefore drove the estimate to the search
ceiling, which was misread as evidence that no finite penalty exists.

Both refutations are exhaustive over the declared environment set and the 51×51 policy
grid. The manuscript no longer makes either claim.

## The framework in brief

The manuscript proposes an explicit regulatory decomposition for cognitive systems that
must remain functional over long horizons, organized around five competing considerations:

| Component | Role |
|---|---|
| Epistemic pull | acquisition of information that reduces uncertainty |
| Protective shield | preservation of states whose loss is unrecoverable |
| Computational drag | the resource cost of inference itself |
| Action efficiency | action within the window in which it remains useful |
| Sustainability | feasibility of the operating policy over long horizons |

It develops these as a vector-field template with an admissibility constraint, gives a
restricted one-dimensional analytical example, and sets out a research programme for
testing the decomposition. It is a conceptual contribution: it reports no experiments, and
its hypotheses are untested.

## Repository contents

| Path | Description |
|---|---|
| `main.tex`, `Sections/`, `Figures/` | Manuscript source |
| `Sections/References.bib` | Bibliography |
| `notebook/` | Companion policy-grid demonstrations, executed |
| `notebook/outputs/` | Figures, tables and run log produced by the notebook |

## Building

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

## Running the companion code

```bash
pip install numpy pandas matplotlib jupyter
jupyter notebook notebook/UVIF_Cognitive_Equilibrium_Demonstrations.ipynb
```

Runs in under a minute on a laptop; no GPU, no external data. It is committed with outputs
executed, so results can be read without running it.

## What the companion code shows

| Item | Status |
|---|---|
| Departure from scalar optimization | **Not shown.** The score is itself a unit-weighted scalarization; see the correction notice. |
| Irreversibility irreducible to a finite monotone penalty | **Refuted.** A hinge penalty reproduces constrained choice in 180/180 environments. |
| Horizon dependence of the selected policy | Shown, by stipulation. The horizon enters the sustainability term explicitly, so this does not separate a sustainability force from a long-horizon utility term. |
| Distinct single-component ablation signatures | Shown for this model. Five ablations differ in score and in viability, scored without assigning values to steps after viability failure. |
| Evidence about cognitive systems | **None.** The functional forms are stipulated; nothing here is measured. |

Two results in that analysis are worth stating plainly because they do not flatter the
model. Removing action efficiency *raises* the mean score while remaining fully viable,
which indicates the intact agent's greedy per-step choice is not optimal for the score it
is graded on. And the sensitivity sweep does not come back clean: the property that
ablating sustainability lowers viability fails when the drawdown constant is reduced by
40%.

The sweep varies six constants one at a time. It does not vary them jointly, and does not
cover grid resolution, environment ranges, the ablation set, or the penalty families.

## What a supporting study would require

A state-aware fixed-weight baseline tuned under a matched budget; independent safety and
resource outcomes rather than a single composite score; held-out conditions with retuning
after each ablation; sensitivity over grid resolution and interacting parameters; and
comparators from the free-energy, resource-rational and constrained-control literatures
implemented on equal terms.

## Citation

```bibtex
@misc{Hamam2026GitHub,
  author       = {Hamam, Habib},
  title        = {{UVIF} cognitive equilibrium: manuscript and companion simulation},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/hamamh66/uvif-cognitive-equilibrium},
  note         = {Companion policy-grid demonstrations}
}
```

## Contact

Habib Hamam — Habib.Hamam@umoncton.ca

## License

All rights reserved pending publication. Public accessibility of this repository does not
constitute an open-source license.
