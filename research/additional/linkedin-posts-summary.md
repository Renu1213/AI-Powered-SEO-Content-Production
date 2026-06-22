# LinkedIn Posts and Key Insights from Experts

---

## Expert: Dan Petrovic

### POST 01:

Title: Past, Present, and Future of AI SEO (Part 1)

Link: https://www.linkedin.com/posts/seoguy_1-past-present-and-future-of-ai-seo-2-activity-7407253126552092672-6CFY/

Date: ~6 months before collection (≈Dec 2025)

Summary: Dan opens this three-part series by pointing back to an article he wrote in 2013 predicting Google would eventually become a conversational assistant, which he argues is essentially what happened with Gemini. He traces the real evolutionary arc from TF-IDF and PageRank through to Transformers, noting that GPT's original architecture choices (12 layers, 768 dimensions) came from one researcher's hardware constraints, not deliberate design, and that Google copied those same numbers assuming there was intent behind them. His core point is humbling: nobody, including the people who built these models, fully understands why they behave the way they do. He trained his own small language model from scratch, including a custom tokenizer, specifically to understand the mechanics rather than take anyone's word for it.

Key Insights:
- Dan predicted a Google-as-chatbot future in 2013, well before anyone else was talking about it
- GPT's foundational architecture choices were arbitrary engineering shortcuts, not deliberate design, and Google copied them anyway
- He frames mechanistic interpretability as the new core discipline for understanding what these models actually do, since their own builders don't fully know either
- He trained his own language model entirely from scratch to earn the right to speak credibly about how these systems work

---

### POST 02:

Title: AI SEO Part 2: Model Attention and Primary Bias

Link: https://www.linkedin.com/posts/seoguy_ai-seo-part-2-1-model-attention-primary-activity-7407534293498900481-uRN4/

Date: ~6 months before collection (≈Dec 2025)

Summary: This is the technical core of Dan's series. He introduces two original concepts: "selection rate," the machine equivalent of click-through rate, and "primary bias," meaning what a model already believes about a brand before it runs any grounding search. He walks through how attention patterns inside a transformer drive token weighting, and shows a method for measuring a model's opinion of a brand over time by comparing mention frequency against ranking position to produce a weighted visibility score. He also covers probing model confidence at the token level to find the exact moments where a model is uncertain about a brand, since those are the spots most worth optimizing.

Key Insights:
- "Selection rate" is proposed as the direct machine-era analog to click-through rate, measuring how often a model chooses to cite a brand
- "Primary bias" describes what a model believes about a brand before any grounding search runs, separate from what it says after grounding
- A simple structured prompt repeated over time (asking a model to list brands in a category) can produce a trackable visibility score combining mention frequency and position
- Token-level confidence analysis can reveal exactly where a model is uncertain about a brand, pinpointing what content needs to be created or fixed
- This tracking framework is available free through his own tool, Diane AI

---

### POST 03:

Title: AI SEO Part 3: Automated Citation Mining

Link: https://www.linkedin.com/posts/seoguy_ai-seo-part-3-1-automated-citation-mining-activity-7407969688003104769-GvI2/

Date: ~6 months before collection (≈Dec 2025)

Summary: The final part closes the loop Dan opened in Parts 1 and 2, walking through a full automated pipeline: define brand entities, auto-generate dozens or hundreds of prompts around those entities, run them against AI platforms, then mine and analyze the resulting citations at scale. He argues that seeing what a model considered but didn't cite is just as valuable as what it did cite, since that gap is exactly where targeted content work should go. He closes by listing a substantial stack of free tools he built for this purpose, covering citation mining, AI content detection, and a tool called Tree Walker for finding high and low confidence points in model output.

Key Insights:
- A real end-to-end pipeline is described: entities → auto-generated prompts → API querying → citation parsing → prioritized action
- What a model considered but chose not to cite is treated as equally valuable data to what it did cite
- The optimization cycle he proposes is: collect data, analyze, then prioritize effort specifically where a brand's perception is weakest
- He's built and made freely available a substantial toolkit covering citation mining, query fan-out generation, AI content detection, brand sentiment scoring, and more

---

## Expert: Bernard Huang

Title: When Kevin, Su, and I First Started Building

Link: https://www.linkedin.com/posts/bernardjhuang_when-kevin-su-and-i-first-started-building-activity-7379157060388794368-2CyN/

