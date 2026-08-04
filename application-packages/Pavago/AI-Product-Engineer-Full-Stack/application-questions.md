# Application Questions - Pavago AI Product Engineer (Full Stack)

## What experience do you have integrating AI or LLMs into real applications? Can you share a specific use case you implemented?

I’ve integrated LLMs mostly in full-stack products where the model is one part of the workflow, not the whole product. A specific example is Fix-It-Flow, a Next.js PWA I built for repair guidance. The app takes camera input and spoken context, sends visual frames through Gemini Vision, combines that with conversation state and Llama-style reasoning, then returns structured findings, safety warnings, and repair steps. I built typed Next.js API routes and DynamoDB session persistence so the app could remember the inspection, repair steps, frames, findings, and user questions. I also built RocketGrader with LangChain and Mistral AI for AI-assisted assignment feedback, including document parsing and structured scoring outputs.

## How do you approach designing backend systems and APIs?

I usually start by writing down the product flow, the data that has to survive each step, and the failure cases I do not want to hide from users. From there I design the database shape, API boundaries, auth model, and state transitions before I worry about UI details. At SmartSolve, that meant using PostgreSQL with Drizzle, SSO, and auth middleware for an onboarding tracker where employee data needed to stay protected. In Fix-It-Flow, it meant separating inspection turns, repair sessions, generated steps, frames, findings, and chat so the AI workflow had durable state. For AI features, I also design for bad model output up front with structured responses, validation, retries, and human-readable fallback paths.
