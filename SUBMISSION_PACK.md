# Consent Loom

## CSH Social Impact Ideathon 2026

**Track:** AI

**Project name:** Consent Loom

**One-line idea:** A local-first AI policy compiler that turns a student's own words into a minimal, time-bounded support protocol that teachers can act on without receiving a diagnosis or a private life story.

## Problem

Students who need an accommodation often have to repeat the same explanation to every teacher. The explanation then gets copied into systems that preserve more personal detail than the next adult actually needs. A generic chatbot can make this worse by inventing a label, turning a temporary preference into a permanent identity, or suggesting an action the student never authorized.

## Proposed solution

Consent Loom lets a student write a support request in ordinary language, such as: "When group work gets loud, please give me the written first step and let me move to the side table for ten minutes." An AI extractor proposes a structured protocol:

```json
{
  "trigger": "high-noise group work",
  "support_action": "written first step + side table",
  "duration": "10 minutes",
  "expiry": "end of this class",
  "source_spans": ["gets loud", "written first step", "side table", "ten minutes"]
}
```

The student confirms or edits the proposal. A deterministic policy checker rejects unsupported diagnosis, unbounded duration, hidden recipients, and actions not grounded in the source text. The teacher receives only the minimum actionable protocol. The student can revoke it or let it expire, and the local receipt shows exactly which words supported each field.

## Technology component

1. A constrained AI extraction step proposes typed fields and source spans.
2. A schema validator and policy checker enforce expiry, consent, recipient, and provenance rules.
3. A small local state machine handles `draft -> confirmed -> shared -> expired/revoked` transitions.
4. A redaction layer produces the minimum teacher view while retaining the full text only in the student's local vault.

The important technical decision is that the model is not the authority. It proposes a structure; the verifier and the student's explicit confirmation decide what can be shared.

## Beneficiaries

- Students who repeatedly explain support needs during transitions, group work, or high-load tasks.
- Teachers and learning-support teams that need one concrete next action rather than a sensitive narrative.
- Schools that need measurable consent and retention boundaries without buying a surveillance dashboard.

## Potential impact

The first pilot would measure time from request to usable support, student correction rate, unsupported-field rejection rate, revocation/expiry compliance, and how many sensitive fields are omitted from the teacher view. Success is not a higher AI confidence score; it is fewer repeated explanations and fewer unauthorized assumptions.

## Feasibility and implementation plan

**Week 1:** implement the typed schema, source-span receipt, policy checker, and a mocked local extractor.

**Weeks 2–3:** add a small on-device model or a consented hosted model behind the same verifier; test adversarial prompts and unsupported diagnosis claims.

**Pilot:** run with student volunteers and one learning-support team using synthetic data first, then consented data only after the retention and revocation tests pass.

## Challenges and limitations

- Natural language is ambiguous; the product must ask for clarification instead of guessing.
- A local vault still needs device security and a recovery policy.
- A protocol is not a legal accommodation decision and cannot replace a school's safeguarding process.
- The model may miss a need; every field must remain editable and the student must be able to bypass extraction.

## Originality and relationship to prior work

This is a new CSH-specific concept developed during the ideathon window. It draws on Cora's broader interest in local-first, inspectable systems, but it is not SignalBridge's voice-state classifier, Recovery Ledger's recovery planner, or Boundary Lab's explanation tutor. Its distinctive unit is a **consent-bounded policy**, not an emotion label, a next step, or a confidence score.

## Supporting material

- `pitch.html` is a standalone visual for the problem, architecture, lifecycle, and pilot metrics.
- The local package contains no external student data or account state. CSH registration is complete, but no CSH project draft, upload, or submission has been created.

## AI-use disclosure

AI coding assistance was used to draft and edit this local pitch material. The project owner reviewed the concept, technical boundaries, and claims and remains responsible for the submission.
