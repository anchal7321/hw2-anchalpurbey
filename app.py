"""
app.py - Meeting Transcript Summarizer using Gemini API
Usage:
  python app.py --case 1 --prompt v1
  python app.py --case 3 --prompt v1
"""

import os
import argparse
from datetime import datetime
from google import genai

# -- Gemini client -------------------------------------------------------------
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-lite"

# -- Built-in transcript cases (matching eval_set.md) --------------------------
TRANSCRIPTS = {
    1: {
        "label": "Normal case - Supplier & Warehouse",
        "text": (
            "We reviewed the supplier issue in today's meeting. Delivery delays have improved "
            "from 10 days to 4 days. Finance approved the revised payment schedule. The warehouse "
            "team still needs to confirm whether it can handle the additional inventory by Friday."
        ),
    },
    2: {
        "label": "Normal case - Marketing Campaign",
        "text": (
            "The marketing campaign launch has been moved to next Tuesday. The design team "
            "completed all banner assets. Legal has not yet approved the product claims, so "
            "external communication remains on hold."
        ),
    },
    3: {
        "label": "Edge case - Unhappy Client / Uncertain Follow-up",
        "text": (
            "The client seemed unhappy during the call. There may be a budget issue, but it was "
            "not clearly confirmed. The team agreed that a follow-up is needed, but no one was "
            "assigned ownership of the next step."
        ),
    },
    4: {
        "label": "Human review needed - Sensitive Leadership Discussion",
        "text": (
            "Leadership briefly discussed possible layoffs and a possible acquisition target. "
            "No decision has been finalized. This information is confidential and should not "
            "be shared widely."
        ),
    },
    5: {
        "label": "Hallucination risk - Uncertain Numbers & Timeline",
        "text": (
            "One team member said the project may reduce costs by around 15 percent, but they "
            "were not sure. Another person said the timeline could be June or maybe July. "
            "Final numbers were not available yet."
        ),
    },
}

# -- Prompt versions -----------------------------------------------------------
def build_prompt(transcript: str, version: str) -> str:
    if version == "v1":
        return f"""You are a business writing assistant.
Read the meeting transcript and produce:
1. a brief summary of important points to consider
2. actionable next steps

Meeting Transcript:
\"\"\"{transcript}\"\"\""""

    else:
        raise ValueError(f"Unknown prompt version: {version}. Use 'v1'.")


# -- Call Gemini API -----------------------------------------------------------
def call_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )
    return response.text.strip()


# -- Save output to file -------------------------------------------------------
def save_output(case_num: int, label: str, prompt_version: str,
                transcript: str, output: str) -> str:
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/case{case_num}_{prompt_version}_{timestamp}.txt"

    content = f"""MEETING TRANSCRIPT SUMMARIZER
==============================
Case:           {case_num} - {label}
Prompt Version: {prompt_version}
Timestamp:      {timestamp}
Model:          {MODEL}

-- TRANSCRIPT ------------------------------------------
{transcript}

-- GENERATED OUTPUT ------------------------------------
{output}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename


# -- Main ----------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Meeting Transcript Summarizer using Gemini API"
    )
    parser.add_argument(
        "--case", type=int, choices=[1, 2, 3, 4, 5], default=1,
        help="Transcript case number (1-5, default: 1)"
    )
    parser.add_argument(
        "--prompt", type=str, choices=["v1"], default="v1",
        help="Prompt version (default: v1)"
    )
    args = parser.parse_args()

    case = TRANSCRIPTS[args.case]
    transcript = case["text"]
    label = case["label"]

    print(f"\n{'='*60}")
    print(f"  MEETING TRANSCRIPT SUMMARIZER")
    print(f"{'='*60}")
    print(f"  Case {args.case}: {label}")
    print(f"  Prompt Version: {args.prompt}")
    print(f"  Model: {MODEL}")
    print(f"{'='*60}\n")

    print("-- TRANSCRIPT ------------------------------------------")
    print(transcript)
    print()

    print("-- Calling Gemini API... -------------------------------")
    prompt = build_prompt(transcript, args.prompt)
    output = call_gemini(prompt)

    print("\n-- GENERATED OUTPUT ------------------------------------")
    print(output)

    saved_path = save_output(args.case, label, args.prompt, transcript, output)
    print(f"\n-- Output saved to: {saved_path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
