# Application Questions - ElevenLabs Full-Stack Engineer

## Why ElevenLabs, and why now?

ElevenLabs feels like the right company to apply to now because the product is moving past impressive audio demos into systems people actually build around. The posting talks about voice and chat agents, developer APIs, integrations, testing, monitoring, reliability, and customer workflows. That is the part that interests me most. The model matters, but the product around the model decides whether people can use it every day.

My recent work has been pulling me in that direction. At SmartSolve, I have been building full-stack internal tools with Next.js, TypeScript, PostgreSQL, SSO, and auth middleware. In side projects, I have been building AI products where the hard part is keeping the user flow, backend state, model output, and reviewability connected. ElevenLabs is a place where that kind of product engineering is central, especially as voice becomes part of agents, creative tools, and developer platforms.

The timing also feels real because I have already used ElevenLabs in projects, not just read about it. I have seen how much better an AI workflow feels when audio is part of the experience. I want to work on that closer to the source, with a team where voice is not an add-on but the core product surface.

## What's the most impactful thing you've built? What was your specific contribution?

The most impactful thing I have built so far was a production data workflow at AAIS that automated a manual SQL billing process. The workflow processed 20+ TB of production insurance data and supported charge calculations for 700+ member companies. It was not the flashiest project, but it mattered because it took a recurring manual process and turned it into something repeatable, traceable, and easier to maintain.

My specific contribution was building the Python and PySpark processing logic, working with AWS Glue and S3, and understanding how the source data needed to move through the workflow. I also had to think through validation and access patterns instead of only writing a script that worked once. The work sat close to the business process, so small mistakes could have created bad downstream data or extra manual cleanup.

What I took from that project is that impact often looks like removing fragile handoffs. A good system should make the next run less stressful than the last one.

## How did you know it worked? What did success actually look like?

I knew it worked when the workflow could produce the expected billing outputs from production-scale data without relying on the old manual SQL process. Success was not just that the code ran. It had to process the right data, keep the workflow repeatable, and fit into the AWS Glue and S3 path the team could maintain after the initial build.

There were a few practical signs of success. The workflow handled 20+ TB of golden-table insurance data, supported calculations for 700+ member companies, and became part of a broader move toward validated cloud data workflows. On related AAIS work, success also meant keeping controlled self-service data access and 24-hour data latency in the new MDM workflows.

The simplest test was whether the process made the operational work less manual without making the data harder to trust. That was the standard I cared about.

## Have you used ElevenLabs, even in a personal or side project? What did you build or explore?

Yes. I used ElevenLabs in Fix-It-Flow, a voice-first AI repair assistant built for RocketHacks 2026. The app lets a user describe an appliance problem by voice while showing the item through the camera. Gemini Vision analyzes the visual context, Llama-style reasoning turns the conversation and image evidence into structured repair guidance, and ElevenLabs text-to-speech reads repair steps aloud so the user can stay hands-free.

I worked on the full-stack product flow around that experience. That included typed Next.js API routes, DynamoDB session state, inspection turns, repair sessions, chat, uploads, findings, frames, text-to-speech, and repair steps. ElevenLabs made the repair flow feel more practical because the user did not need to keep looking at the screen while following instructions.

I also explored ElevenLabs in DreamScape, a React Native and Expo learning app that generated study cues and used text-to-speech audio for simulated sleep learning sessions. Those projects made me more interested in voice as a product interface, especially when the goal is to make AI output easier to act on rather than just easier to read.
