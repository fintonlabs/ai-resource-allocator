import unittest
from main import AITool

class TestAITool(unittest.TestCase):

    def setUp(self):
        self.ai_tool = AITool('http://example.com/api', 'http://example.com/api', 'http://example.com/api', 'http://example.com/api', 'http://example.com/api')

    def test_get_workload_data(self):
        df = self.ai_tool.get_workload_data('server1')
        self.assertIsNotNone(df)

    def test_predict_workload(self):
        df = self.ai_tool.get_workload_data('server1')
        future_workload = self.ai_tool.predict_workload(df, 24)
        self.assertIsNotNone(future_workload)

if __name__ == '__main__':
    unittest.main()