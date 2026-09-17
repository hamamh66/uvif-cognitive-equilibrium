# Review support

The notebook is an unchanged copy of the public repository snapshot cited in the paper. Its claims have not been silently rewritten. The notebook's existing outputs are author-supplied, not independently regenerated here.

`verify_companion.py` executes only the inspected model-definition cell. It verifies the state-aware fixed-unit-weight equivalence and constructs a finite hinge penalty matching the constrained policies on the declared finite grid. It does not run Drive setup, notebook file-writing cells, full parameter fits, or plotting cells. It requires NumPy.

The H3 coefficient is checked on all 180 declared environments and the 51x51 policy grid. This is a finite-set counterexample to a universal non-equivalence claim, not held-out model-selection evidence. It makes no claim about continuous policies.

`source_changes.patch` records text changes against the uploaded ZIP. `source_validation.json` records structural LaTeX checks. `horizon_spot_check.json` contains a limited check of the two stated horizon policies. None of these review files is a new empirical study.
