import os
import shutil

dest_dir = r"C:\Personal\Website\assets\evidence"
os.makedirs(dest_dir, exist_ok=True)

# Candidate sources on the system (excluding the destination directory itself)
candidates = {
    "counter-legal-notice-redacted.pdf": [
        r"C:\Users\rajee\Downloads\Redacted Reply to Deepak Daga and Counter Legal Notice.pdf",
        r"C:\Users\rajee\Downloads\Reply to Legal Notice and Counter-Legal Notice from Rajeev Kasat to Mr. Deepak Daga.pdf",
    ],
    "police-complaint-redacted.pdf": [
        r"C:\Users\rajee\Downloads\Rajeev_Kasat_Police_Complaint_vs_Deepak_Daga_Child_Custody_Dowry_Intimidation_2026-02-03.pdf.pdf",
        r"C:\Users\rajee\OneDrive\Documents\Police Complaint against Mr Deepakji Daga PDF.pdf",
        r"C:\Users\rajee\Downloads\Rajeev_Kasat_Police_Complaint_vs_Deepak_Daga_Child_Custody_Dowry_Intimidation_2026-02-03.pdf (1).pdf"
    ]
}

def search_exact_on_system(filename):
    # Scan user home directory for exact filename (ignoring destination folder)
    for root, dirs, files in os.walk(r"C:\Users\rajee"):
        if r"C:\Personal\Website" in root:
            continue
        if filename in files:
            return os.path.join(root, filename)
    return None

def copy_evidence():
    print("=== Copying Redacted Legal Evidence PDFs ===")
    
    for dest_name, src_list in candidates.items():
        dest_path = os.path.join(dest_dir, dest_name)
        copied = False
        
        # 1. Look for exact filename on the system first
        exact_match = search_exact_on_system(dest_name)
        if exact_match:
            print(f"[+] Found exact system match for {dest_name} at: {exact_match}")
            shutil.copy2(exact_match, dest_path)
            print(f"[+] Successfully copied to {dest_path}")
            copied = True
            
        # 2. Try candidate files if exact match wasn't found
        if not copied:
            for candidate in src_list:
                if os.path.exists(candidate):
                    print(f"[+] Found candidate file for {dest_name} at: {candidate}")
                    shutil.copy2(candidate, dest_path)
                    print(f"[+] Successfully copied to {dest_path}")
                    copied = True
                    break
                    
        if not copied:
            print(f"[-] Warning: No source file found for {dest_name} on the system.")

if __name__ == "__main__":
    copy_evidence()
