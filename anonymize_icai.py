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
