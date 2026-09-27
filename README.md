<!-- ======================================================================
     Aayush Mishra · GitHub profile
     Palette: void #0A0F1F · signal cyan #22D3EE · synapse violet #A78BFA · pass green #34D399
     ====================================================================== -->

<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Aayush Mishra, Senior SDET and Automation Architect" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2600&pause=900&color=22D3EE&center=true&vCenter=true&width=720&height=40&lines=Testing+software%2C+and+the+AI+inside+it;Playwright+%2B+MCP+agents+that+plan%2C+write+and+heal+tests;Evaluating+LLMs+with+DeepEval+and+Ragas;Quality+gates+for+RAG+pipelines+and+AI+agents" alt="Typing animation" />
</p>

<p align="center">
  <a href="https://aayushmishra.tech/"><img src="https://img.shields.io/badge/Portfolio-aayushmishra.tech-0A0F1F?style=for-the-badge&logo=googlechrome&logoColor=22D3EE&labelColor=0A0F1F" alt="Portfolio" /></a>
  <a href="https://linkedin.com/in/aayush-mishra072/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A0F1F?style=for-the-badge&labelColor=0A0F1F&color=22D3EE" alt="LinkedIn" /></a>
  <a href="mailto:Aayushmishra026@gmail.com"><img src="https://img.shields.io/badge/Email-Say_hello-0A0F1F?style=for-the-badge&logo=gmail&logoColor=A78BFA&labelColor=0A0F1F&color=A78BFA" alt="Email" /></a>
  <a href="https://twitter.com/Aayush_Mishraa"><img src="https://img.shields.io/badge/@Aayush__Mishraa-0A0F1F?style=for-the-badge&logo=x&logoColor=E2E8F0" alt="X" /></a>
</p>

<br/>

## `$ cat aayush.spec.yml`

```yaml
role:        Senior SDET & Automation Architect @ Keywords Studio
based_in:    Gurugram, India
experience:  4+ years across gaming, banking, healthcare, e-commerce and logistics
education:   MSc Data Science, BSc Computer Science

what_i_do:
  - design test automation frameworks for web, API and mobile
  - wire quality gates into CI/CD so regressions never reach main
  - test LLM apps, RAG pipelines and AI agents like any other critical system

building_now:
  - one framework that runs UI, API and mobile suites from a single pipeline
  - a microservices test automation framework
  - LLM evaluation suites that fail the build when answers drift

ask_me_about: [Playwright, Selenium, RestAssured, Postman/Newman, DeepEval, Playwright MCP]
```

<br/>

## 🧠 AI quality engineering

AI features don't fail like normal code. The same prompt can pass today and hallucinate tomorrow, so I treat model output, retrieval quality and agent behaviour as things to measure and gate, not eyeball.

```mermaid
flowchart LR
    subgraph AGENTS["AI-assisted automation"]
        A["Test intent<br/>in plain English"] --> B["Playwright MCP<br/>planner · generator · healer"]
        B --> C["Playwright suites<br/>UI + API"]
    end
    subgraph EVALS["Testing the AI itself"]
        D["LLM / RAG app"] --> E["DeepEval<br/>pytest-style LLM evals"]
        D --> F["Ragas<br/>retrieval metrics"]
        D --> G["Promptfoo<br/>red-teaming"]
    end
    C --> H{"CI quality gate<br/>GitHub Actions / Jenkins"}
    E --> H
    F --> H
    G --> H
    H -- pass --> I["🚀 Ship"]
    H -- fail --> J["🔍 Trace, report, fix"]
```

| Layer | Tools | What it checks |
|:--|:--|:--|
| **Agentic UI testing** | Playwright MCP, Playwright Test Agents, Browser-Use, Amazon Nova Act | Agents explore the live app through the accessibility tree, draft test plans, generate specs and repair broken locators |
| **LLM output evals** | DeepEval (G-Eval, hallucination, answer relevancy) | Pytest-style assertions on model responses, with pass/fail thresholds that run in CI |
| **RAG evaluation** | Ragas | Faithfulness, context precision and context recall, so you know whether retrieval or generation is the weak link |
| **Red-teaming & prompt regression** | Promptfoo | Prompt injection, jailbreaks and PII leaks, plus side-by-side comparison of prompt versions |
| **MCP servers & agents** | MCP Inspector, tool-call assertions | Tool schemas, tool-call accuracy and whether the agent actually reached its goal |
| **Observability** | Langfuse, Arize Phoenix | Production traces that feed real failures back into the eval dataset |

