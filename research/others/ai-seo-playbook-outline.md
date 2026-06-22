# AI SEO Playbook Outline

## Introduction

This playbook translates the expert content, video transcripts, LinkedIn posts, and commentary from ten leading AI SEO practitioners into an operational guide built for real-world use. It is designed to serve as the foundation for an enterprise-grade AI SEO operating manual: something a content team, an agency, or a growth function can actually run from.

The ten practitioners whose work underpins this guide are Kevin Indig, Eric Siu, Nathan Gotch, Koray Tugberk Gübür, Dan Petrovic, Bernard Huang, Michał Suski, Britney Muller, Lily Ray, and Olga Zarr. Their combined output represents the most credible practitioner-level thinking currently available on AI-powered SEO content production.

The chapters that follow move from foundational understanding through to advanced measurement and automation. They are designed to be read in sequence for teams new to AI search, or used as standalone reference chapters for teams already operating in this space.


## Chapter 01: Understanding the New Search Landscape

### What This Chapter Covers

Before any operational work can be done, a team needs a clear, accurate picture of how search has actually changed and where the real disruption is coming from. This chapter cuts through the hype to establish what is measurably different, what remains the same, and what that means for a content production operation.

### Sub-Topics

**Traditional SEO vs GEO and AEO**
The terms GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) describe real phenomena, but the evidence suggests they are largely extensions of traditional SEO rather than replacements for it. Olga Zarr's data puts it directly: approximately 90% of what practitioners call AI SEO is traditional SEO done correctly. The remaining 10% covers genuine differences in how content needs to be structured for machine extraction, how citations work differently from backlinks, and how brand mentions have taken on a new weight that did not exist in classic search.

**AI Overviews as the Primary Disruption**
The real disruption in search is not ChatGPT. It is Google's AI Overviews, which now appear in over 50% of searches and have been documented reducing organic click-through rates by between 18% and 64% depending on the query. AI Overviews are not a separate channel; they sit directly inside the Google interface most users have not left. Understanding how they select sources and how they handle different query types is the most immediately practical area of focus for most SEO operations.

**LLM-Based Search Behaviors**
LLMs do not rank content the way search engines do. They are probabilistic next-word predictors that retain patterns of brand mention frequency from training data, without tracking which specific URL any piece of content came from. This means domain authority as a concept does not transfer cleanly into LLM behavior. What matters instead is how frequently and in what context a brand is mentioned across the web, and whether the sources doing the mentioning are the same ones AI models draw from when grounding their answers.

**The Correlation Question**
Perplexity citation patterns are nearly 1:1 correlated with traditional Google rankings; Perplexity is essentially a Google derivative. ChatGPT shows close to zero correlation with Google rankings, drawing more heavily from sources like Brave. This means "rank well on Google and you'll do well on AI" is only true for some AI platforms and false for others. A team needs to know which platform their audience uses and optimize accordingly.

**How Much AI Traffic Actually Is**
LLM referral traffic currently represents roughly 1% to 2% of total traffic for most sites, compared to 30% to 50% from organic search. The industry is giving AI search 10 to 100 times more attention than its actual current usage justifies, according to Rand Fishkin's data. That does not mean it should be ignored; it means the investment level should be calibrated to where the traffic actually is today, with a longer time horizon built in.

**Primary Experts:** Bernard Huang, Lily Ray, Kevin Indig, Olga Zarr, Britney Muller


## Chapter 02: Topic Discovery and Research

### What This Chapter Covers

Topic discovery in the AI era requires two separate research tracks: one for traditional search demand and one for AI citation demand. This chapter covers both, including how to design a rigorous prompt tracking panel, how to identify where AI is already citing sources in your category, and how to use that data to prioritize content investment.

### Sub-Topics

**Intent Modeling Across Platforms**
Search intent still governs content strategy, but the intent signals available have expanded. Traditional intent (informational, navigational, commercial, transactional) still applies to Google. AI platforms show a different pattern: problem-focused queries carry the highest purchase intent signal and are where AI citations have the most commercial value. Designing your research around that distinction changes which opportunities get prioritized.

