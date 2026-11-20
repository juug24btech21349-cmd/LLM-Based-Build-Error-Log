# LLM-Based Build Error Log

A small Python project for practicing tests and GitHub Actions CI.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

In VS Code, select the `.venv` interpreter with **Python: Select Interpreter**.

## GitHub Actions and failed runs

The workflow in `.github/workflows/ci.yml` runs tests on every push and pull
request. A red run means a job or step failed; it makes regressions visible
before changes are accepted. To view a test failure, open the repository's
**Actions** tab, select the red **CI** run, open the **build** job, and expand
**Run tests**. The pytest output identifies the failing test and assertion.

To reproduce a red run for the lab, temporarily change a test's expected value
to an incorrect value, commit and push that change, and inspect its run log.
Then restore the correct expectation, commit, and push again. The corrected
push should produce a green run.
