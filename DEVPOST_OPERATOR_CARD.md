# CSH Social Impact Ideathon - Consent Loom operator card

## Competition gate

- Official page: https://csh-social-impact-ideathon.devpost.com/
- Challenge ID: `31151`
- Registration: https://csh-social-impact-ideathon.devpost.com/register?flow%5Bdata%5D%5Bchallenge_id%5D=31151&flow%5Bname%5D=register_for_challenge
- Manage submissions: https://devpost.com/submit-to/31151-csh-social-impact-ideathon/manage/submissions
- Deadline shown in the Cora-owned page: 2026-09-12 11:45 AM GMT+8
- Eligibility: ages 13+, students only, all countries except standard exceptions
- Format: online; individual or teams up to three
- Track: AI
- Required content: project/idea name, track, problem, proposed solution, technology component, beneficiaries, impact, feasibility, limitations, and pitch material

The official rules say submissions should be original work developed during the August 31–September 11 ideathon window. The registration form asks for teammate mode, referral, eligibility agreement, and official-rules/Devpost-terms agreement. Registration was completed solo on 2026-09-06; project creation then opened an unsolved Devpost image CAPTCHA. No CSH project draft, upload, or submission exists.

## Project fields

- Name: `Consent Loom`
- Tagline: `A local-first AI policy compiler that turns a student's words into a consent-bounded support protocol.`
- Track: `AI`
- Supporting visual: `pitch.html`
- Rendered supporting visual: `pitch.png`
- Working local prototype: `prototype.html` (propose, verify, confirm, minimum-share, revoke)
- Local review assets: `demo/consent_loom_draft.png`, `demo/consent_loom_proposed.png`, `demo/consent_loom_shared.png`, `demo/consent_loom_demo_2026-09-05.webm`
- Full copy: `SUBMISSION_PACK.md`
- Structured fields: `DEVPOST_FIELD_PAYLOAD.json`
- Local check: `python submission_preflight.py`

## Submission story

Consent Loom addresses the repeated, privacy-costly explanation students face when they need classroom support. The student writes a request in ordinary language. An AI extractor proposes typed fields and source spans; a deterministic verifier rejects unsupported diagnosis, hidden recipients, unbounded duration, and actions not grounded in the source. The student confirms or edits the result before a teacher sees the minimum actionable protocol. It can expire or be revoked, and the local receipt makes the reasoning inspectable.

The project is distinct from Cora's other competition work: it is not SignalBridge's voice-state classifier, Recovery Ledger's recovery planner, or Boundary Lab's explanation tutor. Its unit of design is a consent-bounded policy with provenance.

## Action boundary

1. Solve the Devpost project-creation CAPTCHA manually, then create a separate Devpost project for Consent Loom.
2. Paste the CSH-specific fields and attach the supporting visual.
3. Review the originality/date statement and submit only after action-time confirmation.
