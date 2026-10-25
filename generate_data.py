import json

proprietary_tools = [
    {
        "id": "notion",
        "name": "Notion",
        "tagline": "All-in-one workspace for notes, docs, and project management",
        "category": "Productivity & Notes",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://notion.so",
        "website": "https://notion.so",
        "description": "Notion is a popular proprietary collaboration platform for note-taking, task management, and databases."
    },
    {
        "id": "airtable",
        "name": "Airtable",
        "tagline": "Low-code platform for building relational database workflows",
        "category": "Database & Spreadsheets",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://airtable.com",
        "website": "https://airtable.com",
        "description": "Airtable is a cloud-based collaborative database and spreadsheet hybrid."
    },
    {
        "id": "trello",
        "name": "Trello",
        "tagline": "Kanban-style visual task management and collaboration tool",
        "category": "Project Management",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://trello.com",
        "website": "https://trello.com",
        "description": "Trello is a popular Kanban project management web application originally created by Fog Creek."
    },
    {
        "id": "slack",
        "name": "Slack",
        "tagline": "Real-time team messaging and channel-based collaboration",
        "category": "Team Communication",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://slack.com",
        "website": "https://slack.com",
        "description": "Slack is an enterprise messaging application designed for team communication and file sharing."
    },
    {
        "id": "typeform",
        "name": "Typeform",
        "tagline": "Interactive conversational forms, surveys, and quizzes",
        "category": "Forms & Surveys",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://typeform.com",
        "website": "https://typeform.com",
        "description": "Typeform specializes in dynamic online form building and user-friendly online surveys."
    },
    {
        "id": "1password",
        "name": "1Password",
        "tagline": "Password management and secure credential storage",
        "category": "Security & Passwords",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://1password.com",
        "website": "https://1password.com",
        "description": "1Password provides secure password storage, digital vaults, and enterprise access management."
    },
    {
        "id": "zapier",
        "name": "Zapier",
        "tagline": "Workflow automation platform connecting web apps",
        "category": "Automation & Integration",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://zapier.com",
        "website": "https://zapier.com",
        "description": "Zapier connects thousands of web apps to automate repetitive business processes."
    },
    {
        "id": "jira",
        "name": "Jira",
        "tagline": "Agile issue tracking and software project management",
        "category": "Developer Tools",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://atlassian.com",
        "website": "https://www.atlassian.com/software/jira",
        "description": "Jira is an enterprise software development and bug tracking system developed by Atlassian."
    },
    {
        "id": "calendly",
        "name": "Calendly",
        "tagline": "Automated meeting scheduling and calendar booking platform",
        "category": "Scheduling",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://calendly.com",
        "website": "https://calendly.com",
        "description": "Calendly eliminates email tag for scheduling meetings and appointments with clients."
    },
    {
        "id": "docusign",
        "name": "DocuSign",
        "tagline": "Electronic signatures and digital agreement management",
        "category": "Document Management",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://docusign.com",
        "website": "https://docusign.com",
        "description": "DocuSign is the world leader in electronic signature technology and digital contracts."
    },
    {
        "id": "mailchimp",
        "name": "Mailchimp",
        "tagline": "Marketing automation and email newsletter platform",
        "category": "Marketing & Email",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://mailchimp.com",
        "website": "https://mailchimp.com",
        "description": "Mailchimp is a marketing automation platform and email marketing service for businesses."
    },
    {
        "id": "shopify",
        "name": "Shopify",
        "tagline": "Cloud e-commerce platform for online stores and POS systems",
        "category": "E-Commerce",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://shopify.com",
        "website": "https://shopify.com",
        "description": "Shopify is an all-in-one commerce platform powering millions of businesses worldwide."
    }
]