Date: ~8 months before collection (≈Oct 2025)

Summary: A reflective post marking Clearscope's largest update to date. Bernard looks back nine years to when he and Kevin Su started the company out of borrowed desk space, trying to answer one question: how do you know if content is actually good before you publish it. He frames Clearscope 2.0 as a direct response to search no longer being just search, now including AI chatbots and generative summaries, and outlines the new features: topic exploration for authority mapping, AI visibility tracking across Gemini and GPT, AI-assisted drafting in the brand's own voice, and a lower price point.

Key Insights:
- Clearscope 2.0 is positioned as a full discoverability platform, not just a content optimization tool
- The new feature set targets AI-era needs directly: AI visibility tracking, topic and authority mapping, and AI-assisted drafting that preserves brand voice
- Bernard frames the company's mission as unchanged across nine years: getting brands discovered, regardless of whether people are searching through Google, ChatGPT, or whatever comes next

---

## Expert: Britney Muller

### POST 01:

Title: AI Cheatsheet for Marketers 2026

Link: https://www.linkedin.com/posts/britneymuller_ai-cheatsheet-for-marketers-2026-orange-labs-activity-7444766189719052288-2DND/

Date: ~2 months before collection (≈April 2026)

Summary: One of the most practically dense posts in the research set. Britney leads with what she calls Rule #0: you need to be able to state the actual problem in one clear sentence before involving AI at all. From there she covers few-shot prompting, building a real brand-mentions strategy (noting Reddit accounts for roughly 24% of all Perplexity citations), gut-checking before automating anything with real consequences, writing your own draft before handing it to AI rather than starting with AI output, and treating a fast imperfect first version as better than a slow perfect one.

Key Insights:
- Reddit alone drives roughly 24% of all Perplexity citations, a specific benchmark worth tracking
- "Brand mentions are the new backlinks," and most brands are still only posting to their own feed and wondering why AI search ignores them
- Recommended sequence: write your own draft first, then hand it to AI to sharpen, because AI tends to produce "the average of everything it's seen"
- A simple gut-check before automating anything: could mistakes here harm people, damage the brand, or cause unintended consequences
- The marketers winning right now aren't avoiding mistakes; they're making them faster than everyone else

---

### POST 02:

Title: The AI Search Gold Rush: What's Real vs What's Hype

Link: https://www.linkedin.com/posts/britneymuller_the-ai-search-gold-rush-whats-real-vs-whats-activity-7449472539904458752-TV7-/

Date: ~2 months before collection (≈April 2026)

Summary: Britney shares and summarizes a deeply reported Verge piece she describes as one of the most balanced pieces of journalism on AI search, neither hyping nor dismissing what's actually happening. She pulls out several grounded, skeptical points: that gamed "best of" listicles are an information-retrieval problem rather than something unique to AI, that anyone promising guaranteed influence over AI answers is overselling, and that PR and earned media budgets are predicted by Gartner to double by 2027 specifically because third-party mentions are mattering more.

Key Insights:
- Gartner predicts PR and earned media budgets will double by 2027, driven by the rising importance of third-party brand mentions in AI answers
- Anyone claiming guaranteed ability to influence AI results is flagged directly as overselling, since the AI and search companies themselves are still figuring this out
- Rand Fishkin's point is highlighted: AI search is getting 10 to 100 times more industry attention than its actual current usage justifies
- SparkToro data shows Amazon, Bing, and YouTube each currently drive more desktop search activity than ChatGPT
- Brands succeeding in AI search aren't abandoning traditional SEO basics; they're doing them better

---

## Expert: Eric Siu

### POST 01:

Title: There Are 3 Levels to How Teams Are Using AI

Link: https://www.linkedin.com/posts/ericosiu_there-are-3-levels-to-how-teams-are-using-activity-7471958389653274624-z1ZE/

Date: ~1 week before collection (≈June 2026)

Summary: Eric lays out a three-tier maturity model for how companies actually use AI. Level one is manually going back and forth with ChatGPT or Claude, useful but not a real competitive advantage since everyone has the same access. Level two is where specialist agents handle defined end-to-end workflows with a human reviewing output. Level three involves stacking multiple agent workflows into loops managed by a single person, which he calls the org chart of the future.

