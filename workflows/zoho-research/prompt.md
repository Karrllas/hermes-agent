
## Requirements

- Research each company using Lithuanian and non-Lithuanian public sources.
- Check company websites, media coverage, public announcements, registries, financial profiles, court and procurement traces, and other credible public sources.
- Focus on the last 5 years.
- Prefer concrete facts and dated events over vague summaries.
- If a point is uncertain, say that clearly instead of overstating it.
- Write everything in Lithuanian.
- This report is for Klaipėdos LEZ account-management team.
- Optimize for practical readiness: trajectory, reputation, business direction, likely sensitivities, and issues that may surface in conversation.
- Do not overproduce. Be selective and decision-useful rather than exhaustive.

## Research approach

- Start from the company’s official website and basic company profile sources to confirm identity.
- Then expand to Lithuanian and international media, registries, financial profile sites, public support/project databases, court or legal traces, and procurement/public institution traces when relevant.
- Prefer primary sources and dated reporting over copied directory content.
- Use aggregator sites carefully: they are useful for signals and dates, but avoid overstating claims that are not corroborated.
- Exclude weak or generic filler points.
- If a section has little reliable public evidence, say so briefly instead of padding it.

## Output

- Your entire response must be a single raw JSON object — no text before or after it, no markdown fences.
- Use this structure:

{
  "short": "<timeline section only, plain text, max 2000 chars>",
  "long": "<full dossier, plain text, using caps headers and dashes for structure>",
  "swot": "<SWOT section only, plain text>",
  "log": "<brief process notes: dead sources, uncertainties, search issues — empty string if none>"
}

- Produce one dossier per company.
- Use this exact high-level structure for each company:

### 1. General points
- Give 3-4 main overview points and company trajectory.
- Each point must have:
  - a short title under 5 words
  - a longer descriptive sentence or short paragraph
- Each description should be concise and specific, usually 1-3 sentences.

### 2. Timeline of key events
- Start the timeline section with exactly this line: TIMELINE:
- Cover the last 5 years.
- Include up to 10 main events where possible. If there are none - dont do excuses , just a shorter section.
- **This entire section must not exceed 2000 characters total.** Keep event descriptions concise.
- Format each event as:
  - `yyyy-mm` (thats the only date, dont duplicate dates)
  - short but informative description
- Prefer events that help a relationship manager understand momentum, stress, growth, ownership, funding, disputes, expansion, layoffs, management shifts, or strategic changes.

### 3. Okredo stats
- If public Okredo data is available, provide a concise but sufficiently full stats section.
- Format this section as:
  - stat name
  - one paragraph summary
  - then fuller details
- If Okredo data is not available, say that clearly.
- Keep this section compact. Prefer the few metrics that best explain scale, growth, solvency, workforce, and risk.

### 4. Business direction and reputation
- Include possible current issues or pain points when supported by sources.
- This section should answer: where the company seems to be going, how it is positioned, and what tone or sensitivities may matter in a meeting.

### 5. Financial situation and past issues
- Focus on trend, resilience, pressure points, and any notable warning signs.

### 6. Legal situation and past issues
- Separate routine low-signal traces from genuinely meaningful legal issues.

### 7. PR situation and past issues
- Focus on public image, communications style, visibility, and any past reputational issues.

### 8. SWOT
- Keep SWOT crisp and executive-facing.
- Use exactly 4 bullets:
  - `Stiprybės`
  - `Silpnybės`
  - `Galimybės`
  - `Grėsmės`

- End each company section with a `Sources` subsection listing the key URLs used for that company.

## Style rules

- Write in clear business Lithuanian.
- Avoid hype, PR language, and generic consultant phrasing.
- Avoid repeating the same fact across multiple sections unless it is genuinely important.
- Do not invent motives or internal strategy.
- If a claim is inferred rather than directly stated by sources, phrase it cautiously.
- Assume the reader is intelligent but busy: the dossier should help them enter a meeting better prepared, not overwhelm them.


Company name : {{COMPANY_NAME}}