**Prompt Panel Design**
A rigorous AI visibility tracking panel starts with roughly 40 seed prompts split across brand queries (12), category queries (12), and problem-focused queries (16). Each prompt should be run five times per platform per week. ChatGPT, Perplexity, Gemini, and Google AI Overviews should be scored separately; averaging them together hides meaningful differences in which brands each platform favors. Results should be segmented by buyer persona, since a CFO and a marketing buyer evaluating the same product category may see very different AI responses.

**Opportunity Discovery at Scale**
The fastest way to find high-value AI content opportunities is to extract the citation URLs for your core commercial keywords from all major AI platforms, then treat that list as a prioritized research set. The pages on that list are the ones an AI model is already reading when it answers questions in your category. If your brand is not mentioned on those pages, that is the gap. If your brand is mentioned but your own domain is not being cited, that tells you something different: that third-party coverage is driving AI visibility more than owned content.

**Competitive Gap Analysis**
Running competitor content through an AI model with a direct instruction to identify topic gaps is faster and more comprehensive than manual analysis. This should be done at the beginning of any new content program and repeated quarterly. The output feeds directly into the content brief creation stage.

**Trend Velocity**
Content freshness is not optional in the AI era. Approximately 95% of AI citations pull from content published within the last ten months. A topic research system needs to include a freshness signal that flags when existing content is aging out of the citation window and needs to be updated or replaced.

**Primary Experts:** Kevin Indig, Eric Siu, Nathan Gotch


## Chapter 03: Semantic SEO and Topical Authority

### What This Chapter Covers

Topical authority is not just about publishing a lot of content on a subject. It is about building a structured, semantically complete coverage of a topic space that search engines and AI models can recognize as authoritative. This chapter covers the technical and strategic foundations of that work.

### Sub-Topics

**Entity Graphs and Knowledge Mapping**
Every topic area can be mapped as a network of entities, the relationships between them, and the specific attribute-value pairs that define each entity. Content that supplies named, specific values (not vague claims) aligns with the "consensus" that search engines try to detect. Content that leaves attribute values unspecified or implied gets passed over in favor of content that makes the relationship explicit.

**The Topical Authority Formula**
Koray Tugberk Gübür's core formula frames topical authority as topical coverage multiplied by historical data, divided by cost of retrieval. Each variable is actionable: coverage means the breadth of entities and sub-topics addressed; historical data means the age and consistency of the content record on a site; cost of retrieval means how cheaply and quickly a model can extract a useful answer from any given page.

**Topical Map Architecture**
A well-structured topical map splits into two sections. The core section focuses directly on monetization: the commercial queries, product category pages, and comparison content that drives revenue. The outer section builds authority through location-agnostic, context-rich content that does not target commercial queries directly but feeds trust and relevance signals back into the core. Sites should be made ready approximately 20 days before an anticipated Google core update to maximize the chance of being re-evaluated.

**Source Context**
Search engines cluster competing sites by source type before ranking within each cluster. An affiliate site competes with other affiliates; a brand site competes with other brand sites; a publisher competes with other publishers. Content strategy needs to account for which source type already dominates a given query and whether it is realistic to compete in that context or whether a different query cluster is more accessible.

**Programmatic Topical Clustering**
At scale, topical maps need to be built and maintained programmatically. This means defining the entity structure, generating the sub-topic clusters, and mapping content to gaps algorithmically rather than by hand. AI tools can accelerate this work significantly, but the entity taxonomy needs to be defined by a human who understands the domain.

**Query Fan-Out**
A single user query gets reformulated internally by search engines and AI models into roughly 100 different variations before an answer is constructed. Understanding the fan-out pattern for your target queries tells you which sub-topics and related entities need to be covered for a piece of content to remain relevant across the full range of query variations a user might enter.

**Primary Experts:** Koray Tugberk Gübür, Dan Petrovic


## Chapter 04: AI-Powered Content Planning

### What This Chapter Covers

A content brief in the AI era carries more responsibility than it used to. It needs to specify not just what to write but how to structure the writing so that both human readers and machine retrievers can extract value from it. This chapter covers the components of a modern brief and the planning systems that make brief production scalable.

