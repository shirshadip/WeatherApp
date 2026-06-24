# Contributing to AI Weather App 🌦️

Thank you for your interest in contributing to the AI Weather App! We welcome contributions from developers of all skill levels. This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Ways to Contribute](#ways-to-contribute)
3. [Getting Started](#getting-started)
4. [Development Workflow](#development-workflow)
5. [Commit Guidelines](#commit-guidelines)
6. [Pull Request Process](#pull-request-process)
7. [Code Style & Standards](#code-style--standards)
8. [Testing Guidelines](#testing-guidelines)
9. [Documentation](#documentation)
10. [Need Help?](#need-help)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors. We expect all participants to:

- Be respectful and inclusive in all interactions
- Welcome diverse perspectives and backgrounds
- Focus on constructive feedback
- Respect others' opinions and ideas
- Report inappropriate behavior professionally

### Enforcement

Violations of the Code of Conduct may result in removal from the project. For serious violations, contact the maintainers directly.

## Ways to Contribute

### 🐛 Report Bugs

If you find a bug, please open an issue with:

- **Clear title**: Describe the bug concisely
- **Detailed description**: What happened and what you expected
- **Steps to reproduce**: Exact steps to trigger the bug
- **Screenshots**: If applicable
- **Environment**: Python version, OS, browser
- **Logs**: Error messages or stack traces

**Template:**

```
**Bug Description:**
[Clear description]

**Steps to Reproduce:**
1. ...
2. ...
3. ...

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happened]

**Environment:**
- Python Version: X.X.X
- OS: Windows/macOS/Linux
- Browser: Chrome/Firefox/Safari

**Additional Context:**
[Any other relevant information]
```

### 💡 Suggest Features

Feature suggestions should include:

- **Title**: Clear, concise feature name
- **Motivation**: Why this feature would be valuable
- **Use Cases**: Specific scenarios where this would help
- **Proposed Solution**: How you envision implementing it
- **Alternatives**: Other approaches considered

**Template:**

```
**Feature Title:**
[Clear feature name]

**Motivation:**
[Why is this needed?]

**Use Cases:**
- Use case 1
- Use case 2

**Proposed Solution:**
[How it could be implemented]

**Alternatives Considered:**
[Other approaches]

**Additional Context:**
[Screenshots, examples, research links]
```

### 📝 Improve Documentation

- Fix typos or unclear explanations
- Add code examples
- Improve README sections
- Create tutorials or guides
- Update API documentation

### 🔧 Submit Code Changes

- Bug fixes
- Performance improvements
- New features
- Code refactoring
- Test coverage improvements

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- GitHub account
- Basic understanding of Git workflow

### Fork & Clone

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/WeatherApp.git
cd WeatherApp

# 3. Add upstream remote
git remote add upstream https://github.com/original-owner/WeatherApp.git

# 4. Verify remotes
git remote -v
# origin    -> your fork
# upstream  -> original repository
```

### Setup Development Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pylint black pytest pytest-cov

# Configure API key
# Create .streamlit/secrets.toml with your OpenWeatherMap API key
```

## Development Workflow

### 1. Create a Branch

```bash
# Update your local repository
git fetch upstream
git checkout main
git merge upstream/main

# Create a new branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix-name
```

**Branch Naming Conventions:**

- Feature: `feature/feature-name` (e.g., `feature/add-hourly-forecast`)
- Bug fix: `fix/bug-description` (e.g., `fix/api-timeout-issue`)
- Documentation: `docs/description` (e.g., `docs/add-api-guide`)
- Testing: `test/description` (e.g., `test/add-unit-tests`)

### 2. Make Your Changes

```bash
# Edit files
# Create new files as needed
# Test frequently
```

### 3. Commit Your Changes

```bash
git add .
git commit -m "Your descriptive commit message"
```

## Commit Guidelines

Follow these guidelines for clear, maintainable commit history:

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without feature changes
- **perf**: Performance improvements
- **test**: Test additions or modifications
- **chore**: Build process, dependencies, or tools

### Scope (Optional)

Specify the affected component:

- `weatherreport`
- `visualization`
- `api`
- `ui`
- `testing`

### Subject

- Use imperative mood: "add" not "added" or "adds"
- Don't capitalize first letter
- No period at the end
- Maximum 50 characters

### Body (Optional)

- Explain what and why, not how
- Wrap at 72 characters
- Separate from subject with blank line

### Footer (Optional)

Reference issues: `Fixes #123`, `Closes #456`

### Examples

```
feat(api): add weather alerts integration

Add real-time weather alert notifications for severe weather conditions.
Users can now receive push notifications for tornado warnings, severe
thunderstorms, and other significant weather events.

Fixes #245
```

```
fix(weatherreport): handle null precipitation values

Previously, null precipitation values caused data processing errors.
Now they are properly handled as zero precipitation.

Closes #198
```

```
docs: update installation instructions for Windows users
```

## Pull Request Process

### Before Submitting

```bash
# Pull latest changes from upstream
git fetch upstream
git rebase upstream/main

# Run tests
python test.py

# Check code style
pylint *.py
black --check *.py

# Format code
black *.py
```

### 1. Push Your Branch

```bash
git push origin feature/your-feature-name
```

### 2. Create Pull Request

On GitHub:

1. Click "New Pull Request"
2. Select base: `upstream/main`, compare: `your-branch`
3. Fill in the PR template (see below)
4. Click "Create Pull Request"

### PR Template

```markdown
## Description

Brief description of changes

## Related Issues

Closes #123

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes

- Change 1
- Change 2

## Testing

Describe tests performed:

- Test 1
- Test 2

## Screenshots (if applicable)

[Add screenshots]

## Checklist

- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests
- [ ] New and existing tests pass
```

### 3. Respond to Feedback

- Address all comments
- Make requested changes
- Push updates to the same branch
- Respond respectfully to suggestions

### 4. Merge

Once approved:

```bash
# Maintainers will merge your PR
# Delete your branch afterward
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

## Code Style & Standards

### Python Style Guide

We follow **PEP 8** with these tools:

- **Black**: Code formatter
- **Pylint**: Linter
- **Type Hints**: Use Python type hints

### Code Style Checklist

- [ ] Follow PEP 8
- [ ] Use meaningful variable names
- [ ] Add docstrings to functions/classes
- [ ] Keep lines under 100 characters
- [ ] No trailing whitespace
- [ ] Use 4 spaces for indentation

### Docstring Format

```python
def generate_30_day_report(lat, lon):
    """Generate a 30-day weather report for given coordinates.

    Args:
        lat (float): Latitude coordinate
        lon (float): Longitude coordinate

    Returns:
        pd.DataFrame: Weather data with date, temp_max, temp_min, rain_mm

    Raises:
        requests.HTTPError: If API request fails
        ValueError: If coordinates are invalid

    Examples:
        >>> df = generate_30_day_report(22.5726, 88.3639)
        >>> print(df.head())
    """
```

### Example Code

```python
# Good
def calculate_average_temperature(temperatures: list[float]) -> float:
    """Calculate average temperature from a list."""
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)


# Avoid
def calc_avg_temp(temps):
    return sum(temps) / len(temps)
```

## Testing Guidelines

### Writing Tests

```python
# tests/test_weatherreport.py
import unittest
from weatherreport import generate_30_day_report


class TestWeatherReport(unittest.TestCase):
    def test_generate_30_day_report(self):
        """Test report generation with valid coordinates."""
        df = generate_30_day_report(22.5726, 88.3639)
        self.assertIsNotNone(df)
        self.assertIn('date', df.columns)

    def test_invalid_coordinates(self):
        """Test with invalid coordinates."""
        with self.assertRaises(ValueError):
            generate_30_day_report(None, None)
```

### Running Tests

```bash
# Run all tests
python -m pytest test.py -v

# Run with coverage
pytest --cov=. test.py

# Run specific test
pytest test.py::TestWeatherReport::test_generate_30_day_report
```

### Coverage Requirements

- Minimum 80% code coverage for new features
- All public functions must have tests
- Test both success and failure cases

## Documentation

### Updating README

- Keep installation instructions current
- Add features to the feature list
- Update dependencies if changed
- Document new API endpoints or functions

### Adding Docstrings

All public functions must have docstrings:

```python
def your_function(param1: str, param2: int) -> bool:
    """One-line summary of what function does.

    Longer description if needed.

    Args:
        param1: Description
        param2: Description

    Returns:
        Description of return value

    Raises:
        ExceptionType: When/why this exception is raised
    """
```

### API Documentation

If adding new features:

- Document in README.md
- Add docstrings
- Provide examples
- Update CONTRIBUTING.md if needed

## Need Help?

### Questions?

- 💬 Open a Discussion on GitHub
- 📧 Email: [your-email@example.com]
- 📚 Check existing documentation

### Stuck on a Bug?

- 🔍 Search existing issues
- 📖 Review related code
- 🤔 Ask for help in issue comments
- 🧠 Rubber duck debugging

### Getting Advice

- Comment on relevant issues
- Ask in discussions
- Tag maintainers respectfully
- Provide context and code examples

## Recognition

Contributors are recognized in:

- README.md contributors section
- GitHub contributors page
- Release notes

We appreciate all contributions, no matter how small!

---

**Thank you for helping make AI Weather App better! 🙌**

Questions? Feel free to reach out!
