# Multi-Agent Coordination Benchmark

A benchmark framework to evaluate coordination failures in multi-agent AI systems using role-based agents powered by LangGraph and LLM APIs.

## Problem Statement

Multi-agent AI systems often fail due to:

- Echo chambers
- Information loss
- Dominant agents
- Poor coordination
- Weak final synthesis

This project benchmarks those failures.

## Features

- Multi-agent workflow:
  - Planner Agent
  - Research Agent
  - Critic Agent
  - Final Agent

- LangGraph orchestration
- Supports OpenAI / Gemini / Mistral / Mock mode
- Task benchmark suite
- Transcript logging
- Streamlit dashboard

## Tech Stack

- Python
- LangGraph
- Streamlit
- JSON
- LLM APIs

## Project Structure

multi_agent/
├── main.py
├── model_api.py
├── app.py
├── tasks.json
├── results.json
├── requirements.txt
├── .env

## How to Run

### Install dependencies

pip install -r requirements.txt

### Run benchmark

python main.py

### Run dashboard

streamlit run app.py

## Example Output

- Multi-agent transcript
- Final answer
- Results dashboard

## Future Improvements

- More benchmark tasks
- Advanced failure detectors
- Compare multiple providers
- Better analytics dashboard

## Author

Mangali Prathyusha

AIzaSyBcYGQoRCsF4wCSaKfsTskHG_XIgu0JM0E
