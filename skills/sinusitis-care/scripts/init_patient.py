#!/usr/bin/env python3
"""
Initialize a new patient profile for sinusitis care tracking.

This script creates the patient data directory structure and saves
baseline patient information.
"""

import json
import os
from pathlib import Path
from datetime import datetime


def init_patient(patient_data):
    """
    Initialize a new patient profile with baseline information.

    Args:
        patient_data (dict): Dictionary containing patient baseline information.
                            Should include fields like age, gender, medical_history, etc.

    Returns:
        dict: Status of initialization with paths created
    """
    # Define data directory
    data_dir = Path.home() / ".sinusitis-care"
    profile_file = data_dir / "patient_profile.json"
    consultations_dir = data_dir / "consultations"

    # Create directories if they don't exist
    data_dir.mkdir(parents=True, exist_ok=True)
    consultations_dir.mkdir(parents=True, exist_ok=True)

    # Add metadata
    patient_data["created_at"] = datetime.now().isoformat()
    patient_data["last_updated"] = datetime.now().isoformat()

    # Save patient profile
    with open(profile_file, 'w', encoding='utf-8') as f:
        json.dump(patient_data, f, indent=2, ensure_ascii=False)

    # Create initial consultation record
    initial_consultation = {
        "date": datetime.now().isoformat(),
        "type": "initial_assessment",
        "baseline_information_collected": True,
        "notes": "Patient profile initialized"
    }

    consultation_file = consultations_dir / f"{datetime.now().strftime('%Y-%m-%d')}_initial.json"
    with open(consultation_file, 'w', encoding='utf-8') as f:
        json.dump(initial_consultation, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "profile_path": str(profile_file),
        "consultations_dir": str(consultations_dir),
        "message": "Patient profile initialized successfully"
    }


def check_patient_exists():
    """
    Check if a patient profile already exists.

    Returns:
        bool: True if profile exists, False otherwise
    """
    profile_file = Path.home() / ".sinusitis-care" / "patient_profile.json"
    return profile_file.exists()


if __name__ == "__main__":
    # Example usage
    if check_patient_exists():
        print("Patient profile already exists!")
        print(f"Location: {Path.home() / '.sinusitis-care' / 'patient_profile.json'}")
    else:
        # Example patient data structure
        example_patient = {
            "demographics": {
                "age": 35,
                "gender": "male"
            },
            "medical_history": {
                "sinusitis_history": "Recurrent acute, 3-4 episodes per year",
                "previous_surgeries": [],
                "last_ct_scan": {
                    "date": "2024-03-15",
                    "findings": "Bilateral maxillary sinus mucosal thickening"
                }
            },
            "allergies": {
                "environmental": ["dust mites", "pollen"],
                "medication": []
            },
            "current_medications": [],
            "comorbidities": [],
            "social_history": {
                "smoking_status": "never",
                "occupation": "office worker",
                "environment": "urban, air conditioning"
            }
        }

        result = init_patient(example_patient)
        print(json.dumps(result, indent=2))
