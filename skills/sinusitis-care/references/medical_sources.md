# Authoritative Medical Sources for Sinusitis Information

This document lists authoritative medical websites to consult for evidence-based sinusitis information. Use your judgment to select the most appropriate source(s) based on the question type and complexity.

## Primary Clinical Sources

### 1. UpToDate
- **URL**: https://www.uptodate.com
- **Best for**: Clinical decision support, detailed treatment protocols, drug information
- **Strengths**: Evidence-based, regularly updated, preferred by clinicians
- **Search tips**: Use specific terms like "acute bacterial rhinosinusitis treatment"

### 2. Mayo Clinic
- **URL**: https://www.mayoclinic.org
- **Best for**: Patient education, symptom assessment, general treatment overview
- **Strengths**: Balanced approach for both patients and professionals, highly reliable
- **Search tips**: Search "sinusitis" or specific symptoms

### 3. Cleveland Clinic
- **URL**: https://my.clevelandclinic.org
- **Best for**: ENT-specific information, surgical procedures, specialized care
- **Strengths**: Strong ENT department reputation, comprehensive patient resources
- **Search tips**: Look for Health Library section

## Professional Guidelines

### 4. American Academy of Otolaryngology–Head and Neck Surgery (AAO-HNS)
- **URL**: https://www.enthealth.org and https://www.entnet.org
- **Best for**: Official clinical practice guidelines, professional standards
- **Strengths**: Definitive professional guidelines, consensus statements
- **Search tips**: Look for "Clinical Practice Guideline: Rhinosinusitis"

### 5. European Position Paper on Rhinosinusitis and Nasal Polyps (EPOS)
- **URL**: Available through https://www.rhinologyjournal.com
- **Best for**: International perspective, comprehensive European guidelines
- **Strengths**: Evidence-based European consensus, detailed management algorithms
- **Search tips**: Search for "EPOS 2020" for latest guidelines

## Academic and Research Sources

### 6. Johns Hopkins Medicine
- **URL**: https://www.hopkinsmedicine.org
- **Best for**: Academic medical perspective, research-backed information
- **Strengths**: Research institution credibility, cutting-edge information
- **Search tips**: Use their health library and conditions section

### 7. PubMed / National Library of Medicine (NLM)
- **URL**: https://pubmed.ncbi.nlm.nih.gov
- **Best for**: Latest research, systematic reviews, meta-analyses
- **Strengths**: Primary literature, most current research findings
- **Search tips**: Use MeSH terms like "Sinusitis/therapy" or "Rhinosinusitis, Chronic"

### 8. PubMed Central (PMC)
- **URL**: https://pmc.ncbi.nlm.nih.gov
- **Best for**: Full-text peer-reviewed research articles
- **Strengths**: Free access to full articles, detailed research data
- **Search tips**: Use for in-depth reading of specific studies

### 9. Springer Medical Journals
- **URL**: https://link.springer.com
- **Best for**: European and international research, specialized ENT journals
- **Strengths**: High-impact research publications, international perspectives
- **Search tips**: Search for "rhinosinusitis" or "empty nose syndrome" in ENT journals

## Specialized ENT Sources

### 10. ENT Today
- **URL**: https://www.enttoday.org
- **Best for**: Current ENT practice trends, case discussions, clinical insights
- **Strengths**: Practical clinical perspectives, recent developments in field
- **Search tips**: Search for specific conditions or surgical techniques

### 11. USA Sinus Institute
- **URL**: http://www.usasinus.org
- **Best for**: Sinus-specific conditions, patient advocacy information
- **Strengths**: Focus on sinus disorders, patient-centered resources
- **Search tips**: Look for specific sinus conditions and treatment options

### 12. National Organization for Rare Disorders (NORD)
- **URL**: https://rarediseases.org
- **Best for**: Rare ENT conditions, uncommon presentations, Empty Nose Syndrome
- **Strengths**: Comprehensive rare disease information, patient support resources
- **Search tips**: Use for conditions like Empty Nose Syndrome or rare complications

## Patient Community Resources

### 13. Mayo Clinic Connect
- **URL**: https://connect.mayoclinic.org
- **Best for**: Patient experiences, community support, long-term management
- **Strengths**: Moderated patient forums, real-world experiences
- **Search tips**: Search for patient discussions on specific conditions

