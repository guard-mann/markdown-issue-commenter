# Markdown-to-Issue Commenter

Post markdown files as comments to GitHub Issues via GitHub Actions.  
Useful for collaborative discussions, AI-generated logs, review notes, and documentation-driven workflows.

---

## Features

- Write comments in markdown files (e.g., `docs/issue_updates/42.md`)
- Automatically post them to GitHub Issue #42 via GitHub Actions
- Fully Git-tracked: keep comment history with commits
- No need to open the GitHub UI manually — just `git push`

---

## Getting Started

### 1. Clone or use this template

```bash
git clone https://github.com/yourname/markdown-issue-commenter.git
cd markdown-issue-commenter
```

### 2. Add a markdown file under docs/issue_updates/:
```markdown
// docs/issue_updates/42.md
This is an auto-posted comment for Issue #42.
```
### 3. Push your changes:
```bash
git add docs/issue_updates/42.md
git commit -m "Add comment for issue #42"
git push
```

The comment will be posted automatically to Issue #42.

## Demo
```bash
docs/issue_updates/1.md → posted to Issue #1
```
Example file:
```markdown
# this is a test
Comment on the md is reflected to the corresponding No. issue.
```