Key Insights:
- Level 1 (manually chatting with AI tools) is not a competitive advantage since it's available to everyone equally
- The real shift happens at Level 2: building actual end-to-end workflows with a defined human input step, AI processing step, and human review step
- Level 3 involves stacking multiple specialist agents (SEO, CRO, paid media, ad creative) into loops managed by one person at the top
- His framing of the future org chart is direct: humans managing systems, not executing tasks inside them

---

### POST 02:

Title: Highest Leverage Claude Code Dynamic Workflow

Link: https://www.linkedin.com/posts/ericosiu_highest-leverage-claude-code-dynamic-workflow-activity-7466843524991401984-EPk1/

Date: ~3 weeks before collection (≈June 2026)

Summary: A practical post sharing four full Claude Code workflow prompts aimed at revenue generation: a "Revenue Command Center" that pulls together available data sources to surface ranked opportunities, a "Stalled Revenue Recovery" prompt that mines old sales history for forgotten deals, a "Client Expansion Engine" for finding upsell opportunities account by account, and a "Churn Prevention" workflow that scores accounts by risk and drafts save plans. Each prompt is written out in full, specific enough to run as-is rather than just described in the abstract.

Key Insights:
- All four prompts are complete, ready-to-use Claude Code workflows, not vague suggestions
- The "Revenue Command Center" prompt asks the AI to ingest CRM exports, call transcripts, emails, analytics, and internal docs simultaneously to find where revenue is being created, delayed, or lost
- Each workflow ends with concrete deliverables (ranked opportunity lists, draft emails, execution plans) rather than just analysis
- The included meta-prompt for building full context first, then spawning parallel specialist subagents and synthesizing, is a useful pattern in itself

---

## Expert: Kevin Indig

### POST 01:

Title: Good Prompt Tracking Starts With Sample Design

Link: https://www.linkedin.com/posts/kevinindig_good-prompt-tracking-starts-with-sample-design-activity-7470197035565002752-T8ow/

Date: ~1 week before collection (≈June 2026)

Summary: A methodology-focused post on how to design a rigorous AI visibility tracking panel rather than running a handful of random prompts. For a typical B2B SaaS CRM category, Kevin recommends starting with around 40 seed prompts split across brand, category, and problem-focused queries, since purchase intent tends to concentrate in the problem prompts. He stresses running each prompt multiple times per week per platform, scoring each AI engine separately rather than averaging them together, and segmenting by buyer persona since different roles evaluate the same category by different criteria.

Key Insights:
- Recommended starting sample: roughly 40 seed prompts split 12 brand / 12 category / 16 problem-focused, since problem prompts are where purchase intent concentrates
- Each prompt should run 5 times per platform per week, with ChatGPT, Perplexity, Gemini, and Google AI Overviews scored separately rather than aggregated
- Persona segmentation matters: a CFO, an IT buyer, and a marketing buyer evaluate the same product category differently, and averaging their results hides where a brand actually wins or loses
- Recommended metrics: mention rate, citation rate, average position, sentiment, and the specific attributes attached to each mention, all reported with confidence intervals

---

### POST 02:

Title: Two Brands Can Run Identical Optimization

Link: https://www.linkedin.com/posts/kevinindig_two-brands-can-run-identical-on-page-optimization-activity-7473336241837731841-Dl3f/

Date: 3 days before collection (≈June 2026)

Summary: A focused post arguing that on-page optimization alone can't explain why two equally well-optimized brands get cited by AI at very different rates. Kevin's explanation is that AI reuses trust already attached to the sources it pulls from, and favors entities it already recognizes for a given topic rather than forming a fresh opinion each time. A brand's own blog is one of the weaker trust signals available, since a model has no particular reason to take a brand at its word. Third-party publications, analysts, and even competitors mentioning the brand carry more weight precisely because they're not self-interested.

Key Insights:
- With on-page optimization held roughly equal, the brand that wins AI citations is the one already trusted through outside sources, not the one with the better-optimized page
- A brand's own blog is explicitly one of the weaker inputs to AI trust, since the model has no reason to take a brand's self-description at face value
- Third-party mentions from publications, analysts, and even competitors carry more AI trust weight because they're not self-interested
- Practical first step: check which sources AI actually cites in your category and whether any of them mention you at all, before doing more on-page tuning

---

## Expert: Koray Tugberk Gübür

Title: Good News for SEOs: Google Is Bringing Generative AI

Link: https://www.linkedin.com/posts/koray-tugberk-gubur_good-news-for-seos-google-is-bringing-generative-activity-7467874512357797888-FXPW/

