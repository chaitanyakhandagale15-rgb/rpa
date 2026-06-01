

# Secure Document Redaction Bot (UiPath RPA POC)

## Overview
This repository contains a **UiPath-based proof-of-concept** for automating the **detection and redaction of sensitive information (PII/PHI)** in PDF documents.  
It features **human-in-the-loop validation**, **configurable detection rules**, and **full audit logging** to support compliance workflows such as FOIA/Privacy Act responses and HIPAA de-identification.

**Key highlights:**
- Fully local execution — no sensitive data leaves the machine.
- Uses **synthetic and publicly available documents only** for demonstration purposes.
- Implements deterministic **regex- and dictionary-based** detection for auditability, with a clear seam to integrate AI/ML extractors later.
- Includes **confidence scoring** to trigger human review when needed.
- Generates **redacted PDFs**, structured Excel summaries, and JSONL audit logs.

---

## Features
- **Automated Intake** — Reads PDF files from a designated folder.
- **Classification** — Assigns document type (e.g., Claim, General) based on keyword rules.
- **PHI/PII Detection** — Matches HIPAA identifiers via regex patterns (SSN, DOB, phone, email, address, MRN, etc.).
- **Confidence Scoring** — Determines whether a document requires human validation.
- **Human-in-the-Loop (HITL)** — UiPath Form interface for adding or correcting redactions before processing.
- **Redaction Engine** — Removes/masks identified text in the PDF output.
- **Audit Trail** — Excel registry and JSONL log for every processed document.
- **Synthetic Dataset** — Includes public/synthetic PDFs for reproducibility.

---

## Architecture

![Secure Document Redaction Bot – High-Level Architecture](docs/architecture_diagram.svg)

This diagram shows the end-to-end workflow of the bot, from PDF intake to redaction, output, and optional notification.  
The process supports both **automatic processing** for high-confidence detections and a **human-in-the-loop (HITL)** review for low-confidence cases.  
Configuration files (`ref/*`) and logging/metrics are integrated into the process for auditability and maintainability.

---

## Repository Structure

```
.
├── input/ # Folder for incoming PDF files to process
├── output/ # Folder for redacted PDFs & Excel registry
├── logs/ # Folder for JSONL audit logs
├── ref/ # Reference data (regex patterns, keyword lists)
├── samples/ # Synthetic/public PDFs for testing
├── docs/ # Documentation assets (diagrams, images)
│ └── architecture_diagram.svg # High-level architecture diagram
├── DetectPHI.xaml # Workflow for identifying PHI/PII in text
├── Main.xaml # Main process workflow
├── project.json # UiPath project settings
└── README.md # This file
```

---

## Requirements
- **Windows 10/11**
- **UiPath Studio** (Community or Enterprise)
- **Git** (if cloning from this repo)
- **Packages installed in UiPath Studio:**
  - `UiPath.System.Activities`
  - `UiPath.Excel.Activities`
  - `UiPath.Mail.Activities`
  - `UiPath.PDF.Activities`
  - `UiPath.FormActivityLibrary`

---

## Installation & Setup

### 1. Clone the repository
git clone https://github.com/binodthapachhetry/uipath-doc-redact-rpa-bot.git


Or download the ZIP from GitHub and extract it.

### 2. Open in UiPath Studio

* Launch **UiPath Studio**.
* Go to **Home → Open Local Project** and select the `project.json` file in this repo.

### 3. Install dependencies

* In Studio, open the **Manage Packages** panel.
* Install the packages listed in the **Requirements** section.

### 4. Prepare the working folders

* Place any **PDFs you want to process** (synthetic only) in the `input/` folder.
* Ensure `output/` and `logs/` folders exist — the bot will write results here.

### 5. Configure detection rules

* Open `ref/hipaa_identifiers.csv` to adjust regex patterns or add/remove identifiers.
* Open `ref/keywords_claims.json` to configure classification keywords.

---

## Usage

### Run the Bot

1. Open `Main.xaml` in UiPath Studio.
2. Click **Run** (green ▶ button).
3. The bot will:

   * Read PDFs from `input/`.
   * Classify document type.
   * Detect PII/PHI using regex patterns.
   * Calculate a confidence score.
   * If confidence `< threshold`, open a **review form** for manual validation.
   * Apply redactions and save results to `output/`.
   * Log details in Excel and JSONL format.

### Outputs

* **Redacted PDFs** — `output/<original_name>_REDACTED.pdf`
* **Registry Excel** — `output/redaction_registry.xlsx` with metadata.
* **Audit Log** — `logs/audit.jsonl` with masked values and reviewer actions.

---

## Example Workflow Diagram

```
.
[ Intake PDFs ] 
       ↓
[ Classify Doc Type ]
       ↓
[ Detect PII/PHI ]
       ↓
[ Confidence ≥ Threshold? ]
       ↙              ↘
[ Yes ]           [ No → HITL Form ]
       ↓
[ Apply Redactions ]
       ↓
[ Save Outputs + Audit ]
```

---

## Notes for Demonstration

* The included PDFs are **synthetic/public** — no real PHI/PII is stored in this repository.
* You can replace them with your own **synthetic test cases** to demonstrate edge cases (e.g., near-miss SSNs, invalid DOBs).
* In a production setting, the bot would:

  * Run unattended via **UiPath Orchestrator**.
  * Store credentials and config in **Orchestrator Assets**.
  * Use **Action Center** instead of local forms for HITL.
  * Integrate with secure storage and audit systems.

---

## Future Enhancements

* **Document Understanding (DU)** for improved name/address extraction.
* **Action Center Integration** for web-based HITL.
* **Queue-based scaling** in Orchestrator.
* **Dashboard Metrics** for STP%, precision/recall per field.
* **RMF/ATO controls mapping** for government deployment.

---

## License

This project is provided for demonstration purposes only.
It contains **no real PHI/PII** and should not be used with sensitive data without additional security and compliance review.
