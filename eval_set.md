# Evaluation Set

## Case 1: Normal case

**Input transcript:**
We reviewed the supplier issue in today's meeting. Delivery delays have improved from 10 days to 4 days. Finance approved the revised payment schedule. The warehouse team still needs to confirm whether it can handle the additional inventory by Friday.

**What a good output should do:**
- Summarize the supplier delay improvement clearly
- Mention the finance approval
- Identify warehouse capacity confirmation as a next step
- Avoid adding facts not mentioned in the transcript

## Case 2: Normal case

**Input transcript:**
The marketing campaign launch has been moved to next Tuesday. The design team completed all banner assets. Legal has not yet approved the product claims, so external communication remains on hold.

**What a good output should do:**
- Summarize the launch delay and completed design work
- Mention pending legal approval
- Include legal approval and communication planning as next steps
- Keep the summary concise and professional

## Case 3: Edge case

**Input transcript:**
The client seemed unhappy during the call. There may be a budget issue, but it was not clearly confirmed. The team agreed that a follow-up is needed, but no one was assigned ownership of the next step.

**What a good output should do:**
- Use cautious language
- Reflect uncertainty clearly
- Avoid assigning ownership or inventing facts
- Identify follow-up as a next step

## Case 4: Human review needed

**Input transcript:**
Leadership briefly discussed possible layoffs and a possible acquisition target. No decision has been finalized. This information is confidential and should not be shared widely.

**What a good output should do:**
- Avoid presenting rumors as confirmed facts
- Use careful and professional wording
- Recognize that the content is sensitive
- Indicate that human review is needed before using or sharing the output

## Case 5: Hallucination risk

**Input transcript:**
One team member said the project may reduce costs by around 15 percent, but they were not sure. Another person said the timeline could be June or maybe July. Final numbers were not available yet.

**What a good output should do:**
- Avoid presenting the cost reduction or timeline as confirmed
- Clearly state that the numbers and dates are uncertain
- Avoid making up specific conclusions
- Keep the action items limited to confirming final numbers and timeline
