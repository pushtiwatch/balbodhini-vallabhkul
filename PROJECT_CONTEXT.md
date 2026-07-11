# PROJECT CONTEXT: Balbodhini Pathshala Inquiry Portal

This file contains the complete layout, configuration, and codebase of our legal public interest disclosure portal. You can feed this entire document into Gemini to ask questions with 100% context.

## Project Directory Tree
`
C:\Personal\Website\
├── app.py
├── timeline_data.json
├── Dockerfile
├── requirements.txt
├── anonymize_icai.py
├── README.md
├── LICENSE
├── templates/
│   └── index.html
└── assets/
    └── evidence/ (redacted PDFs, images, and text logs)
`

## File: app.py
`py
import os
import json
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/timeline')
def get_timeline():
    json_path = os.path.join(os.path.dirname(__file__), 'timeline_data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "timeline_data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding timeline_data.json"}), 500

@app.route('/assets/evidence/<path:filename>')
def serve_evidence(filename):
    evidence_dir = os.path.join(app.root_path, 'assets', 'evidence')
    
    # 1. Try exact match first
    if os.path.exists(os.path.join(evidence_dir, filename)):
        return send_from_directory(evidence_dir, filename)
        
    # 2. Try normalized case and separator (hyphen/underscore) matching
    normalized_target = filename.lower().replace('_', '-').replace(' ', '-')
    try:
        for existing_file in os.listdir(evidence_dir):
            normalized_existing = existing_file.lower().replace('_', '-').replace(' ', '-')
            if normalized_existing == normalized_target:
                return send_from_directory(evidence_dir, existing_file)
    except OSError:
        pass
        
    # Fallback to standard handler
    return send_from_directory(evidence_dir, filename)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

`

