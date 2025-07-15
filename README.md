# usdm-uploader
Automated uploader for USDM-formatted clinical trial studies


# Clinical Study USDM Uploader – Version 0.1

This script automates the upload of a clinical trial study structured in the USDM (Unified Study Data Model) format to a frontend system via API. It handles the creation of study objects such as objectives, endpoints, criteria, visits, and activities.

## ⚙️ Setup & Usage

### 1. Configure API Base URL
Update the `API_BASE_URL` variable in the script to point to your specific frontend instance:
```python
API_BASE_URL = "http://<your-ip>:<port>/api"
```

### 2. Study Creation
- Once a study is created, **note the study UID**.
- This UID will be used as input across **all functions** (objectives, criteria, visits, etc.). Make sure to **update this accordingly**.

### 3. JSON File Placement
Ensure the study JSON file (USDM) is located in the **same directory** as the script, or update the file path reference accordingly.

### 4. Study Number for Activity Upload
After the study is created in the frontend:
- Confirm the **Study Number** assigned.
- This number must be used during **activity posting**, in the final function.

## 🧪 Limitations

### 1. Objective, Endpoint, Criteria Preprocessing
- Square brackets (`[ ]`) in names are **automatically replaced** with round brackets (`( )`) to prevent issues when generating templates.
- This preprocessing is required to **avoid the frontend treating them as parameterized templates**.

### 2. SOA Hardcoding
- In the activity creation function, the Schedule of Activities (SOA) is **hardcoded** as:
  ```
  "Subject related information"
  ```
- You must change this to a **user-specific or study-specific SOA** name manually in the OSB **Edit** option.

### 3. Global Anchor Limitation
- The current version supports **only one global anchor** per visit.
- **Anchoring a visit to a group is not supported** in version 0.1.

## ✅ USDM Version Validation

Before using this uploader, validate your USDM JSON using the companion script:

- **Script:** `usdm_validation_full_with_logging.py`
- This checks that all **required sections** are present for both USDM v3 and v4.
- A **separate README** is available in that validation script’s directory for reference.

## ✅ Tested Datasets

This script has been successfully tested on **5 different USDM files** across various therapeutic areas and trial structures. Files can be found here https://github.com/cdisc-org/DDF-RA/tree/main/Documents/Examples

## 🔖 Version
**v0.1**

> Please report issues or feature requests by raising an issue in this GitHub repository.

