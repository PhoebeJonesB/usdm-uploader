
import json
import logging
import sys
from datetime import datetime

# Setup logging to output to a physical file
log_file = f"usdm_section_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Redirect stdout and stderr to the logger
class StreamToLogger:
    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.strip():
            for line in message.strip().splitlines():
                self.logger.log(self.level, line.strip())

    def flush(self):
        pass

sys.stdout = StreamToLogger(logging.getLogger(), logging.INFO)
sys.stderr = StreamToLogger(logging.getLogger(), logging.ERROR)

# Define required sections for top-level 'version' and nested 'studyDesign'
REQUIRED_VERSION_SECTIONS = [
    "studyDesigns",
    "studyIdentifiers",
    "titles",
    "studyInterventions",
    "biomedicalConcepts"
]

REQUIRED_STUDYDESIGN_SECTIONS = [
    "activities",
    "encounters",
    "objectives",
    "epochs",
    "elements",
    "scheduleTimelines",
    "eligibilityCriteria",
    "studyType",
    "studyPhase",
    "arms",
    "population",
    "therapeuticAreas",
    "instanceType",
    "subTypes",
    "model",
    "intentTypes",
    "blindingSchema"
]

CORE_SECTIONS = [
    "activities",
    "encounters",
    "objectives",
    "epochs",
    "elements",
    "scheduleTimelines",
    "eligibilityCriteria",
    "arms",
    "studyType",
    "studyPhase"
]

def validate_usdm_sections(usdm_json):
    """
    Validates whether the USDM JSON file has all required sections for upload.
    First checks for required version-level sections, then checks nested studyDesign sections.
    Logs missing/null sections and their types.
    """
    logging.warning("=== START: USDM Section Validation ===")
    version = usdm_json.get("study", {}).get("versions", [{}])[0]
    missing_version_sections = []

    logging.info("--- Checking top-level version sections ---")
    for section in REQUIRED_VERSION_SECTIONS:
        value = version.get(section, None)
        if not value:
            missing_version_sections.append(section)
            logging.warning(f"Missing or null: {section} | Type: {type(value).__name__}")

    study_designs = version.get("studyDesigns")
    missing_design_sections = []

    if study_designs:
        study_design = study_designs[0] if isinstance(study_designs, list) else study_designs
        logging.info("--- Checking nested studyDesign sections ---")
        core_present = []
        for section in REQUIRED_STUDYDESIGN_SECTIONS:
            value = study_design.get(section, None)
            if not value:
                missing_design_sections.append(section)
                logging.warning(f"Missing or null: studyDesign.{section} | Type: {type(value).__name__}")
            elif section in CORE_SECTIONS:
                core_present.append(section)

        # Evaluate minimum core requirements
        missing_core = [s for s in CORE_SECTIONS if s not in core_present]
        if len(missing_design_sections) <= 3 and not missing_core:
            logging.info("Minimum USDM core section requirements met.")
            logging.info("These critical sections are present:")
            for s in core_present:
                logging.info(f" - studyDesign.{s}")
            logging.info("The importer script can now be used to test upload.")
        elif missing_core:
            logging.warning("One or more core sections are missing. Minimum requirements not met.")
    else:
        logging.warning("Cannot validate studyDesign sections because 'studyDesigns' is missing or empty.")

    logging.info("Section validation completed.")
    logging.warning("=== END: USDM Section Validation ===")
    return missing_version_sections, missing_design_sections

# Load the JSON file to perform validation
with open("Alexion_NCT04573309_Wilsons.json", "r", encoding="utf-8") as f:
    usdm_json = json.load(f)

# Run validation
validate_usdm_sections(usdm_json)
