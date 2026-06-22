# AI-Powered SEO Content Production Framework

## Overview

This framework pulls together the recurring patterns, workflows, and hard-won practices shared across ten of the most credible voices working at the intersection of SEO and AI search: Kevin Indig, Eric Siu, Nathan Gotch, Koray Tugberk Gübür, Dan Petrovic, Bernard Huang, Michał Suski, Britney Muller, Lily Ray, and Olga Zarr.

What emerges from their combined output is not ten separate approaches but one coherent production system, applied at different scales and with different tool stacks. The consensus is clear: AI-powered content production is not about replacing human judgment but about compressing the time between insight and execution, while keeping a human in the loop at every stage that matters.

The eight stages below reflect that shared logic. They move from opportunity identification through to measurement, and each stage is grounded in what these practitioners are actually doing with clients, not what they predict might work.


## Stage 01: Opportunity Discovery

**Objective:** Identify where genuine search demand exists across both traditional and AI-driven platforms before a single word of content is written.

**Activities:**
- Pull data from Google Search Console, GA4, and AI rank tracking tools to build a unified demand picture
- Map queries across traditional Google rankings and AI platform citations (ChatGPT, Perplexity, Gemini) separately, since correlation between platforms varies significantly
- Segment opportunity by buyer persona and purchase intent stage, since problem-focused queries carry the highest commercial signal
- Identify which third-party sources AI models currently cite for your target queries, and assess whether your brand appears in any of them
- Use a seed prompt panel of roughly 40 prompts split across brand, category, and problem-focused queries to establish a baseline AI visibility reading
- Cross-reference Common Crawl visibility with traditional indexation to understand training data exposure

**Common Tools:** Google Search Console, GA4, Ahrefs, Semrush, Rankability, ChatGPT, Perplexity, Gemini, SparkToro

**Experts Referenced:** Kevin Indig, Eric Siu, Nathan Gotch

**Key Takeaway:** Opportunity discovery in the AI era requires two separate research tracks running in parallel. What ranks in Google and what gets cited in AI answers are not the same list, and treating them as one is where most strategies go wrong from the start.


## Stage 02: Topic and Entity Research

**Objective:** Build a structured, semantically complete understanding of the topic space before content planning begins, including the entities, attributes, and relationships a model needs to see.

**Activities:**
- Map the full entity graph for your target topic area: core entities, related entities, and the specific attribute-value pairs that define each one
- Identify the "source context" your site occupies (affiliate, publisher, brand, tool) and assess whether that context matches the dominant source type already ranking for target queries
- Apply the topical authority formula as a planning constraint: coverage and historical data divided by retrieval cost
- Split your topical map into a core section (direct monetization focus) and an outer section (authority-building content that feeds back to the core)
- Use mechanistic interpretability thinking to assess what a model already believes about your brand before any grounding search runs, and where confidence is lowest
- Run query fan-out analysis to understand the roughly 100 reformulations a search engine or AI model might apply to a single seed query

**Common Tools:** ChatGPT, Claude, Surfer, Clearscope, Ahrefs, custom entity mapping tools, Dan Petrovic's free toolkit (citation mining, query fan-out generator)

**Experts Referenced:** Koray Tugberk Gübür, Dan Petrovic

**Key Takeaway:** Content that lacks entity depth and attribute specificity gets passed over by AI models regardless of how well it is optimized on the surface. You cannot write your way into AI citations without first understanding what the model already knows and where the gaps are.


## Stage 03: Content Brief Creation

**Objective:** Translate research into a structured brief that gives writers and AI tools enough context to produce content that serves both human readers and machine retrieval.

**Activities:**
- Build a three-layer "search brainiac" brief: a data layer (GSC, GA4, AI rank tracking), a company knowledge layer (products, FAQs, founder insights), and an expertise layer (original data, user-generated content, interview material)
- Define the primary query intent and map secondary intents at the heading level, assigning specific keywords to specific sections rather than distributing them loosely
- Run a gap analysis by feeding top competitor pages into an AI model and asking it directly to identify what topics are missing
- Set a clear information retrieval cost target: the brief should specify that the final content must allow an AI to extract a clear, complete answer from any individual section without reading the full piece
- Include schema markup requirements, FAQ architecture, and structured data targets as part of the brief rather than treating them as post-production additions
- Specify the "source context" the piece should establish and the third-party sources it should be positioned to appear alongside

