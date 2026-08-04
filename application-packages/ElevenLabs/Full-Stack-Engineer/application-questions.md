# Application Questions - ElevenLabs Full-Stack Engineer

## Why ElevenLabs, and why now?

The part that pulled me in is not only the voice model. It is the product work around it, like APIs, agents, integrations, reliability, and workflows that make voice useful in real products.

I have already used ElevenLabs in side projects, so this is not just name recognition for me. I have seen how much more practical an AI workflow feels when the output can be heard while someone is doing something else. I want to work closer to that kind of product problem.

## What's the most impactful thing you've built? What was your specific contribution?

Probably the AAIS billing workflow. It was not flashy, but it replaced manual SQL work around production insurance data and supported billing calculations for 700+ member companies.

My contribution was building the Python and PySpark processing logic, wiring it into AWS Glue and S3, and checking how the source tables actually behaved. The useful part was making the next run less manual and less fragile.

## How did you know it worked? What did success actually look like?

I knew it worked when it could run against production-scale data and produce the expected billing outputs without depending on the old manual SQL process.

Success looked practical. It handled 20+ TB of golden-table insurance data, supported 700+ member-company calculations, and fit into the AWS Glue and S3 workflow the team could keep using. The standard was simple. It had to remove manual work without making the data harder to trust.

## Have you used ElevenLabs, even in a personal or side project? What did you build or explore?

Yes. I used ElevenLabs in Fix-It-Flow, a voice-first AI repair assistant I built for RocketHacks 2026.

The app let a user describe an appliance problem by voice while showing it through the camera, then used ElevenLabs text-to-speech to read repair steps aloud. I built the full-stack flow around typed Next.js API routes, DynamoDB session state, inspection turns, repair sessions, findings, and generated repair steps. I also used ElevenLabs in DreamScape for text-to-speech study cues.
