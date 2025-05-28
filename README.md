# LeetCode Practice with CI/CD

[![LeetCode CI Test](https://github.com/HilariousCheese/leetcode-ci-cd/actions/workflows/test.yml/badge.svg)](https://github.com/HilariousCheese/leetcode-ci-cd/actions/workflows/test.yml)


This repository contains my LeetCode solutions, complete with automated CI/CD testing to ensure code correctness and quality.  
Each solution is tested automatically with every update, helping me maintain a high standard in my coding practice.

---

## About

This project helps me practice coding problems with continuous integration and automated tests, mimicking professional development workflows.

---

## How It Works

- Push your code to GitHub  
- GitHub Actions runs the test pipeline inside a Docker container  
- Tests and code style checks are executed automatically  
- Test results are displayed right here with the badge above  

---

## Getting Started

1. Clone this repo  
2. Run tests locally with Docker:  
   ```bash
   docker build -t leetcode-ci .
   docker run --rm leetcode-ci