**Common Tools:** Surfer, Clearscope, ChatGPT, Claude, Rankability, Google Search Console

**Experts Referenced:** Bernard Huang, Michał Suski, Nathan Gotch

**Key Takeaway:** A brief that only covers keywords and word count is not sufficient for AI-era content. The brief needs to specify what an AI model should be able to extract from the piece and how that extraction should happen, alongside the traditional SEO requirements.


## Stage 04: AI-Assisted Content Generation

**Objective:** Produce a high-quality first draft efficiently using AI tools, while keeping human judgment central to the parts of the process that determine whether the content is actually good.

**Activities:**
- Write a human-authored first draft or detailed outline before handing anything to an AI tool; AI performs significantly better as a sharpening tool than as a starting point
- Apply few-shot prompting with real examples from your own brand voice rather than relying on generic instructions
- Use multi-step generation: outline first, then section by section, rather than prompting for a full piece in one pass
- Run a mandatory human review pass focused on four things: factual accuracy, brand voice consistency, internal link placement, and any claim that could cause harm if wrong
- For long-form content, use AI agent workflows to parallelize research, draft generation, and schema planning simultaneously rather than running them sequentially
- Apply a pre-automation gut-check before any content enters a publishing pipeline: could a mistake here damage the brand, mislead a reader, or cause a real consequence

**Common Tools:** Claude, ChatGPT, Cursor, Claude Code, Surfer, Clearscope, Jasper

**Experts Referenced:** Britney Muller, Eric Siu

**Key Takeaway:** The marketers producing the best AI-assisted content right now are not the ones who use AI the most. They are the ones who use it at the right moments and stay in the loop at the moments that matter. AI produces the average of everything it has seen; the human's job is to push past that average.


## Stage 05: Verification and Citation Enhancement

**Objective:** Ensure the published content can be trusted by both human readers and AI retrieval systems, and that it is positioned to be cited rather than just indexed.

**Activities:**
- Run citation mining against your target commercial queries across all major AI platforms to identify which sources are currently being cited and how frequently
- Cross-reference the "consideration set" (all pages the model could have cited) against the "selected set" (pages it actually cited) to find the gap your content needs to close
- Check token-level confidence in AI outputs about your brand to identify the specific claims or topic areas where the model is most uncertain and most open to influence
- Verify all factual claims against primary sources before publication; AI-generated content carries a higher-than-average risk of confident-sounding inaccuracies
- Apply structured E-E-A-T signals: named authors with credentials, publication dates, sourced statistics, and links to primary research rather than secondary summaries
- Identify the highest-frequency cited third-party URLs for your target queries and assess whether your content or brand is mentioned on any of them

**Common Tools:** Dan Petrovic's citation mining toolkit, Ahrefs Brand Radar, Profound, Lily Ray's tooling stack (Data for SEO, SimilarWeb, Search Console, Peak)

**Experts Referenced:** Dan Petrovic, Lily Ray

**Key Takeaway:** Publishing accurate, well-cited content is not just good editorial practice; it is the primary mechanism by which AI models learn to trust a source. Every factual error is a signal against future citation, and that signal accumulates over time.


## Stage 06: GEO and AEO Optimization

**Objective:** Optimize published content specifically for inclusion in AI-generated answers, recognizing that this is a different optimization target from traditional search ranking even though the two are correlated.

**Activities:**
- Structure content so that any individual section delivers a complete, self-contained answer to a specific question without requiring the full page to be read
- Reduce information retrieval cost by writing in a dense, fact-forward style that prioritizes extractability over narrative engagement
- Target the grounding layer specifically: create content that targets how an AI model researches a topic in real time, not just what it already knows from training
- Run digital PR campaigns targeting publications that already rank on page one of Google for your core commercial queries, since those sources receive heavier model weighting
- Build or earn unlinked brand mentions on high-frequency cited domains; links and nofollow tags appear to make no measurable difference to AI citation outcomes
- Avoid self-promotional comparison and alternative pages at scale; these are on enforcement radar and represent a short-term tactic with real long-term risk
- Ensure all published content is server-side rendered and parsable HTML; JavaScript-heavy pages are effectively invisible to most AI crawlers