Date: ~2 weeks before collection (≈June 2026)

Summary: Koray reacts to Google's announcement of Generative AI Performance reporting inside Search Console, which separates traditional web-result impressions from AI-result impressions for the first time. While the data is currently limited to impression-level reporting, he outlines several new analytical comparisons this unlocks: crawl stats against AI appearances, content freshness and sentence structure against AI visibility, and AI performance against average ranking position for commercial queries. His closing point reframes the goal: AI visibility isn't just about being mentioned, it's about understanding why, when, and through which signals a source actually gets selected.

Key Insights:
- Google's new Search Console reporting separates traditional and AI-result impressions for the first time, opening new analysis even though it's currently impression-level only
- New comparison angles become possible: crawl stats vs. AI appearances, content freshness vs. AI visibility, free-tool content vs. broader topical relevance
- The real goal is understanding the why behind AI selection (semantic, technical, and behavioral signals), not just tracking whether a brand got mentioned at all

---

## Expert: Lily Ray

### POST 01:

Title: The Worst Thing You Can Do for Your AI Search Strategy

Link: https://www.linkedin.com/posts/lily-ray-44755615_the-worst-thing-you-can-do-for-your-ai-search-activity-7467554630458093568-81Xg/

Date: ~2 weeks before collection (≈June 2026)

Summary: Lily makes a direct, well-evidenced argument that the worst move for AI search visibility is damaging your underlying SEO. She points to dozens of documented cases of sites losing Google visibility followed shortly after by their ChatGPT citations collapsing in the same pattern. Her broader point is that many people newer to GEO don't yet have the experience to recognize when a tactic is a loophole that will eventually be treated as spam, since SEO is as much about knowing what not to do as what to do.

Key Insights:
- She's documented dozens of real cases where SEO visibility loss on Google was followed by a matching drop in ChatGPT citations; the two are tightly linked, not separate tracks
- Many GEO-specific tactics being recommended right now are flagged as bad ideas for long-term SEO health
- Years of SEO experience is what lets you recognize a "too good to be true" tactic as a loophole before it becomes a liability
- Google employees have publicly discouraged "inauthentic mentions" and other GEO manipulation tactics, signaling it's already on enforcement radar
- New research she's working on reportedly shows ChatGPT and Claude are actively taking steps to reduce spam and manipulation in their own citation behavior

---

### POST 02:

Title: Next Frontier of Spam Fighting

Link: https://www.linkedin.com/posts/lily-ray-44755615_i-think-the-next-frontier-of-spam-fighting-share-7472261352552718336-kAj-/

Date: 6 days before collection (≈June 2026)

Summary: Lily predicts that comparison and "alternative" pages (Brand X vs. Y, Product X vs. Y) are the next category likely to get hit by spam enforcement from search and AI companies. She draws a direct parallel to what she's already documented with listicles, noting that Google's product review standards technically require a brand to have genuinely tested competitors, a bar almost no company authoring comparison content has actually met. Several companies that scaled these pages into the hundreds were hit by Google's late January 2026 update.

Key Insights:
- Comparison and alternative pages are predicted as the next major spam-enforcement target, following the same pattern already seen with listicles
- Google's product review standards technically require genuine hands-on testing of competitors, a bar almost no brand comparing itself to rivals has actually met
- Real consequence cited: companies that scaled comparison pages into the hundreds were hit by Google's late January 2026 update
- Search and AI companies are expected to increasingly favor objective third-party reviews (Reddit, YouTube, Trustpilot, G2) over brand-authored comparison content
- Test and experiment, but doing this at scale inauthentically is a long-term liability, not a shortcut

---

## Expert: Michał Suski

Title: This Blew My Mind: Did You Know You Can...

Link: https://www.linkedin.com/posts/michal-suski_this-blew-my-mind-did-you-know-you-can-ugcPost-7270706278581116928-flXo/

Date: 1 year before collection (≈June 2025)

Summary: A casual, screen-recorded discovery post where Michał walks through using Surfer's guidelines directly inside ChatGPT's Canvas mode via a Chrome extension, eliminating the need to switch between tools. He demonstrates the full loop live: importing Surfer's SEO guidelines into a Canvas session, building an outline with keywords assigned to specific headings, expanding bullets into full paragraphs using remaining keywords, then pasting the finished draft back into Surfer's content editor to check the resulting optimization score.