### Sub-Topics

**The Three-Layer Brief**
An effective AI-era brief layers three types of input. The data layer pulls from Search Console, GA4, and AI rank tracking to establish the demand context. The company knowledge layer adds product information, FAQs, and anything that makes the content specific to the brand rather than generic. The expertise layer adds original insight: founder commentary, proprietary data, user research, or anything that cannot be replicated by a competitor running the same AI tool with the same prompt.

**Semantic Brief Structure**
Keywords need to be assigned to specific headings rather than distributed loosely across a piece. Each section should be planned to answer a specific question completely and independently, so that a model extracting that section in isolation can still provide a useful answer. FAQ architecture should be treated as a structural requirement in the brief, not an afterthought.

**Programmatic Intent Mapping**
At scale, brief creation needs to be partially automated. This means building a system that takes a target query, runs the discovery and gap analysis steps programmatically, and produces a structured brief template that writers or AI tools can work from. The brief template should include the target entity, the required attribute-value pairs, the intent at each heading level, and the information retrieval cost target for the finished piece.

**Information Retrieval Cost as a Planning Constraint**
Michał Suski's concept of information retrieval cost (how cheaply and quickly an AI can extract an answer from a page) should be built into brief planning as an explicit constraint. A brief should specify that the finished content needs to be structured so that a model can extract a complete, accurate answer from any individual section without reading the full piece. This drives decisions about heading structure, sentence density, and the use of lists and tables.

**Automated FAQ Architecture**
FAQ sections are not just a schema markup opportunity; they are an AI extraction optimization. They should be built around the actual questions users ask across the full query fan-out for the target topic, not just the obvious head-term questions. Building these programmatically from search data and AI platform query analysis produces better coverage at lower cost than manual research.

**Primary Experts:** Bernard Huang, Michał Suski


## Chapter 05: AI Content Production

### What This Chapter Covers

AI content production is not a prompt-and-publish workflow. The practitioners producing the most durable, citation-worthy content are using AI as one step in a multi-stage production process that keeps human judgment central. This chapter covers how to design that process and how to avoid the most common failure modes.

### Sub-Topics

**The Right Sequence**
The most important structural principle in AI content production is sequence: write a human-authored outline or first draft before involving an AI tool. AI performs significantly better as a sharpening and expansion tool than as a starting point. When AI generates first, the output tends to produce the statistical average of what has already been written on the topic. When a human generates first and AI refines, the output is more distinctive and more likely to contain the kind of original framing that AI models cite.

**Prompt Engineering Loops**
Effective AI content production uses multi-step prompt loops rather than single prompts. A typical loop moves through: brief input, outline generation, section-by-section expansion, gap identification, revision pass, and final formatting. Each step uses a different prompt optimized for that specific task. Few-shot prompting with real brand examples produces more consistent voice alignment than generic instructions.

**Human-in-the-Loop Quality Metrics**
Every piece of AI-assisted content should pass through a mandatory human review focused on four criteria: factual accuracy (every specific claim verified against a primary source), brand voice consistency (does it sound like the brand or like a generic AI), internal link quality (are the right links present and correctly placed), and potential harm (could any claim mislead a reader or cause a consequence if wrong). These four criteria should be built into the production workflow as a gate, not a suggestion.

**Pre-Automation Gut-Check**
Before any content type enters an automated publishing pipeline, it needs to pass a gut-check: could a mistake in this content harm someone, damage the brand, or cause a real consequence? This is especially important for medical, financial, legal, or safety-adjacent topics. Automating content production in high-stakes categories without this check is one of the fastest ways to create a liability.

**Avoiding AI Slop**
Google's systems are already capable of identifying low-quality AI-generated content at scale. The January 2026 update specifically penalized sites that had scaled self-promotional AI-generated listicles. The practical implication is that AI-assisted content needs to contain something a model could not have generated on its own: original data, a specific client example, a named statistic from primary research, or an expert perspective that adds genuine information value.

