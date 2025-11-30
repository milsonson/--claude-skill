# Patient Profile Information Fields

This document provides suggested baseline information to collect from sinusitis patients. Use this as a **flexible guide**, not a rigid checklist. Adapt the conversation naturally based on the patient's needs and situation.

## Essential Baseline Information

### Demographic Information
- **Age** - Important for risk stratification and treatment selection
- **Gender** - Some conditions (e.g., nasal polyps) have gender differences

### Current Symptoms
- **Symptom duration** - Critical for classifying as:
  - Acute: <4 weeks
  - Subacute: 4-12 weeks
  - Chronic: >12 weeks
  - Recurrent acute: ≥4 episodes/year with symptom-free intervals
- **Primary symptoms** - Nasal obstruction, discharge (color, consistency), facial pain/pressure, headache, post-nasal drip, cough, hyposmia/anosmia, etc.
- **Symptom severity** - Mild, moderate, severe (impact on daily activities)
- **Laterality** - Unilateral vs bilateral symptoms

## Medical History

### Sinusitis-Specific History
- **Previous episodes** - Frequency, typical triggers, what helped
- **Diagnosis confirmation** - Ever diagnosed by physician? Imaging done?
- **Typical pattern** - Seasonal? After colds? Environmental triggers?

### Surgical History
- **Sinus surgery** - Type (e.g., FESS - Functional Endoscopic Sinus Surgery), date, outcome
- **Nasal surgery** - Septoplasty, turbinate reduction, polypectomy, etc.
- **Complications** - Any issues with previous procedures

### Diagnostic Testing
- **Last CT scan** - Date, key findings (if available)
  - Mucosal thickening location and extent
  - Air-fluid levels
  - Anatomic variants (deviated septum, concha bullosa, etc.)
  - Polyps
- **Endoscopy findings** - If performed by ENT
- **Allergy testing** - Results if available

## Allergy and Immunology

### Allergies
- **Environmental allergies** - Pollen, dust mites, mold, pet dander
- **Drug allergies** - Especially antibiotics (penicillin, sulfa, etc.)
- **Allergy treatment** - Immunotherapy, medications
- **Asthma** - Presence and control level (important comorbidity)

### Drug Sensitivities
- **Aspirin sensitivity** - Associated with Samter's triad (aspirin sensitivity, asthma, nasal polyps)
- **Previous adverse reactions** - To any sinusitis medications

## Current Medications

### Sinusitis-Related
- **Current treatments** - Nasal steroids, oral steroids, antibiotics, decongestants
- **Duration of current treatment** - How long on current regimen
- **Effectiveness** - What has worked/not worked in the past
- **Nasal irrigation** - Frequency, technique, solution type

### Other Medications
- **Chronic medications** - May interact with sinusitis treatments
- **Immunosuppressants** - Increase infection risk and affect treatment choices
- **Anticoagulants** - May affect surgical decisions

## Optional but Valuable Information

### Microbiology (If Available)
- **Culture results** - From nasal swab or sinus aspirate
- **Antibiotic sensitivities** - Especially for recurrent/chronic cases
- **Fungal cultures** - If fungal sinusitis suspected

### Comorbidities
- **Diabetes** - Affects healing and infection risk
- **Immune disorders** - HIV, immunoglobulin deficiency, etc.
- **Cystic fibrosis** - Chronic sinusitis is common
- **Primary ciliary dyskinesia** - Affects mucociliary clearance
- **Granulomatosis with polyangiitis** - Can cause chronic rhinosinusitis

### Environmental and Social History
- **Smoking status** - Current, former (quit date), never
  - Pack-years if former/current smoker
- **Secondhand smoke exposure**
- **Occupational exposures** - Chemicals, dust, fumes
- **Home environment** - Humidity, air quality, pets, mold
- **Geographic location** - Climate affects sinusitis patterns

### Lifestyle Factors
- **Physical activity** - May affect nasal airflow and symptoms
- **Sleep quality** - Nasal obstruction often affects sleep
- **Stress levels** - Can affect immune function

## Data Collection Approach

### First Consultation
Focus on:
1. Demographics (age, gender)
2. Current symptom duration and severity
3. Previous sinusitis history
4. Allergies (environmental and drug)
5. Current medications
6. Other chronic conditions
7. Smoking history

### Subsequent Consultations
Update:
- Current symptoms and any changes
- Treatment response
- New medications or tests
- Any new relevant medical history

## Tips for Natural Information Gathering

- **Don't interrogate** - Weave questions into natural conversation
- **Prioritize relevance** - Focus on information that will impact current recommendations
- **Allow elaboration** - Patients often volunteer important context
- **Clarify as needed** - Ask follow-up questions when responses are vague
- **Respect privacy** - Some patients may not want to share everything immediately
- **Build gradually** - Not all information is needed in the first conversation

## Storage Consideration

All collected information should be saved in structured format to the patient's profile using `scripts/init_patient.py` (for new patients) and updated with `scripts/save_consultation.py` (for each consultation).
