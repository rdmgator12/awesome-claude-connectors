# Awesome List for Claude Connectors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="media/banner.svg" alt="Awesome Claude Connectors" width="800">
</p>

> A comprehensive directory of every connector in Anthropic's official [Claude Connectors Directory](https://www.anthropic.com/partners/mcp) — 735 tracked MCP integrations across both directory surfaces, organized by category with descriptions and use cases.

**Last updated:** July 15, 2026 | **Connectors tracked:** 735 | **Categories:** 30

Claude connectors are verified MCP (Model Context Protocol) servers that extend Claude with real-time access to external tools, data sources, and services. They work across Claude.ai, Claude Desktop, Claude Mobile, and Claude Code. Every connector in the official directory is vetted by Anthropic for security, reliability, and compatibility.

For more information, see the [Connectors Documentation](https://claude.com/docs/connectors/directory), [Submission Guidelines](https://claude.com/docs/connectors/building/submission), and [MCP Protocol Specification](https://modelcontextprotocol.io).

Connectors marked with **`A`** are built and maintained by Anthropic.

This list is maintained weekly. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

> This is an independent, community-maintained list. Not affiliated with, endorsed by, or sponsored by Anthropic PBC. "Claude" and related marks are the property of Anthropic PBC. Each connector is the property of its respective owner.


> [!TIP]
> ### Connector of the Week — July 15, 2026
>
> **Kastra** · *Observability and Monitoring*
>
> A connector whose subject is the agent itself: Kastra inspects and audits Claude Code's own actions, giving an execution-governance and authorization layer over what an agent did and was allowed to do. It headlines the largest single reconcile in this list's history — **+184 entries** in one pass — almost all of it from the in-app catalog's Community and desktop-extension tiers rather than the web directory, which moved only 401 → 404. The shape of that influx is the story. Long-tail vertical tooling arrived in volume — Moroccan law (Juridata), Japanese procurement bids (JP Bid), Romanian company filings (iSpv), Brazilian e-commerce data (JoomPulse), Mexican commercial real estate (Spot2) — alongside a wave of agent-infrastructure plumbing that assumes agents now spend money and need supervision: scoped virtual cards with audit trails, execution-governance layers over Claude Code's own actions (Kastra), and design-token drift detection for AI-written UI (swatchdog). Also this week: three entries were removed after failing the two-surface test (Outlook, folded into Microsoft 365; BlueConic; protocols.io), the first removals the list has ever made. Nine in-app Community entries are held pending a verifiable vendor URL rather than shipped with a guessed link.

---

## Contents

- [AI and ML](#ai-and-ml)
- [Automation and Integration](#automation-and-integration)
- [Calendar and Scheduling](#calendar-and-scheduling)
- [Cloud and Infrastructure](#cloud-and-infrastructure)
- [CMS and Web Building](#cms-and-web-building)
- [Communication](#communication)
- [Customer Support](#customer-support)
- [Data and Analytics](#data-and-analytics)
- [Design and Creative](#design-and-creative)
- [Desktop Automation](#desktop-automation)
- [Development Tools](#development-tools)
- [Documents and Files](#documents-and-files)
- [Education](#education)
- [Entertainment](#entertainment)
- [Finance and Trading](#finance-and-trading)
- [Government and Nonprofit](#government-and-nonprofit)
- [Healthcare and Life Sciences](#healthcare-and-life-sciences)
- [Jobs](#jobs)
- [Legal](#legal)
- [Lifestyle and Local](#lifestyle-and-local)
- [Marketing and Sales](#marketing-and-sales)
- [Observability and Monitoring](#observability-and-monitoring)
- [Productivity](#productivity)
- [Project Management](#project-management)
- [Research and Academic](#research-and-academic)
- [SAP](#sap)
- [Security](#security)
- [SEO and Web](#seo-and-web)
- [Ticketing and Events](#ticketing-and-events)
- [Travel](#travel)
- [Related](#related)

---

## AI and ML

- [Cloudglue](https://cloudglue.dev) - Video analysis and processing. *Use case: Extracting insights from video content, automated video summarization.*
- [ElevenLabs Agents MCP App](https://elevenlabs.io/conversational-ai) - Build conversational AI agents with voice. *Use case: Voice-enabled AI assistants, phone agents, voice-first applications.*
- [ElevenLabs Player](https://elevenlabs.io/text-to-speech) - Audio generation and playback. *Use case: Text-to-speech, audio content creation, voiceover generation.*
- [Graffiticode](https://graffiticode.org) - An open toolbox of task-specific AI tools. *Use case: Calling a purpose-built tool for a narrow task, chaining task-specific tools into an agent workflow, extending an agent with a new tool.*
- [Hugging Face](https://huggingface.co) - Access Hugging Face Hub models and Gradio apps. *Use case: Model exploration, running inference on hosted models, discovering pretrained models for ML workflows.*
- [Mem0](https://mem0.ai) - Persistent memory for AI agents and assistants. *Use case: Long-term memory that survives across sessions, semantic recall of prior context, shared memory across tools.*
- [Mnemoverse Memory](https://mnemoverse.com) - Long-term memory for AI agents. *Use case: Persistent memory across Claude, Cursor, and ChatGPT, semantic recall of context across sessions, projects, and tools.*
- [Orbismo](https://orbismo.com) - Build collaborative worlds with AI. *Use case: Maintaining a novel's character and timeline canon, tracking a game campaign's world lore, keeping a knowledge base of people and relationships current.*
- [Owkin](https://owkin.com) - AI agents for biology. *Use case: Biological research, computational biology workflows, drug discovery.*
- [Parallel Search](https://parallel.ai) - Free token-efficient web search built for AI agents. *Use case: Grounding answers with a search API tuned for LLM consumption, low-token retrieval in agent pipelines.*
- [Roboflow](https://roboflow.com) - Build, search, and run computer vision models. *Use case: Searching a model catalog, running inference on an image, managing a training dataset.*
- [ToolUniverse](https://tooluniverse.org) - Access 600+ scientific tools. *Use case: Scientific computing, running domain-specific tools for chemistry, physics, and biology research.*
- [Wolfram](https://www.wolframalpha.com) - Inject precise computation and curated knowledge. *Use case: Symbolic math, unit conversions, real-world data lookups, scientific calculation, and step-by-step problem solving against Wolfram's knowledge engine.*


## Automation and Integration

- [CData](https://www.cdata.com) - Managed MCP for 350+ data sources. *Use case: Universal data connector, querying databases and SaaS APIs through a single interface.*
- [CodeWords](https://codewords.ai) - Build AI agents and automations by chatting with AI. *Use case: Building a custom automation workflow, creating an agent without code, chaining tools together via chat.*
- [IFTTT](https://ifttt.com) - Automate 1000+ apps. *Use case: Cross-app automation, trigger-based workflows connecting disparate services.*
- [Jentic](https://jentic.com) - Universal tool access. *Use case: Connecting to APIs without writing integration code.*
- [Make](https://www.make.com) - Run automation scenarios. *Use case: Visual workflow automation, connecting apps without code.*
- [n8n](https://n8n.io) - Run automation workflows. *Use case: Self-hosted workflow automation, open-source alternative to Zapier.*
- [PlayMCP](https://playmcp.kakao.com) - Kakao MCP gateway and toolbox. *Use case: Browsing Kakao-registered MCP servers, bundling up to 10 into a personal toolbox, and routing through a single OAuth2 gateway endpoint.*
- [ServiceNow](https://www.servicenow.com) - Trigger, automate, and orchestrate enterprise workflows. *Use case: Kicking off ServiceNow workflows from chat, orchestrating cross-department processes, enterprise service automation.*
- [SignalSync](https://signalsync.ai) - Query workflows and requests across an organization. *Use case: Checking workflow request status, querying cross-department process data, monitoring operational workflow health.*
- [Tekst](https://www.tekst.com) - Analyze and automate enterprise processes. *Use case: Mapping a quote-to-cash exception into an automated rule, auditing where a procure-to-pay process breaks down, generating process documentation from workflow data.*
- [Tines](https://www.tines.com) - Deploy and manage automation servers. *Use case: Security orchestration, workflow automation for SecOps.*
- [Tray.ai](https://tray.ai) - AI orchestration platform with iPaaS, agent builder, and 700+ connectors. *Use case: Enterprise integration with built-in governance, MCP tool policies via Agent Gateway, embedded automation across business apps.*
- [Workato](https://www.workato.com) - Automate and connect apps. *Use case: Enterprise integration, workflow automation across business systems.*
- [Zapier](https://zapier.com) - Automate workflows across apps. *Use case: No-code automation, connecting 6000+ apps with trigger-based workflows.*


## Calendar and Scheduling

- [Akiflow](https://akiflow.com) - Plans tasks across multiple calendars from any AI assistant. *Use case: Unifying calendars from multiple accounts, blocking time for tasks, planning a daily schedule.*
- [BusyCal](https://www.busymac.com/busycal) - Calendar management for macOS. *Use case: Managing complex schedules on Apple devices, syncing with multiple calendar providers.*
- [Calendly](https://calendly.com) - Event types and bookings. *Use case: Scheduling meetings, managing availability, automating appointment booking workflows.*
- [Clockwise](https://www.getclockwise.com) - AI-powered calendar and time management. *Use case: Intelligent scheduling, focus-time protection, meeting coordination, calendar optimization.*
- [Fantastical](https://flexibits.com/fantastical) - Calendar management for Apple devices. *Use case: Natural language event creation, calendar views, Apple ecosystem calendar management.*
- [Google Calendar](https://calendar.google.com) - Manage your schedule and coordinate meetings. *Use case: Creating and updating events, finding free time, coordinating across multiple calendars, scheduling automation.*


## Cloud and Infrastructure

- [AWS API MCP Server](https://aws.amazon.com) - Manage AWS resources. *Use case: Cloud infrastructure management, querying AWS services, deployment automation.*
- [AWS Marketplace](https://aws.amazon.com/marketplace) - Browse cloud solutions. *Use case: Discovering SaaS tools and infrastructure components on AWS.*
- [Azure MCP Server](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/) - Manage Azure resources via natural language. *Use case: Querying storage accounts, running KQL against databases, deploying with Entra ID auth and RBAC scoping.*
- [Blynk](https://www.blynk.io) - Create, monitor, and control Blynk IoT devices. *Use case: Monitoring sensor data from IoT devices, controlling connected hardware remotely, building an IoT dashboard.*
- [Cloudflare](https://www.cloudflare.com) - Compute, storage, and AI on Cloudflare. *Use case: Edge deployment, Workers management, CDN configuration, AI inference at the edge.*
- [Costory](https://costory.io) - FinOps cost-context layer for engineering teams. *Use case: Investigating a cloud cost spike, attributing spend to services or teams, surfacing cost context during engineering work.*
- [Databricks](https://www.databricks.com) - Unity Catalog and Mosaic AI. *Use case: Data engineering, ML model management, lakehouse analytics.*
- [Dremio Cloud](https://www.dremio.com) - Access lakehouse data. *Use case: Querying data lakes, federated SQL across multiple data sources.*
- [Google Compute Engine](https://cloud.google.com/compute) - GCP virtual machine management and provisioning. *Use case: Managing GCP virtual machines, instance configuration, cloud compute workflows.*
- [Kubernetes MCP Server](https://kubernetes.io) - Container orchestration cluster management via kubectl. *Use case: Cluster management, pod debugging, deployment automation.*
- [MotherDuck](https://motherduck.com) - DuckDB in the cloud. *Use case: Serverless analytical queries, local-first data analysis that scales to cloud.*
- [Netlify](https://www.netlify.com) - Create, deploy, and manage websites. *Use case: Static site deployment, serverless functions, CI/CD for web projects.*
- [OneLens](https://www.astuto.ai) - Cloud cost and FinOps analytics. *Use case: Finding Kubernetes cost overruns, allocating cloud spend by team, root-cause analysis on a cost anomaly.*
- [PlanetScale](https://planetscale.com) - Managed PostgreSQL and MySQL. *Use case: Database branching, schema management, serverless database operations.*
- [QuickNode](https://www.quicknode.com) - High-performance Blockchain RPC infrastructure across 80+ chains. *Use case: Web3 endpoint provisioning, onchain data streaming, Blockchain app scaling, multi-chain development.*
- [StackQL MCP Server](https://stackql.io) - SQL-native query and provisioning for cloud infrastructure. *Use case: Querying and deploying cloud resources across AWS, Azure, and GCP through a single SQL interface.*
- [Starburst](https://www.starburst.io) - Federated data access. *Use case: Querying data across multiple sources with a single SQL interface.*
- [Supabase](https://supabase.com) - Databases, auth, and storage. *Use case: Postgres-backed backend, real-time subscriptions, auth, file storage for modern apps.*
- [Vercel](https://vercel.com) - Analyze, debug, and manage deployments. *Use case: Next.js deployment, serverless functions, edge config, deployment analytics.*
- [Zylo](https://zylo.com) - View, update, and manage a SaaS portfolio. *Use case: Auditing SaaS license spend, tracking app usage, managing renewals.*


## CMS and Web Building

- [Adobe Experience Manager](https://business.adobe.com/products/experience-manager/adobe-experience-manager.html) - Enterprise content and digital asset management. *Use case: Large-scale web content management, digital asset workflows, omnichannel experience delivery for enterprises.*
- [Base44](https://base44.com) - Build and manage Base44 apps. *Use case: Low-code app development on the Base44 platform.*
- [Deplixo](https://deplixo.com) - Build and deploy web apps to a live URL in seconds. *Use case: Spinning up a prototype app, deploying a landing page, sharing a working demo.*
- [Laioutr](https://www.laioutr.com) - Edit Cockpit sections, blocks, and props in real time. *Use case: Composing storefront pages from sections and blocks, editing component props live, managing a composable-commerce frontend.*
- [Lindo AI](https://lindo.ai) - Create websites, pages, and blog posts with AI. *Use case: AI website generation, landing-page and blog creation, client and credit management.*
- [Mystore](https://www.mystore.in) - Search products, orders, customers, and analytics from a Mystore store. *Use case: Checking order status, pulling sales analytics, looking up customer purchase history.*
- [Natoma](https://natoma.com) - Internal tools and apps. *Use case: Building internal dashboards and admin tools.*
- [Sanity](https://www.sanity.io) - Manage content in Sanity CMS. *Use case: Headless CMS content management, structured content queries, editorial workflows.*
- [Shopify](https://www.shopify.com) - Build, manage, and analyze your Shopify store. *Use case: Storefront management, product and inventory queries, order analytics, e-commerce automation.*
- [Webflow](https://webflow.com) - CMS and site management. *Use case: Visual web development, CMS content management, design-to-production workflows.*
- [Wix](https://www.wix.com) - Website creation and management on the Wix platform. *Use case: Site building, e-commerce setup, domain management, blog publishing.*
- [WordPress.com](https://wordpress.com) - Manage WordPress sites. *Use case: Content management, plugin configuration, site administration for WordPress.*


## Communication

- [AgentMail](https://agentmail.to) - Email inboxes for AI agents. *Use case: Programmatic email send and receive, dedicated agent mailboxes, automated email workflows.*
- [Circleback](https://circleback.ai) - Meeting context and notes. *Use case: Pulling context from past meetings into current conversations.*
- [CometChat](https://www.cometchat.com) - Add real-time chat, voice, and video to your app. *Use case: Building in-app messaging features, wiring voice and video calling into a product, programmatic chat moderation.*
- [Fathom](https://fathom.ai) - Meeting recording, transcription, and AI summaries. *Use case: Automatic Zoom/Meet/Teams call recording, AI-generated summaries, action-item extraction, CRM sync.*
- [Fellow.ai](https://fellow.app) - Chat with your meeting data. *Use case: Querying meeting transcripts, finding action items, reviewing past discussions.*
- [Fireflies](https://fireflies.ai) - Meeting transcripts and search. *Use case: Searching across all meeting transcripts, extracting decisions and action items.*
- [Fyxer](https://fyxer.com) - AI email assistant for inbox and replies. *Use case: Inbox triage, drafting context-aware replies in your voice, follow-up automation.*
- [Gmail](https://mail.google.com) - Draft replies, summarize threads, and search your inbox. *Use case: Email triage, composing context-aware replies, finding specific conversations, summarizing long threads.*
- [Grain](https://grain.com) - Turn meetings into insights and next steps. *Use case: Meeting recording, AI-generated highlights, deal-coaching insights, automated CRM updates.*
- [Granola](https://granola.ai) - AI notepad for meetings. *Use case: Real-time meeting notes with AI enhancement, structured meeting summaries.*
- [Krisp](https://krisp.ai) - Meeting transcripts. *Use case: Noise-cancelled meeting transcription, speaker identification.*
- [MeetGeek](https://meetgeek.ai) - Meetings and transcripts. *Use case: Automated meeting recording, transcript search, meeting analytics.*
- [Minutes — Meeting Memory for AI](https://minutes.me) - Local-only meeting transcription. *Use case: Privacy-first meeting transcription that processes entirely on-device. No data leaves your machine.*
- [Otter.ai](https://otter.ai) - Meeting intelligence and transcription. *Use case: Live meeting notes, searchable transcripts, automatic summaries and action items across Zoom/Meet/Teams.*
- [Quo](https://www.quo.com) - Business phone with call insights and transcripts. *Use case: Pulling call transcripts, surfacing missed-opportunity patterns from voice/SMS, querying voicemail history.*
- [Read AI](https://www.read.ai) - Bring meeting transcripts and summaries into Claude. *Use case: Meeting recording across Zoom/Meet/Teams, AI-generated summaries, sentiment and engagement analytics, action-item extraction.*
- [Slack](https://slack.com) - Send messages, create canvases, and fetch data from Slack. *Use case: Team communication, searching channel history, posting updates, creating collaborative documents.*
- [Spark](https://sparkmailapp.com) - Read, draft, triage, and act on email. *Use case: Inbox triage, drafting replies in your voice, managing email, calendar, and contacts across Gmail and Outlook.*
- [Superhuman Mail](https://superhuman.com) - Drive your email and calendar from Claude. *Use case: Inbox triage at speed, AI-drafted replies in personal voice, calendar coordination, follow-up automation.*
- [tldv](https://tldv.io) - AI meeting notetaker for Zoom, Google Meet, and Teams. *Use case: Pulling call transcripts and AI summaries, extracting action items, searching past meeting insights, syncing notes to CRM.*
- [Twilio](https://www.twilio.com) - Programmable messaging, voice, and customer engagement APIs. *Use case: SMS/MMS/RCS/WhatsApp messaging, phone-number provisioning, verification flows for production apps.*
- [Vani by Zoho](https://www.vanihq.com) - Collaboration spaces by Zoho. *Use case: Team messaging, shared spaces, creating and sharing Vani content across projects.*
- [Webex Meetings](https://www.webex.com/meetings.html) - AI-powered workflows for Cisco Webex meetings. *Use case: Meeting summaries, action-item extraction, post-meeting follow-up across Webex calls.*
- [Zoom for Claude](https://zoom.us) - Search, recap, and act on Zoom meetings. *Use case: Meeting recaps, finding key moments in recordings, extracting action items from Zoom calls.*


## Customer Support

- [Computer by DevRev](https://devrev.ai/meet-computer) - Conversational AI teammate with shared memory. *Use case: Ticket resolution, service desk automation, CRM updates, customer support.*
- [Freshservice](https://www.freshworks.com/freshservice/) - IT service management and ticketing. *Use case: Managing IT tickets, assets, and change requests, automating service-desk workflows.*
- [Guru](https://www.getguru.com) - Access company knowledge base. *Use case: Finding internal documentation, answering team questions from a centralized knowledge source.*
- [Intercom](https://www.intercom.com) - Customer insights and support data. *Use case: Analyzing customer conversations, tracking support trends, surfacing customer feedback.*
- [Lorikeet](https://lorikeet.ai) - Universal support concierge. *Use case: Automated customer support workflows, ticket routing, response generation.*
- [Pylon](https://usepylon.com) - Support issues management. *Use case: Tracking and managing support tickets, escalation workflows.*
- [RT (Request Tracker)](https://bestpractical.com/request-tracker) - Search tickets and manage queues. *Use case: IT helpdesk workflows, ticket search, queue management for open-source RT installations.*
- [Unthread](https://unthread.io) - Support ticket management. *Use case: Converting Slack messages into trackable support tickets.*
- [Unwrap](https://www.unwrap.ai) - Customer feedback analysis. *Use case: Aggregating and analyzing feedback across channels, surfacing product themes and sentiment.*
- [Zoho Desk](https://www.zoho.com/desk) - Helpdesk and support ticket automation. *Use case: Ticket routing, SLA management, customer support analytics, knowledge base integration.*


## Data and Analytics

- [Adobe Customer Journey Analytics](https://business.adobe.com/products/adobe-analytics/customer-journey-analytics.html) - Cross-channel analytics across the full customer journey. *Use case: Omnichannel journey analysis, attribution modeling, customer-level insights, conversion optimization.*
- [Amplitude](https://amplitude.com) - Search and get product analytics insights. *Use case: Understanding user behavior, funnel analysis, retention metrics, A/B test results.*
- [Asset Vision](https://www.assetvision.com.au) - Unlocks asset insights through conversation. *Use case: Querying asset maintenance status, reviewing infrastructure inspection data, planning asset lifecycle decisions.*
- [Aura](https://aura.co) - Company and workforce analytics. *Use case: HR analytics, workforce planning, organizational insights.*
- [Baremetrics](https://baremetrics.com) - Subscription analytics for SaaS. *Use case: MRR, churn, and LTV reporting, customer and subscription metrics, revenue trend analysis.*
- [BlockchainQuery](https://www.blockchainquery.com) - Blockchain data across 60+ networks. *Use case: Querying on-chain data, analyzing transaction history, monitoring wallet activity across multiple chains.*
- [Blockscout](https://www.blockscout.com) - Analyze Blockchain data with a block explorer. *Use case: Smart contract verification, transaction tracing, token analytics.*
- [Carbon Arc](https://www.carbonarc.co) - Data infrastructure for the AI economy. *Use case: Sourcing external datasets for AI models, integrating third-party data feeds, building data pipelines.*
- [ChartMogul](https://chartmogul.com) - Analyzes subscribers, recurring revenue, and churn. *Use case: Tracking MRR trends, analyzing churn rate, segmenting subscriber cohorts.*
- [CKAN MCP Server](https://ckan.org) - Access open data portals. *Use case: Querying government and public datasets, open data exploration for research.*
- [ClickHouse](https://clickhouse.com) - Query and explore your ClickHouse Cloud data. *Use case: Analytical SQL over ClickHouse Cloud, schema exploration, ad-hoc OLAP queries from chat.*
- [Contentsquare](https://contentsquare.com) - Digital experience analytics and session replay. *Use case: Understanding user behavior across web and mobile, identifying UX friction, conversion optimization.*
- [Coupler.io](https://www.coupler.io) - Pull data from hundreds of sources. *Use case: Cross-platform data aggregation, building dashboards from multiple SaaS tools.*
- [Crustdata](https://crustdata.com) - Search and enrich B2B company and people data. *Use case: Building a prospect list, enriching a CRM record, researching a company's headcount and funding.*
- [DataHub](https://datahub.com) - Connect AI agents to enterprise data and context. *Use case: Data discovery, cataloging, lineage tracking, governed access to enterprise datasets.*
- [dbt](https://www.getdbt.com) - Explore, query, and build with dbt projects. *Use case: Analytics engineering, data transformation, modeling and testing data pipelines.*
- [Enterpret](https://www.enterpret.com) - Unified customer feedback analysis. *Use case: Aggregating feedback from multiple channels, identifying product themes and trends.*
- [Felt Maps](https://felt.com) - Collaborative geospatial mapping and analysis. *Use case: Mapping spatial data, geographic analysis, sharing interactive maps with teams.*
- [Global Database](https://www.globaldatabase.com) - Turns a company name into full company insight and data. *Use case: Researching a prospective business partner, verifying a company's financial standing, building a target list for outreach.*
- [Google Cloud BigQuery](https://cloud.google.com/bigquery) - Analytical insights from Google BigQuery. *Use case: Large-scale data analysis, SQL queries against data warehouses, business intelligence.*
- [Helium 10](https://www.helium10.com) - Amazon seller analytics data access. *Use case: Analyzing keyword rankings for a listing, tracking competitor product performance, reviewing PPC campaign analytics.*
- [Hex](https://hex.tech) - Answer questions with Hex notebooks. *Use case: Data science workflows, querying databases via notebooks, sharing analytical results.*
- [iSpv](https://ispv.ro) - Romanian company and financial data. *Use case: Looking up a Romanian company's filings, checking a partner's registration status, researching a competitor's financials.*
- [JoomPulse](https://joompulse.com) - Brazilian e-commerce data on products, sellers, and trends. *Use case: Finding high-margin products to sell, tracking a competitor seller's pricing changes, spotting a trending category early.*
- [Kamai AI](https://kamai.io) - AI takeoff for construction that turns blueprints into structured, traceable quantities. *Use case: Extracting material quantities from a blueprint set, generating structured output for estimating software, validating takeoffs across sheets.*
- [Kpler](https://www.kpler.com) - Real-time trade and maritime intelligence for global markets. *Use case: Vessel tracking, commodity flow analysis, supply chain monitoring, market intelligence.*
- [Listen Labs](https://listenlabs.ai) - User research and insights analysis. *Use case: Synthesizing user interviews, surfacing customer insights, qualitative research at scale.*
- [Meltwater](https://www.meltwater.com) - Search and analyze billions of news articles and social posts. *Use case: Monitoring brand mentions across media, tracking social sentiment, researching competitor coverage.*
- [Metabase](https://www.metabase.com) - Analytics and dashboards. *Use case: Business intelligence, SQL-free data exploration, embedded analytics.*
- [Metabase (Unofficial — Community)](https://github.com/jerichosequitin/metabase-mcp) - Community MCP server for Metabase BI data access. *Use case: Run SQL queries, execute saved cards, browse dashboards and databases, optimize token usage with caching.*
- [Microsoft Clarity](https://clarity.microsoft.com) - Session replays and heatmaps. *Use case: Understanding how users interact with your website, identifying UX friction points.*
- [Microsoft Dataverse](https://www.microsoft.com/en-us/power-platform/dataverse) - Query and manage Power Platform data. *Use case: Reading and writing Dataverse tables, building data-backed Power Platform apps, enterprise data operations.*
- [Mixpanel](https://mixpanel.com) - Analyze and query product data. *Use case: Event-based analytics, cohort analysis, engagement tracking.*
- [Monte Carlo](https://www.montecarlodata.com) - Data and AI observability. *Use case: Detecting data freshness, schema, volume, and quality incidents across warehouses, lakes, and ML pipelines.*
- [MyCoach Pro](https://mycoachpro.io) - Query MyCoach Pro performance and scouting data. *Use case: Reviewing athlete performance dashboards, pulling scouting reports, tracking training load across a squad.*
- [Omni Analytics](https://omni.co) - Query data via natural language. *Use case: Asking business questions in plain English against your data warehouse.*
- [Orion by Gravity](https://www.bygravity.com) - Autonomous AI analyst for your data stack. *Use case: Proactive data monitoring, automated insight generation, Looker and warehouse analysis delivered to Slack.*
- [Pigment](https://www.gopigment.com) - Analyze business planning data. *Use case: Financial planning, revenue forecasting, scenario modeling.*
- [PostHog](https://posthog.com) - Query and manage product insights. *Use case: Open-source product analytics, feature flags, session recording analysis.*
- [Qlik](https://www.qlik.com) - Data integration, quality, and AI-powered analytics platform. *Use case: Data integration, self-service analytics, interactive dashboards, business intelligence reporting.*
- [Ramp Data](https://ramp.com/data) - Anonymized business spending data across 50,000+ companies. *Use case: Benchmarking corporate spend, tracking AI/advertising adoption trends, surfacing economic signals from real transactions.*
- [Sellerise](https://sellerise.com) - Analyze Amazon seller business data. *Use case: Tracking Amazon sales trends, monitoring profit margins, auditing inventory levels.*
- [Shapes](https://shapes.co) - HR people analytics covering headcount, comp, DEI, and time off. *Use case: Querying live workforce data through chat, surfacing engagement trends, automating people-analytics reports.*
- [Sigma](https://sigmacomputing.com) - Natural-language data exploration on warehouse data. *Use case: Asking governed questions of cloud-warehouse data, generating explorable workbooks, deploying AI agents that respect column-level security.*
- [Similarweb](https://www.similarweb.com) - Web, mobile app, and market data. *Use case: Competitive analysis, traffic estimation, market research.*
- [SkyWatch](https://skywatch.com) - Search and price satellite imagery worldwide. *Use case: Finding satellite imagery of a location, comparing pricing across providers, tasking a new capture.*
- [Snowflake](https://www.snowflake.com) - Structured and unstructured data. *Use case: Data warehousing, cross-cloud analytics, data sharing.*
- [Speeda](https://www.ub-speeda.com) - Japanese business intelligence covering standardized company financials, industry reports, and expert views. *Use case: Pulling a Japanese company's financials before a deal, gathering industry reports for a market-entry study, sourcing expert commentary.*
- [SQD](https://sqd.dev) - Query validated onchain data across 200+ blockchains. *Use case: Pulling historical transaction data for a token across chains, auditing smart contract activity, building a cross-chain analytics dashboard.*
- [Stats Compass](https://statscompass.com) - Data science tools for loading, visualization, and ML. *Use case: Statistical analysis, data visualization, running ML models within Claude.*
- [Streamkap](https://streamkap.com) - Build, monitor, and troubleshoot real-time change-data-capture pipelines. *Use case: Debugging a lagging CDC pipeline, monitoring data freshness across source-to-warehouse syncs, standing up a pipeline for a database migration.*
- [Supermetrics](https://supermetrics.com) - Marketing performance data. *Use case: Aggregating marketing metrics across ad platforms, reporting automation.*
- [Syntitan](https://syntitan.ai) - Score, refine, and reproduce AI-ready data. *Use case: Cleaning a dataset before model training, scoring data quality across sources, regenerating a reproducible dataset for retraining.*
- [Tableau MCP Server](https://www.tableau.com) - Data visualization and business intelligence dashboards. *Use case: Interactive analytics, visual data exploration, cross-source reporting, dashboard publishing.*
- [ThoughtSpot Spotter](https://www.thoughtspot.com) - AI data analyst from question to trusted insight. *Use case: Natural-language data exploration on enterprise warehouses, governed semantic-model queries, automated chart generation grounded in a curated business glossary.*
- [Trackunit IrisX](https://trackunit.com) - Turns construction fleet telematics into action. *Use case: Flagging underutilized equipment across a fleet, scheduling preventive maintenance from telematics data, tracking fuel usage across job sites.*
- [Triple Whale](https://triplewhale.com) - Real-time e-commerce analytics across every channel. *Use case: Tracking e-commerce attribution, monitoring ad spend ROI, unifying multi-channel revenue data.*
- [Ultipa](https://www.ultipa.com) - Graph database and analytics. *Use case: Running GQL graph queries and algorithms, managing Ultipa Cloud instances, graph-based data exploration.*
- [Upsolve AI](https://upsolve.ai) - Natural-language analytics over business data. *Use case: Querying business data in plain language, generating analytics answers, exploring datasets conversationally.*
- [Vaisala Xweather](https://www.xweather.com) - Real-time, forecast, and historical weather data. *Use case: Pulling current conditions, retrieving forecasts, analyzing historical weather trends.*
- [Visier](https://www.visier.com) - People and productivity insights. *Use case: Workforce analytics, talent planning, organizational health metrics.*
- [Windsor.ai](https://windsor.ai) - Connect 325+ marketing data sources. *Use case: Marketing attribution, cross-channel performance analysis.*
- [Wizerr](https://www.wizerr.ai) - Component decisions for hardware programs. *Use case: Finding component cross-references and alternates, checking BOM lifecycle risk, comparing part pricing and availability.*
- [Zint](https://www.zint.io) - UK company data, financials, and news. *Use case: Pulling UK company financials, researching director and ownership data, monitoring corporate news signals.*
- [Zite](https://www.zite.com) - Manage and query Zite data. *Use case: Querying custom databases in natural language, creating and updating records, building data from uploaded documents.*
- [Zocks](https://www.zocks.ai) - Analyze client conversations. *Use case: Financial advisor conversation analysis, compliance review, client insight extraction.*
- [Zoho Analytics](https://www.zoho.com/analytics) - Self-service BI and reporting across the Zoho stack. *Use case: Visual analytics across Zoho CRM/Books/Desk data, custom dashboards, AI-assisted data preparation and natural-language querying.*


## Design and Creative

- [Adobe for creativity](https://developer.adobe.com/adobe-for-creativity/) - Photoshop, Lightroom, Illustrator, Firefly, Premiere, Express, InDesign, and Adobe Stock through Claude. *Use case: Edit photos and vectors, design from templates, resize video for social, license stock — all through natural language without app-switching.*
- [Agentic Presentations by SlidesGPT](https://slidesgpt.com) - Make presentations and slides, export to PowerPoint. *Use case: Generating slide decks from prompts, exporting to PowerPoint, rapid presentation drafting.*
- [Autodesk Fusion](https://www.autodesk.com/products/fusion-360) - Create, modify, and inspect CAD geometry in Fusion. *Use case: Parametric CAD modeling, mechanical part design, engineering geometry inspection.*
- [B12 Website Generator](https://www.b12.io) - Create websites with AI. *Use case: Rapid website prototyping, small business site generation.*
- [Beautiful.ai](https://www.beautiful.ai) - Turn ideas into presentations. *Use case: Generating slide decks from prompts with design-automated layouts, updating decks conversationally.*
- [Blender](https://www.blender.org) - Natural language interface to Blender's Python API and docs. *Use case: 3D modeling automation, scene scripting, animation workflows controlled by natural language.*
- [Brandfetch](https://brandfetch.com) - Brand asset lookup that keeps generated output on-brand. *Use case: Pulling a company's logo and brand colors, applying brand guidelines to generated content, looking up brand assets for a domain.*
- [Canva](https://www.canva.com) - Create, autofill, and export designs. *Use case: Quick graphics, social media posts, presentation slides, brand-consistent visual content.*
- [Descript](https://www.descript.com) - Import, edit, or create video with prompts. *Use case: Podcast and video editing through transcript editing, AI voice cloning, automated multi-cam editing, and script-driven video production.*
- [Eraser](https://www.eraser.io) - AI co-pilot for technical design and documentation. *Use case: Diagram-as-code architecture diagrams, codebase-driven system diagrams, sequence and ERD generation that exports cleanly to PNG/SVG/MD.*
- [Excalidraw](https://excalidraw.com) - Interactive hand-drawn style diagrams. *Use case: Whiteboarding, architecture sketches, informal diagrams that feel approachable.*
- [Figma](https://www.figma.com) - Generate diagrams and code from Figma designs. *Use case: Design-to-code workflows, inspecting Figma files, extracting design tokens.*
- [Fonts](https://www.myfonts.com) - AI-powered font discovery. *Use case: Finding a typeface matching a brand's tone, pairing fonts for a campaign, getting font recommendations for a redesign.*
- [Gamma](https://gamma.app) - AI-powered presentations, docs, and webpages. *Use case: Rapid presentation generation, visual document creation, landing pages.*
- [HyperFrames by HeyGen](https://hyperframes.heygen.com/) - Build animated slides and motion graphics with HTML. *Use case: Motion design, animated presentation frames, HTML-based graphics for video and slides.*
- [Lens Studio](https://ar.snap.com/lens-studio) - Build, debug, and generate Lenses for Snapchat and Spectacles. *Use case: AR Lens development, asset and effect generation, Snap Spectacles content creation.*
- [Lucid](https://lucid.co) - Ideation and diagramming. *Use case: Flowcharts, org charts, process maps, collaborative visual planning.*
- [Magic Patterns](https://www.magicpatterns.com) - AI-powered UI pattern exploration and component prototyping. *Use case: UI pattern exploration, design iteration, component prototyping.*
- [Maze](https://maze.co) - Pull Maze user research. *Use case: Retrieving usability-test results, reviewing research findings, summarizing a product research study.*
- [Mermaid Chart](https://www.mermaidchart.com) - Validate Mermaid syntax and render SVG diagrams. *Use case: Architecture diagrams, sequence diagrams, flowcharts rendered from code. Clean SVG output for docs and papers.*
- [Miro](https://miro.com) - Collaborative online whiteboard for teams. *Use case: Mind mapping, workshop facilitation, brainstorming, visual project planning.*
- [Mobbin](https://mobbin.com) - Find UI and UX design references. *Use case: Researching mobile app design patterns, benchmarking competitor onboarding flows, building a reference library for a redesign.*
- [OpenSTAAD MCP Server](https://www.bentley.com/software/staad-pro/) - Bentley STAAD.Pro structural analysis via the OpenSTAAD API. *Use case: Programmatic access to STAAD.Pro models, finite-element analysis automation, structural design integration with custom apps.*
- [Presentations.AI](https://www.presentations.ai) - Create slides and decks from topics, text, or files. *Use case: Drafting a deck from a document or outline, restyling presentations, template-driven slide generation.*
- [Resolume Arena MCP Server](https://www.resolume.com/software/avenue-arena) - Control Resolume Arena VJ software. *Use case: Live visual performance, video mixing, projection mapping driven by natural language.*
- [Resolume Wire MCP Server](https://resolume.com/software/wire) - Control Resolume Wire node-based effects. *Use case: Building real-time visual effects, generative graphics patches, VJ effect chains.*
- [Shutterstock](https://www.shutterstock.com) - Stock photo, video, and creative asset search. *Use case: Searching stock photos for a project, finding licensed video clips, sourcing campaign assets.*
- [Sketch](https://www.sketch.com) - Explore designs in Sketch. *Use case: Inspecting Sketch files, extracting assets, reviewing design specs on macOS.*
- [Three.js 3D Viewer](https://threejs.org) - Interactive 3D scenes. *Use case: 3D visualization, WebGL prototyping, rendering 3D models.*
- [tldraw](https://www.tldraw.com) - Sketch, draw, and diagram. *Use case: Quick sketching, informal diagrams, lightweight whiteboarding.*
- [Trimble SketchUp](https://www.sketchup.com) - 3D modeling and design for AEC professionals. *Use case: Iterating on architectural and product 3D models, accessing 3D Warehouse libraries, building from real-world geocoded data.*
- [Whimsical](https://whimsical.com) - Visual collaboration for diagrams, flowcharts, mind maps, and wireframes. *Use case: Flowchart creation, wireframing, mind mapping, product team brainstorming.*
- [zeroheight](https://zeroheight.com) - Reference zeroheight design system context. *Use case: Looking up design tokens, checking component documentation, keeping design system references in sync.*


## Desktop Automation

- [Android-MCP](https://github.com/CursorTouch/Android-MCP) - Control Android devices. *Use case: Android app testing, mobile automation workflows, device management.*
- [Asteroid](https://asteroid.ai) - Builds and runs agentic, repeatable browser and computer-use workflows. *Use case: Automating portal workflows, running repeatable data-entry tasks, scaling browser-based back-office work.*
- [Control Chrome](https://chromedevtools.github.io/devtools-protocol/) - Chrome tab and navigation control. *Use case: Browser automation, tab management, web scraping from Chrome.*
- [Control your Mac](https://support.apple.com/guide/terminal/use-applescript-apd44b0e5b2-3b9b-46de-8bfc-4741be13ef5b) - Execute AppleScript to automate macOS. *Use case: System-level Mac automation, app control, file management via AppleScript.*
- [Dash](https://kapeli.com/dash) - Search documentation in Dash. *Use case: Quick API reference lookups from the Dash documentation browser on macOS.*
- [Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP) - Local machine automation. *Use case: File system operations, process management, system-level tasks.*
- [macOS](https://support.apple.com/guide/terminal/use-applescript-apd44b0e5b2-3b9b-46de-8bfc-4741be13ef5bos) - Lightweight macOS system interaction. *Use case: Basic Mac control, window management, system queries.*
- [MacOS-MCP](https://github.com/CursorTouch/MacOS-MCP) - Lightweight macOS desktop interaction. *Use case: Computer-use automation on macOS, app and window control, system-level Mac tasks.*
- [Read and Send iMessages](https://claude.com/plugins/imessage) - Send and read Apple Messages. *Use case: Messaging automation, reading conversation history, sending quick replies from Claude.*
- [Vybit Notifications](https://vybit.net) - Custom push notification routing and alert delivery. *Use case: Custom alert systems, notification routing, event-driven alerts.*
- [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) - Windows OS automation and system control. *Use case: Windows application automation, file management, system administration tasks.*


## Development Tools

- [Alpic](https://alpic.ai) - Manage MCP servers and apps hosted on Alpic. *Use case: Deploying and operating hosted MCP servers, managing MCP app infrastructure.*
- [Atlassian Rovo](https://www.atlassian.com/rovo) - Access Jira and Confluence. *Use case: Issue tracking, searching wiki documentation, project management within the Atlassian ecosystem.*
- [Autodesk Product Help](https://help.autodesk.com) - Securely access Autodesk product documentation. *Use case: Looking up AutoCAD/Revit/Maya/Fusion docs, troubleshooting Autodesk software, in-context help retrieval.*
- [Caffeine](https://caffeine.ai) - Describe an app and Caffeine builds, deploys, and hosts it — no servers, no setup. *Use case: Natural-language app building on the Internet Computer, zero-infrastructure prototyping and hosting.*
- [Clerk](https://clerk.com) - Authentication and billing management. *Use case: User management, auth configuration, billing setup for web applications.*
- [commercetools Knowledge](https://commercetools.com) - Product knowledge and API references for the commercetools platform. *Use case: Composable-commerce development, API reference lookup, commercetools integration guidance.*
- [Compiler Explorer](https://godbolt.org) - Compile, run, and explore assembly in 80+ languages. *Use case: Inspecting compiler output, comparing optimization flags, teaching and debugging at the assembly level.*
- [Componecat](https://componecat.ai) - Hierarchical registry of systems, services, and libraries with Git integration and hosted docs. *Use case: Cataloging services across a codebase, keeping docs synced with repos, letting an agent query the software catalog.*
- [Context7](https://context7.com) - Up-to-date documentation for libraries, frameworks, and SDKs. *Use case: Getting current API docs instead of relying on training data. Essential for coding against any library that updates frequently.*
- [Devart Learn](https://devart.com) - Search Devart product documentation. *Use case: Looking up driver documentation, troubleshooting a connection issue, finding setup instructions.*
- [DevRev](https://devrev.ai) - Company knowledge graph. *Use case: Connecting product, support, and engineering data into a unified graph.*
- [dot.](https://www.leaveadot.com) - Collect feedback on anything you build in Claude. *Use case: Getting stakeholder feedback on a live prototype, collecting pinned comments on a build, iterating on an artifact in conversation.*
- [Emergent](https://emergent.sh) - Build and ship full-stack apps. *Use case: Scaffolding a new application, shipping an app to production, iterating on features conversationally.*
- [GitHub MCP](https://github.com/github/github-mcp-server) - The official GitHub MCP server. *Use case: Repo and issue management, PR workflows, code search, CI/CD automation on GitHub.*
- [GitLab](https://about.gitlab.com) - DevSecOps platform for the entire software lifecycle. *Use case: Source code management, CI/CD pipelines, merge requests, issue tracking, security scanning.*
- [GraphOS MCP Tools](https://www.apollographql.com) - Apollo GraphQL documentation and best practices. *Use case: GraphQL schema design guidance, Apollo Connectors specification lookup, agentic GraphQL development.*
- [GrowthBook](https://www.growthbook.io) - Feature flags and experiments. *Use case: A/B testing, gradual rollouts, experiment analysis.*
- [Harness.io](https://app.harness.io) - Build, ship, and secure apps on the Harness Platform. *Use case: End-to-end software delivery spanning CI, CD, feature flags, IaC, cloud cost, chaos engineering, and security testing in a single workspace.*
- [Harness MCP Server](https://www.harness.io) - AI-native CI/CD, deployment, and feature management platform. *Use case: Pipeline orchestration, AI-verified rollbacks, GitOps for multi-cloud deployments, feature-flag-driven release control.*
- [Kapture Browser Automation](https://kapture.dev) - Browser control via DevTools. *Use case: Browser automation using Chrome DevTools Protocol.*
- [KARP Inspector Lite](https://github.com/souldriver007/karp-inspector-lite) - Semantic codebase search. *Use case: Understanding unfamiliar codebases, finding relevant code by meaning rather than keywords.*
- [Lovable](https://lovable.dev) - Build, iterate, inspect, and deploy web apps. *Use case: AI-assisted app building, prototyping full-stack web apps from natural language, one-click deployment.*
- [Mailtrap](https://mailtrap.io) - Email testing and templates. *Use case: Testing email delivery, previewing templates, email sandbox for development.*
- [Manufact](https://manufact.com) - Deploy and monitor MCP servers. *Use case: Hosting MCP servers, monitoring server health, managing connector infrastructure.*
- [Mastercard Developers](https://developer.mastercard.com) - Up-to-date Mastercard APIs, docs, and guides. *Use case: Payments API integration, Mastercard product documentation lookup, developer onboarding.*
- [MercadoLibre](https://developers.mercadolibre.com) - Mercado Libre developer documentation. *Use case: Looking up the API reference while coding, checking endpoint parameters, integrating marketplace listings.*
- [Microsoft Learn](https://learn.microsoft.com) - Microsoft documentation. *Use case: Azure, .NET, Office, and Windows development documentation.*
- [Mintlify](https://mintlify.com) - Search, read, and edit your documentation. *Use case: Editing developer docs in-place, surfacing the right page for a coding task, keeping API references in sync with code.*
- [Mozilla MDN](https://developer.mozilla.org) - Official MDN web platform documentation. *Use case: Looking up HTML, CSS, and JavaScript API references, checking browser compatibility tables, verifying web standards while coding.*
- [Pega Blueprint](https://blueprint.pega.com) - Application design built on enterprise best practices. *Use case: Drafting an enterprise app workflow from a description, generating a case-management design, accelerating a Pega app build.*
- [pg-aiguide](https://www.postgresql.org/docs/) - PostgreSQL docs and skills. *Use case: PostgreSQL query help, configuration guidance, performance tuning.*
- [Port IO](https://www.getport.io) - Developer portal context lake. *Use case: Internal developer platform management, service catalog, developer experience.*
- [Postman](https://www.postman.com) - API context and collections. *Use case: API testing, documentation, sharing request collections across teams.*
- [Qase Test Management](https://qase.io) - Manage test cases, runs, plans, and suites. *Use case: QA test management, test plan automation, run tracking and reporting for engineering teams.*
- [React Aria](https://react-spectrum.adobe.com/react-aria/) - Accessible React UI primitives from Adobe. *Use case: Building keyboard- and screen-reader-accessible components, custom design systems on top of WAI-ARIA-compliant hooks.*
- [React Spectrum (S2)](https://react-spectrum.adobe.com) - Adobe's React Spectrum component library. *Use case: Building apps on Adobe's design system, themed UI development, accessible component composition.*
- [Replit](https://replit.com) - Turn ideas into apps and websites instantly. *Use case: Cloud IDE, collaborative coding, AI-assisted development, instant app deployment.*
- [Resend](https://resend.com) - Email for developers covering transactional and marketing email at scale. *Use case: Sending transactional email from an app, managing marketing campaigns, debugging deliverability.*
- [Retool](https://retool.com) - Build production apps and manage Retool with AI agents. *Use case: Internal tool creation, custom admin dashboards, database UIs, AI-assisted app generation from natural-language prompts.*
- [Runway (runway.team)](https://www.runway.team) - Automate, coordinate, and monitor mobile app releases. *Use case: Kicking off a mobile release, coordinating release steps across a team, monitoring release status.*
- [Shadcn UI](https://ui.shadcn.com) - shadcn/ui component source and demos. *Use case: Browsing component implementations, copying component code, exploring the shadcn/ui library.*
- [SmartBear MCP](https://smartbear.com) - AI access to BugSnag, PactFlow, QMetry, Reflect, Swagger, and Zephyr. *Use case: Unified access across SmartBear's quality and observability suite — bug tracking, contract testing, test management, API documentation in one connector.*
- [Socket](https://socket.dev) - Dependency security scanning. *Use case: Checking npm/PyPI packages for supply chain risks, vulnerability detection.*
- [Sourcegraph](https://sourcegraph.com) - Full enterprise-scale codebase context. *Use case: Cross-repo code search, symbol lookup, and code intelligence against very large monorepos and multi-repo codebases — answers questions that don't fit in Claude's context window.*
- [Stack Overflow](https://stackoverflow.com) - Access Stack Overflow's trusted content. *Use case: Grounding coding answers in accepted solutions, searching canonical developer Q&A during debugging.*
- [Stytch](https://stytch.com) - Authentication management. *Use case: Passwordless auth, OAuth, session management for web apps.*
- [Swagger](https://swagger.io) - API design, documentation, and testing tools built on OpenAPI. *Use case: API spec authoring, interactive documentation, client SDK generation, API lifecycle management.*
- [swatchdog](https://www.swatchdog.dev) - Checks AI-built UI code against design tokens and reports drift. *Use case: Catching an agent that introduced an off-palette color, auditing a component for spacing-token violations, generating a drift report before a merge.*
- [Tomba MCP Server](https://tomba.io) - Professional email address discovery and verification. *Use case: Finding work emails for outreach, domain-based contact search, email deliverability verification.*
- [WorkOS](https://workos.com) - Manage your WorkOS workspace from Claude. *Use case: Enterprise SSO and directory-sync administration, auth configuration, WorkOS resource management from chat.*


## Documents and Files

- [Avanquest PDF API](https://developers.avanquest.com/products/pdf-api) - Scalable PDF processing API. *Use case: PDF conversion, merging, compression, splitting, and document-processing automation.*
- [Box](https://www.box.com) - Enterprise cloud content management and file sharing. *Use case: Document collaboration, secure file sharing, content governance, workflow automation.*
- [Datasite](https://datasite.com) - Virtual data rooms for M&A and dealmaking. *Use case: Diligence document management, deal pipeline tracking, AI-powered redaction of PII across deal artifacts, post-deal archiving.*
- [DeviceLink](https://devicelink.ai) - Secure, real-time file access from your own devices. *Use case: Reading files from a local machine, searching a local codebase, listing directories.*
- [Docling MCP](https://github.com/DS4SD/docling) - Document processing and extraction. *Use case: Parsing PDFs, extracting structured data from documents.*
- [Document360](https://document360.com) - Read, create, update, and publish Document360 knowledge base articles. *Use case: Drafting a help center article, updating documentation, publishing a knowledge base change.*
- [DocuSeal](https://www.docuseal.co) - Sign and manage documents. *Use case: Digital signature workflows, document template management.*
- [Docusign](https://www.docusign.com) - Contract management and e-signatures. *Use case: Sending documents for signature, managing contract lifecycle, tracking envelope status.*
- [Dropbox](https://www.dropbox.com) - Search, organize, and act on Dropbox content. *Use case: Cloud file management, content search, organizing and retrieving documents across a Dropbox account.*
- [Egnyte](https://www.egnyte.com) - Access Egnyte content. *Use case: Enterprise file sharing, content governance, hybrid cloud storage management.*
- [Entropia](https://entropia.io) - Access and analyze your data rooms. *Use case: Diligence document review, data-room search and analysis, deal-artifact insights.*
- [Files.com](https://files.com) - Secure file orchestration platform. *Use case: Automating a file transfer workflow, searching files across connected storage, setting up a secure share.*
- [Filesystem](https://github.com/modelcontextprotocol/servers) - Local filesystem read and write. *Use case: File management, reading and writing files on your machine. Note: Claude Code has this built in.*
- [Google Drive](https://drive.google.com) - Find and analyze files in Drive. *Use case: Searching Google Drive, summarizing documents, cross-referencing files.*
- [iManage Work](https://imanage.com) - Governed knowledge management for law firms and professional services. *Use case: Matter-centric document and email management, version control, ethical-wall enforcement, AI-ready knowledge retrieval.*
- [iScanner](https://iscanner.com) - Scan and create PDF files. *Use case: Scanning a paper document into a PDF, converting a photo into a searchable PDF, merging scanned pages.*
- [Kiteworks MCP Server](https://www.kiteworks.com) - Connect AI assistants to a Kiteworks instance for file, folder, and search operations. *Use case: Searching files stored in Kiteworks, retrieving folder contents, running secure file operations.*
- [Lumin](https://www.luminpdf.com) - Documents, signatures, and Markdown-to-PDF conversion. *Use case: PDF annotation, e-signatures, converting Markdown to formatted PDFs.*
- [NetDocuments](https://www.netdocuments.com) - Securely access your documents in NetDocuments. *Use case: Cloud DMS for law firms and regulated industries — matter-scoped document search, version control, and governance.*
- [Nutrient DWS](https://www.nutrient.io/api/processor-api/) - Hosted document processing — generation, conversion, OCR, redaction, signatures. *Use case: HTML/Office-to-PDF conversion, AI redaction at scale, PDF form filling, watermarking, archive-grade PDF/A workflows.*
- [Nutrient PDF Editor](https://www.nutrient.io/products/pdf-editor) - View, annotate, fill forms, and redact PDFs directly from Claude. *Use case: Interactive PDF editing, form completion, redaction, and annotation without leaving the conversation.*
- [PandaDoc](https://www.pandadoc.com) - Create, send, sign, and track documents. *Use case: Proposal and quote generation, e-signature workflows, document analytics across the sales lifecycle.*
- [PDF Tools - Fill, Sign, Merge, Split, Extract](https://github.com/Open-Document-Alliance/PDF-Tools) - Local PDF workflow extension for Claude Desktop. *Use case: Fill and sign PDF forms, merge and split files, fetch PDFs from URLs, extract structured data locally without uploading.*
- [pdf-viewer](https://github.com/anthropics/anthropic-quickstarts) **`A`** - Read and interact with PDFs. *Use case: Extracting text from PDFs, answering questions about PDF content.*
- [PDF Viewer](https://github.com/anthropics/anthropic-quickstarts#pdf-viewer) **`A`** - Render PDFs from URLs. *Use case: Quick preview of PDFs from arxiv.org and other URL-based sources.*
- [PowerPoint (By Anthropic)](https://github.com/anthropics/anthropic-quickstarts#powerpoint) **`A`** - Control PowerPoint with AppleScript. *Use case: Creating and modifying presentations programmatically on macOS.*
- [Send](https://www.send.co) - Create shareable documents, one-pagers, and decks. *Use case: Turning conversations into tracked, shareable web documents with view analytics — no re-sharing required when content updates.*
- [SignNow](https://www.signnow.com) - Automate e-signatures. *Use case: Bulk signature requests, document workflow automation.*
- [SignWell](https://www.signwell.com) - E-signature workflows. *Use case: Simple document signing, tracking signature completion.*
- [Superhuman Docs](https://superhuman.com/docs) - Create, search, and update docs and tables. *Use case: Drafting a project brief, searching workspace docs for a past decision, updating a tracking table from a conversation.*
- [Word (By Anthropic)](https://github.com/anthropics/anthropic-quickstarts#word) **`A`** - Control Microsoft Word with AppleScript. *Use case: Creating and editing Word documents programmatically on macOS. Useful for formatted reports and documents.*


## Education

- [Brisk Teaching](https://www.briskteaching.com) - Build classroom activities and lessons with AI. *Use case: Lesson planning, classroom activity generation, K-12 teaching workflows.*
- [Coteach](https://coteach.ai) - Create classroom-ready K-12 math diagrams. *Use case: Building a tape diagram for an equation, generating multiple representations of a concept, creating worksheet visuals.*
- [Coursera](https://www.coursera.org) - Online courses and skill building. *Use case: Course discovery, structured skill-building paths, turning prompts into active learning.*
- [DataCamp](https://www.datacamp.com) - Course catalog and team admin for your AI assistant. *Use case: Course discovery for data skills, managing team learning assignments, tracking training progress.*
- [Diffit](https://diffit.me) - Classroom-ready differentiated resources on any topic. *Use case: Building a reading passage at multiple levels, creating a worksheet, generating differentiated materials.*
- [Eedi](https://eedi.com) - Access Eedi's math question bank. *Use case: Pulling diagnostic math questions for a lesson, building a topic quiz, finding questions targeting a specific misconception.*
- [Kuliko AI](https://kuliko.ai) - Study flashcards and quiz generator. *Use case: Building flashcard decks from study material, generating practice quizzes, running spaced-repetition review.*
- [Learning Commons Knowledge Graph](https://learningcommons.org) - K-12 standards and skills. *Use case: Curriculum alignment, standards-based assessment, educational content mapping.*
- [MagicSchool AI](https://www.magicschool.ai) - Save teaching materials to a MagicSchool Resource Library. *Use case: Storing a generated lesson plan, organizing materials by class, retrieving saved materials for reuse.*
- [Mathify](https://mathify.dev) - Create math animations. *Use case: Generating an animation of a math concept, producing a visual explanation for teaching, rendering an animated proof from a prompt.*
- [O'Reilly](https://www.oreilly.com) - Discover O'Reilly's expert learning content. *Use case: Searching technical books and courses, pulling authoritative learning material into study workflows.*
- [QuizHP](https://www.quizhp.com) - Turns any topic into an interactive quiz mini-game. *Use case: Self-quizzing on a study topic, turning a document into a grounded quiz, generating question sets by difficulty.*
- [Udemy Business](https://business.udemy.com) - Skill-building resources. *Use case: Employee training, course discovery, learning path management.*


## Entertainment

- [Ableton Knowledge](https://www.ableton.com) - Ask Claude about Ableton products. *Use case: Music production help, Ableton Live and Push reference lookups, workflow guidance for producers.*
- [Audible](https://www.audible.com) - Audiobook recommendations and library access. *Use case: Discovering new audiobooks, managing listening queue, exploring genres and series.*
- [Melon](https://www.melon.com) - Music charts and data. *Use case: Music industry analytics, charting data, trend tracking.*
- [Play Sheet Music](https://claude.com/docs/connectors/directory#play-sheet-music) - Generate and play sheet music. *Use case: Music composition, MIDI playback, music theory exploration.*
- [Splice](https://splice.com) - Royalty-free sample library, virtual instruments, and music production tools. *Use case: Searching the catalog, building sound stacks, integrating samples into music production workflows.*
- [Spotify](https://www.spotify.com) - Control Spotify playback. *Use case: Music control, playlist management, listening history.*


## Finance and Trading

- [AgentServices](https://github.com/vbkotecha/aiservices-api) - x402-paid data APIs for AI agents: crypto prices, OHLCV, DeFi yields, technical indicators, DEX swap quotes, prediction markets, on-chain analytics, marketing intelligence, IP geolocation, web search, FX rates. 37 MCP tools, 41 x402-paid endpoints. *Use case: Real-time and historical market data, agent-native API access with micropayments.*
- [Aiera](https://www.aiera.com) - Financial events, filings, and publications. *Use case: Earnings call analysis, SEC filing search, financial event monitoring.*
- [Airwallex](https://www.airwallex.com) - Global payment platform. *Use case: Cross-border payments, multi-currency accounts, payment processing.*
- [Aiwyn Tax (formerly Column Tax)](https://aiwyn.ai) - Tax estimation and analysis. *Use case: Tax planning, estimation workflows, accounting firm automation.*
- [Alpha Vantage MCP Server](https://www.alphavantage.co) - Global stock prices, fundamentals, earnings, option chains, technical indicators, indices, forex, and commodities data. *Use case: Real-time stock quotes, company fundamentals analysis, technical indicator charting.*
- [Bigdata.com](https://bigdata.com) - Real-time financial data. *Use case: Market data feeds, stock screening, financial research.*
- [Brex](https://www.brex.com) - Corporate card management and spend automation. *Use case: Expense tracking, corporate card controls, receipt management, budget monitoring.*
- [Campfire](https://campfire.ai) - AI-native ERP and accounting platform. *Use case: General ledger automation, revenue recognition, close management for high-growth finance teams.*
- [Canary Data](https://canarydata.ai) - AI-powered investment research data and analysis. *Use case: Investment idea generation, risk scoring, disclosure analysis, fundamental research.*
- [Carta](https://carta.com) - Connected ERP for private capital. *Use case: Cap-table management, 409A valuations, fund administration, and LP reporting for private companies and funds.*
- [Chargebee (US Region)](https://www.chargebee.com) - Live billing intelligence for revenue teams. *Use case: Monitoring subscription billing status, analyzing revenue metrics, managing invoicing operations.*
- [Chronograph](https://www.chronograph.pe) - Private market data. *Use case: Private equity analytics, fund performance tracking.*
- [Clarity AI](https://clarity.ai) - Sustainability data and SFDR fund classification. *Use case: ESG reporting, SFDR 2.0 fund categorization, sustainable investment disclosures.*
- [CoinDesk](https://data.coindesk.com) - Institutional-grade crypto market and on-chain data. *Use case: Real-time and historical prices across 300+ exchanges, derivatives data, on-chain metrics for Bitcoin/Ethereum, indices and reference data.*
- [CRE Agents (Vic)](https://creagents.com) - Commercial real estate expertise with expert methods, live market data, and review-ready deliverables. *Use case: Underwriting a deal, drafting an LOI or IC memo, pulling comps for market analysis.*
- [CredCore - Tusk Liquid](https://credcore.com) - Curated database of public credit-agreement terms covering covenants, debt structure, pricing, and amendments. *Use case: Researching covenant language across deals, comparing debt structures, tracking amendment history.*
- [Crypto.com](https://crypto.com) - Cryptocurrency trading. *Use case: Crypto portfolio management, trading, market data.*
- [Daloopa](https://www.daloopa.com) - Financial KPIs from public filings. *Use case: Fundamental analysis, extracting KPIs from 10-Ks and 10-Qs.*
- [D&B Finance Analytics](https://www.dnb.com/en-us/products/dnb-credit-intelligence.html) - Credit origination and workflow tools built on Dun and Bradstreet business data. *Use case: Running a credit decision on a new customer, automating a credit origination workflow, monitoring portfolio risk.*
- [D&B Risk Analytics](https://www.dnb.com/products/dnb-supplier-intelligence.html) - Supplier intelligence and third-party risk monitoring from the Dun & Bradstreet Data Cloud. *Use case: Supplier screening, ongoing risk monitoring, compliance reporting, supply-chain due diligence powered by the commercial graph.*
- [Digits](https://digits.com) - Real-time bookkeeping and financial intelligence for small businesses. *Use case: Automated transaction categorization, cash-flow forecasting, expense analysis, AI-assisted accounting.*
- [Embat](https://embat.io) - Treasury management for cash, debt, payments, and accounting. *Use case: Cash-flow forecasting, debt and payments management, accounting reconciliation for finance teams.*
- [Era Context](https://era.app/context) - Personal finance MCP server connecting bank, card, and investment accounts. *Use case: Asking Claude about real balances, spending patterns, recurring charges; automating money movement; cross-agent memory across MCP-compatible AI clients.*
- [FactSet AI-Ready Data](https://www.factset.com) - Institutional financial data. *Use case: Enterprise-grade market data, quantitative analysis, portfolio analytics.*
- [FinancialFilings](https://financialfilings.com) - Regulatory filings and financials for listed companies. *Use case: Pulling a company's latest 10-K, comparing financials across quarters, researching public disclosures.*
- [Fiscal.ai](https://fiscal.ai) - Clean public equity fundamental data. *Use case: Stock fundamentals, financial statement analysis, equity research.*
- [Fitch Solutions](https://www.fitchsolutions.com) - Credit intelligence and analysis. *Use case: Credit-risk assessment, country and industry risk research, fixed-income analysis.*
- [Flanks Aggregate](https://flanks.io) - Connect bank accounts and portfolios. *Use case: Reviewing portfolio holdings across banks, checking account balances, pulling investment transaction history.*
- [FMP](https://financialmodelingprep.com) - Financial Modeling Prep real-time and historical financial datasets. *Use case: 30+ years of fundamentals, real-time quotes via REST and WebSocket, earnings transcripts, insider and congressional ownership data.*
- [GoCardless](https://gocardless.com) - Bank-to-bank payment collection and recurring direct debit API. *Use case: Recurring billing, subscription payments, open banking payment initiation.*
- [Grasp](https://www.grasp-ai.com) - Find, screen, and analyse private-market opportunities. *Use case: Screening acquisition targets, building a buyer list for an M&A mandate, analyzing a private company before an investment.*
- [Grasshopper Bank](https://www.grasshopper.bank) - Digital business banking for startups and small businesses. *Use case: Business checking and savings, ACH and wire transfers, SBA lending, treasury management.*
- [Gusto](https://gusto.com) - Payroll, benefits, and HR for small businesses. *Use case: Running payroll, managing benefits, onboarding employees, tax filing automation.*
- [Hanover Park](https://hanoverpark.com) - Run your investment firm in real time with access to portfolio, accounting, performance, and LP data. *Use case: Portfolio and performance queries, fund-accounting lookups, LP reporting context in chat.*
- [IBISWorld](https://www.ibisworld.com) - Industry intelligence and structured market data on 50,000+ industries. *Use case: Industry benchmarking, market sizing, five-year forecasts, competitive landscape research grounded in human-verified data.*
- [ICE Data Services](https://www.ice.com/fixed-income-data-services) - U.S. fixed income trade and reference data. *Use case: Bond pricing, fixed income trade analysis, reference data for institutional fixed income desks.*
- [In Practise](https://inpractise.com) - Library of expert interviews and company primary research for fundamental investors. *Use case: Researching management commentary before an investment decision, reviewing primary research on a company, studying expert interviews for due diligence.*
- [Interactive Brokers (IBKR)](https://www.interactivebrokers.com) - Global multi-asset brokerage for stocks, options, futures, and forex. *Use case: Place and manage trades across 170+ markets, monitor portfolio and P&L, analyze positions and market data, check account balances.*
- [Intuit Credit Karma](https://www.creditkarma.com) - Credit score insights. *Use case: Personal credit monitoring, financial health assessment.*
- [Intuit QuickBooks](https://quickbooks.intuit.com) - Small business accounting, invoicing, and financial reporting. *Use case: Bookkeeping, expense categorization, invoice management, tax preparation.*
- [Intuit TurboTax](https://turbotax.intuit.com) - Consumer tax preparation and refund estimation. *Use case: Tax filing assistance, deduction identification, refund estimation.*
- [isolved People Cloud](https://www.isolvedhcm.com) - HR, payroll, and time-off management. *Use case: Requesting and tracking time off, payroll data, HR self-service workflows.*
- [Jaz Accounting](https://jaz.ai) - Full accounting platform. *Use case: Bookkeeping, financial reporting, invoice management.*
- [Lili](https://lili.co) - Access Lili business accounts or client accounts. *Use case: Checking business banking balances, reviewing recent transactions, managing client accounts for bookkeeping.*
- [LSEG](https://www.lseg.com) - Data across asset classes. *Use case: Institutional market data, fixed income, derivatives, ESG data from London Stock Exchange Group.*
- [Lumonic](https://www.lumonic.com) - Portfolio data and reporting. *Use case: Venture-debt and private-credit portfolio monitoring, financial reporting, portfolio-company analytics.*
- [LunarCrush](https://lunarcrush.com) - Social media data for markets. *Use case: Social sentiment analysis for crypto and stocks, trending asset detection.*
- [MANDA](https://manda.bz) - Japan-wide M&A and business-succession deal search. *Use case: Searching nationwide M&A listings by industry and region, finding business-succession opportunities, screening buyer or seller candidates.*
- [Mantle Portal](https://www.withmantle.com) - Intelligence layer for private markets. *Use case: Tracking capital calls and fund documents, aggregating alternative-investment data, summarizing investor statements.*
- [Massive Market Data](https://massive.com) - Stocks, options, and indices via Massive.com. *Use case: Real-time and historical market data, options chains, backtesting data feeds.*
- [Mercury](https://mercury.com) - Banking and finances on Mercury. *Use case: Startup banking, transaction management, financial operations for Mercury customers.*
- [Meridian AI](https://www.meridian-ai.com) - Query deals, companies, and documents. *Use case: Searching a private-equity deal pipeline, pulling company records, reviewing investment-committee decisions.*
- [Mesh](https://meshpayments.com) - Expense management, cards, and travel through natural language. *Use case: Issuing and managing corporate cards, automating expense-report processing, booking business travel.*
- [Metal](https://metal.ai) - AI context platform for private capital. *Use case: Deal intelligence, pipeline research, surfacing firm knowledge during diligence.*
- [Moody's Analytics](https://www.moodys.com) - Credit risk analytics and economic forecasting. *Use case: Fixed income analysis, credit risk assessment, economic scenario modeling.*
- [Morningstar](https://www.morningstar.com) - Investment insights. *Use case: Fund analysis, stock ratings, portfolio research for individual and institutional investors.*
- [Morningstar Credit Analytics](https://credit.morningstar.com) - Credit ratings, data, and analytics for structured finance. *Use case: Credit risk assessment, CMBS and CRE analysis, structured finance research, corporate credit insights.*
- [MSCI](https://www.msci.com) - Data-to-insight platform. *Use case: ESG ratings, factor models, risk analytics for institutional investors.*
- [MT Newswires](https://www.mtnewswires.com) - Real-time global financial news. *Use case: Breaking financial news, market-moving event detection, news-based trading signals.*
- [Multiples.vc](https://multiples.vc) - Public comps, M&A multiples, and VC data. *Use case: Benchmarking sector valuation multiples, pulling M&A deal comps, checking VC round pricing.*
- [NAVI Protocol](https://naviprotocol.io) - DeFi lending pool and oracle data on Sui. *Use case: Checking pool utilization and rates, pulling flash loan configuration, reviewing a wallet's claimed rewards history.*
- [Numeric](https://www.numeric.io) - Manage your close tasks, reports, and Numeric workflows. *Use case: Month-end close management, accounting workflow queries, close-status reporting.*
- [OilPriceAPI — Oil, Gas & Commodity Prices](https://www.oilpriceapi.com) - Real-time oil, gas, and commodity prices covering spot, history, futures, and alerts. *Use case: Pulling a live crude spot price, checking historical commodity trends, setting a price alert.*
- [Oracle NetSuite](https://www.netsuite.com) - Access NetSuite data. *Use case: ERP data, financial reporting, inventory management within Oracle NetSuite.*
- [Pagos](https://www.pagos.ai) - Query harmonized payments data and the Pagos BIN database. *Use case: Looking up a card BIN for routing decisions, reconciling payments data across processors, investigating a decline pattern.*
- [Parallel](https://getparallel.com) - Query a Parallel financial model. *Use case: Checking current runway and burn, modeling the impact of a new hire, prepping a board or investor report.*
- [PayPal](https://www.paypal.com) - Payment processing and transaction history. *Use case: Transaction management, payment tracking, dispute monitoring, financial reporting.*
- [Paytm for Business](https://business.paytm.com) - Paytm payments for businesses. *Use case: Accepting and managing payments, transaction reporting, business payment workflows.*
- [Pinegap](https://www.pinegap.ai) - AI-powered equity research platform. *Use case: Ramping up on a newly covered company, pulling peer comps and historical valuation, prepping management questions before earnings.*
- [PitchBook](https://pitchbook.com) - Private market data. *Use case: Venture capital research, startup valuations, M&A data, fundraising intelligence.*
- [Plaid](https://plaid.com) - Financial data integration. *Use case: Bank account linking, transaction data, identity verification for fintech apps.*
- [Privacy.com](https://privacy.com) - Manage virtual cards and track spending patterns. *Use case: Generating burner virtual cards per merchant, capping merchant spend, monitoring subscription leakage and unauthorized charges.*
- [Pyth](https://pyth.network) - Access financial market data across every asset class. *Use case: Real-time and historical price feeds for crypto, equities, and FX from the Pyth oracle network.*
- [Qonto](https://qonto.com) - Business banking and finances. *Use case: Managing business accounts, payments, invoices, and expense tracking for European SMBs.*
- [Quartr](https://quartr.com) - Earnings call transcripts and investor presentation research. *Use case: Fundamental analysis, listening to management commentary, tracking company guidance.*
- [Ramp](https://ramp.com) - Financial data from Ramp. *Use case: Corporate spend management, expense tracking, vendor management.*
- [Razorpay](https://razorpay.com) - Payment processing and subscription management for Indian markets. *Use case: Online payment collection, recurring billing, payment analytics.*
- [Revolut X](https://www.revolut.com/revolut-x/) - Advanced crypto exchange with low fees. *Use case: Crypto trading, market and limit orders, backtesting, portfolio management for active traders.*
- [Rho](https://www.rho.co) - Analyze and model Rho business finances. *Use case: Reviewing business banking transactions, modeling cash flow, analyzing spend by category.*
- [Rillet](https://www.rillet.com) - Live general-ledger and financials querying in plain English. *Use case: Natural-language GL queries, real-time financial reporting, finance team self-service analytics.*
- [Rydoo](https://www.rydoo.com) - Expense management through conversation. *Use case: Submitting an expense report, checking reimbursement status, categorizing a receipt.*
- [Sequence](https://www.sequencehq.com) - Billing, invoicing, and revenue data tools. *Use case: Chasing overdue invoices, reporting invoiced revenue by period, auditing product pricing setup.*
- [Spendflo](https://www.spendflo.com) - AI-native procurement platform. *Use case: Tracking SaaS spend across vendors, flagging renewal risk before deadlines, benchmarking vendor pricing during negotiations.*
- [Spendify](https://spendify.ca) - Track spending, manage budgets, and analyze finances. *Use case: Monitoring monthly spending against budget categories, generating an expense report, flagging unusual transactions.*
- [S&P Global](https://www.spglobal.com) - Query financial datasets. *Use case: Market intelligence, credit ratings, commodity data, institutional research.*
- [Square](https://squareup.com) - Transaction and payment data. *Use case: POS data, payment analytics, merchant services management.*
- [Stripe](https://stripe.com) - Payment processing infrastructure. *Use case: Payment management, subscription billing, revenue analytics, checkout configuration.*
- [Switch](https://switch-soft.com) - Spanish-language ERP covering sales, accounts receivable, and inventory. *Use case: Checking overdue receivables, reviewing monthly sales against inventory levels, reconciling invoices issued through the ERP.*
- [Tabs](https://tabs.com) - Revenue operations at scale. *Use case: Automating invoice-to-cash for usage-based billing, reconciling revenue recognition across contracts, reviewing outstanding receivables.*
- [TaxAct](https://www.taxact.com) - Estimate your refund and check what documents you need. *Use case: Tax-refund estimation, document checklists, filing preparation guidance.*
- [Tiller](https://tiller.com) - Connect to transactions in a Tiller spreadsheet. *Use case: Pulling recent bank transactions into a budgeting review, reconciling a spreadsheet against actual spending, generating a monthly cash-flow summary.*
- [Tropic](https://www.tropicapp.io) - SaaS procurement and contract negotiation intelligence. *Use case: Software spend benchmarking, renewal negotiation, vendor contract management.*
- [Vendr Software Pricing Tools](https://www.vendr.com) - Software pricing insights. *Use case: SaaS procurement, license negotiation, software spend optimization.*
- [Verisk Underwriting Intelligence](https://www.verisk.com/resources/verisk-underwriting-intelligence/) - ISO loss costs, indications, and experience-trend data for P&C insurers. *Use case: Plain-language queries against actuarial filings, indication-driver analysis, loss-cost trend research for underwriting and pricing teams.*
- [Verisk XactRestore](https://www.verisk.com/products/xactrestore/) - Natural-language restoration job estimating. *Use case: Building water-mitigation and remediation estimates with restoration-specific pricing, project tracking, Xactimate integration for restoration contractors.*
- [viaNexus vAST](https://vianexus.com) - Agent-ready financial data marketplace. *Use case: Pulling market data feeds, integrating financial datasets into agents, sourcing trading data.*
- [Xero](https://www.xero.com) - Cloud accounting for small business. *Use case: Bank reconciliation, invoicing, expense tracking, financial reporting from your Xero ledger.*
- [Yardi Matrix](https://www.yardimatrix.com) - Commercial real estate market intelligence. *Use case: Multifamily and commercial real estate research, market data, underwriting and investment analysis.*
- [Zoho Books](https://www.zoho.com/books) - Online accounting and finance operations. *Use case: Invoicing, expense management, bank reconciliation, financial reporting within the Zoho ecosystem.*


## Government and Nonprofit

- [Benevity](https://www.benevity.com) - Nonprofit discovery and corporate giving platform. *Use case: Corporate social responsibility programs, donation matching, nonprofit vetting.*
- [Blackbaud](https://www.blackbaud.com) - Software for nonprofits, foundations, and education. *Use case: Fundraising, donor management, grantmaking, nonprofit financial management.*
- [Candid](https://candid.org) - Research nonprofits and funders. *Use case: Grant research, foundation discovery, nonprofit due diligence.*
- [GovQuery](https://govquery.ai) - Search US government reports and oversight recommendations. *Use case: Researching GAO audit findings on a federal program, finding open Inspector General recommendations, pulling agency press releases on a topic.*
- [GovTribe](https://govtribe.com) - Federal procurement, awards, and spending intelligence. *Use case: Government contract discovery, competitive intelligence, agency spending analysis, capture management.*
- [Granted](https://granted.dev) - Discover grant opportunities. *Use case: Finding federal, state, and foundation grants. Useful for researchers, nonprofits, and anyone writing grant applications.*
- [Instrumentl](https://www.instrumentl.com) - Grant discovery and management. *Use case: Finding matching grants, tracking applications and deadlines, grant prospecting for nonprofits and researchers.*
- [JP Bid](https://jp-bid.com) - Japan government procurement bid search and analysis. *Use case: Finding open procurement bids in an industry, analyzing a bid's requirements before proposing, tracking upcoming tenders.*
- [Kindora Funder Discovery](https://www.kindora.co) - AI funder discovery for nonprofits. *Use case: Matching mission-aligned funders, grant prospecting, personalized funder outreach for fundraising teams.*
- [MoSPI](https://www.mospi.gov.in) - India official statistics. *Use case: Indian economic data, demographic statistics, government datasets.*
- [Planning Center](https://www.planningcenteronline.com) - Church management data access. *Use case: Pulling a congregation's giving report, checking volunteer scheduling, looking up a member's group involvement.*
- [Policy Doctor](https://policydoctor.com) - Regulatory monitoring, analysis, and public affairs intelligence. *Use case: Tracking a bill's progress through committee, monitoring an agency's rulemaking docket, briefing on an emerging policy risk.*
- [Tango](https://www.tango.us) - US Government contracting data. *Use case: Federal procurement research, contract analysis, government sales intelligence.*


## Healthcare and Life Sciences

- [10x Genomics Cloud](https://www.10xgenomics.com) - Access the 10x Genomics platform. *Use case: Single-cell genomics, spatial transcriptomics, chromatin accessibility analysis.*
- [AdisInsight](https://adisinsight.springer.com) - Drug, clinical trial, and pharma pipeline intelligence. *Use case: Drug development tracking, competitive pipeline analysis, licensing opportunity identification.*
- [Alma](https://alma.food) - AI nutrition coach that tracks meals and micronutrients. *Use case: Reviewing logged meals and macros, identifying micronutrient gaps, tracking diet-quality score trends, GLP-1 and athlete nutrition coaching.*
- [Amass Connector](https://amass.tech) - Unifies life sciences intelligence across publications, trials, drugs, genes, regulatory approvals, and patents in one cross-linked connector. *Use case: Researching a drug's regulatory approval history, cross-referencing a target across publications and patents, tracking competitor pipeline trials.*
- [Benchling](https://www.benchling.com) - R&D data and notebooks. *Use case: Lab notebook management, experiment tracking, biological sequence design.*
- [Biomni Lab](https://biomni.phylo.bio) - Integrated biology environment for AI-native research. *Use case: Agentic biology workflows, computational research, AI-native lab automation.*
- [BioRender](https://www.biorender.com) - Scientific templates and icons. *Use case: Creating publication-quality scientific figures, graphical abstracts, pathway diagrams.*
- [bioRxiv](https://www.biorxiv.org) - Access bioRxiv and medRxiv preprint data. *Use case: Preprint search for biology and medicine, catching research 6-12 months before peer review.*
- [Boltz API](https://boltz.bio) - Predict molecular structures and binding interactions. *Use case: Protein structure prediction, binding-affinity screening, binder design for drug discovery.*
- [ChEMBL](https://www.ebi.ac.uk/chembl) - Access ChEMBL drug compound data. *Use case: Drug discovery research, compound activity data, target-drug relationships.*
- [Clinical Trials](https://clinicaltrials.gov) - Access ClinicalTrials.gov data. *Use case: Finding active trials, checking eligibility criteria, tracking trial results, identifying recruiting studies.*
- [CMS Coverage](https://www.cms.gov/medicare-coverage-database) - Access the CMS Coverage Database. *Use case: Checking Medicare coverage determinations, prior authorization requirements, coverage policy lookups.*
- [Consensus](https://consensus.app) - Explore scientific research with AI synthesis. *Use case: Evidence-based research across 200M+ papers, systematic literature review, finding consensus across studies.*
- [Cortellis Regulatory Intelligence](https://clarivate.com/life-sciences-healthcare/research-development/regulatory-compliance-intelligence/regulatory-intelligence-solutions/) - Global pharma regulatory intelligence platform. *Use case: Regulatory compliance, submission strategy, global requirement monitoring, life sciences R&D.*
- [DappleOS](https://dappleos.com) - Cosmetic medicine practice management across clinical, operational, and commercial workflows. *Use case: Managing patient intake for an aesthetics clinic, scheduling treatments, handling billing for cosmetic procedures.*
- [Demographic and Health Surveys](https://dhsprogram.com) - Data from The DHS Program. *Use case: Global population, health, and demographic survey data, public health research, cross-country health-indicator analysis.*
- [EDEN by Basecamp Research](https://basecamp-research.com) - Biological foundation model for antibiotic and vaccine design. *Use case: Designing antibiotics and prioritizing vaccine targets against drug-resistant pathogens.*
- [Enrichr MCP Server](https://maayanlab.cloud/Enrichr) - Gene set enrichment analysis. *Use case: Genomics research, pathway analysis, gene ontology enrichment.*
- [Function](https://www.functionhealth.com) - Lab test insights and health answers (beta). *Use case: Biomarker data analysis, lab result trends, personalized health insights from blood work.*
- [HealthEx](https://healthex.io) - Connect health records (beta). *Use case: Health record integration, personal health data access.*
- [Helix GenoSphere](https://www.helix.com) - Query human genomics and longitudinal clinical data. *Use case: Population genomics research, clinical-genomic data exploration.*
- [ICD-10 Codes](https://www.cms.gov/medicare/coding-billing/icd-10-codes) - Access ICD-10-CM and ICD-10-PCS code sets. *Use case: Clinical coding, diagnostic classification, billing code lookup, health informatics.*
- [Inductive Bio](https://www.inductive.bio) - State-of-the-art ADMET prediction models for drug discovery. *Use case: ADMET property prediction for any chemical structure, lead optimization.*
- [Ketryx](https://www.ketryx.com) - Regulated software lifecycle data for medical device and life sciences teams. *Use case: FDA-compliant SDLC tracking, design control, traceability for SaMD/SiMD development.*
- [LatchBio](https://latch.bio) - Analyze data and launch bioinformatics workflows. *Use case: Running bioinformatics pipelines, biological data analysis, computational biology workflow orchestration.*
- [Medidata](https://www.medidata.com) - Clinical trial software. *Use case: Clinical trial data management, EDC systems, regulatory compliance in trials.*
- [NPI Registry](https://npiregistry.cms.hhs.gov) - US National Provider Identifier lookup. *Use case: Provider verification, referral workflows, healthcare directory lookups, credentialing.*
- [Open Targets](https://www.opentargets.org) - Drug target discovery. *Use case: Target identification, disease-gene associations, drug repurposing research.*
- [PopHIVE](https://www.pophive.org) - Yale's harmonized US public health surveillance data, covering immunizations, respiratory disease, chronic conditions, and hospital capacity. *Use case: Checking regional flu and RSV trends, monitoring hospital capacity in a service area, tracking vaccination coverage rates.*
- [PubMed](https://pubmed.ncbi.nlm.nih.gov) - Search biomedical literature. *Use case: Medical literature search, finding clinical evidence, systematic reviews, accessing abstracts and full-text articles via NCBI.*
- [Redacta](https://www.pharmatools.ai/redacta) - On-device de-identification of PII and patient identifiers. *Use case: Pseudonymizing patient identifiers and PII in text and restoring them locally, privacy-preserving clinical data handling.*
- [Revvity Signals AI](https://revvitysignals.com) - Natural-language access to the Signals electronic lab notebook. *Use case: ELN search, research data retrieval, lab-notebook querying.*
- [SandboxAQ](https://www.sandboxaq.com) - Large quantitative models for scientific discovery. *Use case: Quantum-grade simulation for drug-design lead optimization, protein-ligand binding, materials science, and PQC cryptography research.*
- [SNOMED CT Terminology](https://www.snomed.org) - Search, validate, and expand SNOMED CT concepts from SNOMED International. *Use case: Looking up a clinical concept code, validating a SNOMED CT term for a record, expanding a concept hierarchy for terminology mapping.*
- [Synapse.org](https://www.synapse.org) - Access scientific data on Synapse. *Use case: Open science data sharing, collaborative research datasets, challenge platforms.*
- [Synthesize Bio](https://www.synthesize.bio) - Generative genomics: predict gene expression from natural-language experiment descriptions. *Use case: Drug-discovery hypothesis testing, biomarker prediction, in silico RNA-seq experiments grounded in the largest annotated public corpus.*
- [Turquoise](https://turquoise.health) - Healthcare pricing data. *Use case: Querying hospital and payer prices, healthcare cost transparency, rate benchmarking.*
- [Virtual Fly Brain](https://virtualflybrain.org) - Drosophila anatomy, neurons, connectomics, genes, and transcriptomics. *Use case: Exploring fly neural circuits, querying connectome data, researching gene expression.*


## Jobs

- [Ashby](https://www.ashbyhq.com) - Search, analyze, and act on recruiting data. *Use case: Reviewing candidate pipeline status, analyzing hiring funnel metrics, acting on recruiting tasks from a conversation.*
- [BrightHire](https://brighthire.com) - Interview intelligence and hiring data. *Use case: Recording and analyzing interviews, structured hiring decisions, candidate evaluation insights.*
- [Deel](https://www.deel.com) - Manage your global workforce, right in Claude. *Use case: International hiring and payroll queries, contractor management, cross-border compliance context.*
- [Dice](https://www.dice.com) - Technology-focused job search and career marketplace. *Use case: Finding tech roles, salary benchmarking, tech hiring market data.*
- [Indeed](https://www.indeed.com) - Job search across all industries and experience levels. *Use case: Job discovery, salary research, employer reviews, hiring market analysis.*
- [Metaview](https://www.metaview.ai) - AI recruiting and interview intelligence. *Use case: Interview transcription and summarization, candidate search, automated ATS updates for hiring teams.*
- [Recooty](https://recooty.com) - AI-powered hiring platform. *Use case: Posting a job opening, screening applicant resumes, tracking candidates through a pipeline.*
- [Remote.com](https://remote.com) - Connect AI to your Remote employment infrastructure. *Use case: Global payroll and HR data access, employment records, onboarding workflows.*
- [Snagajob](https://www.snagajob.com) - Hourly job search and applications. *Use case: Searching hourly job openings, applying to a posting, tracking application status.*
- [Tenzo AI](https://tenzo.ai) - Query Tenzo candidates, jobs, and AI screening calls. *Use case: Pulling a summary of a candidate's screening interview, comparing finalists for an open role, auditing screening transcripts for compliance review.*
- [Upwork](https://www.upwork.com) - Freelance talent marketplace. *Use case: Finding and hiring freelancers, managing contracts, sourcing talent for projects.*
- [Workable](https://www.workable.com) - Hiring and HR platform with applicant tracking and AI sourcing. *Use case: Posting to 200+ job boards, AI-powered candidate sourcing, interview scheduling, performance reviews, onboarding.*
- [ZipRecruiter](https://www.ziprecruiter.com) - Job-search marketplace with AI-powered matching. *Use case: Searching open US roles, salary research, candidate-employer matching for job seekers and small-business hiring.*


## Legal

- [Aurora](https://consilio.com) - Consilio Aurora matter, document, and review intelligence. *Use case: Searching eDiscovery matters, surfacing documents across review platforms, accelerating litigation workflows.*
- [BoardWise](https://boardwise.com) - Board-defense guidance for licensed professionals. *Use case: Calm, structured guidance for physicians and other licensees facing board complaints or disciplinary actions.*
- [Clarivate IPOne CompuMark Trademarks](https://clarivate.com/intellectual-property/compumark/) - Trademark intelligence. *Use case: Trademark clearance searches, brand protection, IP risk assessment.*
- [CoCounsel Legal](https://legal.thomsonreuters.com/en/c/cocounsel) - Thomson Reuters CoCounsel Legal, in Claude. *Use case: Westlaw-grade research, contract review, deposition prep, and brief drafting with Thomson Reuters' legal AI.*
- [CourtListener](https://www.courtlistener.com) - Legal research across millions of court records. *Use case: Federal and state opinion search, docket monitoring, citation analysis from the Free Law Project's open archive.*
- [Courtroom5](https://courtroom5.com) - Civil legal guidance for self-represented litigants. *Use case: Pro se procedural support, motion drafting templates, case-strategy guidance for litigants without counsel.*
- [Definely](https://www.definely.com) - Structured contract review tools for legal teams. *Use case: Defined-term review, cross-reference checking, and definition-level navigation inside long contracts.*
- [Descrybe Legal Engine](https://descrybe.ai) - Ground your work in clean, structured U.S. primary law. *Use case: Statute-and-case research grounded in normalized primary-law data, with citation-level provenance.*
- [Everlaw](https://www.everlaw.com) - Search and explore your Everlaw eDiscovery database. *Use case: Litigation document review, deposition-binder building, predictive coding queries inside Everlaw matters.*
- [Harvey](https://www.harvey.ai) - Legal queries, vault search, and research. *Use case: Legal research, case law analysis, contract review, document search within Harvey's legal AI platform.*
- [HeyCounsel](https://www.heycounsel.com) - Lawyer network, work opportunities, templates, and benchmarks. *Use case: Finding contract work through a lawyer network, benchmarking billing rates against peers, accessing legal document templates.*
- [Intapp Celeste](https://www.intapp.com/celeste/) - Agentic AI for regulated professional firms. *Use case: Conflict clearance, ethical walls, compliance-aware workflows for law firms and advisory services.*
- [Ironclad Contracts](https://ironcladapp.com) - Plain-language search for faster contract answers. *Use case: Natural-language queries across executed contracts, obligation tracking, clause and counterparty lookup.*
- [Juridata](https://juridata.ma) - Sourced Moroccan law, built to scale across Africa. *Use case: Researching a Moroccan statute, finding case law for a court proceeding, comparing legal frameworks across African jurisdictions.*
- [Jus Mundi](https://jusmundi.com) - Global arbitration intelligence. *Use case: Researching precedent in an international arbitration, finding an arbitrator's prior rulings, comparing arbitration clauses across treaties.*
- [Lawve AI](https://lawve.ai) - Expert-written skills for legal work. *Use case: Workflow library of attorney-authored task skills (drafting, review, research) callable from Claude.*
- [Legal Data Hunter](https://legaldatahunter.com) - Search 23M+ legal docs in 160+ jurisdictions. *Use case: Cross-jurisdictional case and statute search, comparative-law research, multi-country regulatory review.*
- [LegalZoom](https://www.legalzoom.com) - Business formation and attorney-assisted legal services. *Use case: LLC formation, trademark filing, estate planning documents, on-demand attorney guidance.*
- [Lloyd by The L Suite](https://www.lsuite.co/lloyd) - In-house counsel insights for L Suite members. *Use case: Peer-curated in-house legal guidance, playbooks, and benchmarking for corporate legal teams.*
- [Midpage Legal Research](https://www.midpage.ai) - Legal research and work product. *Use case: Case law search, legal citation analysis, brief drafting support, jurisdiction-specific research.*
- [Ontra](https://www.ontra.ai) - Contract automation for private markets. *Use case: Automating routine legal contracts, NDA workflows, obligation management for investment firms.*
- [Relativity](https://www.relativity.com) - Organize data, discover the truth, act on it. *Use case: eDiscovery, internal investigations, and regulatory response inside the RelativityOne review platform.*
- [SeedLegals](https://seedlegals.com) - Legal and fundraising platform for startups. *Use case: Drafting funding round documents, managing a cap table, handling equity paperwork.*
- [Solve Intelligence](https://www.solveintelligence.com) - Search, draft, and chart patents. *Use case: Patent prior-art search, claim drafting, prosecution-history analysis, and IP-portfolio visualization.*
- [TopCounsel by The L Suite](https://topcounsel.ai) - Outside counsel recommendations from in-house counsel. *Use case: Vendor selection and warm-intro outside-counsel referrals sourced from in-house attorney peers.*
- [Trellis](https://trellis.law) - Claude for trial court litigators. *Use case: State trial-court data search, judge analytics, motion outcomes, and litigant history across U.S. trial courts.*


## Lifestyle and Local

- [Aisle Wedding](https://aislewedding.com) - AI-assisted destination wedding planning. *Use case: Building a destination wedding itinerary, comparing venues and vendors, coordinating guest travel logistics.*
- [CourtsApp](https://courtsapp.com) - Book tennis, pickleball, and racquet courts. *Use case: Finding open court time nearby, booking recurring sessions, coordinating games.*
- [DoorDash](https://www.doordash.com) - Food, grocery, and retail delivery. *Use case: Same-day food and grocery delivery, order tracking, restaurant discovery, local errands.*
- [Figaro Immobilier](https://immobilier.lefigaro.fr) - French real estate listings search. *Use case: Searching listings in a French city, comparing rental prices in a neighborhood, tracking new listings.*
- [Fresha](https://www.fresha.com) - Find and book beauty, grooming, and wellness appointments. *Use case: Booking a haircut, finding a nearby spa, scheduling a massage.*
- [Glovo](https://glovoapp.com) - Anything delivered in minutes. *Use case: Food delivery, grocery shopping, courier services across 1500+ cities in Europe, LATAM, and Africa.*
- [Honeydew](https://honeydewcook.com) - Search a recipe library and turn it into grocery lists and meal plans. *Use case: Building a weekly meal plan from saved recipes, generating a grocery list, finding a recipe by ingredient.*
- [Instacart](https://www.instacart.com) - Grocery and household delivery as fast as 30 minutes. *Use case: Grocery shopping automation, recipe-to-cart workflows, household supply restocking.*
- [Order by Cash App](https://cash.app) - Discover local food spots and order with a conversation. *Use case: Finding nearby restaurants, placing food orders, paying through Cash App, tracking local merchant deals.*
- [Peepz](https://peepz.ai) - Foster healthy relationships in your groups. *Use case: Coordinating get-togethers with a friend circle, staying on top of group birthdays and check-ins, reducing the friction of staying connected.*
- [PGA – Play Golf](https://www.pga.com) - Find a golf coach. *Use case: Locating a PGA-certified instructor nearby, booking a lesson, comparing coaching options before a trip.*
- [Promocodes.com](https://www.promocodes.com) - Finds promo codes, coupons, and deals. *Use case: Finding a discount code before checkout, comparing deals across retailers, tracking coupon expiration.*
- [Resy](https://resy.com) - Restaurant discovery and reservation booking. *Use case: Finding restaurants, booking tables, managing dining plans.*
- [Shop](https://shop.app) - Shopify's consumer shopping app across favorite brands. *Use case: Tracking a package delivery, browsing products from favorite brands, managing saved payment info.*
- [Spot2](https://spot2.mx) - Search and explore commercial real estate in México. *Use case: Finding office or warehouse space in a Mexican city, comparing industrial property listings, researching commercial lease terms by region.*
- [Strava](https://www.strava.com) - GPS fitness tracking for running, cycling, and other activities. *Use case: Activity tracking, training analysis, route discovery, fitness community engagement.*
- [Tarteel](https://tarteel.ai) - Quran search, tafsir, translations, and recitations. *Use case: Searching verses, comparing translations, studying tafsir, finding recitations.*
- [Taskrabbit Booking Assistance](https://www.taskrabbit.com) - Find and book local Tasker services. *Use case: Furniture assembly, moving help, handyman services, errands, local task booking.*
- [Thumbtack](https://www.thumbtack.com) - Find and hire local pros. *Use case: Home services, contractors, event vendors, professional services discovery and booking.*
- [Uber Eats](https://www.ubereats.com) - Restaurant discovery and food delivery. *Use case: Restaurant search, dish recommendations, order placement, delivery tracking.*
- [wer kennt den BESTEN](https://www.werkenntdenbesten.de) - Find and compare local services in Germany. *Use case: Searching local service providers, comparing reviews, finding tradespeople.*
- [Zomato](https://www.zomato.com) - Online food ordering and delivery. *Use case: Ordering food delivery, browsing restaurant menus, tracking delivery status.*


## Marketing and Sales

- [ActiveCampaign](https://www.activecampaign.com) - Marketing automation. *Use case: Email campaigns, lead scoring, CRM automation, customer journey mapping.*
- [Actively](https://www.actively.ai) - AI agents that work every account across the revenue funnel. *Use case: Pipeline generation, deal execution, account prioritization, GTM sales intelligence.*
- [Adobe Journey Optimizer](https://business.adobe.com/products/journey-optimizer.html) - Campaign and customer journey orchestration. *Use case: Cross-channel campaign troubleshooting, journey performance analysis, marketing automation diagnostics.*
- [Adobe Marketing Agent](https://business.adobe.com/blog/introducing-adobe-marketing-agent-microsoft-365-copilot) - Marketing campaign and audience insights from the Adobe stack. *Use case: Campaign performance analysis, audience segmentation, cross-product Adobe marketing diagnostics.*
- [Affinity](https://www.affinity.co) - Relationship intelligence CRM for private capital. *Use case: Venture capital and private equity deal sourcing, warm-intro mapping, automatic CRM enrichment.*
- [AfterShip Channels for TikTok Shop](https://www.aftership.com) - Lists, syncs, and grows a TikTok Shop business. *Use case: Syncing TikTok Shop product listings, monitoring order status, tracking sales growth.*
- [Apollo.io](https://www.apollo.io) - Find buyers and book meetings. *Use case: Sales prospecting, lead enrichment, outbound campaign management.*
- [Attention](https://www.attention.com) - Sales conversation intelligence. *Use case: Analyzing client calls, CRM auto-fill, surfacing coaching insights and next steps from conversations.*
- [Attio](https://attio.com) - Search and manage CRM data. *Use case: Modern CRM workflows, relationship tracking, deal management.*
- [AutoDS — Dropshipping Product Research & Store Automation](https://www.autods.com) - Finds dropshipping products and automates store operations. *Use case: Researching trending products, automating listings across stores, managing order fulfillment.*
- [Braze MCP Server](https://www.braze.com) - Access Braze REST API. *Use case: Customer engagement campaigns, push notification management, marketing automation.*
- [Brevo](https://www.brevo.com) - Marketing campaigns, audience insights, and drafts. *Use case: Email and SMS campaigns, audience segmentation, drafting and analyzing marketing sends.*
- [CB Insights](https://www.cbinsights.com) - Predictive intelligence. *Use case: Market research, startup tracking, industry trend analysis, competitive intelligence.*
- [Channel3 MCP](https://trychannel3.com) - Product search across the internet. *Use case: Finding and comparing products across merchants, searching for an item by description, retrieving product offers for a shopping agent.*
- [Clarify](https://www.clarify.ai) - Query CRM and create records. *Use case: CRM data management, contact creation, pipeline tracking.*
- [Clay](https://www.clay.com) - Find prospects, research, and outreach. *Use case: Lead enrichment, personalized outreach, prospect research automation.*
- [Close](https://www.close.com) - Inside sales CRM for calls, emails, and pipeline. *Use case: Sales pipeline management, call tracking, email sequences for inside sales teams.*
- [Cloze MCP](https://cloze.com) - Relationship management CRM that automatically tracks emails, calls, meetings, and social interactions. *Use case: Summarizing contact history, logging a follow-up task, pushing a listing to a marketing tool.*
- [Common Room](https://www.commonroom.io) - Community and go-to-market signal detection across social, product, and support channels. *Use case: Identifying high-intent prospects, tracking community engagement, surfacing buying signals.*
- [Crossbeam](https://www.crossbeam.com) - Partner data and ecosystem intelligence. *Use case: Partner overlap analysis, co-selling opportunities, ecosystem mapping.*
- [Customer.io](https://customer.io) - Explore customer data. *Use case: Behavioral messaging, customer segmentation, lifecycle email campaigns.*
- [Day AI](https://www.day.ai) - AI-powered CRM with automatic relationship tracking. *Use case: Prospect research, contact enrichment, pipeline management, meeting prep.*
- [Euler](https://eulerapp.com) - Partner relationship management platform for partner and affiliate programs. *Use case: Onboard and manage channel partners, track partner-sourced deals and revenue, manage affiliate and reseller programs, query partner program data conversationally.*
- [folk](https://www.folk.app) - Search, create, and update a folk CRM. *Use case: Looking up a contact before a meeting, logging a new lead from an email thread, updating a deal's stage after a call.*
- [G2](https://www.g2.com) - B2B software buyer intent and review data. *Use case: Identifying accounts researching your category, competitive analysis, leveraging review insights for sales.*
- [Gainsight (CS)](https://www.gainsight.com/customer-success/) - Customer success data and automation. *Use case: Customer health scoring, renewal and churn workflows, querying and writing back CS data.*
- [Gainsight (Staircase AI)](https://www.gainsight.com) - Customer success management and health scoring. *Use case: Renewal forecasting, churn prevention, customer health monitoring, expansion tracking.*
- [Harmonic](https://www.harmonic.ai) - Discover companies and people. *Use case: Company discovery, people search, market mapping for sales and recruiting.*
- [Highspot](https://highspot.com) - Sales enablement and content. *Use case: Surfacing and sharing sales content, deal actions, buyer engagement to win deals.*
- [HilltopAds](https://hilltopads.com) - Check HilltopAds campaigns, stats, and balances. *Use case: Monitoring ad campaign performance, checking account balance, reviewing traffic statistics.*
- [HubSpot](https://www.hubspot.com) - All-in-one CRM, marketing, and sales platform. *Use case: CRM queries, marketing analytics, sales pipeline management, inbound marketing.*
- [Insider One](https://insiderone.com) - Query the Insider One CDP and APIs in natural language. *Use case: Customer data platform queries, cross-channel marketing orchestration.*
- [Intuit Mailchimp](https://mailchimp.com) - Marketing campaign management. *Use case: Email campaigns, audience segmentation, marketing analytics.*
- [item](https://item.app) - Search, analyze, and act on CRM data. *Use case: Pulling a customer's deal history before a call, updating a CRM record from a conversation, triggering a sales workflow action.*
- [Klaviyo](https://www.klaviyo.com) - Real-time marketing data. *Use case: E-commerce email and SMS marketing, customer segmentation, predictive analytics.*
- [Leadsquared](https://www.leadsquared.com) - Access to LeadSquared CRM. *Use case: Querying leads and opportunities, updating CRM records, automating sales follow-up tasks.*
- [Lightfield](https://lightfield.app) - AI-native CRM. *Use case: A CRM that captures context automatically, surfacing relationship history and next steps.*
- [LoyaltyLion](https://loyaltylion.com) - Loyalty program management. *Use case: Managing loyalty point rules, reviewing reward redemptions, analyzing program performance.*
- [Lusha](https://www.lusha.com) - B2B contact and company enrichment. *Use case: Sales prospecting, verified email and direct-dial discovery, CRM data enrichment, buying-signal detection.*
- [magnews](https://www.magnews.com) - Email marketing analytics and automation. *Use case: Analyzing email campaign performance, automating marketing workflows, segmenting subscriber lists.*
- [MailerLite](https://www.mailerlite.com) - Email marketing and subscriber management. *Use case: Newsletter campaigns, landing pages, automation workflows, subscriber segmentation.*
- [Motion Creative Analytics](https://motionapp.com) - Meta ad creative performance and competitor ad-library analysis. *Use case: Identifying winning Facebook/Instagram ad creatives, comparing against competitor libraries, optimizing dynamic creative variants for ROAS.*
- [Nexoya](https://www.nexoya.com) - Query cross-channel attribution, budget optimizations, and campaign performance. *Use case: Comparing channel attribution, getting recommended budget shifts, reviewing campaign KPI trends.*
- [Nooks](https://www.nooks.ai) - Search, access, and get insights on Nooks data. *Use case: Reviewing dialer call outcomes, pulling sequence performance, checking sourced signals on target accounts.*
- [OpenFunnel Agent Primitives](https://openfunnel.ai) - Durable and benchmarked primitives for in-house GTM engineering. *Use case: Building a custom lead-scoring agent, benchmarking a GTM automation before shipping, assembling reusable sales-ops components.*
- [Outreach](https://www.outreach.io) - Team performance and engagement. *Use case: Sales engagement, sequence automation, pipeline management.*
- [Peec AI](https://peec.ai) - Brand visibility analytics across LLMs. *Use case: Tracking how brands appear in ChatGPT/Claude/Gemini answers, AI-search SEO, generative-engine optimization.*
- [Pendo](https://www.pendo.io) - Product and user insights. *Use case: Product analytics, in-app guidance, user onboarding, feature adoption tracking.*
- [Phoenix by HG Insights](https://hginsights.com) - AI-powered B2B data intelligence and analytics. *Use case: Account-level technographic and firmographic intelligence, market mapping, and sales targeting grounded in HG's IT-spend dataset.*
- [Polar Analytics](https://www.polaranalytics.com) - Shopify and DTC e-commerce analytics dashboard. *Use case: Centralizing Shopify, ad, and marketing data in one dashboard; tracking gross/net sales, retention, and profit metrics for DTC brands.*
- [Productised](https://www.productised.ai) - Create assessments and lead magnets. *Use case: Building a lead-diagnostic quiz, generating a personalized readiness scorecard, producing a branded outcome report for a prospect.*
- [Realize MCP](https://ads.realizeperformance.com) - Create, manage, and analyze Realize (Taboola) advertising campaigns. *Use case: Launching a native ad campaign, monitoring campaign performance, adjusting targeting and budget.*
- [SaaSify - Cloud Marketplaces GTM Platform](https://saasify.ai) - Cloud-marketplace revenue, subscriptions, deals, and pricing across AWS, Microsoft, and Google Cloud. *Use case: Tracking marketplace deal pipeline, analyzing co-sell revenue, managing marketplace pricing.*
- [Salesflare](https://salesflare.com) - Manage and explore a Salesflare CRM. *Use case: Looking up a contact's deal history, updating a pipeline stage, reviewing CRM activity.*
- [Salesloft](https://www.salesloft.com) - AI revenue orchestration and sales engagement platform. *Use case: Sales cadence automation, pipeline generation, deal management, conversation intelligence.*
- [Seismic](https://www.seismic.com) - Sales enablement content access with generative search. *Use case: Finding sales content for a deal, searching enablement material, surfacing a case study for a prospect.*
- [Sociality.io](https://sociality.io) - Analyze social media performance, competitor activity, and post-level results. *Use case: Benchmarking competitor campaigns, tracking engagement trends across platforms, compiling performance reports.*
- [Sprouts Data Intelligence](https://sproutsai.com) - Query to qualified lead. *Use case: Lead qualification, data enrichment, sales intelligence.*
- [Sumble](https://sumble.com) - Account research on teams, tech, and people. *Use case: Deep account intelligence, tech-stack discovery, org mapping for sales prospecting.*
- [Sybill](https://www.sybill.ai) - Sales calls and pipeline intelligence. *Use case: AI meeting summaries, behavioral analysis of sales calls, pipeline updates.*
- [Trussi AI](https://trussi.ai) - Roofing CRM covering projects, customers, pipeline, schedules, and dashboards. *Use case: Managing a roofing sales pipeline, scheduling crews, tracking customer projects.*
- [Vibe Prospecting](https://www.vibeprospecting.ai) - Company and contact data. *Use case: B2B prospecting, company information, contact discovery.*
- [Watching That](https://watchingthat.com) - Ad stack data covering yield insights, revenue performance, and delivery issues. *Use case: Monitoring video ad revenue, troubleshooting fill-rate issues, tracking yield performance.*
- [Wistia](https://wistia.com) - Video hosting, captions, channels, and analytics. *Use case: Hosting marketing videos, generating captions, tracking video engagement.*
- [Zoho CRM](https://www.zoho.com/crm) - CRM pipeline and workflow automation within the Zoho ecosystem. *Use case: Contact management, deal tracking, sales automation, lead scoring.*
- [ZoomInfo](https://www.zoominfo.com) - Enrich contacts and accounts. *Use case: B2B data enrichment, company intelligence, contact information, sales targeting.*


## Observability and Monitoring

- [Coralogix](https://coralogix.com) - Explore and debug observability data. *Use case: Log and metrics analysis, troubleshooting incidents, querying telemetry without indexing costs.*
- [Datadog](https://www.datadoghq.com) - End-to-end observability across logs, metrics, and traces. *Use case: APM, infrastructure visibility, distributed tracing, security threat detection across the full stack.*
- [Dynatrace MCP Server](https://www.dynatrace.com) - Observability via DQL. *Use case: Application performance monitoring, infrastructure observability, root cause analysis.*
- [Grafana MCP Server](https://grafana.com) - Dashboards and alerting. *Use case: Monitoring infrastructure, querying Prometheus/Loki, visualizing metrics.*
- [Honeycomb](https://www.honeycomb.io) - High-cardinality observability for distributed systems. *Use case: Distributed tracing, debugging production issues, query-driven investigation.*
- [incident.io](https://incident.io) - Incident management. *Use case: Declaring and managing incidents, post-mortems, on-call coordination.*
- [Jam](https://jam.dev) - Screen recording for bug reports. *Use case: Capturing and sharing browser-based bug reproductions with context.*
- [Kastra](https://kastra.ai) - Execution-governance and audit-trail layer for Claude Code actions. *Use case: Reviewing an agent's action history, auditing automated changes before they ship, enforcing authorization policy on agent execution.*
- [Lightrun](https://lightrun.com) - Connect AI assistants to live production runtime data including snapshots, call stacks, and metrics. *Use case: Debugging a production issue with a live snapshot, inspecting a call stack without redeploying, pulling runtime metrics into a session.*
- [MCP Instana Server](https://www.instana.com) - Observability platform. *Use case: Auto-instrumented application monitoring, infrastructure visibility.*
- [OpenReplay MCP](https://openreplay.com) - Session replay and product analytics. *Use case: Reviewing user session replays, debugging frontend issues, analyzing product-usage charts.*
- [PagerDuty](https://www.pagerduty.com) - Incidents and on-call management. *Use case: Incident response, on-call scheduling, alerting workflows.*
- [Sentry](https://sentry.io) - Error tracking and debugging. *Use case: Monitoring production errors, stack trace analysis, performance monitoring, release health.*
- [Tsuga](https://www.tsuga.com) - Query telemetry and manage assets. *Use case: Investigating production incidents, searching logs and traces, monitoring infrastructure assets.*


## Productivity

- [Airtable](https://www.airtable.com) - Structured data in Claude. *Use case: Database-spreadsheet hybrid, project tracking, content calendars, inventory management.*
- [AppFolio Realm-X](https://www.appfolio.com/ai) - Operate your property portfolio. *Use case: Property-management operations, portfolio queries, tenant and leasing workflows from Claude.*
- [Basic Memory Cloud](https://basicmemory.com) - Shared knowledge base for people, AI tools, and teams, structured as a living graph of plain Markdown. *Use case: Maintaining a team knowledge base, syncing notes across AI tools, building a searchable markdown graph.*
- [Blinq](https://blinq.me) - Digital contacts and business-card app. *Use case: Creating a digital business card, capturing contact details at events, following up with new contacts.*
- [Celayix](https://www.celayix.com) - Workforce management data. *Use case: Querying employees, shifts, scheduling, time off, and site assignments, workforce reporting.*
- [CloudMindMaps](https://www.cloudmindmaps.com) - AI mind map generator that turns notes, docs, and ideas into shareable mind maps, compatible with .mm files. *Use case: Converting meeting notes into a mind map, turning a document outline into a visual map, sharing a mind map with collaborators.*
- [Cognito Forms](https://www.cognitoforms.com) - Online form builder with workflow automation. *Use case: Data collection, custom forms, approval workflows, no-code business solutions.*
- [Craft](https://www.craft.do) - Notes and second brain. *Use case: Linked note-taking, document creation, knowledge management on Apple devices.*
- [DeepL](https://deepl.com) - Translate text and documents across 100+ languages with a configured style. *Use case: Translating a contract, localizing marketing copy, translating an email reply.*
- [Dex Personal CRM](https://getdex.com) - Manage Dex personal CRM contacts. *Use case: Logging a conversation with a contact, setting a follow-up reminder, reviewing relationship history.*
- [Dovetail](https://dovetail.com) - Customer feedback and research repository. *Use case: User research synthesis, customer interview analysis, feedback theming and decision tracking.*
- [Drafts](https://getdrafts.com) - Access Drafts on macOS. *Use case: Quick text capture, processing notes into actions, markdown drafting.*
- [Glean](https://www.glean.com) - Enterprise context and search. *Use case: Searching across all company knowledge sources, finding internal information.*
- [Goodnotes](https://www.goodnotes.com) - AI insights from documents. *Use case: Handwritten note analysis, document search, study note management.*
- [iknow.dev](https://iknow.dev) - Knowledge management platform agents can read and write via MCP. *Use case: Logging accumulated expertise to a shared knowledge base, retrieving documented know-how for a task, building a searchable knowledge library.*
- [Jotform](https://www.jotform.com) - Online form builder and submission management. *Use case: Custom form creation, collecting payments and registrations, routing submissions to downstream tools.*
- [Klarity](https://www.klarity.com) - Explore your org's processes. *Use case: AI-powered process intelligence, workflow mapping, and contract data extraction across operational systems.*
- [Lace Labs](https://inlace.co) - Team knowledge layer shared across agents. *Use case: Briefing an agent on team context and past decisions, tracing agent output back to source work, sharing a knowledge graph across workflows.*
- [Lattice](https://lattice.com) - HR platform covering goals, performance reviews, and employee records. *Use case: Checking goal and performance-review progress, pulling employee records, prepping for a 1:1.*
- [LILT](https://lilt.com) - Enterprise translation and localization platform. *Use case: Multilingual content management, translation memory, real-time document translation workflows.*
- [Mem](https://mem.ai) - AI-powered self-organizing notebook. *Use case: Auto-tagged note management, knowledge retrieval, meeting notes with semantic search.*
- [Memoket](https://memoket.ai) - Read-only access to your own meeting recordings, transcripts, and summaries. *Use case: Querying a past meeting transcript, retrieving action items from a recorded call, summarizing a week of calls.*
- [Microsoft 365](https://www.microsoft.com/microsoft-365) - SharePoint, OneDrive, Outlook, and Teams access. *Use case: Enterprise document search, email and calendar workflows, Teams chat context, SharePoint knowledge mining.*
- [Noteplan](https://noteplan.co) - Markdown-based planning and daily notes for macOS. *Use case: Markdown-based planning, daily notes, task management integrated with calendar.*
- [Notion](https://www.notion.so) - Connect your Notion workspace. *Use case: Knowledge base management, project documentation, wiki search, database queries.*
- [ProductNow](https://productnow.ai) - Turns prototype feedback into traceable product decisions. *Use case: Triaging user feedback on a prototype, tracing decisions back to source feedback, keeping a team aligned on rationale.*
- [prox](https://useprox.com) - Search, read, and edit industrial product knowledge. *Use case: Manufacturing and engineering knowledge management, product-documentation search and editing.*
- [Read and Write Apple Notes](https://support.apple.com/guide/notes) - Read, write, and organize notes in Apple Notes. *Use case: Quick capture, reading note content, creating structured notes from Claude.*
- [Readwise](https://readwise.io) - Save, read, search, and learn. *Use case: Surfacing highlights from books and articles, spaced-repetition review, searching your reading archive.*
- [Roam Research](https://roamresearch.com) - Read, search, and write in Roam graphs. *Use case: Searching notes across a graph, adding linked notes, reviewing daily notes.*
- [SpeakApp](https://speakapp.com) - AI transcripts and summaries for meetings, voice notes, and lectures. *Use case: Transcribing and summarizing a team meeting, converting a lecture recording into study notes, logging voice memos into searchable text.*
- [Spinach AI](https://www.spinach.ai) - AI meeting notes and action system. *Use case: Meeting summaries, action-item tracking, turning conversation data into follow-through.*
- [SurveyMonkey](https://www.surveymonkey.com) - Design surveys, collect responses, and analyze results. *Use case: Survey design, distribution, response analysis, quantitative research workflows.*
- [TickTick](https://ticktick.com) - Search, create, and manage your tasks and habits in TickTick. *Use case: Task capture from conversation, habit tracking, daily planning.*
- [Todoist](https://www.todoist.com) - Task management with natural-language scheduling. *Use case: Capturing tasks, organizing by Today/Upcoming/custom filters, recurring tasks, shared team projects.*
- [Trint](https://trint.com) - Brings Trint transcripts and files into the chat. *Use case: Pulling meeting transcripts into a workflow, searching recorded content, repurposing transcript text.*
- [Voicenotes](https://voicenotes.com) - Search and chat with Voicenotes. *Use case: Querying transcribed voice memos, turning spoken ideas into structured notes.*
- [Yardi Virtuoso](https://www.yardi.com) - Real estate and property management data from Yardi. *Use case: Property management, real estate portfolio analytics, tenant management.*
- [Zsper](https://zsper.com) - AI writing tool with memory of the author's style. *Use case: Drafting content in your own voice, maintaining writing context across sessions, personalizing AI-assisted writing.*


## Project Management

- [Adobe Workfront](https://business.adobe.com/products/workfront.html) - Enterprise work management: planning, projects, tasks, approvals. *Use case: Enterprise work management, project planning, resource allocation, approval workflows.*
- [Asana](https://asana.com) - Tasks, projects, and goals. *Use case: Team task management, project planning, goal tracking, workflow automation.*
- [Backlog MCP Server](https://nulab.com/services/backlog/) - Nulab Backlog project management. *Use case: Issue tracking, Git/SVN repository management, wiki documentation, and Gantt-chart project planning within Nulab's Backlog platform.*
- [ClickUp](https://clickup.com) - All-in-one project and task management platform. *Use case: Team task tracking, time management, document collaboration, sprint planning.*
- [Linear](https://linear.app) - Issues, projects, and team workflows. *Use case: Software development project tracking, issue management, sprint planning. Popular with engineering teams.*
- [Monday](https://monday.com) - Projects, boards, and workflows. *Use case: Visual project management, cross-team workflows, custom automations.*
- [Pathmode](https://pathmode.io) - Strategic context and dependency graphs. *Use case: Strategic planning, dependency visualization, project prioritization.*
- [Process Street](https://www.process.st) - Process and workflow data. *Use case: Standard operating procedures, recurring workflow management, compliance checklists.*
- [Saga](https://github.com/spranab/saga-mcp) - Jira-like project tracker for AI agents. *Use case: Per-project task hierarchy and activity logging so agents keep track of multi-step work.*
- [Smartsheet](https://www.smartsheet.com) - Analyze and manage data. *Use case: Enterprise work management, resource planning, portfolio management.*
- [Strety](https://strety.com) - Brings EOS Rocks, Issues, Scorecard, To-dos, and Level 10 meetings into Claude. *Use case: Prepping for a weekly leadership meeting, reviewing quarterly Rocks progress, tracking open Issues and To-dos across a team.*
- [Trello](https://trello.com) - Boards, lists, and cards for team task tracking. *Use case: Tracking project boards, managing task lists, organizing team workflows.*
- [Wrike](https://www.wrike.com) - Work and project management. *Use case: Managing tasks and projects, updating work items, moving work forward across teams.*
- [Zoho Projects](https://www.zoho.com/projects) - Task and project automation. *Use case: Project management within the Zoho ecosystem, Gantt charts, time tracking.*


## Research and Academic

- [alphaXiv](https://www.alphaxiv.org) - Search and full-text access over arXiv preprints. *Use case: Finding and reading arXiv papers, full-text search, staying current on research.*
- [Atomscale](https://www.atomscale.ai) - Search, analyze, and build insights from materials science and engineering data. *Use case: Extracting information from synthesis and characterization data, analyzing materials-processing datasets, accelerating materials research.*
- [Elicit](https://elicit.com) - Search and analyze scientific papers. *Use case: Literature-review automation, extracting findings across papers, evidence synthesis for research questions.*
- [Guidepoint](https://www.guidepoint.com) - On-demand expert network with 1.6M+ industry advisors. *Use case: Sourcing 1:1 expert calls, scheduling surveys for consensus checks, accessing curated expert transcripts for institutional research and consulting projects.*
- [HaitiDocs](https://www.haitidocs.org) - Haiti documents, data, and maps supporting research and policy development. *Use case: Researching historical documents for an academic paper, pulling maps and data for a policy brief, supporting development-sector research.*
- [Oxford Economics](https://www.oxfordeconomics.com) - Economic analysis and forecast data. *Use case: Pulling GDP or inflation forecasts for a market, checking macro risk analysis for a region, citing economic data in a report.*
- [Scholar Gateway](https://scholargateway.com) - Scholarly research and citation discovery. *Use case: Academic paper search, citation analysis, cross-disciplinary research that spans beyond biomedical literature.*
- [Scholar Sidekick](https://scholar-sidekick.com) - Resolve scholarly identifiers and citations. *Use case: Converting DOI, PMID, PMCID, ISBN, and arXiv IDs into citation styles, retraction and open-access checks, citation verification.*
- [Scite](https://scite.ai) - Evidence-based answers grounded in research. *Use case: Smart citations showing whether papers support or contrast a claim, AI-assisted literature review, citation context analysis.*
- [Third Bridge](https://www.thirdbridge.com) - Expert insights and 100,000+ vetted transcripts across 65,000+ companies. *Use case: Investment-thesis validation, due-diligence research, accessing forensic-style expert transcripts inline during research workflows.*


## SAP

- [SAP CAP MCP Server](https://cap.cloud.sap) - SAP Cloud Application Programming Model. *Use case: Building enterprise apps on SAP Business Technology Platform.*
- [SAP Fiori MCP Server](https://www.sap.com/products/technology-platform/fiori.html) - Enterprise UX development for SAP applications. *Use case: SAP enterprise UX development, Fiori element configuration.*
- [SAP MDK MCP Server](https://developers.sap.com/topics/mobile-development-kit.html) - SAP Mobile Development Kit. *Use case: Building SAP mobile apps, offline-capable enterprise mobile development.*
- [SAPUI5 MCP Server](https://sapui5.hana.ondemand.com) - SAP web application development using the SAPUI5 framework. *Use case: SAP web application development using the SAPUI5 framework.*


## Security

- [Apiiro Guardian](https://apiiro.com) - Application security risk context and developer guardrails. *Use case: Querying code-to-runtime risk, surfacing AppSec findings, remediating security issues before code ships.*
- [BigID](https://bigid.com) - Explore, manage, and act on organizational data. *Use case: Discovering sensitive data across systems, managing privacy compliance, acting on data governance policy.*
- [Conviso MCP Server](https://www.convisoappsec.com) - Application security metrics. *Use case: AppSec posture management, vulnerability tracking, security program metrics.*
- [DataGrail](https://www.datagrail.io) - Agentic data privacy orchestration. *Use case: DSR fulfillment, privacy impact assessments, PII discovery across SaaS stacks, AI governance.*
- [Defense.com Threat Analysis](https://www.defense.com) - Cybersecurity threat intelligence and monitoring. *Use case: Attack surface management, threat detection, vulnerability prioritization.*
- [GoPlus AgentGuard](https://agentguard.gopluslabs.io) - Security guard for AI agents. *Use case: Blocking malicious skills, preventing data leaks, protecting secrets in agent workflows.*
- [Have I Been Pwned](https://haveibeenpwned.com) - Check email addresses and domains for data breaches. *Use case: Breach-exposure checks during security reviews, domain-wide compromise monitoring.*
- [Is It Legit by M8ven](https://m8ven.ai) - Checks whether a brand or company is legitimate. *Use case: Verifying an unfamiliar online store before purchasing, checking a vendor's legitimacy before a transfer, screening a business before signing a contract.*
- [Isometric](https://isometric.com) - Agentic certification for the industrial economy. *Use case: Verifying a carbon removal or industrial claim, certifying an industrial process against a standard, auditing a supply chain claim.*
- [Malwarebytes](https://www.malwarebytes.com) - Check links, phone numbers, and emails for scams. *Use case: On-demand scam detection for suspicious URLs and contacts, phishing triage, consumer-grade threat checks.*
- [McAfee](https://www.mcafee.com) - Scam protection for messages, links, and more. *Use case: Checking a suspicious link before clicking, scanning a message for scam indicators, verifying sender legitimacy.*
- [Miggo](https://www.miggo.io) - Vulnerability and findings management. *Use case: Security finding triage, vulnerability management, risk assessment.*
- [Norton](https://us.norton.com) - Verify scams from web and email. *Use case: Checking suspicious links, phone numbers, and emails for scam patterns before engaging.*
- [Origin](https://www.originhq.com) - Visibility into AI agent activity across your fleet. *Use case: Monitoring what AI agents do across endpoints, fleet-wide agent observability, endpoint security.*
- [PanOS MCP](https://www.paloaltonetworks.com) - Palo Alto Networks firewall management. *Use case: Firewall rule management, network security configuration, PAN-OS administration.*
- [Phished](https://phished.io) - Security awareness training and phishing simulation data. *Use case: Checking an employee's phishing click-rate trend, reviewing a simulated campaign's results, pulling an organization's behavioral risk score.*
- [Rapid7 Bulk Export](https://www.rapid7.com) - Bulk export of Rapid7 vulnerability and exposure data. *Use case: Pulling InsightVM/InsightAppSec findings into reports, bulk asset and vulnerability data analysis.*
- [Robtex Network Intelligence](https://robtex.com) - DNS, IP, domain reputation, and network intelligence. *Use case: Looking up DNS records, checking an IP's reputation, investigating a network for security research.*
- [Scorechain](https://www.scorechain.com) - Blockchain AML tooling. *Use case: Screening a crypto wallet for AML risk, tracing transaction flows, generating a compliance report.*
- [Snyk Security](https://snyk.io) - Developer-first security platform for code, dependencies, containers, and IaC. *Use case: SAST/SCA scanning, vulnerability triage with reachability analysis, AI-generated code security guardrails, automated fix PRs.*
- [Sumsub](https://sumsub.com) - Verify identities and businesses, and prevent fraud. *Use case: Running KYC checks during onboarding, screening users against sanctions and watchlists, investigating linked accounts in a suspected fraud ring.*
- [Zscaler MCP Server](https://www.zscaler.com) - Zero Trust Exchange. *Use case: Zero trust network access, cloud security, secure web gateway management.*


## SEO and Web

- [Ahrefs](https://ahrefs.com) - SEO and AI search analytics. *Use case: Backlink analysis, keyword research, site audits, competitive SEO analysis.*
- [AirOps](https://www.airops.com) - Content that wins AI search. *Use case: SEO content optimization, AI-era search strategy, programmatic content.*
- [Apify](https://apify.com) - Extract data from any website. *Use case: Web scraping, data extraction, automated content collection at scale.*
- [Bitly](https://bitly.com) - Link shortening and QR codes. *Use case: Link management, click analytics, branded short URLs, QR code generation.*
- [Cloudinary](https://cloudinary.com) - Image and video management. *Use case: Media asset optimization, image transformation, CDN delivery.*
- [Cloudinary Asset Management](https://cloudinary.com/products/digital_asset_management) - Digital asset management. *Use case: Media library management, asset organization, DAM workflows.*
- [Evarist](https://evarist.ai) - AI-native website traffic analytics. *Use case: Asking why traffic dropped, finding top referral sources, identifying pages with high bounce rates.*
- [Exa](https://exa.ai) - Neural web search and code documentation search. *Use case: AI-powered web search that understands intent. Describe the ideal page in natural language instead of keywords. Returns clean content ready for LLM use.*
- [GoDaddy](https://www.godaddy.com) - Domain search and availability. *Use case: Domain registration, DNS management, domain availability checking.*
- [Lnk.Bio](https://lnk.bio) - Add, edit, and style Lnk.Bio links, blocks, and pages. *Use case: Building a link-in-bio page, updating link blocks, restyling a bio page.*
- [Local Falcon](https://www.localfalcon.com) - Local search intelligence. *Use case: Local SEO tracking, Google Maps ranking analysis, local search visibility.*
- [Nimble](https://www.nimbleway.com) - Real-time web search and data extraction. *Use case: Web scraping and extraction for AI agents, structured data from any site, real-time web access.*
- [Profound](https://www.tryprofound.com) - AI search visibility and citation analytics. *Use case: Tracking brand visibility in AI answers, citation and AI-bot-visit data, AI-search optimization.*
- [Semrush](https://www.semrush.com) - SEO, market data, and brand visibility insights. *Use case: Keyword research, competitor SEO analysis, content audits, paid-search planning, and brand-mention monitoring across organic and AI search.*
- [Tavily](https://tavily.com) - Connect AI agents to the web. *Use case: Web search API for AI applications, real-time web data access.*


## Ticketing and Events

- [Fever Event Discovery](https://feverup.com) - Discover live events and experiences worldwide. *Use case: Finding concerts, immersive experiences, tours, and cultural events across 200+ cities.*
- [Quinbook](https://quinbook.com) - Ticketing and booking management. *Use case: Managing bookings, slots, calendars, contacts, coupons, and cart and order operations in plain language.*
- [StubHub](https://www.stubhub.com) - Secondary-market ticket marketplace for concerts, sports, and theater. *Use case: Finding event tickets, price comparison across the world's largest ticket marketplace, last-minute event access.*
- [Ticketmaster](https://www.ticketmaster.com) - Search Ticketmaster for events and view tickets. *Use case: Finding upcoming concerts in a city, checking ticket availability and pricing, looking up already-purchased tickets.*
- [Ticket Tailor](https://www.tickettailor.com) - Event platform for tickets and orders. *Use case: Event ticketing, order management, attendee tracking.*
- [Tixel](https://tixel.com) - Buy and sell tickets safely, fan to fan, at fair prices. *Use case: Finding resale tickets with price caps, listing spares, avoiding ticket fraud.*


## Travel

- [AllTrails](https://www.alltrails.com) - Hike, bike, and trail discovery with reviews and maps. *Use case: Finding nearby trails, planning outdoor activities, accessing trail conditions and reviews.*
- [Booking.com](https://www.booking.com) - Hotels, homes, apartments, and accommodations worldwide. *Use case: Hotel search, vacation rental booking, multi-property comparison, travel planning.*
- [CargoAi](https://www.cargoai.co) - Air cargo rates, quotes, and tracking. *Use case: Instant air-freight pricing, booking quotes, shipment tracking for logistics teams.*
- [Cottages](https://www.cottages.com) - Discover UK holiday cottages. *Use case: Finding self-catering stays across the UK, comparing cottage options for dates and party size.*
- [DirectBooker](https://www.directbooker.com) - Compare and book hotels. *Use case: Hotel search, price comparison, direct booking.*
- [Expedia](https://www.expedia.com) - Flights, hotels, car rentals, and vacation packages. *Use case: Travel planning, hotel comparison, flight + hotel bundling, multi-leg trip building.*
- [GuruWalk](https://www.guruwalk.com) - Free walking tours and activities in 200+ cities. *Use case: Finding a free walking tour in a city, booking a local guide for a day trip, discovering activities while traveling.*
- [Kiwi.com](https://www.kiwi.com) - Flight search with multi-city and self-transfer routing. *Use case: Complex itinerary building, budget flight discovery, multi-carrier route planning.*
- [komoot](https://www.komoot.com) - Discover outdoor routes and highlights. *Use case: Planning hikes and bike tours, finding community-recommended highlights along a route.*
- [lastminute.com](https://www.lastminute.com) - Last-minute travel deals for flights and hotels. *Use case: Spontaneous trip planning, discounted flight and hotel packages.*
- [Novasol](https://www.novasol.com) - Search holiday homes across Europe. *Use case: Finding a vacation rental for a family trip, comparing holiday home pricing by region, checking availability for a date range.*
- [Otto Travel](https://ottotheagent.com) - Business travel planning and booking. *Use case: Planning trips, booking flights and hotels, managing corporate travel.*
- [Ryanair](https://www.ryanair.com) - Explore Ryanair routes and find cheap flights. *Use case: Low-cost route discovery across Europe, fare comparison with date flexibility.*
- [Super.com](https://www.super.com) - Compare hotels and find the lowest rate. *Use case: Hotel price comparison, discounted room discovery, budget travel planning.*
- [Telgani](https://www.telgani.com) - Car rental across Saudi Arabia. *Use case: Booking a rental car for a trip to Riyadh, comparing rental rates across Saudi cities, extending a reservation.*
- [TomTom Maps](https://www.tomtom.com) - Interactive maps, routing, geocoding, and traffic. *Use case: Route planning, real-time traffic, geocoding, map visualization.*
- [TomTom Maps MCP](https://developer.tomtom.com) - Real-time geospatial context from TomTom covering maps, routing, search, geocoding, and traffic. *Use case: Turn-by-turn routing with live traffic, geocoding a batch of addresses, searching nearby points of interest.*
- [Traveler.md](https://traveler.md) - Portable travel memory covering preferences and trips. *Use case: Recalling seat and airline preferences when booking, pulling up an upcoming itinerary, carrying travel history between planning tools.*
- [Tripadvisor](https://www.tripadvisor.com) - Hotel discovery powered by traveler reviews. *Use case: Review-driven hotel selection, restaurant and attraction discovery, trip planning research.*
- [Trivago](https://www.trivago.com) - Hotel price comparison across booking platforms. *Use case: Finding the best hotel rates, comparing properties, travel planning.*
- [Turkish Airlines](https://www.turkishairlines.com) - Search flights, plan trips, and manage bookings. *Use case: Flight search and booking across Turkish Airlines' global network, Miles&Smiles account management, multi-city itinerary building.*
- [Uber](https://www.uber.com) - Ride pricing and ETA estimates for any ride option. *Use case: Comparing ride options, trip cost estimation, transportation planning.*
- [Veltra Activities](https://www.veltra.com) - Book tours, activities, and things to do worldwide. *Use case: Finding local experiences at a destination, comparing tour options, booking activities.*
- [Viator](https://www.viator.com) - Tours, activities, and travel experiences worldwide. *Use case: Booking travel experiences, day tours, multi-day itineraries, attraction tickets.*
- [Wyndham Hotels and Resorts](https://www.wyndhamhotels.com) - Discover Wyndham hotels. *Use case: Wyndham property search, loyalty program management, hotel booking.*


## Related

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Model Context Protocol servers powering many of the connectors above.
- [awesome-chatgpt-apps](https://github.com/rdmgator12/Chtgpt-Apps-Awesome-List) - Companion list cataloging apps in the ChatGPT directory.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM-powered applications across providers.


---


[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Ralph Martello](https://github.com/rdmgator12) has waived all copyright and related or neighboring rights to this work.
