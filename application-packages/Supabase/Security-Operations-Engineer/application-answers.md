# Application Answers

## Tell us about your experience working in an async and/or remote environment. What practices or approaches have worked well for you? What challenges have you faced?

At AAIS, I learned pretty quickly that async work only goes well if you make your thinking easy to follow. A lot of my work was around SQL, AWS Glue, S3, IAM, and messy insurance data, so I couldn't just make a change and assume people would understand why. I got into the habit of writing down what I found, what I changed, what I tested, and where I still had questions. That helped a lot, especially when I was profiling tables or working through data workflows where the context was spread across different systems.

APKD taught me the same lesson in a different way. That internship was before AI coding tools really blew up, so I had to understand the legacy Lucee/CFML codebase and type through everything by hand. I was working on a healthcare workflow platform, and some fixes were tied to real operational details like audit logging, anti-CSRF protection, Matchgrid imports, MFI uploads, and access-denied flows. The hardest part wasn't always the code. It was understanding why the workflow existed in the first place and being careful not to break something someone depended on. What has worked best for me is being clear, leaving notes another person can actually use, asking specific questions when I'm blocked, and making small changes that are easier to review.

## Have you made any open source contributions in the past that you'd like to share with us?

I haven't made a meaningful open source contribution yet, and I don't want to dress that up as something it isn't. The closest related work I can point to is my research around software repositories and developer workflows.

One project I worked on was an ICSME-published research pipeline for generating better GitHub pull request descriptions from actual repo evidence like commits, file diffs, linked issues, and metadata. My part involved building structured context, improving weak commit messages, summarizing file-level changes, and evaluating whether the generated descriptions were actually grounded in the code changes. It gave me a lot of respect for the way open source work depends on clear written context, not just code. I'd like to make real open source contributions going forward, but for now my honest answer is that my strongest related experience is research built around GitHub workflows and evidence-based developer communication.
