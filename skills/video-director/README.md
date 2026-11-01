# Video Director

One entry point for choosing a video, coordinating its existing specialists, preparing the upload package, and learning from its results. Start at the requested stage; direct specialist use continues to work.

Examples: “What should I film next?”, “Package this finished video”, “Review this long-form outline”, or “What should change after these results?”

Requires the sibling `script-my-video`, `make-my-video-awesome`, `roast-my-short` and `no-ai-slop-writing` skills for their respective tasks. Uses the creator's project instructions, tracker and profiles. No API key, collector or scheduler is installed. Editing still uses the existing HyperFrames/FFmpeg workflow and its preview approvals.

## Design references reviewed

The implementation is original prose; no upstream scripts or prompt passages were copied. These MIT-licensed projects informed the choices below. Their numerical claims and rigid timing rules were not imported.

| Repository / reviewed commit | Idea used |
| --- | --- |
| [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube/tree/84c3fa6805200632fadb4fe2795ef265511271c7) | Load only relevant task guidance; compact packaging and results briefs; pre-filming drop-off annotations |
| [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill/tree/a2feb2104981a375ffd4f87ee04f4f5344ac43c6) | Judge title/thumbnail together; align retention with the actual transcript; prioritize a primary fix; treat heuristic scoring honestly |
| [petergyang/video-short](https://github.com/petergyang/video-short/tree/8b7dce36db279557facfed0dbe49f4c6938df2bb) | Retain plan-before-build, readable real proof, and final frame checks in the existing editor |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/88c79f6528a9347420e57ceb1fff9a60de651768) | Read context first; consider intended discovery and useful standalone repurposing without adding channels |

`SKILL.md` owns routing and topic selection. `references/packaging.md` owns the package method; `references/results.md` owns result interpretation and learning. The specialist skills retain their existing production tools and dated lessons. Private results stay in the creator's project.