projects = [
    {
        "id": "appflowy",
        "name": "AppFlowy",
        "tagline": "Open-source AI collaborative workspace for wikis, docs, and tasks",
        "category": "Productivity & Notes",
        "alternative_to": ["notion"],
        "github_repo": "AppFlowy-IO/AppFlowy",
        "stars": 77800,
        "forks": 6100,
        "license": "AGPL-3.0",
        "languages": ["Rust", "Flutter", "Dart"],
        "website": "https://appflowy.io",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://appflowy.io",
        "screenshot": "https://raw.githubusercontent.com/AppFlowy-IO/AppFlowy/main/assets/images/appflowy-banner.png",
        "description": "AppFlowy is the leading open-source alternative to Notion. Built with Rust and Flutter, it offers complete data control, local-first storage, native desktop apps, and customizable AI extensions.",
        "features": [
            "100% Data privacy & offline local-first mode",
            "Kanban boards, tables, calendars, and nested pages",
            "Self-hosted sync server support via Docker",
            "Native performance across Windows, macOS, and Linux"
        ]
    },
    {
        "id": "affine",
        "name": "AFFiNE",
        "tagline": "Next-gen workspace merging docs, whiteboards, and relational tables",
        "category": "Productivity & Notes",
        "alternative_to": ["notion", "trello"],
        "github_repo": "toeverything/AFFiNE",
        "stars": 74100,
        "forks": 3900,
        "license": "MIT",
        "languages": ["TypeScript", "Rust"],
        "website": "https://affine.pro",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://affine.pro",
        "screenshot": "https://raw.githubusercontent.com/toeverything/AFFiNE/master/assets/cover.png",
        "description": "AFFiNE combines docs, infinite whiteboards, and multi-dimensional tables into a unified block-based environment. Privacy-focused with full peer-to-peer and self-hosting options.",
        "features": [
            "Seamless switch between Document mode and Whiteboard canvas",
            "Local-first architecture with real-time CRDT sync",
            "Extensible plugin system and Markdown export",
            "True MIT open-source license"
        ]
    },
    {
        "id": "nocodb",
        "name": "NocoDB",
        "tagline": "Open source Airtable alternative that turns any SQL database into a smart spreadsheet",
        "category": "Database & Spreadsheets",
        "alternative_to": ["airtable"],
        "github_repo": "nocodb/nocodb",
        "stars": 65500,
        "forks": 4200,
        "license": "AGPL-3.0",
        "languages": ["TypeScript", "Vue", "Node.js"],
        "website": "https://nocodb.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://nocodb.com",
        "screenshot": "https://raw.githubusercontent.com/nocodb/nocodb/develop/packages/nc-gui/assets/img/icons/512x512.png",
        "description": "NocoDB connects directly to PostgreSQL, MySQL, SQLite, or SQL Server and generates an intuitive spreadsheet interface with grid, gallery, kanban, and form views.",
        "features": [
            "Works on top of your existing production databases",
            "REST APIs & Webhooks for workflow automation",
            "Fine-grained role-based access control (RBAC)",
            "Collaborative multi-user spreadsheet views"
        ]
    },
    {
        "id": "focalboard",
        "name": "Focalboard",
        "tagline": "Self-hosted project and task management for technical teams",
        "category": "Project Management",
        "alternative_to": ["trello", "notion"],
        "github_repo": "mattermost/focalboard",
        "stars": 26800,
        "forks": 2200,
        "license": "MIT",
        "languages": ["Go", "TypeScript", "React"],
        "website": "https://www.focalboard.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://focalboard.com",
        "screenshot": "https://www.focalboard.com/static/hero-screenshot.png",
        "description": "Focalboard (by Mattermost) is a multilingual, open-source project management solution that replaces Trello, Notion, and Asana with clean Kanban and table boards.",
        "features": [
            "Kanban, table, calendar, and gallery card layouts",
            "Single-binary standalone install or Docker deployment",
            "Deep integration with Mattermost team chats",
            "Unlimited board filtering, properties, and templates"
        ]
    },
    {
        "id": "planka",
        "name": "Planka",
        "tagline": "Real-time collaborative Kanban board for workgroups",
        "category": "Project Management",
        "alternative_to": ["trello"],
        "github_repo": "plankanban/planka",
        "stars": 12800,
        "forks": 1100,
        "license": "AGPL-3.0",
        "languages": ["JavaScript", "React", "Node.js"],
        "website": "https://planka.app",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://planka.app",
        "screenshot": "https://raw.githubusercontent.com/plankanban/planka/master/client/public/images/screenshot.png",
        "description": "Planka is a sleek, lightweight Kanban board alternative to Trello. Supports projects, multiple boards, lists, cards, attachments, checklists, and real-time updates.",
        "features": [
            "Real-time team collaboration with WebSocket synchronization",
            "Custom card labels, deadlines, and markdown descriptions",
            "OIDC / Single Sign-On (SSO) authentication support",
            "Ultra-lightweight Docker container setup"
        ]
    },
    {
        "id": "mattermost",
        "name": "Mattermost",
        "tagline": "Secure team communication and collaboration platform",
        "category": "Team Communication",
        "alternative_to": ["slack"],
        "github_repo": "mattermost/mattermost",
        "stars": 32000,
        "forks": 7300,
        "license": "Apache-2.0",
        "languages": ["Go", "React", "TypeScript"],
        "website": "https://mattermost.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://mattermost.com",
        "screenshot": "https://mattermost.com/wp-content/uploads/2022/03/Channels_Overview.png",
        "description": "Mattermost provides enterprise-grade team messaging, voice calling, workflow playbooks, and file sharing designed for DevOps and technical organizations.",
        "features": [
            "Channel-based messaging, direct messages, and group threads",
            "End-to-end encrypted voice calling & screen sharing",
            "Full compliance, data sovereignty, and audit logs",
            "Rich integration with GitHub, GitLab, Jira, and CI/CD"
        ]
    },
    {
        "id": "zulip",
        "name": "Zulip",
        "tagline": "Organized team chat with unique topic-based threading",
        "category": "Team Communication",
        "alternative_to": ["slack"],
        "github_repo": "zulip/zulip",
        "stars": 26200,
        "forks": 3400,
        "license": "Apache-2.0",
        "languages": ["Python", "TypeScript", "Django"],
        "website": "https://zulip.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://zulip.com",
        "screenshot": "https://zulip.com/static/images/features/hero.png",
        "description": "Zulip solves chat fatigue with stream and topic threading, ensuring conversations stay focused and easy to catch up on even after days away.",
        "features": [
            "Topic-based streams eliminate synchronous notification overload",
            "Powerful search syntax across millions of historical messages",
            "Fast keyboard navigation and markdown formatting",
            "Production-ready Docker and self-hosting packages"
        ]
    },
    {
        "id": "formbricks",
        "name": "Formbricks",
        "tagline": "Open-source survey and experience management suite",
        "category": "Forms & Surveys",
        "alternative_to": ["typeform"],
        "github_repo": "formbricks/formbricks",
        "stars": 11500,
        "forks": 1400,
        "license": "AGPL-3.0",
        "languages": ["TypeScript", "Next.js", "Tailwind"],
        "website": "https://formbricks.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://formbricks.com",
        "screenshot": "https://formbricks.com/images/formbricks-hero.png",
        "description": "Formbricks is a modular, privacy-first survey platform that allows in-app surveys, link surveys, and micro-feedback collection with zero tracking cookies.",
        "features": [
            "Conversational multi-step forms with logic branching",
            "In-product micro-surveys via React / Web SDK",
            "Webhook triggers & automated CSV exports",
            "Full data residency and self-hostable Docker stack"
        ]
    },
    {
        "id": "bitwarden",
        "name": "Bitwarden / Vaultwarden",
        "tagline": "Industry-standard open-source password manager and credential vault",
        "category": "Security & Passwords",
        "alternative_to": ["1password"],
        "github_repo": "dani-garcia/vaultwarden",
        "stars": 42500,
        "forks": 2200,
        "license": "AGPL-3.0",
        "languages": ["Rust", "TypeScript"],
        "website": "https://bitwarden.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://bitwarden.com",
        "screenshot": "https://bitwarden.com/images/product-screenshots/desktop-dark.png",
        "description": "Bitwarden offers zero-knowledge end-to-end encryption for passwords, secure notes, TOTP tokens, and cards. Vaultwarden provides a lightweight Rust server backend.",
        "features": [
            "Zero-knowledge AES-256 and PBKDF2 / Argon2 encryption",
            "Cross-platform browser extensions, iOS, Android, and CLI",
            "Secure sharing with organizations and family members",
            "Lightweight single-container deployment with Vaultwarden"
        ]
    },
    {
        "id": "n8n",
        "name": "n8n",
        "tagline": "Fair-code workflow automation tool with extensive API integrations",
        "category": "Automation & Integration",
        "alternative_to": ["zapier"],
        "github_repo": "n8n-io/n8n",
        "stars": 58500,
        "forks": 7900,
        "license": "Sustainable Use License",
        "languages": ["TypeScript", "Vue", "Node.js"],
        "website": "https://n8n.io",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://n8n.io",
        "screenshot": "https://n8n.io/images/n8n-hero.png",
        "description": "n8n is a visual workflow automation tool that lets you connect hundreds of apps, write custom JavaScript/Python code nodes, and self-host without execution limits.",
        "features": [
            "400+ native app nodes and webhooks connectors",
            "Multi-step visual workflow canvas with debugging logs",
            "Support for AI LangChain nodes & vector databases",
            "Host on your own infrastructure with zero pay-per-task fees"
        ]
    },
    {
        "id": "calcom",
        "name": "Cal.com",
        "tagline": "The open-source scheduling infrastructure for individuals and enterprises",
        "category": "Scheduling",
        "alternative_to": ["calendly"],
        "github_repo": "calcom/cal.com",
        "stars": 34500,
        "forks": 8100,
        "license": "AGPL-3.0",
        "languages": ["TypeScript", "Next.js", "Tailwind"],
        "website": "https://cal.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://cal.com",
        "screenshot": "https://cal.com/og-image.png",
        "description": "Cal.com is a modern scheduling infrastructure that replaces Calendly. Embed booking widgets, connect Google/Outlook/CalDAV calendars, and accept payments seamlessly.",
        "features": [
            "Clean embeddable booking pages and routing forms",
            "Native calendar sync with Google, Apple, Nextcloud, and Outlook",
            "Team scheduling with round-robin and collective booking",
            "Comprehensive developer API and webhooks"
        ]
    },
    {
        "id": "docuseal",
        "name": "DocuSeal",
        "tagline": "Open-source digital document signing and contract management platform",
        "category": "Document Management",
        "alternative_to": ["docusign"],
        "github_repo": "docusealco/docuseal",
        "stars": 19200,
        "forks": 1500,
        "license": "AGPL-3.0",
        "languages": ["Ruby", "JavaScript", "HTML"],
        "website": "https://www.docuseal.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://docuseal.com",
        "screenshot": "https://www.docuseal.com/images/docuseal-banner.png",
        "description": "DocuSeal provides an open-source alternative to DocuSign for creating, filling, and signing PDF documents online with compliant digital signatures.",
        "features": [
            "WYSIWYG PDF document and form field builder",
            "Mobile-friendly document signing experience",
            "Automated audit trails with timestamps and IP records",
            "REST API for automated programmatic agreement generation"
        ]
    },
    {
        "id": "listmonk",
        "name": "Listmonk",
        "tagline": "High-performance self-hosted newsletter and mailing list manager",
        "category": "Marketing & Email",
        "alternative_to": ["mailchimp"],
        "github_repo": "knadh/listmonk",
        "stars": 16900,
        "forks": 1400,
        "license": "AGPL-3.0",
        "languages": ["Go", "Vue", "PostgreSQL"],
        "website": "https://listmonk.app",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://listmonk.app",
        "screenshot": "https://listmonk.app/static/screens/screen-campaigns.png",
        "description": "Listmonk is a standalone, super-fast newsletter and mailing list manager powered by Go and PostgreSQL. Delivers millions of emails with ultra-low server resource usage.",
        "features": [
            "Sends thousands of transactional & newsletter emails per second",
            "Subscriber list management with custom JSON attributes",
            "Rich HTML & Markdown template editor",
            "Direct SMTP / SES / Sendgrid integration"
        ]
    },
    {
        "id": "medusa",
        "name": "Medusa.js",
        "tagline": "Composable open-source commerce engine for next-gen digital stores",
        "category": "E-Commerce",
        "alternative_to": ["shopify"],
        "github_repo": "medusajs/medusa",
        "stars": 26800,
        "forks": 2700,
        "license": "MIT",
        "languages": ["TypeScript", "Node.js"],
        "website": "https://medusajs.com",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://medusajs.com",
        "screenshot": "https://medusajs.com/images/og-image.png",
        "description": "Medusa is a modular, headless commerce platform that replaces Shopify for developers wanting custom store logic, automated workflows, and multi-currency billing.",
        "features": [
            "Headless architecture with modern Next.js/Astro storefronts",
            "Complete admin dashboard with order and inventory tracking",
            "Plugins for Stripe, Meilisearch, Algolia, and Sendgrid",
            "Full MIT license without arbitrary GMV transaction fees"
        ]
    },
    {
        "id": "plane",
        "name": "Plane",
        "tagline": "Open-source extensible project management tool for modern software teams",
        "category": "Developer Tools",
        "alternative_to": ["jira"],
        "github_repo": "makeplane/plane",
        "stars": 33100,
        "forks": 2200,
        "license": "Apache-2.0",
        "languages": ["TypeScript", "Python", "Next.js"],
        "website": "https://plane.so",
        "logo": "https://www.google.com/s2/favicons?sz=128&domain_url=https://plane.so",
        "screenshot": "https://plane.so/images/og-image.png",
        "description": "Plane is the open-source alternative to Jira, Linear, and Asana. Track issues, sprints, product roadmaps, and cycle analytics with modern keyboard-first UI.",
        "features": [
            "Kanban, List, Calendar, and Gantt roadmap timeline views",
            "Cycles, Modules, and Pages for documentation integration",
            "Custom workflows, issue types, and automated triage",
            "Self-host with simple Docker compose command"
        ]
    }
]

import os
os.makedirs('/home/ubuntu/projects/downloadsoftware-platform/src/data', exist_ok=True)

with open('/home/ubuntu/projects/downloadsoftware-platform/src/data/proprietary.json', 'w') as f:
    json.dump(proprietary_tools, f, indent=2)

with open('/home/ubuntu/projects/downloadsoftware-platform/src/data/projects.json', 'w') as f:
    json.dump(projects, f, indent=2)

print(f"Generated {len(proprietary_tools)} proprietary tools and {len(projects)} open source projects.")
