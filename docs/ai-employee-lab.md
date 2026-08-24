# AI Employee Lab

This repository carries a conservative five-role DevSpace experiment under `.devspace/agents/`.

## Roles

1. `ai-master` — read-only coordinator. Breaks a business goal into bounded assignments and requires evidence before completion.
2. `ai-planner` — read-only product/growth planner. Produces measurable experiments and implementation-ready tasks.
3. `ai-developer` — bounded implementation worker. May edit repository files only when the task explicitly authorizes it and must hand work to QA.
4. `ai-qa` — read-only independent verifier. Tests acceptance criteria and reports failures without editing them away.
5. `ai-marketer` — read-only growth/marketing researcher. Drafts ideas and experiments but does not publish or spend money.

## Safety boundary

The lab is deliberately semi-autonomous. No profile may autonomously deploy, publish, purchase, change billing/accounts, expose credentials, or take irreversible external actions. Marketing publication, ad spend, customer messaging, and production deployment remain human-approved actions.

## Suggested flow

```text
user goal
  -> ai-master
      -> ai-planner
      -> ai-developer
          -> ai-qa
      -> ai-marketer
  -> ai-master evidence review
  -> human approval for external action
```

Use small, measurable tasks first. Increase autonomy only after repeated QA-backed success.
