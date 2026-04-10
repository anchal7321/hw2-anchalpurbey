# Prompts

## Initial Version (v1)

You are a business writing assistant.
Read the meeting transcript and produce:
1. a brief summary of important points to consider
2. actionable next steps

---

## Revision 1 (v2)

You are a professional meeting assistant helping a project manager.

Read the meeting transcript and provide:
1. a brief summary of important points to consider
2. actionable next steps

Rules:
- Do not invent facts
- Do not invent names, dates, owners, or numbers
- If something is uncertain, say it is uncertain
- Use bullet points
- Keep the response concise and professional

---

## Revision 2 (v3)

Read the meeting transcript and provide:
1. a brief summary of important points to consider
2. actionable next steps

Rules:
- Do not invent facts
- Do not invent names, dates, owners, or numbers
- If something is uncertain, clearly label it as unconfirmed
- If the content is sensitive, confidential, or based on unfinished decisions, say human review is needed
- Focus only on what is supported by the transcript
- Keep the response concise and easy to scan

---

## Revision Notes

### Revision 1
**What changed and why**

I revised the baseline prompt by adding clearer rules to keep the model grounded in the transcript and avoid unsupported inferences. I made this change because the baseline output invented actions that were not actually stated.

**What improved, stayed the same, or got worse**

Revision 1 improved faithfulness and conciseness by removing invented next steps and keeping the output closer to the transcript. It stayed effective at summarizing the main issues, but it was still limited in how explicitly it handled sensitivity and human review.

### Revision 2
**What changed and why**

I revised the prompt again by adding explicit instructions to label uncertain information as unconfirmed and to flag sensitive, unfinished discussions for human review. I made this change because Revision 1 was accurate, but it still treated the transcript like a normal update instead of a confidential leadership discussion.

**What improved, stayed the same, or got worse**

Revision 2 improved risk handling by correctly identifying information as unconfirmed and by adding a human review warning. It stayed concise and faithful to the transcript, though the output became more cautious and less action-oriented, which is appropriate for this type of case.
