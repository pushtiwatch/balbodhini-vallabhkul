# Redaction & Anonymization Guide

To comply with public interest disclosure frameworks and protect the privacy of innocent family members, all raw legal filings must undergo rigorous redaction before publication. We support two distinct, validated workflows for ensuring privacy; you may choose the path that best suits your specific document and security requirements.

---

## Workflow A: Visual Redaction (PDF24)
*Best for: Legal filings, stamped documents, and scanned exhibits.*

This workflow relies on the permanent, visual removal of sensitive data directly from the original document[cite: 1, 16].

1. **Tooling**: Use [PDF24 Tools](https://tools.pdf24.org/) for all visual scrubbing[cite: 1].
2. **Blacken PDF**: Use this feature to permanently overlay black boxes over all PII (names, phone numbers, addresses). This renders the data unreadable and irrecoverable in the final output[cite: 1].
3. **Remove PDF Data**: Always run this feature immediately after blackening to ensure hidden metadata, original layers, and annotations are stripped[cite: 1].
4. **Outcome**: The resulting PDF is sanitized and ready for direct upload to the portal[cite: 16].

---

## Workflow B: Programmatic Anonymization (Python)
*Best for: Long-form text complaints, narrative logs, and complex transcripts.*

This workflow generates a clean, anonymized transcript optimized for web-based reading. The portal follows a strict **single-pass regex substitution dictionary map** to scrub PII without disrupting technical allegations, chronological dates, or respondent identity logs[cite: 16].

### 1. Key Substitution Mappings
* **Phones**: All phone variations are mapped to `[REDACTED PHONE]`.
* **Emails**: Personal emails are mapped to `[REDACTED EMAIL]`.
* **Addresses**: Exact home and office addresses are mapped to `[REDACTED ADDRESS]`.
* **Names**: Primary complainants, family members, and child identities are normalized to neutral terms like `[THE COMPLAINANT]`, `[THE SPOUSE]`, and `[THE CHILD]`.
* **Pronouns**: Gendered pronouns are converted to gender-neutral forms (`he`/`she` to `they`, `his`/`her` to `their`) to eliminate all personal tracing vectors[cite: 16].

### 2. Technical Reference: `redaction_design_reference.py`
The script [redaction_design_reference.py](redaction_design_reference.py) serves as the design template for this automated process[cite: 16].

#### Core Processing Flow
1. **Extraction**: The script uses `fitz` (PyMuPDF) to read the target PDF page-by-page[cite: 16].
2. **Scrubbing**: A single-pass dictionary substitution executes in descending order of string length to prevent nested replacement collisions (e.g., replacing `spouse` with `[THE SPOUSE]` after replacing `wife` with `spouse`)[cite: 16].
3. **Output**: The anonymized plain text is saved to `assets/evidence/` as a text log[cite: 16].

#### Execution
```powershell
python redaction_design_reference.py