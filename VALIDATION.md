# Validation

- Main manuscript: successfully compiled with Tectonic 0.17.0; 41 pages in Elsevier review format.
- Separate abstract and title page: successfully compiled locally.
- 24 active bibliography entries; all cited keys resolve.
- No duplicate bibliography keys or labels; no missing inputs or undefined cross-references in source checks.
- No unbalanced LaTeX environments or braces in source checks.
- Figures, tables, equations, front matter, and bibliography rendered and inspected. The main PDF was checked across all pages at contact-sheet scale, with detailed checks of the figures and tables.
- The build may report underfull bibliography lines and an encoding warning in the bundled `lineno.sty`; no replacement glyph was found in extracted manuscript text. These are not unresolved citations or compilation errors.
- Focused companion-code checks: 180/180 matches for the state-aware fixed-unit-weight comparator; 180/180 matches for a finite hinge penalty with coefficient 23 on the stated grid.
- The full companion notebook has not been independently rerun. Comprehensive reference verification, scientific author approval, journal-specific requirements, and a live Overleaf build remain outstanding.

The source ZIP excludes temporary compiler files and original unused assets. A fresh `main.bbl` is included; Overleaf may regenerate it.