**Common Tools:** Surfer AI Tracker, Clearscope 2.0, Rankability, Ahrefs, SE Ranking, Profound

**Experts Referenced:** Bernard Huang, Nathan Gotch, Lily Ray

**Key Takeaway:** Being cited in an AI answer is not a lucky accident and it is not purely a function of domain authority. It is the result of being mentioned by the right third-party sources, having content structured for fast machine extraction, and maintaining the kind of SEO health that AI models use as a trust proxy.


## Stage 07: Distribution

**Objective:** Extend the reach of every piece of content across the platforms AI models draw from most heavily, rather than publishing once and waiting.

**Activities:**
- Repurpose each piece of pillar content natively across YouTube, LinkedIn, Reddit, and short-form video rather than cross-posting the same format everywhere
- Use AI sub-agent workflows to compress a long-form piece or transcript into platform-specific derivative assets; a single 80-minute session can yield 35 or more pieces with the right pipeline
- Prioritize Reddit and YouTube distribution specifically; Reddit accounts for roughly 24% of Perplexity citations, and YouTube is one of the most heavily weighted sources across multiple AI platforms
- Maintain a strict content freshness system with weekly publishing cadence and quarterly audits, since approximately 95% of AI citations pull from content published within the last ten months
- Build presence across multiple owned retrieval points for each target query (website page, LinkedIn post, YouTube video) rather than concentrating effort on a single ranking page
- Track which distribution channels are driving AI citations as a primary metric, not just traffic referrals

**Common Tools:** Claude Code, Cursor, MCP workflows, LinkedIn, YouTube, Reddit, Buffer, Zapier

**Experts Referenced:** Eric Siu, Kevin Indig

**Key Takeaway:** Distribution in the AI search era is not about reach for its own sake. It is about occupying more of the retrieval surface that AI models draw from when constructing answers. Every additional crawl point is a potential citation point, and freshness is not optional.


## Stage 08: Measurement and Iteration

**Objective:** Track performance against the metrics that actually reflect AI-era visibility, and use that data to drive the next content cycle rather than treating measurement as a retrospective exercise.

**Activities:**
- Track AI mention frequency, citation rate, average mention position, and sentiment across ChatGPT, Perplexity, Gemini, and Google AI Overviews separately rather than averaging them together
- Run each tracked prompt five times per platform per week to account for the inherent variability in AI outputs; a single data point is not reliable
- Monitor the "impressions up, clicks down" pattern in Search Console as an indicator of AI Overview displacement, but do not assume it automatically signals a revenue problem
- Use leading indicators over longer time horizons (six to twelve months) rather than chasing linear attribution; the classic search-click-convert funnel is broken for AI-influenced buying journeys
- Track brand-versus-competitor share of voice across AI platforms as a primary competitive metric
- Segment visibility data by buyer persona since a CFO and a marketing manager evaluating the same product category may be served very different AI responses
- Use the data from each measurement cycle to update the opportunity discovery inputs for the next cycle, closing the loop between measurement and production

**Common Tools:** SE Ranking, Ahrefs (Brand Radar), Clearscope 2.0, Surfer AI Tracker, Profound, Peak, SimilarWeb, Google Search Console, Data for SEO

**Experts Referenced:** Kevin Indig, Olga Zarr

**Key Takeaway:** Measurement in the AI era is not about proving that content worked. It is about generating a clean signal for where to focus next. The brands that iterate fastest are the ones that have built measurement systems capable of feeding directly back into production decisions.


## Framework Summary

STAGE 01: Opportunity Discovery

- Map demand across Google + AI platforms

STAGE 02: Topic and Entity Research

- Build entity graphs and topical authority

STAGE 03: Content Brief Creation

- Translate research into machine-ready briefs

STAGE 04: AI-Assisted Content Generation

- Human-first drafting with AI to sharpen

STAGE 05: Verification and Citation Review

- Fact-check, cite, close the gap to sources

STAGE 06: GEO and AEO Optimization

- Structure for AI extraction and trust

STAGE 07: Distribution

- Repurpose across all AI-weighted platforms

STAGE 08: Measurement and Iteration

- Track AI visibility, feed back into Stage 1

Each stage feeds the next, and Stage 8 feeds back into Stage 1. The loop does not close at publication; it closes when measurement data actively shapes the next round of opportunity discovery.