## File: timeline_data.json
`json
{
  "portal_meta": {
    "title": "Balbodhini Pathshala Hyderabad Inquiry",
    "subtitle": "Exposing Financial Coercion, Custodial Interference, and Third-Party Exploitation Claiming Links to Vallabhkul",
    "compliance_notice": "SECURED EVIDENCE VAULT - CERTIFIED PUBLIC INTEREST DISCLOSURE"
  },
  "timeline_events": [
    {
      "id": "doc_001",
      "date": "2025-04-05",
      "title": "Exhibit 1: The Threat Notice & Counter Legal Rebuttal",
      "description": "Comprehensive legal exposure analyzing the cease-and-desist mandates against third-party intruder Deepak Kumar Daga. Documents the tactical weaponization of marital discord, professional ethical violations under the ICAI Code of Ethics, and the exposure of massive unrecorded fund trails routed under proxy pretexts.",
      "claim": "Deepak Daga's Cease-and-Desist Demands: Asserts status as a neutral spiritual 'elder' and 'kanyadan performer' who acted solely in good faith, claiming that the circulation of unredacted recordings violates basic civil privacy rights.",
      "reality": "Documented Counter-Evidence: Factual tracking reveals a sustained pattern of extrajudicial bullying, extortion of over 15 Lakhs INR, non-transparent layering of funds into proxy relative bank accounts, and explicit verbal declarations boasting corrupt influence over police, taxation, and judicial authorities to force family isolation.",
      "evidence": {
        "type": "pdf",
        "file_path": "/assets/evidence/counter-legal-notice-deepak-daga-redacted.pdf",
        "label": "Read Document: Formal Rebuttal & Counter-Notice Response"
      }
    },
    {
      "id": "doc_002",
      "date": "2026-06-25",
      "title": "Exhibit 2: Formal Criminal Complaint Petition (BNS 2023)",
      "description": "The official omnibus criminal complaint submitted to the Kacheguda Police and senior enforcement directorates. Outlines the demand for immediate FIR registration for systemic financial extortion, cross-border parental child abduction, and organized spiritual grooming patterns linked to Balbodhini Paathshala network operators.",
      "claim": "Institutional Agent Stance: Third-party intermediaries argue that relative financial allocations and spiritual guidance are voluntary, traditional interactions completely separate from any coercive intent or legal non-compliance.",
      "reality": "Official BNS Criminal Filing: Verifiable case records establish deep financial fraud, explicit threats of 'total annihilation' delivered at the Westin Hyderabad, illegal physical detention of a parent inside a commercial CA office, and the intentional propagation of paranoia-inducing superstition ('vashikaran') to block court-directed reconciliation.",
      "evidence": {
        "type": "pdf",
        "file_path": "/assets/evidence/formal-police-complaint-deepak-daga.pdf",
        "label": "Read Document: Certified Criminal Complaint (Kacheguda Police)"
      }
    },
    {
      "id": "event_003",
      "date": "1998-10-09",
      "title": "Exhibit 3: Professional Profile & Credential Audit Timeline",
      "description": "Comprehensive asset auditing contrasting the 21+ year sole proprietorship claims of Deepak Daga & Associates (established Oct 1998, Membership No. 206253) against systemic regulatory compliance reports, corporate stamp records, and unauthorized foreign attest service disclosures compiled for oversight bodies including ICAI, CBI, RBI, and FIU.",
      "claim": "CA Deepak Daga Sole Proprietorship Claim: Asserts continuous, compliant 21+ year sole proprietorship of Deepak Daga & Associates, established October 1998 under Membership No. 206253.",
      "reality": "Oversight Audit Findings: Contrasted against systemic regulatory compliance reports, inconsistent corporate stamp records, and unauthorized foreign attest service disclosures compiled for ICAI, CBI, RBI, and FIU.",
      "evidence": {
        "type": "pdf",
        "file_path": "/assets/evidence/deepak-daga-resume-audit.pdf",
        "label": "Read Document: CA Deepak Daga Resume & Credential Audit"
      }
    },
    {
      "id": "event_004",
      "date": "2026-07-10",
      "title": "Exhibit 4: Official ICAI Disciplinary Complaint Submission",
      "description": "Scrubbed text ledger of the formal complaint submitted to the Director (Discipline) of the Institute of Chartered Accountants of India (ICAI) against the Respondent. Documents 9 comprehensive heads of misconduct detailing systemic credential misrepresentation and irregular financial routing.",
      "claim": "CA Deepak Daga's Compliance Claims: Asserts absolute professional compliance and adherence to the ICAI Code of Ethics, disputing any grounds for disciplinary action or professional misconduct.",
      "reality": "Official ICAI Disciplinary Case: Details 9 comprehensive heads of professional and other misconduct, highlighting systemic credential misrepresentation, fake experience certifications, and irregular financial routing.",
      "evidence": {
        "type": "pdf",
        "file_path": "/assets/evidence/icai-disciplinary-complaint-deepak-daga.pdf",
        "label": "Read Document: ICAI Complaint (Anonymized Submission)"
      }
    }
  ]
}
`

## File: Dockerfile
`Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT:-8080} app:app"]

`

## File: requirements.txt
`txt
Flask==3.0.3
gunicorn==22.0.0
PyMuPDF==1.24.5

`

