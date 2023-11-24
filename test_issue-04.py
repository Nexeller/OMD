from one_hot_encoder import fit_transform
import pytest


def test_transform_first():
    seq = ['КОФЕ', 'ЧАЙ', 'МОЛОКО']
    seq_transform = fit_transform(seq)
    true_transform = [
        ('КОФЕ', [0, 0, 1]),
        ('ЧАЙ', [0, 1, 0]),
        ('МОЛОКО', [1, 0, 0])
    ]
    assert seq_transform == true_transform


def test_transform_second():
    seq = ['КВАС', 'КОЛА', 'КОЛА']
    seq_transform = fit_transform(seq)
    seq_true_transform = [
        ('КВАС', [0, 1]),
        ('КОЛА', [1, 0]),
        ('КОЛА', [1, 0])
    ]
    assert seq_transform == seq_true_transform


def test_transform_third():
    seq = ['КРЕМ', 'СОДА']
    seq_transform = fit_transform(seq)
    seq_true_transform = [
        ('КРЕМ', [0, 1]),
        ('СОДА', [1, 0])
    ]
    assert seq_transform == seq_true_transform


def test_exception():
    data = 89991639517
    with pytest.raises(TypeError):
        fit_transform(data)
