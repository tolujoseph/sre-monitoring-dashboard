import unittest
from monitoring_dashboard.metrics import get_cpu_usage, get_memory_usage, get_disk_usage

class TestMetrics(unittest.TestCase):

    def test_cpu_usage_range(self):
        self.assertGreaterEqual(get_cpu_usage(), 0)
        self.assertLessEqual(get_cpu_usage(), 100)

    def test_memory_usage_range(self):
        self.assertGreaterEqual(get_memory_usage(), 0)
        self.assertLessEqual(get_memory_usage(), 100)

    def test_disk_usage_range(self):
        self.assertGreaterEqual(get_disk_usage(), 0)
        self.assertLessEqual(get_disk_usage(), 100)

if __name__ == "__main__":
    unittest.main()