## File: anonymize_icai.py
`py
### SCOPE: Anonymizes legal PDFs for public release.
### REFER TO: README.md for project overview.

import os
import re
import fitz  # PyMuPDF

source_pdf = r"C:\Personal\Website\assets\evidence\icai-complaint-raw.pdf"
output_txt = r"C:\Personal\Website\assets\evidence\icai-disciplinary-complaint-redacted.txt"

def redact_text(text):
    # Pass 1: Direct Personal Information & Specific Names (longest first to avoid partial replacements)
    replacements = [
        # Phones
        (r'\+1-404-988-5636', '[REDACTED PHONE]'),
        (r'404-988-5636', '[REDACTED PHONE]'),
        (r'4049885636', '[REDACTED PHONE]'),
        (r'\+1-404-927-5001', '[REDACTED PHONE]'),
        (r'404-927-5001', '[REDACTED PHONE]'),
        (r'4049275001', '[REDACTED PHONE]'),
        
        # Emails
        (r'rajeevkasat@gmail\.com', '[REDACTED EMAIL]'),
        
        # Addresses
        (r'1203 Lanier Springs Drive, Buford, GA 30518', '[REDACTED ADDRESS]'),
        (r'1203 Lanier Springs Drive', '[REDACTED ADDRESS]'),
        
        # Complainant Names
        (r'Rajeev C\. Kasat', '[THE COMPLAINANT]'),
        (r'Rajeev Kasat', '[THE COMPLAINANT]'),
        (r'\bRajeev\b', '[THE COMPLAINANT]'),
        
        # Child Names
        (r'Shriya R\. Kasat', '[THE CHILD]'),
        (r'Shriya R Kasat', '[THE CHILD]'),
        (r'\bShriya\b', '[THE CHILD]'),
        
        # Spouse & Family Names
        (r'Radhika R\. Kasat', '[REDACTED]'),
        (r'Radhika R Kasat', '[REDACTED]'),
        (r'\bRadhika\b', '[REDACTED]'),
        (r'\bBhattad\b', '[REDACTED]'),
        (r'\bPadma\b', '[REDACTED]'),
        (r'\bVitthaldasji\b', '[REDACTED]'),
        (r'\bVitthaldas\b', '[REDACTED]'),
        (r'\bKasat\b', '[REDACTED]')
    ]
    
    # Run replacements case-insensitively
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        
    # Pass 2: Relationship Neutralization (using word boundaries to avoid double replacement/collision)
    relation_map = {
        'husband': '[THE SPOUSE]',
        'wife': '[THE SPOUSE]',
        'spouse': '[THE SPOUSE]',
        'daughter': '[THE CHILD]',
        'son': '[THE CHILD]',
        'child': '[THE CHILD]',
        'father-in-law': '[REDACTED RELATIVE]',
        'mother-in-law': '[REDACTED RELATIVE]',
        'indian citizen': '[INDIVIDUAL]',
        'citizen': '[INDIVIDUAL]',
        'man': '[INDIVIDUAL]'
    }
    
    # Compile a single regex of all keys, sorted by length descending
    relation_pattern = re.compile(
        r'\b(' + '|'.join(re.escape(k) for k in sorted(relation_map.keys(), key=len, reverse=True)) + r')\b',
        re.IGNORECASE
    )
    
    text = relation_pattern.sub(lambda m: relation_map[m.group(0).lower()], text)

    # Pass 3: Pronoun Replacement with case-matching
    def replace_pronoun(match):
        word = match.group(0)
        lower = word.lower()
        if lower in ['he', 'she']:
            return 'They' if word[0].isupper() else 'they'
        elif lower in ['his', 'her']:
            return 'Their' if word[0].isupper() else 'their'
        elif lower == 'him':
            return 'Them' if word[0].isupper() else 'them'
        return word

    text = re.sub(r'\b(he|she|his|her|him)\b', replace_pronoun, text, flags=re.IGNORECASE)
    
    return text

def run_redaction():
    print(f"Opening source PDF: {source_pdf}")
    if not os.path.exists(source_pdf):
        print(f"Error: Source file does not exist: {source_pdf}")
        return
        
    doc = fitz.open(source_pdf)
    full_text = []
    
    for i, page in enumerate(doc):
        page_text = page.get_text()
        print(f"Processing Page {i+1} ({len(page_text)} chars)...")
        redacted_page = redact_text(page_text)
        full_text.append(redacted_page)
        
    final_output = "\n--- PAGE BREAK ---\n".join(full_text)
    
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(final_output)
        
    print(f"Redaction completed successfully! Output saved to: {output_txt}")

if __name__ == "__main__":
    run_redaction()

`

