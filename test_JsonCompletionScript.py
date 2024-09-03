import unittest
from unittest.mock import patch, MagicMock
from JsonCompletionScript import promptText_completion, process_promptTexts

class TestMyModule(unittest.TestCase):

    @patch('openai.Completion.create')
    def test_promptText_completion_success(self, mock_create):
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].text.strip.return_value = "Mocked response"
        mock_create.return_value = mock_response

        question = "What is the capital of France?"
        expected_response = "Mocked response"
        actual_response = promptText_completion(question)

        self.assertEqual(actual_response, expected_response)

    @patch('openai.Completion.create')
    def test_promptText_completion_failure(self, mock_create):
        mock_create.side_effect = Exception("API error")

        question = "What is the capital of France?"
        expected_response = "Error: API error"
        actual_response = promptText_completion(question)

        self.assertEqual(actual_response, expected_response)

    @patch('JsonCompletionScript.promptText_completion')
    def test_process_promptTexts(self, mock_promptText_completion):
        mock_promptText_completion.return_value = "Mocked answer"

        question_dict = {"question": "What is the capital of France?"}
        expected_response = {"question": "What is the capital of France?", "answer": "Mocked answer"}
        actual_response = process_promptTexts(question_dict)

        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
