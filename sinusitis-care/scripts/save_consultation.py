#!/usr/bin/env python3
"""
Save a consultation record to the patient's history.

This script appends a new consultation to the patient's records,
organized by date.
"""

import json
from pathlib import Path
from datetime import datetime


def save_consultation(consultation_data):
    """
    Save a consultation record to the patient's history.

    Args:
        consultation_data (dict): Dictionary containing consultation information.
                                 Should include: symptoms, assessment, recommendations, etc.

    Returns:
        dict: Status of save operation with file path
    """
    # Define directories
    data_dir = Path.home() / ".sinusitis-care"
    consultations_dir = data_dir / "consultations"
    profile_file = data_dir / "patient_profile.json"

    # Create directories if they don't exist
    data_dir.mkdir(parents=True, exist_ok=True)
    consultations_dir.mkdir(parents=True, exist_ok=True)

    # Add timestamp if not present
    if "date" not in consultation_data:
        consultation_data["date"] = datetime.now().isoformat()

    # Generate filename based on date
    date_str = datetime.fromisoformat(consultation_data["date"]).strftime('%Y-%m-%d')

    # Check if a file for today already exists
    existing_files = list(consultations_dir.glob(f"{date_str}*.json"))

    if existing_files:
        # Append sequence number if multiple consultations on same day
        sequence = len(existing_files) + 1
        filename = f"{date_str}_{sequence}.json"
    else:
        filename = f"{date_str}.json"

    consultation_file = consultations_dir / filename

    # Save consultation
    with open(consultation_file, 'w', encoding='utf-8') as f:
        json.dump(consultation_data, f, indent=2, ensure_ascii=False)

    # Update patient profile's last_updated timestamp
    if profile_file.exists():
        with open(profile_file, 'r', encoding='utf-8') as f:
            profile = json.load(f)

        profile["last_updated"] = datetime.now().isoformat()

        with open(profile_file, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "consultation_file": str(consultation_file),
        "message": f"Consultation saved successfully to {filename}"
    }


def update_patient_profile(updates):
    """
    Update specific fields in the patient profile.

    Args:
        updates (dict): Dictionary of fields to update in the profile

    Returns:
        dict: Status of update operation
    """
    profile_file = Path.home() / ".sinusitis-care" / "patient_profile.json"

    if not profile_file.exists():
        return {
            "status": "error",
            "message": "Patient profile does not exist. Initialize patient first."
        }

    # Load existing profile
    with open(profile_file, 'r', encoding='utf-8') as f:
        profile = json.load(f)

    # Update fields (deep merge)
    def deep_update(base_dict, update_dict):
        for key, value in update_dict.items():
            if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
                deep_update(base_dict[key], value)
            else:
                base_dict[key] = value

    deep_update(profile, updates)

    # Update timestamp
    profile["last_updated"] = datetime.now().isoformat()

    # Save updated profile
    with open(profile_file, 'w', encoding='utf-8') as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "message": "Patient profile updated successfully"
    }


if __name__ == "__main__":
    # Example usage
    example_consultation = {
        "type": "symptom_assessment",
        "chief_complaint": "Nasal congestion and facial pressure for 5 days",
        "symptoms": {
            "nasal_congestion": "severe, bilateral",
            "facial_pain": "moderate, maxillary region",
            "nasal_discharge": "yellow, thick",
            "fever": "38.2°C",
            "duration": "5 days"
        },
        "assessment": {
            "likely_diagnosis": "Acute bacterial rhinosinusitis",
            "severity": "moderate",
            "danger_signals_identified": []
        },
        "recommendations": {
            "medical_consultation": "Recommended within 24-48 hours",
            "self_care": [
                "Increase nasal irrigation to 3-4 times daily",
                "Rest and hydration",
                "Monitor temperature"
            ],
            "red_flags_to_monitor": [
                "Fever >39°C",
                "Vision changes",
                "Severe headache"
            ]
        },
        "sources_consulted": ["UpToDate", "Mayo Clinic"],
        "notes": "Patient reports worsening symptoms over past 2 days. No improvement with OTC decongestants."
    }

    result = save_consultation(example_consultation)
    print(json.dumps(result, indent=2))

    # Example profile update
    profile_updates = {
        "current_medications": ["Saline nasal spray"],
        "medical_history": {
            "last_consultation_date": datetime.now().isoformat()
        }
    }

    update_result = update_patient_profile(profile_updates)
    print(json.dumps(update_result, indent=2))