## File: templates/index.html
`html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Balbodhini Pathshala Hyderabad Inquiry</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            900: '#0c4a6e',
                            950: '#082f49',
                        },
                        danger: {
                            500: '#ef4444',
                            600: '#dc2626',
                            900: '#7f1d1d',
                            950: '#450a0a',
                        },
                        success: {
                            500: '#22c55e',
                            600: '#16a34a',
                            900: '#14532d',
                            950: '#052e16',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom scrollbar for premium feel */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0b1329;
        }
        ::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #0ea5e9;
        }
        /* Custom styles for glowing glassmorphism effects */
        .glass-panel {
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glow-cyan:hover {
            box-shadow: 0 0 15px rgba(14, 165, 233, 0.25);
            border-color: rgba(14, 165, 233, 0.4);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen font-sans selection:bg-brand-500 selection:text-white flex flex-col">

    <!-- Top Navigation Header -->
    <header class="border-b border-slate-900 bg-slate-900/50 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <!-- Portal Logo Symbol -->
                <div class="h-9 w-9 rounded-lg bg-gradient-to-tr from-brand-600 to-cyan-500 flex items-center justify-center shadow-lg shadow-brand-500/20">
                    <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                </div>
                <div>
                    <h1 id="portal-title" class="font-bold text-lg tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">Loading Portal...</h1>
                    <p id="portal-subtitle" class="text-xs text-slate-500 font-medium">Please wait...</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <span id="compliance-notice" class="hidden md:inline-block px-3 py-1 text-[10px] tracking-wider uppercase font-semibold text-cyan-400 bg-cyan-950/40 border border-cyan-800/50 rounded-full animate-pulse">
                    Loading Status...
                </span>
                <span class="h-2 w-2 rounded-full bg-emerald-500 shadow-lg shadow-emerald-500/50"></span>
                <span class="text-xs text-slate-400 font-mono">LIVE VAULT</span>
            </div>
        </div>
    </header>

    <!-- Main Workspace Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex flex-col lg:flex-row gap-8 overflow-hidden">
        
        <!-- Left Side: Chronological Timeline Panel -->
        <section class="w-full lg:w-5/12 flex flex-col h-[calc(100vh-10rem)] lg:sticky lg:top-24">
            <div class="mb-4">
                <h2 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Chronological Event Index</h2>
                <p class="text-sm text-slate-500">Select any record key below to examine unredacted evidence logs.</p>
            </div>
            
            <!-- Scrollable Timeline Stream -->
            <div class="flex-1 overflow-y-auto pr-2 relative mt-4">
                <!-- Timeline vertical bar -->
                <div class="absolute left-[17px] top-2 bottom-6 w-[2px] bg-slate-800 pointer-events-none"></div>
                
                <!-- Dynamic Nodes Container -->
                <div id="timeline-container" class="space-y-6">
                    <!-- Dynamic nodes loaded here -->
                    <div class="animate-pulse space-y-4">
                        <div class="h-4 bg-slate-800 rounded w-1/3"></div>
                        <div class="h-20 bg-slate-900 rounded-lg"></div>
                        <div class="h-20 bg-slate-900 rounded-lg"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Right Side: Evidence Box / Modal Panel -->
        <section class="w-full lg:w-7/12 flex flex-col h-[calc(100vh-10rem)]">
            <div class="flex-1 flex flex-col glass-panel rounded-xl border border-slate-900 overflow-hidden shadow-2xl relative">
                
                <!-- Interactive Detail View (Active Node) -->
                <div id="viewer-placeholder" class="flex-1 flex flex-col items-center justify-center p-8 text-center select-none">
                    <svg class="h-16 w-16 text-slate-700 mb-4 stroke-1 animate-bounce" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7v8a2 2 0 002 2h6M8 7V5a2 2 0 012-2h4.586a1 1 0 01.707.293l4.414 4.414a1 1 0 01.293.707V15a2 2 0 01-2 2h-2M8 7H6a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2v-2" />
                    </svg>
                    <h3 class="text-lg font-medium text-slate-300">No Record Selected</h3>
                    <p class="text-sm text-slate-500 max-w-sm mt-2">
                        Select a factual node from the chronological timeline on the left to inspect the linked unredacted files, comparison logs, and compliance evidence.
                    </p>
                </div>

                <!-- Main Content Frame (Hidden initially) -->
                <div id="viewer-content" class="hidden flex-1 flex flex-col overflow-y-auto">
                    
                    <!-- Metadata Header -->
                    <div class="p-6 border-b border-slate-900 bg-slate-900/30">
                        <div class="flex items-center justify-between mb-2">
                            <span id="active-event-date" class="text-xs font-mono text-brand-500 font-semibold uppercase tracking-wider">DATE</span>
                            <span class="px-2 py-0.5 text-[10px] bg-slate-800 border border-slate-700 text-slate-400 rounded-md font-mono" id="active-event-id">ID</span>
                        </div>
                        <h3 id="active-event-title" class="text-xl font-bold text-white tracking-tight">Select an Event</h3>
                        <p id="active-event-description" class="text-sm text-slate-400 mt-2 leading-relaxed">Description goes here...</p>
                    </div>

                    <!-- Interactive Evidence Vault Container -->
                    <div class="p-6 flex-1 flex flex-col gap-6">
                        
                        <!-- Evidence Trigger / Title Bar -->
                        <div>
                            <div class="flex items-center justify-between mb-3">
                                <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400 flex items-center space-x-2">
                                    <svg class="h-4 w-4 text-brand-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                    </svg>
                                    <span>Cryptographic Evidence Vault</span>
                                </h4>
                                <a id="evidence-external-link" href="#" target="_blank" class="text-xs text-brand-500 hover:text-brand-600 font-medium flex items-center space-x-1 transition-colors">
                                    <span>Download Original File</span>
                                    <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                                    </svg>
                                </a>
                            </div>

                            <!-- PDF Multi-page View Container -->
                            <div id="pdf-viewer-container" class="hidden">
                                <div class="bg-slate-900 rounded-lg overflow-hidden border border-slate-800 shadow-inner">
                                    <iframe id="pdf-iframe" src="" class="w-full h-[400px]" frameborder="0"></iframe>
                                </div>
                                <div class="mt-2 text-center text-xs text-slate-500 flex items-center justify-center space-x-1">
                                    <svg class="h-3 w-3 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                    <span>To view natively, configure your browser PDF viewer, or click the link above.</span>
                                </div>
                            </div>

                            <!-- Image Lightbox Container -->
                            <div id="image-viewer-container" class="hidden">
                                <div class="relative group cursor-zoom-in bg-slate-900 rounded-lg border border-slate-800 overflow-hidden flex items-center justify-center p-4">
                                    <img id="lightbox-image" src="" alt="Evidence Image scan" class="max-h-[350px] object-contain rounded transition-transform duration-300 group-hover:scale-[1.02]">
                                    <div class="absolute inset-0 bg-slate-950/60 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity duration-200">
                                        <button onclick="openLightboxFullscreen()" class="px-4 py-2 bg-brand-600 hover:bg-brand-500 text-white text-xs font-semibold rounded-lg shadow-md transition-colors flex items-center space-x-1">
                                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7" />
                                            </svg>
                                            <span>Zoom Scan File</span>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Plain Text View Container -->
                            <div id="text-viewer-container" class="hidden">
                                <pre id="text-viewer-pre" style="white-space: pre-wrap; background: #1a1f2c; color: #fff; padding: 20px; border-radius: 8px; height: 600px; overflow-y: auto;"></pre>
                            </div>
                        </div>

                        <!-- Side-by-Side: Claim vs. Reality -->
                        <div>
                            <h4 class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3 flex items-center space-x-2">
                                <svg class="h-4 w-4 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <span>Verification Matrix (Claim vs. Reality)</span>
                            </h4>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <!-- Claim card -->
                                <div class="p-4 rounded-lg bg-danger-950/20 border border-danger-900/40 relative overflow-hidden">
                                    <div class="absolute top-0 right-0 px-2 py-0.5 bg-danger-900/60 text-[9px] font-mono tracking-wider uppercase font-semibold text-danger-500 rounded-bl border-l border-b border-danger-900/40">
                                        Public Claim
                                    </div>
                                    <div class="text-xs text-danger-500 uppercase tracking-widest font-mono mb-2">Claim statement</div>
                                    <p id="active-event-claim" class="text-sm text-slate-300 leading-relaxed font-light italic">No claim loaded</p>
                                </div>
                                <!-- Reality card -->
                                <div class="p-4 rounded-lg bg-success-950/20 border border-success-900/40 relative overflow-hidden">
                                    <div class="absolute top-0 right-0 px-2 py-0.5 bg-success-900/60 text-[9px] font-mono tracking-wider uppercase font-semibold text-success-500 rounded-bl border-l border-b border-success-900/40">
                                        Verified Reality
                                    </div>
                                    <div class="text-xs text-emerald-500 uppercase tracking-widest font-mono mb-2">Audit reality</div>
                                    <p id="active-event-reality" class="text-sm text-slate-300 leading-relaxed font-normal">No reality loaded</p>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- Global Fullscreen Image Lightbox Modal -->
    <div id="global-lightbox" class="fixed inset-0 z-[100] hidden bg-slate-950/95 flex items-center justify-center p-4">
        <button onclick="closeLightboxFullscreen()" class="absolute top-6 right-6 text-slate-400 hover:text-white p-2 rounded-full hover:bg-slate-900/60 transition-colors">
            <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
        </button>
        <div class="max-w-5xl max-h-[85vh] w-full h-full flex flex-col items-center justify-center">
            <img id="global-lightbox-img" src="" alt="Unredacted scan fullscreen" class="max-w-full max-h-full object-contain rounded-lg shadow-2xl">
            <p id="global-lightbox-caption" class="text-slate-400 text-xs font-mono mt-4 tracking-wide text-center">Unredacted File</p>
        </div>
    </div>

    <!-- Scripting and Decoupled Data loading -->
    <script>
        let cachedData = null;

        // Fetch data from Flask backend
        async function initPortal() {
            try {
                const response = await fetch('/api/timeline');
                if (!response.ok) {
                    throw new Error('Failed to load timeline data');
                }
                const data = await response.json();
                cachedData = data;
                
                // Load metadata dynamically
                document.getElementById('portal-title').textContent = data.portal_meta.title;
                document.getElementById('portal-subtitle').textContent = data.portal_meta.subtitle;
                document.getElementById('compliance-notice').textContent = data.portal_meta.compliance_notice;
                document.getElementById('compliance-notice').classList.remove('hidden');
                
                // Build Timeline nodes
                buildTimeline(data.timeline_events);

            } catch (err) {
                console.error("Initialization error:", err);
                document.getElementById('portal-title').textContent = "Connection Error";
                document.getElementById('portal-subtitle').textContent = "Unable to connect to the disclosure server.";
            }
        }

        function buildTimeline(events) {
            const container = document.getElementById('timeline-container');
            container.innerHTML = ''; // Clear skeleton structure

            // Sort events chronologically by date
            const sortedEvents = [...events].sort((a, b) => new Date(a.date) - new Date(b.date));

            sortedEvents.forEach((event, index) => {
                const node = document.createElement('div');
                node.className = 'relative pl-10 group cursor-pointer';
                node.setAttribute('data-id', event.id);
                node.onclick = () => selectEvent(event.id);

                node.innerHTML = `
                    <!-- Timeline Node Pin -->
                    <div class="absolute left-2.5 top-1.5 h-4 w-4 rounded-full border-2 border-slate-700 bg-slate-950 flex items-center justify-center group-hover:border-brand-500 transition-colors duration-200 z-10 node-pin">
                        <div class="h-1.5 w-1.5 rounded-full bg-transparent node-dot"></div>
                    </div>
                    <!-- Timeline Card content -->
                    <div class="p-4 rounded-lg bg-slate-900/40 border border-slate-900 group-hover:bg-slate-900/70 hover:border-slate-800 transition-all duration-300 glow-cyan">
                        <span class="text-[10px] font-mono text-slate-500 group-hover:text-brand-500 transition-colors">${event.date}</span>
                        <h4 class="text-sm font-bold text-slate-200 mt-1">${event.title}</h4>
                        <p class="text-xs text-slate-400 mt-2 line-clamp-2">${event.description}</p>
                        
                        <!-- Trigger Action link -->
                        <div class="mt-3 flex items-center justify-between">
                            <span class="text-[10px] uppercase font-bold text-brand-500 flex items-center space-x-1">
                                <span>Inspect Evidence Vault</span>
                                <svg class="h-3 w-3 transform group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                </svg>
                            </span>
                            <span class="text-[9px] font-mono text-slate-600">${event.evidence.label}</span>
                        </div>
                    </div>
                `;
                container.appendChild(node);
            });
        }

        // Active Event Select logic
        function selectEvent(eventId) {
            if (!cachedData) return;
            const event = cachedData.timeline_events.find(e => e.id === eventId);
            if (!event) return;

            // Highlight selected node, reset others
            document.querySelectorAll('.node-pin').forEach(pin => {
                pin.classList.remove('border-brand-500', 'ring-2', 'ring-brand-500/20');
                pin.classList.add('border-slate-700');
            });
            document.querySelectorAll('.node-dot').forEach(dot => {
                dot.classList.remove('bg-brand-500');
            });

            const selectedNode = document.querySelector(`[data-id="${eventId}"]`);
            if (selectedNode) {
                const pin = selectedNode.querySelector('.node-pin');
                pin.classList.remove('border-slate-700');
                pin.classList.add('border-brand-500', 'ring-2', 'ring-brand-500/20');
                
                const dot = selectedNode.querySelector('.node-dot');
                dot.classList.add('bg-brand-500');
            }

            // Hide placeholder and reveal viewer content
            document.getElementById('viewer-placeholder').classList.add('hidden');
            const viewerContent = document.getElementById('viewer-content');
            viewerContent.classList.remove('hidden');

            // Populate Metadata
            document.getElementById('active-event-date').textContent = event.date;
            document.getElementById('active-event-id').textContent = event.id;
            document.getElementById('active-event-title').textContent = event.title;
            document.getElementById('active-event-description').textContent = event.description;

            // Populate Claims comparison
            document.getElementById('active-event-claim').textContent = event.claim;
            document.getElementById('active-event-reality').textContent = event.reality;

            // Populate Evidence Vault Components
            const pdfContainer = document.getElementById('pdf-viewer-container');
            const imgContainer = document.getElementById('image-viewer-container');
            const textContainer = document.getElementById('text-viewer-container');
            const extLink = document.getElementById('evidence-external-link');

            extLink.href = event.evidence.file_path;

            if (event.evidence.type === 'pdf') {
                pdfContainer.classList.remove('hidden');
                imgContainer.classList.add('hidden');
                textContainer.classList.add('hidden');
                
                // Embed pdf in iframe
                const iframe = document.getElementById('pdf-iframe');
                iframe.src = event.evidence.file_path;
            } else if (event.evidence.type === 'image') {
                imgContainer.classList.remove('hidden');
                pdfContainer.classList.add('hidden');
                textContainer.classList.add('hidden');
                
                // Set Image source
                const img = document.getElementById('lightbox-image');
                img.src = event.evidence.file_path;
            } else if (event.evidence.file_path.endsWith('.txt')) {
                textContainer.classList.remove('hidden');
                pdfContainer.classList.add('hidden');
                imgContainer.classList.add('hidden');
                
                // Load text via fetch
                const pre = document.getElementById('text-viewer-pre');
                pre.textContent = "Loading anonymized complaint transcript...";
                fetch(event.evidence.file_path)
                    .then(response => response.text())
                    .then(txt => {
                        pre.textContent = txt;
                    })
                    .catch(err => {
                        pre.textContent = "Error loading transcript: " + err;
                    });
            } else {
                pdfContainer.classList.add('hidden');
                imgContainer.classList.add('hidden');
                textContainer.classList.add('hidden');
            }
        }

        // Fullscreen Lightbox logic
        function openLightboxFullscreen() {
            const img = document.getElementById('lightbox-image');
            const globalImg = document.getElementById('global-lightbox-img');
            const globalCaption = document.getElementById('global-lightbox-caption');
            const modal = document.getElementById('global-lightbox');

            globalImg.src = img.src;
            const activeId = document.getElementById('active-event-id').textContent;
            globalCaption.textContent = `Vault Scan File (${activeId}) - Certified Evidence Scan`;
            
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden'; // Lock scrolling
        }

        function closeLightboxFullscreen() {
            const modal = document.getElementById('global-lightbox');
            modal.classList.add('hidden');
            document.body.style.overflow = ''; // Unlock scrolling
        }

        // Initialize portal on DOM Ready
        document.addEventListener('DOMContentLoaded', initPortal);
    </script>
</body>
</html>

`

## File: README.md
`md
# Balbodhini Pathshala Inquiry Portal

## Overview
A public interest disclosure portal for verified legal evidence.

## Master Documentation Reference
| Document | Scope |
| :--- | :--- |
| [README.md](README.md) | Project Overview & Navigation (Start Here) |
| [timeline_data.json](timeline_data.json) | The Database (Case Events) |
| [anonymize_icai.py](anonymize_icai.py) | Redaction Tooling & Privacy Logic |
| [app.py](app.py) | Backend Server Logic |
| [Dockerfile](Dockerfile) | Deployment Recipe |
| [LICENSE](LICENSE) | Legal Status (CC0 Public Domain) |

For any questions, start at [README.md](README.md).

`

## File: LICENSE
`LICENSE
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

`

