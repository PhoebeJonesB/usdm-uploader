README: USDM Section Validation Module
======================================

Overview:
---------
This script checks for the presence of all required fields in a USDM (Unified Study Design Model) JSON file 
before attempting to upload data into a system. It ensures that all mandatory sections are present and logs 
any missing data for review.

Required Sections:
------------------
1. Top-level 'version' sections required:
   - studyDesigns
   - studyIdentifiers
   - titles
   - studyInterventions
   - biomedicalConcepts

2. Nested 'studyDesign' sections required:
   - activities
   - encounters
   - objectives
   - epochs
   - elements
   - scheduleTimelines
   - eligibilityCriteria
   - studyType
   - studyPhase
   - arms
   - population
   - therapeuticAreas
   - instanceType
   - subTypes
   - model
   - intentTypes
   - blindingSchema

Logging:
--------
- All checks and outcomes are written to a physical `.log` file.
- Logging includes:
  - START and END markers of validation
  - INFO logs on what is being checked
  - WARNINGS for each missing or null-required section

Usage:
------
Call `validate_usdm_sections(usdm_json)` where `usdm_json` is a loaded JSON dictionary object from your USDM file.
Example:
    with open("your_usdm_file.json") as f:
        usdm_data = json.load(f)
    validate_usdm_sections(usdm_data)
Run from terminal:

python usdm_validation_full_with_logging.py
Output:
-------
A log file is created in the working directory with details of the checks performed.
name of file will start with usdm_section_validation_[date]