**Multi-Step Agent Workflows for Scale**
For teams producing at volume, AI agent workflows can run content research, outline generation, and schema planning in parallel rather than sequentially. Eric Siu's architecture for compressing an 80-minute podcast into 35+ pieces of repurposed content demonstrates what is possible when the workflow is designed as a parallel system rather than a linear one.

**Primary Experts:** Britney Muller, Eric Siu


## Chapter 06: Citation and Trust Building

### What This Chapter Covers

Being cited by an AI model is not primarily a function of having great content. It is a function of being mentioned by the sources that AI models already trust and draw from. This chapter covers how to identify those sources, how to earn placement on them, and how to use citation data to prioritize outreach.

### Sub-Topics

**Source Verification and Citation Mining**
The starting point for any citation-building program is extracting the full citation set for your target commercial queries across all major AI platforms. The resulting list of URLs is a prioritized prospect list. The highest-frequency cited domains are the highest-leverage outreach targets. This is more actionable than general link-building because it is based on what AI models are actually reading when they answer questions in your category, not what general SEO metrics suggest is authoritative.

**The Consideration Set vs the Selected Set**
Dan Petrovic's framework for measuring AI visibility distinguishes between the consideration set (all pages a model could have cited when answering a query) and the selected set (the pages it actually cited). The gap between them is where optimization effort should be concentrated. A brand that appears in the consideration set but not the selected set has a different problem than a brand that does not appear at all, and the fix is different in each case.

**Unlinked Mentions and AI Trust**
Seventy-two percent of the brand mentions that drive AI citation outcomes are unlinked. Links, nofollow tags, and sponsored designations appear to make no measurable difference to AI citation influence. This changes the calculus of earned media investment: the goal is to be mentioned on the right pages, not to secure followed links from them. Paid sponsorships on high-frequency cited publications appear to be as effective as organic editorial mentions.

**Programmatic E-E-A-T Workflows**
E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness) need to be built into content production as a systematic workflow, not added as an afterthought. This means named authors with verifiable credentials on every piece, publication dates maintained and updated, statistics sourced to primary research rather than secondary summaries, and clear disclosure of methodology when original data is presented.

**Third-Party Coverage as the Primary Trust Signal**
Kevin Indig's point is direct: a brand's own blog is one of the weakest trust signals available to AI models, because the model has no reason to take a brand at its word about its own authority. Third-party mentions from publications, analysts, and even competitors carry more weight precisely because they are not self-interested. The practical implication is that owned content and earned coverage should be treated as separate programs, with earned coverage taking priority for AI citation objectives.

**What to Avoid**
Prompt injection attacks through "summarize with AI" page features have already been publicly called out as spam by both Microsoft and Google. Self-promotional comparison and alternative pages are on enforcement radar following the January 2026 update. Any tactic that works by manipulating the AI's outputs rather than earning its trust is a short-term approach with a documented and growing enforcement trajectory.

**Primary Experts:** Dan Petrovic, Lily Ray


## Chapter 07: GEO and AEO Optimization

### What This Chapter Covers

GEO and AEO are optimization disciplines focused specifically on inclusion in AI-generated answers. This chapter covers the tactical and structural changes that make content more likely to be cited, and how to think about the relationship between traditional SEO health and AI search visibility.

### Sub-Topics

**Brand Mention Velocity**
AI models learn brand associations through the frequency and context of mentions across their training data. Brand mention velocity (the rate at which a brand is being mentioned across high-quality, AI-indexed sources) is a leading indicator of future AI citation frequency. A brand that is being consistently mentioned in the right sources today is building the AI visibility it will benefit from in the next training cycle.

**Format Structuring for Citation**
Content structured for AI extraction has specific formatting characteristics: short, complete, self-contained paragraphs at the section level; explicit question-and-answer formatting where appropriate; named entities and specific values rather than vague claims; and data tables and structured lists used for information that would otherwise require reading multiple sentences to extract. The goal is to minimize the cognitive load on the model extracting the answer.

**Optimization for LLM Context Windows**
AI models have context window constraints that affect which sections of a long piece are most likely to be processed and cited. Content at the beginning and end of a document is more reliably processed than content buried in the middle. The most critical information (the specific claim, statistic, or definition most likely to be cited) should appear early in its section, not buried after contextual framing.

