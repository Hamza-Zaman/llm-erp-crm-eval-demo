# Helper functions used across evaluations.
# These are deliberately simple so the demo runs offline without external services.

import re

def extract_contract_fields(text: str):
    """Very small heuristic extractor for demo purposes only.
    In production, plug in a proper model and keep this function signature stable.
    """
    text_l = text.lower()
    days = re.findall(r'(\d+\s*days)', text_l)
    months = re.findall(r'(\d+\s*months?)', text_l)
    termination = None
    if "terminate" in text_l or "termination" in text_l:
        # capture a short phrase following the word 'terminate'
        chunk = text.split("terminate")[-1]
        termination = " ".join(chunk.split(".")[0:1]).strip()
        termination = termination if termination else None
    return {
        "payment_terms": days[0] if days else None,
        "warranty": months[0] if months else None,
        "termination": termination
    }

def qualify_lead(industry:str, employees:int, notes:str)->int:
    """Simple triage heuristic; replace with your scoring model when available."""
    score = 0
    if industry in ["Manufacturing","Construction"]:
        score += 1
    if employees and employees > 100:
        score += 1
    n = notes.lower() if isinstance(notes,str) else ""
    for kw in ["multi", "long-term", "energy"]:
        if kw in n:
            score += 1
            break
    return 1 if score >= 2 else 0

def summarise_note(text:str)->str:
    """One-line summary for handovers. Keep under ~15 words in this demo."""
    t = text.lower()
    if "survey" in t:
        return "Survey booked; prep U-value specs and frame options."
    if "voicemail" in t:
        return "Follow up; send case studies and insurance certificates."
    if "pricing" in t or "delivery" in t:
        return "Provide volume pricing and Q4 delivery schedule."
    # default: first clause
    return text.split(".")[0][:80]
