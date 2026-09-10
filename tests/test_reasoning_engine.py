import os
from pathlib import Path

from copilot.ai.reasoning_engine import (
    build_gemini_prompt,
    deterministic_search_plan,
    gemini_available,
    parse_search_plan,
    summarize_answer,
)


def test_build_gemini_prompt_contains_context():
    prompt = build_gemini_prompt(
        "What is the staircase riser height?",
        {"cad_results": [{"label": "Riser-01"}], "spec_results": [{"title": "Stairs"}]},
    )
    assert "What is the staircase riser height" in prompt
    assert "Riser-01" in prompt
    assert "Stairs" in prompt


def test_gemini_available_without_key_is_false(monkeypatch, tmp_path: Path):
    original = os.environ.get("GEMINI_API_KEY")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setattr("copilot.ai.reasoning_engine.project_root", lambda: tmp_path)
    assert gemini_available() is False
    if original is not None:
        os.environ["GEMINI_API_KEY"] = original


def test_summarize_answer_falls_back_to_local_summary(monkeypatch):
    monkeypatch.setattr("copilot.ai.reasoning_engine.gemini_available", lambda: False)
    result = summarize_answer("what is the staircase riser height", {"summary": "Found CAD matches."})
    assert "Found CAD matches." in result


def test_parse_search_plan_accepts_only_known_sources():
    plan = parse_search_plan('{"searches":["cad","unknown","specs"],"category":"staircase"}')
    assert plan == {"searches": ["cad", "specs"], "category": "staircase"}


def test_deterministic_search_plan_selects_visuals_for_plan_request():
    plan = deterministic_search_plan("show the floor plan")
    assert plan["searches"] == ["visuals"]
