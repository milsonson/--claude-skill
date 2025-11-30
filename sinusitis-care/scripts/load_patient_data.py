#!/usr/bin/env python3
"""
Load patient profile and consultation history.

This script retrieves patient data from the sinusitis care data directory.
"""

import json
from pathlib import Path
from datetime import datetime


def load_patient_profile():
    """
    Load the patient's baseline profile information.

    Returns:
        dict: Patient profile data, or None if not found
    """
    profile_file = Path.home() / ".sinusitis-care" / "patient_profile.json"

    if not profile_file.exists():
        return None

    with open(profile_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_consultation_history(limit=None, days_back=None):
    """
    Load consultation history records.

    Args:
        limit (int, optional): Maximum number of recent consultations to load
        days_back (int, optional): Only load consultations from the last N days

    Returns:
        list: List of consultation records, sorted by date (most recent first)
    """
    consultations_dir = Path.home() / ".sinusitis-care" / "consultations"

    if not consultations_dir.exists():
        return []

    consultations = []

    # Load all consultation files
    for file_path in consultations_dir.glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                consultation = json.load(f)
                consultation['file_name'] = file_path.name
                consultations.append(consultation)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse {file_path}")
            continue

    # Sort by date (most recent first)
    consultations.sort(key=lambda x: x.get('date', ''), reverse=True)

    # Apply time filter if specified
    if days_back is not None:
        cutoff_date = datetime.now().timestamp() - (days_back * 24 * 60 * 60)
        consultations = [
            c for c in consultations
            if datetime.fromisoformat(c['date']).timestamp() > cutoff_date
        ]

    # Apply limit if specified
    if limit is not None:
        consultations = consultations[:limit]

    return consultations


def load_all_patient_data(recent_consultations=5):
    """
    Load complete patient data including profile and recent consultations.

    Args:
        recent_consultations (int): Number of recent consultations to include

    Returns:
        dict: Complete patient data with profile and consultation history
    """
    profile = load_patient_profile()
    consultations = load_consultation_history(limit=recent_consultations)

    return {
        "profile": profile,
        "recent_consultations": consultations,
        "total_consultations": len(list((Path.home() / ".sinusitis-care" / "consultations").glob("*.json"))) if (Path.home() / ".sinusitis-care" / "consultations").exists() else 0,
        "patient_exists": profile is not None
    }


def get_patient_summary():
    """
    Generate a concise summary of patient information for quick reference.

    Returns:
        str: Formatted patient summary
    """
    data = load_all_patient_data(recent_consultations=3)

    if not data["patient_exists"]:
        return "No patient profile found. This appears to be a new patient."

    profile = data["profile"]

    summary_lines = ["=== Patient Summary ===\n"]

    # Demographics
    if "demographics" in profile:
        demo = profile["demographics"]
        summary_lines.append(f"Age: {demo.get('age', 'Unknown')}, Gender: {demo.get('gender', 'Unknown')}")

    # Medical history highlights
    if "medical_history" in profile:
        history = profile["medical_history"]
        if "sinusitis_history" in history:
            summary_lines.append(f"Sinusitis History: {history['sinusitis_history']}")

    # Allergies
    if "allergies" in profile:
        allergies = profile["allergies"]
        if allergies.get("medication"):
            summary_lines.append(f"Drug Allergies: {', '.join(allergies['medication'])}")
        if allergies.get("environmental"):
            summary_lines.append(f"Environmental Allergies: {', '.join(allergies['environmental'])}")

    # Recent consultations
    summary_lines.append(f"\nTotal Consultations: {data['total_consultations']}")

    if data["recent_consultations"]:
        summary_lines.append("\nRecent Consultations:")
        for consult in data["recent_consultations"][:3]:
            date = datetime.fromisoformat(consult['date']).strftime('%Y-%m-%d')
            consult_type = consult.get('type', 'general')
            summary_lines.append(f"  - {date}: {consult_type}")

    return "\n".join(summary_lines)


if __name__ == "__main__":
    # Example usage
    print(get_patient_summary())
    print("\n" + "="*50 + "\n")

    # Load full data
    data = load_all_patient_data()
    print(json.dumps(data, indent=2, default=str))
