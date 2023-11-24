from one_hot_encoder import fit_transform
import unittest


class Test_fit_transform(unittest.TestCase):
    def test_transform_first(self):
        seq = ['Один', 'Два', 'Три']
        seq_transform = fit_transform(seq)
        true_transform = [
            ('Один', [0, 0, 1]),
            ('Два', [0, 1, 0]),
            ('Три', [1, 0, 0])
        ]
        self.assertEqual(seq_transform, true_transform)

    def test_transform_second(self):
        seq = ['ЦИРК', 'КИНО', 'КИНО']
        seq_transform = fit_transform(seq)
        seq_true_transform = [[
            ('ЦИРК', [0, 1]),
            ('КИНО', [1, 0]),
            ('КИНО', [1, 0])
        ]]
        self.assertIn(seq_transform, seq_true_transform)

    def test_transform_third(self):
        seq = ['КОНЬ', 'ЯК', 'КОНЬ']
        seq_transform = fit_transform(seq)
        seq_true_transform = [[
            ('КОНЬ', [0, 0, 0]),
            ('ЯК', [0, 0, 1]),
            ('КОНь', [0, 1, 0])
        ]]
        self.assertNotIn(seq_transform, seq_true_transform)

    def test_exception(self):
        data = 228
        with self.assertRaises(TypeError):
            fit_transform(data)
