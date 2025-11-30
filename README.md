# Sinusitis Care - Claude Skill

A comprehensive Claude skill for providing evidence-based sinusitis patient care and support.

## Overview

This skill transforms Claude into a specialized sinusitis care assistant that provides:

- 🔍 **Symptom Analysis** - Identify sinusitis type and severity
- 💊 **Treatment Guidance** - Evidence-based recommendations from authoritative sources
- 🏥 **Emergency Assessment** - Identify danger signals requiring immediate care
- 📊 **Patient Record Management** - Track symptoms and consultations over time
- 🌐 **Real-time Medical Research** - Search 8 authoritative medical websites

## Features

### Evidence-Based Information
- Integrates with 8 authoritative medical sources (UpToDate, Mayo Clinic, Cleveland Clinic, Johns Hopkins, AAO-HNS, EPOS, PubMed, WebMD)
- Real-time search capability for latest medical information
- Cross-validation from multiple sources for complex cases

### Intelligent Information Gathering
- Tiered approach: simple questions use existing knowledge, complex cases trigger multi-source research
- Full freedom for Claude to determine appropriate research depth
- Flexible output formatting based on question complexity

### Patient Safety
- Automatic danger signal detection
- Medical disclaimer on every response
- Clear guidance on when to seek professional care
- Never provides specific drug dosages

### Continuity of Care
- Structured patient profile collection
- Date-organized consultation history
- Automatic record keeping in `~/.sinusitis-care/` directory

## Installation

1. Download the `sinusitis-care.skill` file
2. Import it into Claude Code or your Claude environment
3. The skill will automatically activate when users ask sinusitis-related questions

## Usage

### First-Time Patient
The skill will guide new patients through collecting baseline information:
- Demographics (age, gender)
- Medical history (previous sinusitis episodes, surgeries)
- Allergies and current medications
- Environmental factors
- Recent diagnostic tests (CT scans, etc.)

### Consultations
Simply ask questions about sinusitis symptoms, treatment, or concerns:
- "I have nasal congestion and facial pain for 5 days"
- "What's the difference between acute and chronic sinusitis?"
- "Should I see a doctor for my symptoms?"
- "How often should I do nasal irrigation?"

### Data Storage
All patient data is stored locally in:
- `~/.sinusitis-care/patient_profile.json` - Baseline patient information
- `~/.sinusitis-care/consultations/` - Individual consultation records by date

## Skill Structure

```
sinusitis-care/
├── SKILL.md                          # Main skill definition
├── references/                       # Medical knowledge resources
│   ├── medical_sources.md           # 8 authoritative medical websites
│   ├── danger_signals.md            # Emergency warning signs
│   ├── patient_profile_fields.md    # Patient information guide
│   └── medical_disclaimer.md        # Disclaimer templates
├── scripts/                         # Patient data management
│   ├── init_patient.py             # Initialize new patient
│   ├── load_patient_data.py        # Load patient history
│   └── save_consultation.py        # Save consultation records
└── assets/
    └── patient_profile_template.json # Patient data structure
```

## Design Philosophy

This skill is designed with **high freedom for AI**:
- Provides authoritative resources without rigid templates
- Gives Claude full discretion in research depth and output format
- Trusts AI's clinical judgment while ensuring safety guardrails
- Focuses on principles over prescriptive procedures

## Medical Disclaimer

⚠️ **Important**: This skill provides educational information only and does not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns.

## Authoritative Medical Sources

1. **UpToDate** - Clinical decision support
2. **Mayo Clinic** - Patient education and clinical guidelines
3. **Cleveland Clinic** - ENT-specific information
4. **Johns Hopkins Medicine** - Academic medical perspective
5. **AAO-HNS** - American Academy of Otolaryngology official guidelines
6. **EPOS** - European Position Paper on Rhinosinusitis
7. **PubMed** - Latest research and systematic reviews
8. **WebMD** - Patient-friendly health information

## Contributing

Contributions are welcome! This skill was created for individual patients but could be enhanced with:
- Additional medical knowledge resources
- Improved patient data visualization
- Integration with health tracking apps
- Multi-language support

## License

MIT License - Feel free to use, modify, and distribute.

## Acknowledgments

Created using Claude Code and the skill-creator framework from Anthropic's Agent Skills marketplace.

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

**Version**: 1.0.0
**Created**: November 2025
**For**: Individual sinusitis patients seeking evidence-based health information
