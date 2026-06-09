"""Simple analysis service engine."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisResult:
    characters: int
    words: int
    sentences: int
    average_word_length: float


class AnalysisServiceEngine:
    """Service engine responsible for text analysis."""

    def analyze(self, text: str) -> AnalysisResult:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        characters = len(text)
        words = text.split()
        word_count = len(words)
        sentence_count = sum(text.count(mark) for mark in (".", "!", "?"))
        average_word_length = (
            sum(len(word.strip(".,!?;:\"'()[]{}")) for word in words) / word_count
            if word_count
            else 0.0
        )

        return AnalysisResult(
            characters=characters,
            words=word_count,
            sentences=sentence_count,
            average_word_length=round(average_word_length, 2),
        )

    def analyze_many(self, texts: list[str]) -> list[AnalysisResult]:
        if not isinstance(texts, list):
            raise TypeError("texts must be a list of strings")
        return [self.analyze(text) for text in texts]
