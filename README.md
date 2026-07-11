# Balbodhini Pathshala Inquiry Portal

A transparent, public interest disclosure vault for legal evidence.

## Repository Manifest
This table provides a high-level overview of the project structure and the objective of each file.

| File/Folder | Type | Objective |
| :--- | :--- | :--- |
| pp.py | Python (Backend) | The core Flask server; routes the website and manages evidence file access. |
| 
edaction_design_reference.py | Python (Utility) | The 'safety engine' that automates text anonymization to protect PII. |
| 	imeline_data.json | JSON (Data) | The 'Single Source of Truth' containing your case narrative and event data. |
| Dockerfile | Configuration | Defines the environment for deploying your portal to the cloud. |
| 
equirements.txt | Configuration | Lists the software dependencies required for the project. |
| ssets/evidence/ | Folder | The secure vault storing your redacted PDFs, images, and text transcripts. |
| docs/ | Folder | Contains architectural specs, redaction workflows, and development roadmaps. |
| 	emplates/ | Folder | Contains index.html, the frontend layout for the public viewer. |

## Quick Start
1. Fork this repo.
2. Place redacted evidence in /assets/evidence/.
3. Update 	imeline_data.json to reflect your case events.
4. Deploy via Docker.

## License
Dedicated to the public domain under [CC0 1.0 Universal](LICENSE).
