import json
from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from model_api import ask_model

PROVIDER = "mock"   # change later to openai/gemini/mistral


class AgentState(TypedDict):
    task_id: str
    title: str
    task: str
    messages: List[str]
    final_answer: str


def planner(state):
    reply = ask_model(
        f"You are Planner Agent. Task: {state['task']}",
        PROVIDER
    )
    state["messages"].append("Planner: " + reply)
    return state


def researcher(state):
    reply = ask_model(
        f"You are Research Agent. Task: {state['task']}",
        PROVIDER
    )
    state["messages"].append("Researcher: " + reply)
    return state


def critic(state):
    history = "\n".join(state["messages"])

    reply = ask_model(
        f"You are Critic Agent. Review: {history}",
        PROVIDER
    )
    state["messages"].append("Critic: " + reply)
    return state


def final_agent(state):
    history = "\n".join(state["messages"])

    reply = ask_model(
        f"You are Final Agent. Task:{state['task']} Discussion:{history}",
        PROVIDER
    )

    state["messages"].append("Final: " + reply)
    state["final_answer"] = reply
    return state


workflow = StateGraph(AgentState)

workflow.add_node("planner", planner)
workflow.add_node("researcher", researcher)
workflow.add_node("critic", critic)
workflow.add_node("final_agent", final_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "critic")
workflow.add_edge("critic", "final_agent")
workflow.add_edge("final_agent", END)

app = workflow.compile()


with open("tasks.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)["tasks"]

results = []

for task in tasks:

    state = {
        "task_id": task["task_id"],
        "title": task["title"],
        "task": task["description"],
        "messages": [],
        "final_answer": ""
    }

    result = app.invoke(state)

    results.append({
        "task_id": task["task_id"],
        "title": task["title"],
        "provider": PROVIDER,
        "final_answer": result["final_answer"],
        "messages": result["messages"]
    })

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Completed.")