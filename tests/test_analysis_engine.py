import unittest

from analysis_engine import AnalysisServiceEngine, AnalysisResult


class AnalysisServiceEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = AnalysisServiceEngine()

    def test_analyze_returns_expected_metrics(self) -> None:
        result = self.engine.analyze("Hello world! This is a test.")

        self.assertEqual(
            result,
            AnalysisResult(
                characters=28,
                words=6,
                sentences=2,
                average_word_length=3.5,
            ),
        )

    def test_analyze_handles_empty_string(self) -> None:
        result = self.engine.analyze("")

        self.assertEqual(result.words, 0)
        self.assertEqual(result.sentences, 0)
        self.assertEqual(result.average_word_length, 0.0)

    def test_analyze_rejects_non_string(self) -> None:
        with self.assertRaises(TypeError):
            self.engine.analyze(123)  # type: ignore[arg-type]

    def test_analyze_many_returns_result_for_each_input(self) -> None:
        results = self.engine.analyze_many(["One.", "Two words"])

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].sentences, 1)
        self.assertEqual(results[1].words, 2)

    def test_analyze_many_rejects_non_string_entries(self) -> None:
        with self.assertRaises(TypeError):
            self.engine.analyze_many(["valid", 123])  # type: ignore[list-item]


if __name__ == "__main__":
    unittest.main()