**The Grounding Layer**
Bernard Huang's three-layer model identifies the grounding layer (where the model performs live searches to validate and freshen its answer) as the fastest lever for influencing AI citations. Creating content that targets how an AI researches a topic in real time (not just what it already knows) means targeting the queries a model might run while grounding an answer, not just the queries a user would type. This requires understanding the query fan-out pattern for your target topic.

**Digital PR for AI Visibility**
The most effective digital PR strategy for AI citation is to target publications that already rank on page one of Google for your target commercial queries. These publications receive faster crawling and heavier model weighting. Earning a mention (linked or unlinked) on a page that already appears in the AI's grounding search results is the most direct path to citation influence.

**The SEO-AI Correlation**
Lily Ray's documented observation that SEO visibility losses on Google are followed by matching drops in ChatGPT citation frequency is the most practically important data point in this chapter. Traditional SEO health is a prerequisite for AI visibility, not a separate track. Tactics that damage SEO health in pursuit of AI-specific gains are likely to damage both simultaneously.

**Primary Experts:** Bernard Huang, Nathan Gotch, Lily Ray


## Chapter 08: Automation and AI Agents

### What This Chapter Covers

AI agents represent the most significant operational change available to content teams right now. This chapter covers how to design agent workflows for content production, how to build multi-agent systems that run at scale, and how to avoid the failure modes that come with over-automation.

### Sub-Topics

**Agentic Research Workflows**
The first and most immediately valuable application of AI agents in content production is research: extracting citation sets, running gap analyses, pulling competitor data, and generating prompt panels. These tasks are repetitive, time-consuming when done manually, and well-suited to agentic automation because the failure modes (missing a citation, misidentifying a gap) are recoverable. Research agent workflows should be the first automation built in any content operation.

**Multi-Agent Writing Pipelines**
At the production level, multi-agent systems can run content generation, schema markup planning, internal linking, and distribution asset creation in parallel. Eric Siu's "fleet commander" architecture (a central coordinating agent managing specialist sub-agents per function) is the clearest operational model for how this works at agency scale. The human role in this architecture is to manage the system and review outputs, not to execute tasks inside the pipeline.

**The Three Levels of AI Adoption**
Eric Siu's three-tier maturity model is a useful benchmark. Level one (manually prompting AI tools) provides no competitive advantage since it is available to everyone. Level two (specialist agents handling defined end-to-end workflows with human review) is where operational advantage begins. Level three (multiple agent workflows stacked into loops managed by one person) is where the organizational structure itself changes. Most teams are at level one; the operational priority is to move to level two.

**Custom GPT Auditing**
AI models can be used to audit their own outputs: identifying factual errors, checking for tone consistency, flagging claims that need source verification, and assessing information retrieval cost. Building a custom auditing step into the production pipeline using an AI tool is faster than manual review for most quality dimensions and catches a higher proportion of systematic errors.

**Human-in-the-Loop as a Design Principle**
The practitioners running the most effective AI-powered content operations are not trying to remove humans from the loop. They are designing workflows that put humans at the points where judgment matters most: initial brief creation, final fact-checking, tone calibration, and strategic prioritization. The goal is not full automation; it is compression of the time between decision and output while maintaining the quality controls that make the output trustworthy.

**Avoiding AI Theater**
Approximately 9% of enterprises are genuinely scaling with AI. The rest are in what Eric Siu calls "AI theater": announcing AI adoption without building the workflows that make it operational. The distinction is measurable: an AI-powered content operation produces more output at higher consistency with fewer human hours per piece. If those metrics are not improving, the AI investment is cosmetic.

**Primary Experts:** Eric Siu, Kevin Indig


## Chapter 09: Measurement and Performance Tracking

### What This Chapter Covers

Measurement in the AI era requires a different set of metrics, a longer time horizon, and a fundamentally different relationship between traffic and revenue than traditional SEO analytics assumed. This chapter covers what to measure, how to measure it, and how to interpret the results in a way that actually informs production decisions.

### Sub-Topics