Key Insights:
- Surfer's content guidelines can be imported directly into ChatGPT's Canvas mode via a browser extension, collapsing a multi-tool workflow into one session
- The demonstrated workflow moves outline → keyword-assigned headings → full paragraph expansion → re-import into Surfer for scoring, entirely within one continuous session
- This is a hands-on workflow demo rather than a strategic argument, most useful as a practical reference

---

## Expert: Nathan Gotch

### POST 01:

Title: AEO/GEO Is Just SEO - Watch This

Link: https://www.linkedin.com/posts/nathangotch_aeogeo-is-just-seo-watch-this-activity-7472346313221656576-JFcM/

Date: 6 days before collection (≈June 2026)

Summary: Nathan uses a Rankability feature to directly test the claim that doing well in traditional Google search guarantees doing well in AI platforms, and the results are split. Perplexity turns out to be nearly perfectly correlated with Google rankings, functioning essentially as a reverse-engineered version of Google search, while ChatGPT shows close to zero correlation with traditional rankings, instead pulling more from sources like Brave. His practical takeaway is that brands should aim to dominate a search result with multiple owned assets (website, LinkedIn, YouTube) rather than ranking one page, since occupying more retrieval points increases citation odds regardless of which platform's mechanics apply.

Key Insights:
- Perplexity citations were found to be nearly 1:1 correlated with traditional Google rankings, essentially functioning as a Google derivative
- ChatGPT showed close to zero correlation with traditional Google rankings in the same reports, pulling more heavily from sources like Brave instead
- The flat claim "if you rank well in Google you'll do well in AI" is directly contradicted by this data; it depends entirely on which AI platform you're talking about
- Practical recommendation: dominate a search result with multiple owned assets (website, LinkedIn, YouTube) rather than ranking just one page, since more retrieval points increases AI citation odds
- Broad visibility across many crawl points also increases the chance of being included in future model training data via Common Crawl, not just immediate retrieval

---

### POST 02:

Title: When Creating Pages for SEO/AEO

Link: https://www.linkedin.com/posts/nathangotch_when-creating-pages-for-seo-aeo-they-activity-7457790873058291712-1MuE/

Date: ~1 month before collection (≈May 2026)

Summary: A six-step framework for building content that performs for both SEO and AEO rather than producing what Nathan calls "slop" with only short-term results. The steps move from building a "search brainiac" data layer combining Search Console, GA4, and AI rank tracking with company knowledge and an expertise layer, through building a competitor swipe file, doing competitive research across both traditional and AI citations, running a page-level gap analysis using ChatGPT, and finally building a genuinely differentiated content angle rather than another rehash.

Key Insights:
- His "search brainiac" concept layers three data types: a data layer (GSC, GA4, AI rank tracking), a company layer (products, FAQs), and an expertise layer (founder interviews, user-generated content)
- Recommended competitive research explicitly pulls from both traditional search rankings and AI citations together, not just one or the other
- A specific tactical step: feed top competitor content into ChatGPT and ask it directly to identify topic gaps rather than doing manual gap analysis by hand
- Once a strong content brief is built this way, whether a human or AI writes the final draft stops mattering much

---

## Expert: Olga Zarr

Title: AI and SEO in 2025: AI Optimization and SEO

Link: https://www.linkedin.com/posts/olgazarr_ai-and-seo-in-2025-ai-optimization-seo-activity-7346816475539615744-Cung/

Date: ~11 months before collection (≈July 2025)

Summary: A reassurance-toned post aimed at SEOs anxious about being replaced by AI. Olga leads with grounding statistics (Google handling roughly 373 times more queries than ChatGPT, AI Overviews appearing in over half of all searches) to argue that SEO skills are becoming more valuable, not less. Her core framing is that what people call "AI SEO" is roughly 90% traditional SEO done properly, not a fundamentally new discipline. The post promotes a comprehensive presentation and a 100-plus-point optimization checklist covering platform-by-platform AI optimization guidance.

Key Insights:
- At the time of this post, Google was handling roughly 373 times more queries than ChatGPT
- AI Overviews were already appearing in more than 50% of searches per her cited data
- "AI SEO" is roughly 90% traditional SEO executed well, not a fundamentally new discipline requiring all-new skills
- SEO skills are becoming more valuable in the AI era, directly countering the "SEO is dying" narrative