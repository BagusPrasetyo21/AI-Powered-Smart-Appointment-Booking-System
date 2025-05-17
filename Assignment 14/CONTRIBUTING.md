# Contributing to AI-Powered Smart Appointment Booking System

Thank you for considering contributing to the AI-Powered Smart Appointment Booking System! This document provides guidelines and instructions for contributing to make the process smooth for everyone.

## Prerequisites

- Git installed on your local machine
- GitHub account
- Python 3.8 or higher
- Basic knowledge of AI/ML concepts (for AI-related features)
- Familiarity with web development (HTML, CSS, JavaScript)
- Understanding of healthcare appointment systems (helpful but not required)

## Setup Instructions

1. **Fork the Repository**
   - Visit the [repository page](https://github.com/ncayiyane/AI-Powered-Smart-Appointment-Booking-System-)
   - Click the "Fork" button in the top-right corner
   - This creates a copy of the repository in your GitHub account

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/AI-Powered-Smart-Appointment-Booking-System-.git
   cd AI-Powered-Smart-Appointment-Booking-System-
   ```

3. **Set Up Development Environment**
   ```bash
   # Create and activate a virtual environment (recommended)
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   
   # Install dependencies
   python -m pip install --upgrade pip
   pip install -e ".[dev]"
   ```

## Coding Standards

### Code Style
- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Include docstrings for all functions, classes, and modules
- Keep lines under 100 characters where possible

### Linting
Before submitting your code, ensure it passes our linting checks:
```bash
# Install linting tools if not included in dev dependencies
pip install flake8 black

# Run linters
flake8 .
black --check .
```

### Testing
All code contributions should include appropriate tests:
```bash
# Run the test suite
pytest

# For test coverage
pytest --cov=.
```

Aim for at least 80% test coverage for new code.

## How to Contribute

### Picking an Issue
1. Browse the [Issues](https://github.com/ncayiyane/Assignment-13/issues) tab
2. Look for issues labeled `good-first-issue` if you're new to the project
3. Comment on the issue you'd like to work on to let maintainers know

### Creating a Branch
```bash
# Create a new branch for your feature/fix
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-you-are-fixing
```

### Making Changes
1. Make your changes to the codebase
2. Ensure all tests pass
3. Add or update tests as needed
4. Commit your changes with clear, descriptive commit messages:
   ```bash
   git add .
   git commit -m "Add feature: brief description of changes"
   ```

### Submitting a Pull Request
1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Go to the original repository on GitHub
3. Click "New Pull Request"
4. Select your branch from your fork
5. Fill out the PR template with:
   - A clear title
   - Description of changes
   - Reference to the issue being addressed (e.g., "Fixes #123")
   - Any additional context or screenshots

### Code Review Process
1. Maintainers will review your PR
2. Address any requested changes or feedback
3. Once approved, a maintainer will merge your PR

## Pull Request Guidelines

- Keep PRs focused on a single issue or feature
- Update documentation as needed
- Ensure CI checks pass
- Be responsive to feedback and questions

## Communication

- For questions or discussions, use the GitHub Discussions feature
- For bug reports or feature requests, create an issue
- Be respectful and considerate in all communications

Thank you for contributing to our project!