**GEO Share-of-Voice KPIs**
The primary competitive metric in AI search is share of voice: what percentage of AI-generated answers in your category mention your brand, and how does that compare to competitors. This should be tracked separately per platform, per persona, and per query type. Aggregating across these dimensions produces a number that looks clean but hides the specific weaknesses and strengths that actually drive decisions.

**LLM Inclusion Metrics**
The recommended metric set for AI visibility tracking includes mention rate (how often the brand appears in responses), citation rate (how often the brand's own domain is linked), average mention position, sentiment (what attributes are associated with the brand when it is mentioned), and confidence (how certain the model appears when making claims about the brand). All of these should be reported with confidence intervals derived from running each prompt multiple times.

**The Impressions-Up, Clicks-Down Pattern**
The pattern of rising impressions paired with flat or declining clicks is now well-documented and directly attributable to AI Overviews answering queries completely enough that users do not click through. The important caveat, demonstrated by Olga Zarr's client data, is that this pattern does not automatically translate into revenue decline. Measurement needs to extend downstream to actual business outcomes rather than stopping at traffic.

**Attribution in the AI Era**
Kevin Indig's "great decoupling" describes the structural breakdown of the traditional search-click-convert attribution model. Users are increasingly researching inside AI interfaces and converting later through a different channel, with no traceable click path connecting the two events. Traditional attribution models systematically undercount the revenue contribution of content that influences AI-mediated research journeys. The practical fix is to shift measurement toward leading indicators (brand search volume, direct traffic to key pages, AI mention frequency) tracked over longer time horizons rather than trying to attribute revenue to specific content pieces.

**Classic vs Modern Funnel**
The classic SEO funnel (search, click, convert) still applies to a meaningful proportion of search journeys, particularly for transactional and navigational queries where users have high intent and want to go directly to a destination. The modern funnel adds a research phase that happens increasingly inside AI interfaces, producing a converted user who arrives through a channel (direct, branded search, referral) that gives no credit to the content that influenced the decision. Both funnels are real and both need to be measured.

**Measurement Cadence and Feedback Loops**
Prompt panels should be run weekly. AI visibility reports should be produced monthly. Strategy reviews should happen quarterly and should explicitly feed measurement findings back into the opportunity discovery stage. The value of measurement is proportional to how directly it drives the next production cycle. Measurement that produces a report but does not change the content plan is not serving its purpose.

**Primary Experts:** Olga Zarr, Kevin Indig


## Future Expansion Opportunities

The following areas represent the cutting edge of where AI-powered SEO content production is heading. Each represents a meaningful investment opportunity for teams that have the foundational chapters of this playbook operational.

- **AI Content Auditing at Scale:** Building automated pipelines that assess existing content libraries against current AI citation patterns, identifying which pages are underperforming relative to their topical coverage and flagging them for update or consolidation. The tooling for this is early but the methodology is well-established.

- **AI Search Analytics Infrastructure:** Most teams are still measuring AI visibility through manual prompt runs and spreadsheet tracking. The next infrastructure layer involves building dedicated analytics pipelines that automate prompt execution, aggregate results across platforms, and feed structured visibility data into existing BI tooling.

- **Retrieval-Augmented Generation (RAG) Optimization:** As more enterprises deploy RAG-based internal and customer-facing AI tools, the question of which content gets retrieved becomes a product question, not just an SEO question. Optimizing content for retrieval in RAG systems requires understanding the chunking, embedding, and retrieval logic of the specific system in use, which is a more technical problem than traditional SEO but builds on the same foundations.

- **Knowledge Graph Optimization:** Google's Knowledge Graph and the entity databases underpinning AI model training are becoming important optimization targets in their own right. Ensuring that a brand's entity is correctly defined, associated with the right attributes, and distinguished from similar entities is work that sits between traditional SEO and structured data engineering.

- **Multi-Agent Content Ecosystems:** The most advanced content operations being built right now are not producing individual pieces; they are building systems that produce, distribute, monitor, and iterate content continuously with minimal human intervention per cycle. Designing the architecture for a content ecosystem of this kind (agent roles, handoff logic, quality gates, feedback loops) is the most complex and highest-leverage investment available to teams that have the foundational infrastructure in place.