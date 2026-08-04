# Application Questions - ElevenLabs Full-Stack Engineer

## Why ElevenLabs, and why now?

Honestly, the part that pulled me in is not only the voice model. It is all the product work that has to happen around it before someone can depend on it. The posting talks about agents, APIs, integrations, testing, monitoring, reliability, and internal workflows. That sounds like building the layer between research and everyday use, which is where I have been spending more of my time.

In my own projects, the interesting part has usually been that layer. Fix-It-Flow was not hard just because it called model APIs. It was hard because the camera flow, voice commands, stored session, generated repair steps, and spoken output all had to line up for the user. At SmartSolve, I have been doing a more practical version of the same thing with internal tools, access control, and messy workflow requirements.

The timing feels right because I have used ElevenLabs enough to know I am interested in the product surface, not just the company name. I have seen how different an AI workflow feels when the output can be heard and acted on while someone is doing something else. I want to work closer to that problem.

## What's the most impactful thing you've built? What was your specific contribution?

Probably the AAIS billing workflow. It was not the flashiest thing I have built, but it was real production work with real consequences. The old process involved manual SQL work around production insurance data. The workflow I worked on processed 20+ TB of data and supported billing calculations for 700+ member companies.

My contribution was building the Python and PySpark processing logic, wiring it into AWS Glue and S3, and spending time understanding how the source tables actually behaved. A lot of the work was less glamorous than the final bullet sounds. I had to trace where the data came from, check assumptions, and make sure the workflow could be maintained instead of being a one-off script that only I understood.

That project changed how I think about useful software. Sometimes the best thing you can build is the thing that makes the next run less stressful for everyone else.

## How did you know it worked? What did success actually look like?

I knew it worked when it stopped feeling like a demo and could run against production-scale data in the way the team needed. The code running once was not enough. It had to produce the expected billing outputs, avoid the old manual SQL path, and fit into the AWS Glue and S3 workflow the team could keep using.

The signs of success were pretty practical. It handled 20+ TB of golden-table insurance data. It supported calculations for 700+ member companies. On related AAIS work, success also meant keeping controlled self-service access and 24-hour data latency in the new MDM workflows.

The standard I cared about was simple. Did this remove manual work without making the data harder to trust. If the answer was yes, then the work was doing its job.

## Have you used ElevenLabs, even in a personal or side project? What did you build or explore?

Yes. I used ElevenLabs in Fix-It-Flow, a voice-first AI repair assistant I built for RocketHacks 2026. The idea was simple. If someone is trying to fix an appliance, they should not have to keep looking back at a screen every few seconds. The app let the user describe the problem by voice while showing the item through the camera, then used ElevenLabs text-to-speech to read repair steps out loud.

I worked on the full-stack flow around that experience. That included typed Next.js API routes, DynamoDB session state, inspection turns, repair sessions, chat, uploads, findings, frames, text-to-speech, and generated repair steps. The audio piece was not decoration. It made the workflow make more sense because the user could keep their hands free.

I also used ElevenLabs in DreamScape, a React Native and Expo learning app that generated study cues and played them back as text-to-speech audio. Both projects made me more interested in voice as an interface, especially for AI products where reading a paragraph is not always the most useful output.