## Supplementary Patient Education

### 14. WebMD
- **URL**: https://www.webmd.com
- **Best for**: Patient-friendly explanations, common questions
- **Strengths**: Accessible language, comprehensive symptom checker
- **Search tips**: Good for validating patient-friendly explanations

## Search Strategy Recommendations

### For Simple Questions
- Start with Mayo Clinic or Cleveland Clinic for quick, reliable patient information
- Cross-check with UpToDate for clinical accuracy

### For Medication Questions
- UpToDate for detailed drug information, interactions, contraindications
- Cross-reference with AAO-HNS guidelines
- PubMed/PMC for latest research on drug efficacy

### For Complex or Atypical Cases
- Search AAO-HNS and EPOS for guideline-based approaches
- PubMed/PMC for recent research on unusual presentations
- Springer journals for international research perspectives
- Cross-validate findings from multiple sources

### For Rare Conditions (e.g., Empty Nose Syndrome)
- NORD (rarediseases.org) for comprehensive rare disease information
- PubMed Central for full-text research articles
- ENT Today for clinical case discussions
- USA Sinus Institute for patient advocacy perspectives
- Mayo Clinic Connect for patient experiences

### For Treatment Decisions
- UpToDate for evidence-based treatment algorithms
- AAO-HNS/EPOS for guideline recommendations
- Cleveland Clinic/Mayo for patient perspective
- PubMed for latest clinical trials and outcomes research

## Using WebSearch and WebFetch Tools

When you determine that external information is needed:

1. **Use WebSearch** to find relevant pages from these sources
   - Example: `WebSearch("acute sinusitis treatment UpToDate")`
   - Example: `WebSearch("chronic rhinosinusitis AAO-HNS guidelines")`

2. **Use WebFetch** to extract detailed information from specific pages
   - Example: `WebFetch(url, "What are the recommended antibiotics for acute bacterial sinusitis?")`

3. **Cross-validate** important information by checking multiple sources

### WebFetch Failure Handling Protocol

**Common Error Codes:**
- **403 Forbidden**: Access denied by server
- **303 See Other**: Redirect to different URL
- **Timeout**: Server took too long to respond

**When WebFetch Fails, Try These Alternatives (in order):**

1. **PMC vs PubMed Switch:**
   - If `pmc.ncbi.nlm.nih.gov/articles/PMC123456/` fails (403)
   - Try `pubmed.ncbi.nlm.nih.gov/123456/` (abstract only, but usually works)

2. **Search for Alternative Article:**
   - Use WebSearch to find similar article from same journal
   - Search: `site:[journal domain] [topic] 2024 2025`

3. **Try Related Sources:**
   - Springer fails → Try PMC or NEJM
   - Paywall journal → Look for preprint or open access version
   - Academic site fails → Try Mayo/Cleveland patient education pages

4. **Document and Continue:**
   - Note in response: "⚠️ Springer article returned 403 error - substituted with PMC systematic review on same topic"
   - **Never give up until you have 3-5 successful WebFetches**

**Example Recovery Strategy:**
```
Attempt 1: WebFetch(link.springer.com/article/X) → 403 error
Attempt 2: WebFetch(pmc.ncbi.nlm.nih.gov/articles/PMC-similar) → Success ✅
Attempt 3: WebFetch(mayoclinic.org/conditions/X) → Success ✅
Attempt 4: WebFetch(clevelandclinic.org/health/X) → Success ✅
Result: 3/5 achieved, continue to 5 total
```

**Priority Order for WebFetch (Most Reliable → Less Reliable):**
1. ✅ Mayo Clinic, Cleveland Clinic (rarely block)
2. ✅ PMC full-text (pmc.ncbi.nlm.nih.gov)
3. ✅ NORD (rarediseases.org)
4. ⚠️ PubMed abstracts (limited info but reliable)
5. ⚠️ Johns Hopkins (occasionally blocks)
6. ⚠️ Springer (often 403 errors, try last)

## Important Notes

- **Always cite sources** when providing information from these websites
- **Prioritize recent information** - guidelines are updated periodically
- **Consider context** - some sources are more technical (UpToDate) vs patient-friendly (Mayo Clinic)
- **Use judgment** - not every question requires external research