<p align="center">
  <img src="https://img.shields.io/badge/Model_Context_Protocol-0A0F1F?style=for-the-badge&logo=modelcontextprotocol&logoColor=22D3EE" alt="MCP" />
  <img src="https://img.shields.io/badge/DeepEval-0A0F1F?style=for-the-badge&logo=pytest&logoColor=22D3EE" alt="DeepEval" />
  <img src="https://img.shields.io/badge/Ragas-0A0F1F?style=for-the-badge&logoColor=22D3EE" alt="Ragas" />
  <img src="https://img.shields.io/badge/Promptfoo-0A0F1F?style=for-the-badge" alt="Promptfoo" />
  <img src="https://img.shields.io/badge/LangChain-0A0F1F?style=for-the-badge&logo=langchain&logoColor=A78BFA" alt="LangChain" />
  <img src="https://img.shields.io/badge/Claude-0A0F1F?style=for-the-badge&logo=claude&logoColor=A78BFA" alt="Claude" />
  <img src="https://img.shields.io/badge/GitHub_Copilot-0A0F1F?style=for-the-badge&logo=githubcopilot&logoColor=A78BFA" alt="GitHub Copilot" />
  <img src="https://img.shields.io/badge/Hugging_Face-0A0F1F?style=for-the-badge&logo=huggingface&logoColor=A78BFA" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/Ollama-0A0F1F?style=for-the-badge&logo=ollama&logoColor=E2E8F0" alt="Ollama" />
</p>

<br/>

## ⚙️ Core automation stack

<p align="center">
  <img src="https://img.shields.io/badge/🎭_Playwright-0A0F1F?style=for-the-badge" alt="Playwright" />
  <img src="https://img.shields.io/badge/Selenium-0A0F1F?style=for-the-badge&logo=selenium&logoColor=34D399" alt="Selenium" />
  <img src="https://img.shields.io/badge/Appium-0A0F1F?style=for-the-badge&logo=appium&logoColor=A78BFA" alt="Appium" />
  <img src="https://img.shields.io/badge/RestAssured-0A0F1F?style=for-the-badge" alt="RestAssured" />
  <img src="https://img.shields.io/badge/Postman_%2F_Newman-0A0F1F?style=for-the-badge&logo=postman&logoColor=22D3EE" alt="Postman" />
  <img src="https://img.shields.io/badge/TestNG-0A0F1F?style=for-the-badge" alt="TestNG" />
  <img src="https://img.shields.io/badge/JMeter-0A0F1F?style=for-the-badge&logo=apachejmeter&logoColor=22D3EE" alt="JMeter" />
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,py,ts,js,selenium,postman,mysql&theme=dark" alt="Languages and tools" /><br/>
  <img src="https://skillicons.dev/icons?i=docker,jenkins,githubactions,aws,azure,git,gitlab&theme=dark" alt="DevOps and cloud" /><br/>
  <img src="https://skillicons.dev/icons?i=pytorch,tensorflow,linux,vscode&theme=dark" alt="ML and tooling" />
</p>

<br/>

## 📊 Signal

<p align="center">
  <img height="165" src="https://github-readme-stats-sigma-five.vercel.app/api?username=aayush-mishraa&show_icons=true&hide_border=true&bg_color=0A0F1F&title_color=22D3EE&icon_color=A78BFA&text_color=E2E8F0&ring_color=22D3EE" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=aayush-mishraa&layout=compact&hide_border=true&bg_color=0A0F1F&title_color=22D3EE&text_color=E2E8F0" alt="Top languages" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=aayush-mishraa&hide_border=true&background=0A0F1F&ring=22D3EE&fire=A78BFA&currStreakNum=E2E8F0&sideNums=E2E8F0&currStreakLabel=22D3EE&sideLabels=7C8BA5&dates=7C8BA5&stroke=15203A" alt="GitHub streak" />
</p>

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=aayush-mishraa&bg_color=0A0F1F&color=7C8BA5&line=22D3EE&point=A78BFA&area=true&area_color=22D3EE&title_color=E2E8F0&hide_border=true" alt="Contribution graph" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aayush-Mishraa/Aayush-Mishraa/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aayush-Mishraa/Aayush-Mishraa/output/github-snake.svg" />
    <img alt="Snake eating my contribution graph" src="https://raw.githubusercontent.com/Aayush-Mishraa/Aayush-Mishraa/output/github-snake.svg" />
  </picture>
</p>

<br/>

<p align="center">
  Open to conversations about test architecture, AI evaluation and quality engineering.<br/>
  Everything I've built lives at <a href="https://aayushmishra.tech/">aayushmishra.tech</a>.
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=aayush-mishraa&label=profile%20views&color=0A0F1F&style=flat-square" alt="Profile views" />
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0F1F,60:22D3EE,100:A78BFA&height=110&section=footer" width="100%" alt="" />
